#!/usr/bin/env python3
"""Derive an Engineering Plan from the Canonical Knowledge Model.

Plans are declared in `model/plans.md` and composed of recommendations and
semantic queries (`ADR-0094`). This tool implements none of them, and **no
language model participates** (`ADR-0092`).

    python3 tools/plan.py <project> plans
    python3 tools/plan.py <project> P-change-implementation Artifact.ConflictGo
    python3 tools/plan.py <project> P-change-concept Concept.Conflict --json
    python3 tools/plan.py <project> P-change-implementation Artifact.ConflictGo --reasoning

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from compiler.query import Model                 # noqa: E402
from compiler.plan import plan, load_plans       # noqa: E402

BAR = "─" * 68


def render(r, reasoning=False):
    L = [BAR, f"ENGINEERING PLAN   {r['plan']}", BAR, "", f"OBJECTIVE", f"  {r['objective']}", ""]

    if r["status"] == "not-applicable":
        L += [f"  NOT APPLICABLE — {r['diagnostics'][0]['message']}", ""]
        return "\n".join(L)

    L += ["RATIONALE"] + [f"  {line}" for line in r["rationale"].splitlines()] + [""]

    L.append("ASSUMPTIONS")
    for a in r["assumptions"]:
        L.append(f"  {a['statement']}")
        for row in a["rows"]:
            L.append(f"      {row['id']}  ({row['type']})")
        if not a["rows"]:
            L.append("      (none found — the assumption is unverified)")
        L.append(f"      [{a['query']}]")
    L.append("")

    L.append("ACTIONS")
    for phase in r["phases"]:
        dep = f"   requires: {', '.join(phase['requires'])}" if phase["requires"] else ""
        L.append(f"  ── {phase['id'].upper()}: {phase['goal']}{dep}")
        if not phase["actions"] and not phase.get("notApplicable"):
            L.append("       (nothing to do — no query returned anything)")
        for s in phase.get("notApplicable") or []:
            L.append(f"       ! {s['action']} skipped: {s['why']}")
            L.append(f"         [{s['query']}]")
        for act in phase["actions"]:
            L.append(f"     {act['order']:>2}. {act['action'].upper()}  {act['because']}")
            for t in act["targets"]:
                via = f"  via {t['via']}" if t["via"] else ""
                L.append(f"         {t['id']}  ({t['type']}){via}")
            L.append(f"         [{act['query']} · {act['recommendation']}]")
    L.append("")

    if r["reviews"]:
        L.append("REQUIRED REVIEWS")
        for rv in r["reviews"]:
            L.append(f"  at {rv['at']}: {rv['because']}")
            L.append(f"      {', '.join(rv['rows']) if rv['rows'] else '(nothing to review)'}"
                     f"   [{rv['query']}]")
        L.append("")

    if r["expectedEvidence"]:
        L.append("EXPECTED EVIDENCE")
        for e in r["expectedEvidence"]:
            L.append(f"  {e['statement']}")
            L.append(f"      currently: "
                     f"{', '.join(e['currently']) if e['currently'] else 'nothing'}"
                     f"   [{e['query']}]")
        L.append("")

    L.append("COMPLETION CONDITIONS")
    for c in r["completion"]:
        L.append(f"  [{'x' if c['holdsNow'] else ' '}] {c['statement']}   [{c['query']}]")
    L.append("")

    j = r["judgment"]
    L += ["JUDGMENT", f"  derived   {len(j['derived'])} item(s) from the model"]
    L.append(f"  deferred  {len(j['deferred'])} decision(s) to the engineer or executor:")
    for d in j["deferred"]:
        L.append(f"      - {d}")
    L.append("")

    if reasoning:
        L.append("REASONING CHAIN")
        for step in r["reasoning"]:
            L.append(f"  {step['query']}({step['subject']}) -> {step['status']}, "
                     f"{len(step['returned'])} row(s)")
            L.append(f"      because {step['because']}")
        L.append("")

    L += [BAR, "Every action above was returned by a declared semantic query.",
          "No language model participated in producing this plan.", BAR]
    return "\n".join(L)


def main(argv):
    as_json = "--json" in argv
    reasoning = "--reasoning" in argv
    argv = [a for a in argv if a not in ("--json", "--reasoning")]
    if len(argv) < 3:
        print(__doc__)
        return 2

    project = ROOT / argv[1]
    ckm_path = project / "build/canonical-knowledge-model.json"
    if not ckm_path.exists():
        print(f"no compiled model at {ckm_path}\nrun: python3 tools/compile.py {argv[1]}")
        return 1

    model = Model(json.loads(ckm_path.read_text()))
    plans = load_plans()
    name = argv[2]

    if name == "plans":
        width = max(len(p) for p in plans)
        for pid, spec in plans.items():
            applies = ", ".join(spec.get("applies-to") or []) or "any"
            print(f"  {pid:<{width}}  {spec['objective']}   [{applies}]")
        return 0

    if name not in plans:
        print(f"unknown plan {name!r}. Try: plans")
        return 2

    result = plan(model, plans[name], argv[3] if len(argv) > 3 else None)
    print(json.dumps(result, indent=2) if as_json else render(result, reasoning))
    return 0 if result["status"] in ("ok", "empty") else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
