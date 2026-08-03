#!/usr/bin/env python3
"""Measure a repository by the engineering questions answered (ADR-0120).

    python3 tools/measure.py external/wa-b2b-onboarding
    python3 tools/measure.py external/wa-b2b-onboarding external/ai-desk-lifecycle

**Not entities, predicates, graph size or proposal count.** Those are
implementation metrics. This reports the percentage of the registered
Engineering Question Set that Engineering OS can answer about a compiled model.

A question is scored against its declared queries, over the subject types it is
asked about:

    answered   rows for at least `threshold` of eligible subjects
    partial    rows, but for fewer
    no-data    a query exists and returns nothing anywhere
    no-query   nothing declared even attempts the question

The last two are different findings and are never merged. `no-data` says the
model is thin. **`no-query` says Engineering OS never learned to ask.**

Semantic Layer: None -- cross-cutting infrastructure (ADR-0039).
"""
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from _cli import help_requested, project as project_arg  # noqa: E402

from compiler import compile_project                            # noqa: E402
from compiler.registry import load_all                          # noqa: E402
from compiler.query import Model, run, load_queries             # noqa: E402

GREEN, RED, YELLOW, BLUE, DIM, OFF = ("\033[32m", "\033[31m", "\033[33m",
                                      "\033[34m", "\033[2m", "\033[0m")
MARK = {"answered": (GREEN, "ANSWERED"), "partial": (YELLOW, "PARTIAL "),
        "no-data": (RED, "NO DATA "), "no-query": (BLUE, "NO QUERY")}


def score(ckm, question, queries):
    """Returns (state, answered_subjects, eligible_subjects)."""
    qids = question.get("answered-by") or []
    if not qids:
        return "no-query", 0, 0

    # A query declared `subject: none` returns the SAME rows whatever subject it
    # is handed. Scoring it per subject reports 453/453 and means nothing — the
    # first version of this tool did exactly that and scored the weakest
    # question in the set as a perfect answer. It is one boolean.
    declared = [queries[x] for x in qids if x in queries]
    model_wide = [q for q in declared if q.get("subject") == "none"]
    per_subject = [q for q in declared if q.get("subject") != "none"]
    if not per_subject:
        got = any(run(Model(ckm), q, None)["rows"] for q in model_wide)
        return ("answered" if got else "no-data"), int(got), 1

    types = question.get("subject-types") or []
    subjects = [n["id"] for n in ckm["nodes"] if not types or n["type"] in types]
    if not subjects:
        # No subject of the right type is itself a shortage of understanding,
        # not an inapplicable question: the repository has capabilities and
        # concepts whatever the model managed to record.
        return "no-data", 0, 0

    model = Model(ckm)
    answered = 0
    for s in subjects:
        for q in per_subject:
            allowed = q.get("applies-to") or []
            node_type = model.by_id[s]["type"]
            if allowed and node_type not in allowed:
                continue
            if run(model, q, s)["rows"]:
                answered += 1
                break

    if answered == 0:
        return "no-data", 0, len(subjects)
    ratio = answered / len(subjects)
    threshold = float(question.get("threshold", 0.5))
    return ("answered" if ratio >= threshold else "partial"), answered, len(subjects)


def score_all(ckm, questions, queries):
    """Reusable scoring, so the longitudinal experiment measures the same way."""
    rows = [(qid, q) + score(ckm, q, queries) for qid, q in questions.items()]
    states = {qid: state for qid, _, state, _, _ in rows}
    answered = sum(1 for s in states.values() if s == "answered")
    return {"answered": answered, "total": len(rows), "states": states,
            "rows": rows}


# ── Understanding Retention (ADR-0128) ────────────────────────────────────
#
# Coverage says how much is answered. **Retention says whether what was once
# answered still is** — and the two can move independently. The longitudinal run
# held coverage at 1/9 for ten steps while the ONE question answered at t0 was
# lost and a different one gained. Coverage called that stability.

RANK = {"no-query": 0, "no-data": 1, "partial": 2, "answered": 3}


