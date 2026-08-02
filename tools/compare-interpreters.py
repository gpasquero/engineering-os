#!/usr/bin/env python3
"""Compare interpreter outputs over one frozen Mechanical Model.

    python3 tools/compare-interpreters.py <project>

Every interpreter must have consumed the same Mechanical Model digest; the
comparison refuses to run otherwise, because two interpreters that saw different
evidence are not comparable (`ADR-0108`).

Measures the axes the benchmark separates: **volume, abstraction and
cross-source synthesis** — reported separately and never combined into a score
(`ADR-0090`).

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import json
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from discovery.interpretive import interpret, STRATEGIES  # noqa: E402
from discovery.candidate import Candidate             # noqa: E402


def _distribution_claim(text):
    """A claim comparing a fact against its own population."""
    t = (text or "").lower()
    return any(k in t for k in ("only one", "exactly one", "of 161", "of the",
                                "every other", "all other", "distribution",
                                "outlier", "unlike", "unique among", "sole"))


def load_probabilistic(path, label):
    if not path.exists():
        return None
    d = yaml.safe_load(path.read_text())
    props = d.get("proposals") or []
    return {
        "label": label,
        "digest": d.get("mechanical-model-digest"),
        "proposals": len(props),
        "byType": {t: sum(1 for p in props if p.get("type") == t)
                   for t in sorted({p.get("type") for p in props if p.get("type")})},
        "distribution": sum(1 for p in props
                            if p.get("population-compared")
                            or _distribution_claim(p.get("reasoning", ""))
                            or _distribution_claim(p.get("label", ""))),
        "withPopulation": sum(1 for p in props if p.get("population-compared")),
        "uncertainty": {u: sum(1 for p in props if p.get("uncertainty") == u)
                        for u in ("low", "medium", "high")},
        "gaps": len(d.get("gaps") or []),
        "ids": sorted(p["id"] for p in props if p.get("id")),
    }


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    project = ROOT / argv[1]
    # Load the FROZEN model the probabilistic workers were given. Re-extracting
    # would compare deterministic rules against a model no probabilistic worker
    # saw — which is the incomparability this harness exists to refuse. The
    # frozen input is the benchmark's fixed point, not the repository.
    frozen = project / "experiment/blind/INPUT-mechanical-model.json"
    if not frozen.exists():
        frozen = project / "mechanical-engineering-model.json"
    mech = json.loads(frozen.read_text())
    digest = mech["digest"]
    print(f"  frozen input: {frozen.relative_to(ROOT)}")

    rows = []
    for strategy in STRATEGIES:
        c = Candidate(mech.get("repository", "unknown"), argv[1])
        interpret(mech, c, strategy)
        m = c.serialize()
        invs = [e for e in m["proposals"]["entities"] if e["type"] == "Invariant"]
        rows.append({
            "label": strategy, "digest": digest,
            "proposals": m["statistics"]["entities"],
            "byType": m["statistics"]["byType"],
            "concepts": sum(1 for e in invs
                            if (e.get("attributes") or {}).get("granularity") == "concept"),
            "guarantees": sum(1 for e in invs
                              if (e.get("attributes") or {}).get("granularity") == "guarantee"),
            "invariants": len(invs),
            "distribution": 0, "withPopulation": 0,
            "gaps": m["statistics"]["gaps"], "reproducible": True,
        })

    exp = project / "experiment"
    for path, label in ((exp / "probabilistic-proposals.yaml", "claude (contaminated)"),
                        (exp / "blind" / "OUTPUT-proposals.yaml", "claude (blind)")):
        got = load_probabilistic(path, label)
        if got:
            got["reproducible"] = False
            got.setdefault("invariants", got["byType"].get("Invariant", 0))
            got.setdefault("concepts", 0)
            got.setdefault("guarantees", 0)
            rows.append(got)

    bad = [r["label"] for r in rows if r["digest"] and r["digest"] != digest]
    if bad:
        print(f"REFUSING TO COMPARE — these saw a different Mechanical Model: {bad}")
        print(f"  expected digest {digest}")
        return 1

    print(f"COMPARATIVE INTERPRETIVE ACQUISITION")
    print(f"  one frozen Mechanical Model, digest {digest}\n")
    w = max(len(r["label"]) for r in rows)
    print(f"  {'interpreter':<{w}}  {'props':>6} {'invar':>6} {'concept':>8} "
          f"{'guaran':>7} {'distrib':>8} {'gaps':>5}  reproducible")
    print("  " + "-" * (w + 52))
    for r in rows:
        print(f"  {r['label']:<{w}}  {r['proposals']:>6} {r.get('invariants',0):>6} "
              f"{r.get('concepts',0):>8} {r.get('guarantees',0):>7} "
              f"{r.get('distribution',0):>8} {r.get('gaps',0):>5}  "
              f"{'exactly' if r['reproducible'] else 'no'}")

    print("\n  Volume, abstraction and cross-source synthesis are separate axes")
    print("  and are never combined into a score (ADR-0090).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
