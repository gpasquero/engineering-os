#!/usr/bin/env python3
"""Turn a Knowledge Drift Report into an engineering work queue (`ADR-0114`).

    python3 tools/drift-queue.py <project>
    python3 tools/drift-queue.py <project> --plan=P-review-unsupported

**A drift report is a work queue, not a document.** Each class routes to an
Engineering Plan; the routing says *what kind of work this is*, not *what to do*.

**Nothing is instantiated automatically.** 238 items would produce 238 plans,
which is a queue nobody can face. Routing groups the work; instantiating a plan
is a curation decision.

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from compiler.registry import load_all      # noqa: E402
from compiler.plan import load_plans, plan  # noqa: E402
from compiler.query import Model            # noqa: E402

BAR = "─" * 74


def main(argv):
    opts = {a.split("=", 1)[0]: a.split("=", 1)[1]
            for a in argv if a.startswith("--") and "=" in a}
    argv = [a for a in argv if not a.startswith("--")]
    if len(argv) < 2:
        print(__doc__)
        return 2

    project = ROOT / argv[1]
    report_path = project / "knowledge-drift-report.json"
    if not report_path.exists():
        print(f"no drift report at {report_path}\nrun: python3 tools/lifecycle.py …")
        return 1
    report = json.loads(report_path.read_text())
    classes = load_all()["REG-drift-categories"]
    plans = load_plans()

    queue = {}
    unroutable = {}
    for cid, items in report["items"].items():
        route = (classes.get(cid) or {}).get("routes-to")
        if route and route != "~":
            queue.setdefault(route, []).extend(
                {"drift": cid, **i} for i in items)
        else:
            unroutable[cid] = items

    print(BAR); print("KNOWLEDGE DRIFT WORK QUEUE"); print(BAR)
    print(f"  {report['authoritativeNodes']} maintained nodes · "
          f"{report['candidateProposals']} fresh proposals\n")

    for route in sorted(queue, key=lambda r: -len(queue[r])):
        spec = plans[route]
        print(f"  {route}   {len(queue[route])} item(s)")
        print(f"      {spec['objective'].replace('{subject}', '…')}")
        by_class = {}
        for i in queue[route]:
            by_class.setdefault(i["drift"], 0)
            by_class[i["drift"]] += 1
        for cid, n in sorted(by_class.items()):
            print(f"      from {cid}  ({n})")
            print(f"           {classes[cid]['routing-rationale']}")
        for i in queue[route][:2]:
            print(f"        e.g. {i['subject']}")
        print()

    if unroutable:
        print("  NOT ROUTED — curation alone, or unroutable by definition")
        for cid, items in sorted(unroutable.items()):
            why = (classes.get(cid) or {}).get("routing-rationale", "no route declared")
            print(f"      {cid}  ({len(items)})  {why}")
        print()

    if "--plan" in opts:
        target = opts["--plan"]
        if target not in queue:
            print(f"no drift items route to {target!r}")
            return 1
        ckm_path = project / "build/canonical-knowledge-model.json"
        model = Model(json.loads(ckm_path.read_text()))
        first = queue[target][0]
        print(BAR)
        print(f"INSTANTIATED  {target}  for  {first['subject']}")
        print(f"  from drift class {first['drift']}")
        print(BAR)
        result = plan(model, plans[target], first["subject"])
        if result["status"] == "not-applicable":
            print(f"  NOT APPLICABLE — {result['diagnostics'][0]['message']}")
            return 1
        for phase in result["phases"]:
            print(f"  ── {phase['id'].upper()}: {phase['goal']}")
            for act in phase["actions"]:
                print(f"     {act['action'].upper()}  {act['because']}")
                for t in act["targets"][:3]:
                    print(f"         {t['id']}")
        j = result["judgment"]
        print(f"\n  derived {len(j['derived'])} · deferred {len(j['deferred'])}")
        for d in j["deferred"]:
            print(f"      defers: {d}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
