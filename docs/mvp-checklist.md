---
id: MVP-CHECKLIST
title: MVP closure checklist
status: current
created: 2026-08-02
updated: 2026-08-02
---

# MVP closure checklist

**Only externally observable requirements.** Nothing here is satisfied by
internal architecture, a design decision, or a passing unit test alone. Each
item is something a person outside this project can verify.

Reproduce the mechanical ones at any time:

```bash
python tools/check.py     # installation health
python tools/smoke.py     # the documented MVP path, in a clean workspace
```

## Status

| # | Requirement | State | Verified by |
|---|---|---|---|
| 1 | Installation works from a clean clone | **done** | `tools/check.py` — 12 checks pass |
| 2 | Every README command is verified | **done** | audited individually; two defects found and fixed |
| 3 | Quick Start completes | **done** | `tools/smoke.py` steps 2–5 |
| 4 | Brownfield onboarding can begin | **done** | `tools/smoke.py` step 6, on `examples/brownfield-demo` |
| 5 | A Candidate Engineering Model can be generated | **done** | `tools/smoke.py` step 7 |
| 6 | Human Curation can be launched | **done** | `tools/curate.py`; step 8 verifies it refuses unattended |
| 7 | Accepted proposals can be applied | **done** | `tools/review.py apply`, and the applier used by the lifecycle |
| 8 | CKM and all advertised projections are generated | **done** | six emitters, `tools/smoke.py` step 3 |
| 9 | Engineering Questions work | **done** | `tools/ask.py`, 17 queries, two engines agree |
| 10 | Engineering Guidance works | **done** | `tools/advise.py`, `tools/direct.py` |
| 11 | Continuous Acquisition documented and executable | **done** | `tools/lifecycle.py`, §14 |
| 12 | Periodic Reacquisition and Drift documented and executable | **done** | `tools/lifecycle.py`, `tools/drift-queue.py`, §15 |
| 13 | Limitations are explicit | **done** | README §21 |
| 14 | **One third-party engineer completes the flow without private guidance** | **NOT DONE** | — |

## The MVP is not complete

**Thirteen of fourteen. The one that is missing is the only one that cannot be
satisfied from inside this repository.**

Item 14 requires a person who did not build Engineering OS to clone it, install
it, onboard a system, curate proposals, and reach a useful result without asking
the authors anything. Until that happens the MVP is not complete, and no amount
of internal verification substitutes for it.

**Two things are needed and neither is code:**

1. **A third-party engineer**, with a repository on a supported stack —
   Node/NestJS/Drizzle or Java/Spring/JPA.
2. **A completed curation session.** Human Curation has never been performed by
   a human in this system. `tools/curate.py` refuses to run unattended
   precisely so that this gap cannot be closed by a script.

## What a third-party run should report

Nothing here is currently filled in, and nothing but a real session will fill it:

```text
did installation work from the README alone?            yes / no
where did you have to guess?
proposals generated · reviewed · authorized · corrected
review time, and accepted per minute
was the evidence sufficient to decide without asking?
which command's output did you not understand?
```

**A "no" anywhere in that list is the most valuable output this project can
currently receive.**
