#!/usr/bin/env python3
"""Review a Candidate Engineering Model and apply an authorized subset.

    python3 tools/review.py <project> summary
    python3 tools/review.py <project> show ambiguities|gaps|conflicts
    python3 tools/review.py <project> apply --types=Capability,Invariant --reviewer=NAME
    python3 tools/review.py <project> apply --ids=A,B,C --reviewer=NAME

**Nothing is applied without an explicit authorization** (`ADR-0100`), and an
accepted proposal becomes an authoring source, never a model write (`ADR-0106`).

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from compiler.apply import authorize, apply, _review_mode   # noqa: E402


def main(argv):
    opts = {a.split("=", 1)[0]: a.split("=", 1)[1]
            for a in argv if a.startswith("--") and "=" in a}
    argv = [a for a in argv if not a.startswith("--")]
    if len(argv) < 3:
        print(__doc__)
        return 2

    project = ROOT / argv[1]
    path = project / "candidate-engineering-model.json"
    if not path.exists():
        print(f"no candidate model at {path}\nrun: python3 discovery/run.py <repo> {argv[1]}")
        return 1
    cand = json.loads(path.read_text())
    cmd = argv[2]
    s = cand["statistics"]

    if cmd == "summary":
        modes = _review_mode()
        print(f"CANDIDATE ENGINEERING MODEL   {cand['repository']}")
        print(f"  digest {cand['digest']}\n")
        print(f"  {s['entities']} entities · {s['relationships']} relationships\n")
        print("  by support        review")
        for sup, n in s["bySupport"].items():
            print(f"    {sup:<28} {n:>4}   {modes.get(sup, '?')}")
        print("\n  by type")
        for t, n in s["byType"].items():
            print(f"    {t:<28} {n:>4}")
        print("\n  by worker")
        for w, n in s["byWorker"].items():
            print(f"    {w:<28} {n:>4}")
        print(f"\n  UNSETTLED   {s['ambiguities']} ambiguities · "
              f"{s['conflicts']} conflicts · {s['gaps']} gaps")
        return 0

    if cmd == "show":
        what = argv[3] if len(argv) > 3 else "gaps"
        for item in cand["unsettled"].get(what, []):
            if what == "ambiguities":
                print(f"  {item['about']}")
                for r in item["readings"]:
                    print(f"      · {r}")
                print(f"      [{item['provenance']['source']}]")
            elif what == "conflicts":
                print(f"  {item['about']}: {item['positions']}")
            else:
                print(f"  {item['what']}")
                print(f"      {item['why']}")
        return 0

    if cmd == "apply":
        types = set(opts["--types"].split(",")) if "--types" in opts else None
        ids = set(opts["--ids"].split(",")) if "--ids" in opts else None
        reviewer = opts.get("--reviewer")
        if not reviewer:
            print("--reviewer is required: an authorization must name who gave it "
                  "(ADR-0023)")
            return 2
        support = set(opts["--support"].split(",")) if "--support" in opts else None
        auth, rejected, diags = authorize(cand, accept_types=types, accept_ids=ids,
                                          accept_support=support, reviewer=reviewer)
        written = apply(auth, project)
        print(f"AUTHORIZED by {reviewer}")
        print(f"  accepted  {len(auth['entities'])} entities, "
              f"{len(auth['relationships'])} relationships")
        print(f"  left      {len(rejected['entities'])} entities unaccepted")
        for d in diags:
            print(f"  ! {d}")
        print(f"  written   {len(written)} authoring sources to {project.name}/model/")
        return 0

    print(f"unknown command {cmd!r}")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