def retention(before, after):
    """Compare two `score_all` results. Returns per-question movement.

    The three states the reviewer named — remained answered, degraded to
    partial, became unanswered — are reported over the questions that WERE
    answered. Gains are reported separately: a gain is Understanding Growth, and
    counting it as retention would let a system that forgets everything and
    learns something else score perfectly.
    """
    moves, was = {}, [q for q, s in before.items() if s == "answered"]
    for qid, prev in before.items():
        now = after.get(qid, "no-data")
        if prev == "answered":
            moves[qid] = ("retained" if now == "answered" else
                          "degraded" if now == "partial" else "lost")
        elif now == "answered":
            moves[qid] = "gained"
        elif RANK[now] > RANK[prev]:
            moves[qid] = "improved"
        elif RANK[now] < RANK[prev]:
            moves[qid] = "weakened"
        else:
            moves[qid] = "unchanged"
    retained = sum(1 for q in was if moves[q] == "retained")
    return {"moves": moves, "previouslyAnswered": len(was), "retained": retained,
            "degraded": sum(1 for q in was if moves[q] == "degraded"),
            "lost": sum(1 for q in was if moves[q] == "lost"),
            "gained": sum(1 for m in moves.values() if m == "gained"),
            "rate": (retained / len(was)) if was else None}


def measure(project, questions, queries):
    ckm, problems = compile_project(project)
    if problems:
        raise SystemExit(f"{project}: {len(problems)} diagnostic(s); "
                         f"first: {problems[0]}")
    rows = []
    for qid, question in questions.items():
        state, got, total = score(ckm, question, queries)
        rows.append((qid, question, state, got, total))
    return ckm, rows


def main(argv):
    if help_requested(argv):
        print(__doc__)
        return 0
    if len(argv) < 2:
        print(__doc__)
        return 2
    questions = load_all()["REG-engineering-questions"]
    queries = load_queries()

    summaries = []
    for arg in argv[1:]:
        project = project_arg(arg)
        ckm, rows = measure(project, questions, queries)
        name = project.name
        print(f"\n{name}  {DIM}{ckm['statistics']['nodes']} nodes, "
              f"{ckm['statistics']['edges']} edges{OFF}")
        print(f"{DIM}{'─' * 72}{OFF}")
        for qid, question, state, got, total in rows:
            colour, label = MARK[state]
            detail = f"{got}/{total}" if total else ""
            print(f"  {colour}{label}{OFF}  {question['question']}")
            print(f"            {DIM}{qid}   {detail}   "
                  f"{', '.join(question.get('answered-by') or ['—'])}{OFF}")
        answered = sum(1 for *_, state, _, _ in [(r[0], r[1], r[2], r[3], r[4])
                                                 for r in rows] if state == "answered")
        pct = 100 * answered / len(rows)
        summaries.append((name, answered, len(rows), pct, rows))
        print(f"\n  {GREEN if pct >= 50 else RED}"
              f"{answered}/{len(rows)} engineering questions answered "
              f"({pct:.0f}%){OFF}")

    if len(summaries) > 1:
        print(f"\n{DIM}{'─' * 72}{OFF}\nComparison")
        for name, answered, total, pct, _ in summaries:
            print(f"  {name:<26} {answered}/{total}  {pct:.0f}%")
        base = summaries[0][4]
        # `no-data` is evidence ABOUT A REPOSITORY: a model was built and still
        # could not answer. `no-query` is a constant — it says the same thing in
        # every repository and can never accumulate, so it is never counted as
        # repeated evidence under ADR-0119.
        repeated = [base[i][0] for i in range(len(base))
                    if all(s[4][i][2] == "no-data" for s in summaries)]
        constant = [base[i][0] for i in range(len(base))
                    if all(s[4][i][2] == "no-query" for s in summaries)]
        if repeated:
            print(f"\n  {RED}unanswered in every repository measured{OFF} "
                  f"{DIM}— repeated evidence under ADR-0119{OFF}")
            for qid in repeated:
                print(f"    {qid}  {questions[qid]['question']}")
        if constant:
            print(f"\n  {BLUE}no declared query attempts these{OFF} "
                  f"{DIM}— a constant, not repository evidence{OFF}")
            for qid in constant:
                print(f"    {qid}  {questions[qid]['question']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
