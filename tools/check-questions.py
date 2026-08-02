#!/usr/bin/env python3
"""Verify the Engineering Question Set (ADR-0120).

The product metric is a declaration, and a declaration can be wrong in ways that
flatter the product. Both defects found on the metric's first run did exactly
that, so the properties that prevent them are checked:

  * **every named query exists** — a mapping to a query that was renamed would
    silently score `no-query`, which reads as an honest gap and is a typo;
  * **no mixed mapping** — a question may not pair a `subject: none` query with a
    per-subject one. The model-wide query answers for every subject and the
    question scores 100 %. `EQ-09` did precisely this;
  * **the subject types overlap the queries' `applies-to`** — a question asked
    about types no mapped query accepts can never be answered, and would be
    reported as a fact about the repository;
  * **every question declares an author, and a threshold in (0, 1]**.

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from compiler.registry import load_all       # noqa: E402
from compiler.query import load_queries      # noqa: E402

GREEN, RED, DIM, OFF = "\033[32m", "\033[31m", "\033[2m", "\033[0m"


def main():
    questions = load_all()["REG-engineering-questions"]
    queries = load_queries()
    bad = []

    for qid, q in sorted(questions.items()):
        for field in ("question", "author", "matters-because", "subject-types"):
            if not q.get(field):
                bad.append(f"{qid}: missing {field!r}")
        threshold = q.get("threshold")
        if not isinstance(threshold, (int, float)) or not 0 < threshold <= 1:
            bad.append(f"{qid}: threshold must be in (0, 1], got {threshold!r}")

        named = q.get("answered-by") or []
        missing = [x for x in named if x not in queries]
        if missing:
            bad.append(f"{qid}: unknown quer{'y' if len(missing) == 1 else 'ies'} "
                       f"{', '.join(missing)}")
            continue
        if not named:
            continue

        modes = {queries[x].get("subject") == "none" for x in named}
        if len(modes) > 1:
            bad.append(f"{qid}: mixes a model-wide query with a per-subject one; "
                       f"the model-wide one answers for every subject")
            continue
        if True in modes:
            continue

        types = set(q["subject-types"])
        reachable = set()
        for x in named:
            allowed = queries[x].get("applies-to")
            reachable |= types if not allowed else (types & set(allowed))
        if not reachable:
            bad.append(f"{qid}: asked about {', '.join(sorted(types))}, and no "
                       f"mapped query accepts any of them")

    for b in bad:
        print(f"  {RED}{b}{OFF}")
    print()
    if bad:
        print(f"{RED}{len(bad)} finding(s) in the Engineering Question Set{OFF}")
        return 1
    unanswerable = sum(1 for q in questions.values() if not q.get("answered-by"))
    print(f"{GREEN}the Engineering Question Set is well formed{OFF} "
          f"{DIM}({len(questions)} questions, {unanswerable} with no query "
          f"declared){OFF}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
