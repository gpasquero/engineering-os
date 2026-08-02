#!/usr/bin/env python3
"""Guidance Preservation — ten commits later, is the recommended work the same?

    python3 tools/guidance.py <project-a> <project-b>

**The first measurement directly connected to customer value** (`ADR-0139`).

Understanding Preservation asks whether the same questions still answer. This
asks something a customer feels more directly: **whether Engineering OS would
still tell a team to do the same work.**

The two are not the same property, and the reason is `ADR-0138`:

> Two systems may answer exactly the same Engineering Questions while
> recommending different engineering actions.

## What is measured, and what is deliberately not

Guidance **should** change when the system changes. A recommendation that
ignored nine commits of real work would be preserving staleness, not
understanding.

So the measurement is narrower and it is the only version that means anything:

> **For a subject whose evidence nobody touched, is the recommended work the
> same?**

An unchanged subject that receives different advice has been affected by
something other than the system — and that is guidance drift.

A recommendation is fingerprinted as its status plus, per action, the sorted
ids of the work it names. Prose is excluded: two recommendations that name the
same work in different words are the same guidance.

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from compiler import compile_project                                # noqa: E402
from compiler.recommend import load_recommendations, advise, applicable  # noqa: E402
from compiler.query import Model, load_queries                      # noqa: E402

GREEN, RED, YELLOW, DIM, OFF = ("\033[32m", "\033[31m", "\033[33m",
                                "\033[2m", "\033[0m")


def fingerprint(model, rec, subject, queries):
    """The recommended WORK, with the wording removed."""
    if applicable(model, rec, subject):
        return None
    result = advise(model, rec, subject, queries)
    steps = []
    for step in result.get("steps") or []:
        rows = sorted(r["id"] for r in (step.get("rows") or []))
        steps.append((step.get("action"), tuple(rows)))
    return (result.get("status"), tuple(sorted(steps)))


def guidance(ckm_before, ckm_after, untouched=None):
    """Compare the work recommended by two models over their common subjects."""
    recs, queries = load_recommendations(), load_queries()
    before, after = Model(ckm_before), Model(ckm_after)
    common = sorted(set(before.by_id) & set(after.by_id))
    if untouched is not None:
        common = [c for c in common if c in untouched]

    rows, counts = [], {"stable": 0, "changed": 0, "lost": 0, "gained": 0}
    for subject in common:
        for rid, rec in sorted(recs.items()):
            if not rec.get("applies-to"):
                continue                       # model-wide advice has no subject
            fb = fingerprint(before, rec, subject, queries)
            fa = fingerprint(after, rec, subject, queries)
            if fb is None and fa is None:
                continue
            if fb is None:
                state = "gained"
            elif fa is None:
                state = "lost"
            elif fb == fa:
                state = "stable"
            else:
                state = "changed"
            counts[state] += 1
            rows.append({"subject": subject, "recommendation": rid,
                         "state": state,
                         "before": fb and fb[0], "after": fa and fa[0]})

    judged = counts["stable"] + counts["changed"] + counts["lost"]
    return {"counts": counts, "rows": rows, "subjects": len(common),
            "judged": judged,
            "rate": (counts["stable"] / judged) if judged else None}


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    models = []
    for arg in argv[1:]:
        ckm, problems = compile_project(ROOT / arg)
        if problems:
            raise SystemExit(f"{arg}: {len(problems)} diagnostic(s)")
        models.append(ckm)
    result = guidance(*models)
    c = result["counts"]
    print(f"  {result['subjects']} common subjects, {result['judged']} "
          f"subject/recommendation pairs judged\n")
    for state, colour in (("stable", GREEN), ("changed", YELLOW),
                          ("lost", RED), ("gained", GREEN)):
        print(f"    {colour}{state:8}{OFF} {c[state]}")
    rate = "—" if result["rate"] is None else f"{100 * result['rate']:.0f}%"
    print(f"\n  Guidance Preservation  {rate}")
    for row in result["rows"]:
        if row["state"] in ("changed", "lost"):
            print(f"    {YELLOW if row['state'] == 'changed' else RED}"
                  f"{row['state']:8}{OFF} {row['subject']}  {row['recommendation']}"
                  f"  {DIM}{row['before']} → {row['after']}{OFF}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
