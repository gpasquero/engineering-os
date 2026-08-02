"""Engineering Recommendations — guidance composed of semantic queries (ADR-0091).

A **consumer** of the Canonical Knowledge Model, like the query engine it is
built on. It holds no recommendation logic: every step names an action and a
declared query, and executing a recommendation executes those queries.

> Every item traces to a query and a path. Nothing is asserted that a query did
> not find.
"""
from ..runtime.phases import feature
from ..registry import load_all
from ..query import Model, run, load_queries, OK, EMPTY, NOT_APPLICABLE

ACTIONS = {
    "review":      "read these before deciding",
    "inspect":     "look at these; they may need to change",
    "validate":    "check that these still hold",
    "update":      "these will be wrong unless changed",
    "verify":      "confirm these still pass",
    "investigate": "these are unexplained and may be a problem",
}


def load_recommendations(strict=True):
    recommendations = load_all()["REG-recommendations"]
    queries = load_queries()
    problems = []
    for rid, rec in recommendations.items():
        for field in ("intent", "rationale", "steps"):
            if not rec.get(field):
                problems.append(f"{rid}: missing {field!r}")
        for i, step in enumerate(rec.get("steps") or []):
            where = f"{rid}.steps[{i}]"
            if step.get("action") not in ACTIONS:
                problems.append(f"{where}: unknown action {step.get('action')!r} "
                                f"(permitted: {sorted(ACTIONS)})")
            if step.get("query") not in queries:
                problems.append(f"{where}: unknown query {step.get('query')!r}")
            if not step.get("because"):
                problems.append(f"{where}: missing 'because'")
            unknown = set(step) - {"action", "query", "because"}
            if unknown:
                problems.append(f"{where}: unknown field(s) {sorted(unknown)}")
    if problems and strict:
        raise SystemExit("invalid recommendations:\n" + "\n".join(f"  {p}" for p in problems))
    return recommendations


def applicable(model, rec, subject):
    """Returns None if applicable, otherwise the reason it is not."""
    allowed = rec.get("applies-to") or []
    if not allowed:
        return None if subject is None else "this recommendation takes no subject"
    if not subject:
        return f"this recommendation requires a subject of type {', '.join(allowed)}"
    if subject not in model.by_id:
        return f"no node {subject!r} in this model"
    if model.by_id[subject]["type"] not in allowed:
        return (f"applies to {', '.join(allowed)}; "
                f"{subject} is a {model.by_id[subject]['type']}")
    return None


@feature("engineering recommendation",
         input_phase="ckm", output_phase="projection",
         invariants=["a recommendation holds no logic; every step is a declared query",
                     "nothing is reported that a query did not return (ADR-0091)",
                     "a step whose query is not applicable says so, and does not "
                     "report an empty result",
                     "no step carries a confidence score (ADR-0090)"],
         determinism="a composition of deterministic queries; step order is declared")
def advise(model, rec, subject=None, queries=None):
    queries = queries if queries is not None else load_queries()
    result = {"recommendation": rec["id"], "intent": rec["intent"],
              "subject": subject, "status": OK, "steps": [], "diagnostics": []}

    reason = applicable(model, rec, subject)
    if reason:
        result["status"] = NOT_APPLICABLE
        result["diagnostics"] = [{"phase": "projection", "message": reason,
                                  "rule": rec["id"]}]
        return result

    produced = 0
    for step in rec["steps"]:
        query = queries[step["query"]]
        answer = run(model, query, subject)
        produced += len(answer["rows"])
        result["steps"].append({
            "action": step["action"],
            "meaning": ACTIONS[step["action"]],
            "because": step["because"].strip(),
            "query": query["id"],
            "question": query["question"],
            "status": answer["status"],
            "rows": answer["rows"],
            "diagnostics": answer["diagnostics"],
        })
    if not produced:
        result["status"] = EMPTY
    return result
