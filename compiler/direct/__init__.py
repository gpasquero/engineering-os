"""The Engineering Director (ADR-0098).

Owns the loop. Workers execute only individual tasks.

    Developer Intent -> Plan -> Task Graph -> Worker Assignment
      -> Execution Context -> [Execution] -> Observations -> Knowledge Update

**Every stage except Execution is deterministic and happens here.** No language
model participates, and no worker receives more than one task and its context.
"""
from ..runtime.phases import feature
from ..registry import load_all
from ..query import Model, run, load_queries
from ..plan import plan as build_plan, load_plans
from ..taskgraph import derive


# ------------------------------------------------------------- assignment
@feature("worker assignment",
         input_phase="projection", output_phase="projection",
         invariants=["assignment is set containment and nothing else (ADR-0099)",
                     "no model or vendor is named",
                     "a task requiring C-approve matches no worker, by design (ADR-0100)",
                     "an unsatisfiable task is reported, never dropped"],
         determinism="a pure function of declared capabilities; workers sorted by id")
def assign(graph):
    registries = load_all()
    workers = registries["REG-workers"]
    gates = registries["REG-governance-gates"]
    out = []
    for task in graph["tasks"]:
        required = set(task["capabilities"])
        matches = sorted(wid for wid, w in workers.items()
                         if required <= set(w["provides"]))
        gate = next((gid for gid, g in gates.items()
                     if task["derivedFrom"].get("taskKind")
                     in (g.get("required-for-task-kinds") or [])), None)
        out.append({
            "task": task["id"], "requires": sorted(required),
            "workers": matches,
            "state": ("awaiting-authorization" if gate else
                      "assignable" if matches else "unsatisfiable"),
            "gate": gate,
            "execution": task["execution"],
        })
    return out


# ---------------------------------------------------------------- context
@feature("execution context",
         input_phase="projection", output_phase="projection",
         invariants=["a worker receives a package, never an objective alone (ADR-0101)",
                     "allowed scope names exactly what the worker may touch",
                     "every field is derived from the plan, the graph or the model"],
         determinism="a pure function of plan, graph and model")
def context(model, plan_result, graph, task):
    queries = load_queries()
    targets = task["targets"]

    scope = []
    for tid in targets:
        node = model.by_id.get(tid)
        if not node:
            continue
        source = (node.get("attributes") or {}).get("source")
        scope.append({"node": tid, "type": node["type"],
                      "source": source, "provenance": node["provenance"]["source"]})

    evidence = []
    for tid in targets:
        if tid in model.by_id:
            answer = run(model, queries["Q-evidence"], tid)
            for row in answer["rows"]:
                node = model.by_id[row["id"]]
                evidence.append({"for": tid, "evidence": row["id"],
                                 "source": (node.get("attributes") or {}).get("source"),
                                 "locator": (node.get("attributes") or {}).get("locator")})

    return {
        "task": task["id"],
        "objective": task["objective"],
        "engineeringRationale": plan_result["rationale"],
        "assumptions": [{"statement": a["statement"],
                         "holds": bool(a["rows"]),
                         "nodes": [r["id"] for r in a["rows"]]}
                        for a in plan_result["assumptions"]],
        "evidence": evidence,
        "affectedNodes": targets,
        "expectedOutputs": task["evidence"],
        "completionConditions": task["completion"],
        "requiredUpdates": [o["id"] for o in load_all()["REG-observation-kinds"].values()
                            if o["intake"] == "record"],
        "allowedScope": scope,
        "capabilities": task["capabilities"],
        "derivedFrom": task["derivedFrom"],
    }


# ----------------------------------------------------------- observations
@feature("observation intake",
         input_phase="projection", output_phase="projection",
         invariants=["a worker never writes to the model (ADR-0101)",
                     "intake produces a proposal, never a model write",
                     "an unknown observation kind is rejected, not ignored",
                     "only additive kinds may record mechanically"],
         determinism="a pure function of the declared observation kinds")
