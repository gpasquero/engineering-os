#!/usr/bin/env python3
"""The Engineering Director — the complete deterministic loop (ADR-0098).

    Developer Intent -> Plan -> Task Graph -> Worker Assignment
      -> Execution Context -> [Execution] -> Observations -> Knowledge Update

    python3 tools/direct.py <project> intents
    python3 tools/direct.py <project> I-modify-behavior Artifact.ConflictGo
    python3 tools/direct.py <project> I-modify-behavior Artifact.ConflictGo --context T02
    python3 tools/direct.py <project> I-modify-behavior Artifact.ConflictGo \\
        --observations external/kubernetes-ssa/simulated-observations.yaml

**No language model participates.** A worker receives one task and its context,
never an intent, a plan or a graph.

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import json
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from compiler.query import Model          # noqa: E402
from compiler.registry import load_all    # noqa: E402
from compiler.direct import direct        # noqa: E402

BAR = "─" * 74
MARK = {"mechanical": "auto", "reasoning": "LLM", "human": "GATE"}


def render(r, context_filter=None):
    L = [BAR, f"ENGINEERING DIRECTOR", BAR, "",
         f"INTENT     {r['intent']}", f"SUBJECT    {r['subject']}"]
    if r.get("asks"):
        L.append(f"ASKS       {r['asks']}")
    L.append("")
    if r["status"] not in ("ok", "empty"):
        for d in r["diagnostics"]:
            L.append(f"  {r['status'].upper()} — {d}")
        return "\n".join(L + ["", BAR])
    for d in r["diagnostics"]:
        L.append(f"  ! {d}")

    for runinfo in r["runs"]:
        g, p = runinfo["graph"], runinfo["planResult"]
        by_task = {a["task"]: a for a in runinfo["assignments"]}
        L += [f"PLAN       {p['plan']}   {p['objective']}", ""]
        L.append("WORK")
        for i, level in enumerate(g["levels"], 1):
            par = "  (parallel)" if len(level) > 1 else ""
            L.append(f"  level {i}{par}")
            for tid in level:
                t = next(x for x in g["tasks"] if x["id"] == tid)
                a = by_task[tid]
                cls = "/".join(MARK[c] for c in t["execution"])
                who = (", ".join(a["workers"]) if a["workers"]
                       else f"gate {a['gate']}" if a["gate"] else "NO WORKER PROVIDES THIS")
                L.append(f"    [{cls:^8}] {tid}")
                L.append(f"               {t['objective']}")
                L.append(f"               {a['state']}: {who}")
        L.append("")

        if context_filter:
            for c in runinfo["contexts"]:
                if not c["task"].startswith(context_filter):
                    continue
                L += [BAR, f"EXECUTION CONTEXT   {c['task']}", BAR,
                      f"  objective        {c['objective']}",
                      f"  rationale        {c['engineeringRationale'][:120]}…"]
                L.append("  assumptions")
                for a in c["assumptions"]:
                    mark = "holds" if a["holds"] else "UNVERIFIED"
                    L.append(f"      [{mark}] {a['statement']}")
                    for n in a["nodes"]:
                        L.append(f"               {n}")
                L.append("  evidence")
                for e in c["evidence"] or []:
                    L.append(f"      {e['for']} ← {e['evidence']}")
                    if e["source"]:
                        L.append(f"          {e['source']}  {e['locator'] or ''}")
                if not c["evidence"]:
                    L.append("      (none)")
                L.append("  affected nodes   " + (", ".join(c["affectedNodes"]) or "none"))
                L.append(f"  expected output  {c['expectedOutputs']}")
                L.append("  completion")
                for cc in c["completionConditions"]:
                    L.append(f"      {cc}")
                L.append("  allowed scope")
                for s in c["allowedScope"] or []:
                    L.append(f"      {s['node']} ({s['type']})")
                    if s["source"]:
                        L.append(f"          {s['source']}")
                if not c["allowedScope"]:
                    L.append("      (nothing — this task modifies no artifact)")
                L.append(f"  capabilities     {', '.join(c['capabilities'])}")
                L.append("")

    if "observations" in r:
        o = r["observations"]
        L += [BAR, "EXECUTION OBSERVATIONS", BAR,
              f"  {len(o['record'])} record · {len(o['govern'])} govern · "
              f"{len(o['reject'])} reject", ""]
        for outcome, label in (("record", "RECORD  — may enter the model"),
                               ("govern", "GOVERN  — requires authorization"),
                               ("reject", "REJECT  — never enters the model")):
            for item in o[outcome]:
                L.append(f"  {label}")
                L.append(f"      {item.get('kind')}  from {item.get('task')}")
                L.append(f"      \"{item.get('statement', '')}\"")
                L.append(f"      produces: {item.get('produces')}")
                if item.get("gate"):
                    L.append(f"      gate:     {item['gate']}")
                if item.get("reason"):
                    L.append(f"      reason:   {item['reason']}")
                L.append("")
        L.append("  Workers never write to the model. This is a proposal, not a write.")
        L.append("")

    k = r["kpi"]
    L += [BAR,
          f"KPI   {k['decisionsBeforeFirstToken']} engineering decisions made "
          f"before the first LLM token",
          f"      {k['decisionsLeftToWorkers']} left to workers", BAR]
    return "\n".join(L)


def main(argv):
    modes = {a for a in argv if a.startswith("--")}
    ctx = next((a.split("=", 1)[1] for a in modes if a.startswith("--context=")), None)
    obs_path = next((a.split("=", 1)[1] for a in modes if a.startswith("--observations=")), None)
    argv = [a for a in argv if not a.startswith("--")]
    if len(argv) < 3:
        print(__doc__)
        return 2

    project = ROOT / argv[1]
    ckm_path = project / "build/canonical-knowledge-model.json"
    if not ckm_path.exists():
        print(f"no compiled model at {ckm_path}")
        return 1

    if argv[2] == "intents":
        intents = load_all()["REG-engineering-intents"]
        width = max(len(i) for i in intents)
        for iid, spec in intents.items():
            plans = ", ".join(spec.get("selects-plans") or []) or "no plan"
            print(f"  {iid:<{width}}  {spec['label']:<22} → {plans}")
        return 0

    model = Model(json.loads(ckm_path.read_text()))
    observations = None
    if obs_path:
        observations = yaml.safe_load((ROOT / obs_path).read_text())["observations"]

    result = direct(model, argv[2], argv[3] if len(argv) > 3 else None, observations)
    print(json.dumps(result, indent=2) if "--json" in modes else render(result, ctx))
    return 0 if result["status"] in ("ok", "empty") else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
