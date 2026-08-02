#!/usr/bin/env python3
"""Verify that every plan phase can do something (SESSION-0044).

A plan phase **borrows a recommendation's steps, not its applicability**. The
plan declares `applies-to`; each step's query declares its own. Nothing checked
that the two overlapped, so a phase could borrow steps that can never apply to
the plan's own subjects — and, before this session, said nothing when they did
not.

The check runs **per subject type**, because that is the granularity at which
the defect hid: `P-review-unsupported` applies to four types, and its `assess`
phase borrows a single step whose query accepts only `Artifact`. Asking whether
the phase works *for the plan* answers yes; asking whether it works *for an
Invariant* answers no, which is the question a team asks.

Two conditions, and only the first is an error:

  * **a dead phase** — no borrowed step applies to *any* of the plan's subject
    types. It can never produce an action, in any model. An authoring defect;
  * **a hollow phase** — empty for some declared subject types and not others.
    Legitimate, since one plan serves several types, but it must be visible:
    reported here at authoring time, and named by the planner at planning time
    (`compiler/plan`). Silence is what let it hide across five plans.

A query with no `applies-to` accepts every subject type.

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from compiler.plan import load_plans                       # noqa: E402
from compiler.query import load_queries                    # noqa: E402
from compiler.recommend import load_recommendations        # noqa: E402

GREEN, RED, YELLOW, DIM, OFF = ("\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[0m")


def main():
    plans = load_plans()
    queries, recommendations = load_queries(), load_recommendations()
    dead, hollow = [], []

    # A subject-scoped recommendation whose step uses a `subject: none` query
    # gives every subject the same answer for that step, and that answer moves
    # whenever the REST of the model moves. Found by Guidance Preservation:
    # two untouched artifacts received different advice across ten commits
    # because the model had grown around them (SESSION-0050).
    #
    # Third appearance of one authoring error — after EQ-09 scoring 216/216 and
    # EQ-05's mixed mapping. Each time a new consumer was built, the same
    # mistake was waiting in a new place. Reported, not failed: whether the step
    # BELONGS there is the author's call, and being unable to see it was not.
    leaks = []
    for rid, rec in sorted(recommendations.items()):
        if not rec.get("applies-to"):
            continue
        for step in rec.get("steps") or []:
            q = queries.get(step.get("query"))
            if q is not None and q.get("subject") == "none":
                leaks.append((rid, step["action"], step["query"]))

    for pid, plan in sorted(plans.items()):
        subjects = plan.get("applies-to") or []
        for phase in plan.get("phases") or []:
            rec = recommendations[phase["recommendation"]]
            borrowed = [s for s in rec["steps"]
                        if s["action"] in (phase.get("actions") or [])]
            if not borrowed:
                continue
            empty_for = []
            for subject in subjects:
                live = [s for s in borrowed
                        if subject in (queries[s["query"]].get("applies-to")
                                       or [subject])]
                if not live:
                    empty_for.append(subject)
            where = f"{pid}.{phase['id']}"
            qs = sorted({s["query"] for s in borrowed})
            if subjects and len(empty_for) == len(subjects):
                dead.append((where, qs, subjects))
            elif empty_for:
                hollow.append((where, qs, empty_for))

    for where, qs, subjects in dead:
        print(f"  {RED}DEAD{OFF}    {where}")
        print(f"          {DIM}no step applies to any of {', '.join(subjects)}"
              f" — {', '.join(qs)}{OFF}")
    for where, qs, empty_for in hollow:
        print(f"  {YELLOW}HOLLOW{OFF}  {where}")
        print(f"          {DIM}produces nothing for {', '.join(empty_for)}"
              f" — {', '.join(qs)}{OFF}")

    for rid, action, qid in leaks:
        print(f"  {YELLOW}MODEL-WIDE{OFF}  {rid}.{action}")
        print(f"          {DIM}{qid} is declared `subject: none`; every subject "
              f"gets the same answer{OFF}")

    print()
    if dead:
        print(f"{RED}{len(dead)} phase(s) can never produce an action{OFF}")
        return 1
    note = (f" — {len(hollow)} hollow for some subject type, each named by the planner"
            if hollow else "")
    if leaks:
        note += f"; {len(leaks)} model-wide step(s) inside subject-scoped advice"
    print(f"{GREEN}every plan phase can act on at least one of its subject types{OFF}{note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