def intake(observations):
    registries = load_all()
    kinds = registries["REG-observation-kinds"]
    gates = registries["REG-governance-gates"]

    proposal = {"record": [], "govern": [], "reject": [], "diagnostics": []}
    for obs in observations:
        kind = kinds.get(obs.get("kind"))
        if not kind:
            proposal["reject"].append({
                **obs, "outcome": "reject",
                "reason": f"unknown observation kind {obs.get('kind')!r}",
                "produces": "a finding; nothing enters the model"})
            proposal["diagnostics"].append(
                f"unknown observation kind {obs.get('kind')!r} from task "
                f"{obs.get('task')!r}")
            continue
        # A gate declared for THIS KIND is more specific than one declared for
        # the outcome class, and must win. The simulation found this: an
        # assumption-disproved observation was routed to the general
        # knowledge-update gate instead of the decision-record gate.
        gate = None
        if kind["intake"] == "govern":
            gate = next((gid for gid, g in gates.items()
                         if obs["kind"] in (g.get("required-for-observation-kinds") or [])), None)
            if gate is None:
                gate = next((gid for gid, g in gates.items()
                             if kind["intake"] in
                             (g.get("required-for-observation-outcomes") or [])), None)
        proposal[kind["intake"]].append({
            **obs, "outcome": kind["intake"], "produces": kind["produces"].strip(),
            "gate": gate, "rationale": kind["rationale"].strip()})
    return proposal


# ------------------------------------------------------------------ loop
@feature("engineering direction",
         input_phase="ckm", output_phase="projection",
         invariants=["the Director owns every stage except Execution (ADR-0098)",
                     "no language model participates before Execution",
                     "an intent selects plans; it is never itself a plan (ADR-0096)",
                     "judgment before the first LLM token is counted and reported"],
         determinism="a composition of deterministic stages")
def direct(model, intent, subject, observations=None):
    intents = load_all()["REG-engineering-intents"]
    plans = load_plans()

    result = {"intent": intent, "subject": subject, "status": "ok",
              "runs": [], "diagnostics": []}

    spec = intents.get(intent)
    if not spec:
        result["status"] = "invalid"
        result["diagnostics"].append(f"unknown intent {intent!r}")
        return result
    result["asks"] = spec["asks"]

    selected = spec.get("selects-plans") or []
    if not selected:
        result["status"] = "empty"
        result["diagnostics"].append(
            f"intent {intent!r} selects no plan; it has no planning support")
        return result

    for pid in selected:
        plan_result = build_plan(model, plans[pid], subject)
        if plan_result["status"] == "not-applicable":
            continue
        graph = derive(plan_result)
        assignments = assign(graph)
        contexts = [context(model, plan_result, graph, t) for t in graph["tasks"]]
        result["runs"].append({"plan": pid, "planResult": plan_result, "graph": graph,
                               "assignments": assignments, "contexts": contexts})

    if not result["runs"]:
        result["status"] = "not-applicable"
        result["diagnostics"].append(
            f"no plan selected by {intent!r} applies to {subject!r}")
        return result

    if observations is not None:
        result["observations"] = intake(observations)

    result["kpi"] = kpi(result)
    return result


def kpi(result):
    """How much engineering judgment happens before the first LLM token (ADR-0098)."""
    upstream, downstream = [], []
    for runinfo in result["runs"]:
        p, g = runinfo["planResult"], runinfo["graph"]
        upstream += [f"plan:{d}" for d in p["judgment"]["derived"]]
        upstream += [f"task:{t['id']}" for t in g["tasks"]]
        upstream += [f"dependency:{t['id']}<-{d}" for t in g["tasks"] for d in t["dependsOn"]]
        upstream += [f"level:{i}" for i, _ in enumerate(g["levels"], 1)]
        upstream += [f"assignment:{a['task']}={a['state']}" for a in runinfo["assignments"]]
        upstream += [f"context:{c['task']}" for c in runinfo["contexts"]]
        downstream += [f"deferred:{d}" for d in p["judgment"]["deferred"]]
        downstream += [f"reasoning-task:{t['id']}" for t in g["tasks"]
                       if "reasoning" in t["execution"]]
    return {
        "decisionsBeforeFirstToken": len(upstream),
        "decisionsLeftToWorkers": len(downstream),
        "upstream": upstream,
        "downstream": downstream,
    }
