"""The Engineering Planning Engine (ADR-0094).

Derives an Engineering Plan **entirely from the Canonical Knowledge Model**, by
executing declared queries and recommendations.

> **No language model participates.** Determinism is a property of how the output
> was produced, not of how it reads (ADR-0092).

The engine holds mechanism. Plans are data.
"""
from ..runtime.phases import feature
from ..registry import load_all
from ..query import run, load_queries, OK, EMPTY, NOT_APPLICABLE
from ..recommend import load_recommendations, ACTIONS


def load_plans(strict=True):
    plans = load_all()["REG-plans"]
    queries, recommendations = load_queries(), load_recommendations()
    problems = []
    for pid, plan in plans.items():
        for field in ("objective", "rationale", "phases", "defers"):
            if not plan.get(field):
                problems.append(f"{pid}: missing {field!r}")
        phase_ids = {p.get("id") for p in plan.get("phases") or []}
        for i, phase in enumerate(plan.get("phases") or []):
            where = f"{pid}.phases[{i}]"
            if phase.get("recommendation") not in recommendations:
                problems.append(f"{where}: unknown recommendation "
                                f"{phase.get('recommendation')!r}")
            for action in phase.get("actions") or []:
                if action not in ACTIONS:
                    problems.append(f"{where}: unknown action {action!r}")
            for dep in phase.get("requires") or []:
                if dep not in phase_ids:
                    problems.append(f"{where}: requires unknown phase {dep!r}")
        for section in ("assumptions", "reviews", "expected-evidence", "completion"):
            for i, item in enumerate(plan.get(section) or []):
                if item.get("query") not in queries:
                    problems.append(f"{pid}.{section}[{i}]: unknown query "
                                    f"{item.get('query')!r}")
                if section == "completion" and item.get("expect") not in ("empty", "non-empty"):
                    problems.append(f"{pid}.completion[{i}]: expect must be "
                                    f"'empty' or 'non-empty'")
    if problems and strict:
        raise SystemExit("invalid plans:\n" + "\n".join(f"  {p}" for p in problems))
    return plans


def applicable(model, plan, subject):
    allowed = plan.get("applies-to") or []
    if not subject:
        return f"this plan requires a subject of type {', '.join(allowed)}"
    if subject not in model.by_id:
        return f"no node {subject!r} in this model"
    if allowed and model.by_id[subject]["type"] not in allowed:
        return (f"applies to {', '.join(allowed)}; "
                f"{subject} is a {model.by_id[subject]['type']}")
    return None


@feature("engineering planning",
         input_phase="ckm", output_phase="projection",
         invariants=["a plan states nothing a query did not return (ADR-0094)",
                     "no language model participates in producing a plan (ADR-0092)",
                     "every action names the query and recommendation it came from",
                     "derived and deferred items are both enumerated (ADR-0093)",
                     "phase order follows declared dependencies, not discovery order",
                     "a step whose query does not apply is reported, never silently skipped"],
         determinism="a composition of deterministic queries; order and dependencies "
                     "are declared, not inferred")
def plan(model, spec, subject=None):
    queries, recommendations = load_queries(), load_recommendations()
    result = {"plan": spec["id"], "subject": subject, "status": OK,
              "objective": spec["objective"].replace("{subject}", str(subject)),
              "rationale": spec["rationale"].strip(),
              "assumptions": [], "reasoning": [], "phases": [],
              "reviews": [], "expectedEvidence": [], "completion": [],
              "judgment": {"derived": [], "deferred": list(spec.get("defers") or [])}}

    reason = applicable(model, spec, subject)
    if reason:
        result["status"] = NOT_APPLICABLE
        result["diagnostics"] = [{"phase": "projection", "message": reason,
                                  "rule": spec["id"]}]
        return result

    def ask(query_id, because):
        """Every query the plan runs is recorded in the reasoning chain."""
        answer = run(model, queries[query_id], subject)
        result["reasoning"].append({
            "query": query_id, "question": queries[query_id]["question"],
            "subject": subject, "because": because,
            "status": answer["status"], "returned": [r["id"] for r in answer["rows"]],
        })
        return answer

    for item in spec.get("assumptions") or []:
        answer = ask(item["query"], item["statement"].strip())
        result["assumptions"].append({
            "statement": item["statement"].strip(), "query": item["query"],
            "status": answer["status"],
            "rows": [{"id": r["id"], "type": r["type"]} for r in answer["rows"]]})

    # Phases in declared dependency order: a stable topological sort.
    phases = {p["id"]: p for p in spec["phases"]}
    ordered, remaining = [], [p["id"] for p in spec["phases"]]
    while remaining:
        ready = [pid for pid in remaining
                 if all(dep in ordered for dep in phases[pid].get("requires") or [])]
        if not ready:
            result["status"] = "invalid"
            result["diagnostics"] = [{"phase": "projection", "rule": spec["id"],
                                      "message": f"cyclic phase dependencies: {remaining}"}]
            return result
        ordered.append(ready[0])
        remaining.remove(ready[0])

    step_no = 0
    for pid in ordered:
        phase = phases[pid]
        rec = recommendations[phase["recommendation"]]
        actions, skipped = [], []
        for step in rec["steps"]:
            if step["action"] not in (phase.get("actions") or []):
                continue
            answer = ask(step["query"], step["because"].strip())
            if answer["status"] == NOT_APPLICABLE:
                # A phase borrows a recommendation's STEPS, not its
                # applicability: the plan declares its own subject types and each
                # query declares its own. A step whose query does not apply to
                # this subject produces nothing — and saying so is the point.
                # Silent empty phases hid this across five plans.
                skipped.append({"query": step["query"], "action": step["action"],
                                "why": answer["diagnostics"][0]["message"]})
                continue
            if not answer["rows"]:
                continue
            step_no += 1
            actions.append({
                "order": step_no, "action": step["action"],
                "meaning": ACTIONS[step["action"]], "because": step["because"].strip(),
                "query": step["query"], "recommendation": rec["id"],
                "targets": [{"id": r["id"], "type": r["type"],
                             "via": (r["path"][0]["predicate"] if r.get("path") else None)}
                            for r in answer["rows"]]})
            result["judgment"]["derived"] += [
                f"{step['action']} {r['id']} ({step['query']})" for r in answer["rows"]]
        result["phases"].append({
            "id": pid, "goal": phase["goal"], "requires": phase.get("requires") or [],
            "actions": actions, "notApplicable": skipped})

    for item in spec.get("reviews") or []:
        answer = ask(item["query"], item["because"].strip())
        result["reviews"].append({
            "at": item["at"], "because": item["because"].strip(),
            "query": item["query"], "status": answer["status"],
            "rows": [r["id"] for r in answer["rows"]]})

    for item in spec.get("expected-evidence") or []:
        answer = ask(item["query"], item["statement"].strip())
        result["expectedEvidence"].append({
            "statement": item["statement"].strip(), "query": item["query"],
            "currently": [r["id"] for r in answer["rows"]]})

    for item in spec.get("completion") or []:
        answer = ask(item["query"], item["statement"].strip())
        holds = bool(answer["rows"]) if item["expect"] == "non-empty" else not answer["rows"]
        result["completion"].append({
            "statement": item["statement"].strip(), "query": item["query"],
            "expect": item["expect"], "holdsNow": holds})

    if not any(p["actions"] for p in result["phases"]):
        result["status"] = EMPTY
    return result
