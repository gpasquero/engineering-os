"""The Task Graph engine (ADR-0097).

Derives a deterministic task graph from an Engineering Plan. A TaskGraph is a
pure function of a plan, which is a pure function of the Canonical Knowledge
Model. **No language model participates.**

Every node declares an objective, its dependencies, its completion conditions,
the evidence it produces, and **the capabilities a worker must have** — never
which worker. Routing is a separate stage.

Parallelism is computed, not annotated: tasks with no dependency path between
them share a level.
"""
from ..runtime.phases import feature
from ..registry import load_all


def load_task_kinds(strict=True):
    kinds = load_all()["REG-task-kinds"]
    capabilities = load_all()["REG-worker-capabilities"]
    problems = []
    for kid, kind in kinds.items():
        for field in ("objective", "capabilities", "completion", "evidence"):
            if not kind.get(field):
                problems.append(f"{kid}: missing {field!r}")
        if not kind.get("from-action") and not kind.get("terminal"):
            problems.append(f"{kid}: must declare from-action or terminal")
        for cap in kind.get("capabilities") or []:
            if cap not in capabilities:
                problems.append(f"{kid}: unknown capability {cap!r}")
    if problems and strict:
        raise SystemExit("invalid task kinds:\n" + "\n".join(f"  {p}" for p in problems))
    return kinds, capabilities


def _levels(nodes):
    """Topological levels. Tasks in one level have no dependency between them."""
    remaining = {n["id"]: set(n["dependsOn"]) for n in nodes}
    done, levels = set(), []
    while remaining:
        ready = sorted(tid for tid, deps in remaining.items() if deps <= done)
        if not ready:
            return None
        levels.append(ready)
        done |= set(ready)
        for tid in ready:
            del remaining[tid]
    return levels


@feature("task graph derivation",
         input_phase="ckm", output_phase="projection",
         invariants=["a task graph is derived from a plan, never declared (ADR-0097)",
                     "every task declares capabilities, never a worker",
                     "no language model participates (ADR-0092)",
                     "parallelism is computed from dependencies, not annotated",
                     "a plan action with no declared task kind is reported, not dropped"],
         determinism="a pure function of the plan; task ids and levels are stable")
def derive(plan_result):
    kinds, capabilities = load_task_kinds()
    by_action = {k["from-action"]: k for k in kinds.values() if k.get("from-action")}
    terminals = sorted((k for k in kinds.values() if k.get("terminal")),
                       key=lambda k: k.get("order", 0))

    graph = {"taskGraph": f"TG-{plan_result['plan']}", "plan": plan_result["plan"],
             "subject": plan_result["subject"], "objective": plan_result["objective"],
             "status": plan_result["status"], "tasks": [], "levels": [],
             "diagnostics": [],
             "execution": {"mechanical": 0, "reasoning": 0, "human": 0}}

    if plan_result["status"] == "not-applicable":
        graph["diagnostics"] = plan_result.get("diagnostics", [])
        return graph

    completion = {c["query"]: c for c in plan_result.get("completion") or []}
    evidence = {e["query"]: e for e in plan_result.get("expectedEvidence") or []}
    reviews = plan_result.get("reviews") or []

    previous_phase_tasks, seq = [], 0
    for phase in plan_result["phases"]:
        phase_tasks = []
        for action in phase["actions"]:
            kind = by_action.get(action["action"])
            if not kind:
                graph["diagnostics"].append({
                    "phase": "projection", "rule": graph["taskGraph"],
                    "message": f"plan action {action['action']!r} has no declared "
                               f"task kind; no task produced"})
                continue
            seq += 1
            targets = [t["id"] for t in action["targets"]]
            conditions = [completion[action["query"]]["statement"]] \
                if action["query"] in completion else [kind["completion"].strip()]
            task = {
                "id": f"T{seq:02d}-{phase['id']}-{action['action']}",
                "objective": kind["objective"].replace(
                    "{targets}", ", ".join(targets) if targets else "nothing"),
                "phase": phase["id"],
                "dependsOn": list(previous_phase_tasks),
                "completion": conditions,
                "evidence": kind["evidence"].strip(),
                "capabilities": list(kind["capabilities"]),
                "execution": sorted({capabilities[c]["execution"]
                                     for c in kind["capabilities"]}),
                "targets": targets,
                "derivedFrom": {"planAction": action["action"], "query": action["query"],
                                "recommendation": action["recommendation"],
                                "taskKind": kind["id"]},
                "requiresReviewAt": [r["because"] for r in reviews
                                     if r["at"] == phase["id"]],
            }
            if action["query"] in evidence:
                task["evidence"] = evidence[action["query"]]["statement"]
            phase_tasks.append(task["id"])
            graph["tasks"].append(task)
        if phase_tasks:
            previous_phase_tasks = phase_tasks

    for kind in terminals:
        seq += 1
        task = {
            "id": f"T{seq:02d}-{kind['id'].replace('T-', '')}",
            "objective": kind["objective"].replace("{targets}", "the completed work"),
            "phase": "close",
            "dependsOn": [t["id"] for t in graph["tasks"]] if kind is terminals[0]
                         else [f"T{seq-1:02d}-{terminals[0]['id'].replace('T-', '')}"],
            "completion": [kind["completion"].strip()],
            "evidence": kind["evidence"].strip(),
            "capabilities": list(kind["capabilities"]),
            "execution": sorted({capabilities[c]["execution"] for c in kind["capabilities"]}),
            "targets": [],
            "derivedFrom": {"taskKind": kind["id"], "terminal": True},
            "requiresReviewAt": [],
        }
        graph["tasks"].append(task)

    for task in graph["tasks"]:
        for cls in task["execution"]:
            graph["execution"][cls] += 1

    levels = _levels(graph["tasks"])
    if levels is None:
        graph["status"] = "invalid"
        graph["diagnostics"].append({"phase": "projection", "rule": graph["taskGraph"],
                                     "message": "cyclic task dependencies"})
        return graph
    graph["levels"] = levels
    graph["parallelism"] = max(len(level) for level in levels) if levels else 0
    graph["judgment"] = plan_result.get("judgment", {})
    return graph
