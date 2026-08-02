---
id: ADR-0127
title: Engineering Knowledge and Engineering Understanding are different things and are never conflated
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0120, ADR-0122, ADR-0123, ADR-0128, ADR-0129]
---

# ADR-0127 — Knowledge is not understanding

## Context

The longitudinal experiment produced a result neither framing had a name for:
the model grew from 10 curated sources to **94**, and answered the same number
of engineering questions at the end as at the beginning.

The reviewer named what the experiment had actually measured:

> **Engineering Understanding is not equivalent to Engineering Knowledge. The
> model accumulated knowledge. Engineering Understanding did not improve. That
> distinction should remain explicit.**

and identified the result that matters:

> **The most important observation of the session is not the percentage. It is
> this sentence: "The model became larger without becoming more useful." That is
> the first product KPI that actually matters. Protect it.**

## Decision

**Knowledge Growth and Understanding Growth are separate measurements and are
never reported as one.**

| | Is | Measured as | Class |
|---|---|---|---|
| **Knowledge Growth** | more assertions in the model | curated sources, nodes, edges | **implementation telemetry** |
| **Understanding Growth** | more questions answerable | Engineering Question coverage (`ADR-0120`) | **product metric** |

**The two move independently, in both directions.**

- Knowledge may increase while understanding stays flat — *observed*: 10 → 94
  sources, 1/9 → 1/9 questions.
- Understanding may improve without much new knowledge — a single `constrains`
  edge would move two questions and adds no assertion at all.

**The protected sentence.** *"The model became larger without becoming more
useful"* is the KPI, and no aggregate may be introduced that could hide it. In
particular **no score may combine knowledge and understanding into one number**,
because such a score would rise on the run that produced this finding.

## Rationale

Conflating them is the natural failure mode of every system that builds a graph,
and this project has been doing it for forty-six sessions. Every published
result — 299 proposals, 453 proposals, 76 maintained nodes — was Knowledge
Growth reported as progress.

The distinction is not philosophical. It is **diagnostic**, and it points
directly at cause: knowledge is nodes, understanding is what connects them, and
the longitudinal model has 94 nodes and 36 edges.

## Consequences

**Every report states both, and states which is which.** `tools/longitudinal.py`
labels Knowledge Growth as implementation telemetry in its own output, so the
distinction survives being read quickly.

**A session that adds knowledge and moves no question has produced telemetry.**
That is not a failure — Acquisition is a real verb (`ADR-0123`) — but it may not
be reported as product progress.

**The reverse case is now expected to be common.** The known fix to Continuous
Acquisition adds *no new assertions*; it preserves relationships that already
have evidence. If it works it will move understanding while leaving knowledge
untouched, which under the old framing would have looked like a session that
did nothing.

## Compliance

- No metric combines a count of assertions with a count of answered questions.
- Reports label counts as implementation telemetry explicitly.
- The sentence *"the model became larger without becoming more useful"* remains
  expressible: any proposed metric must be able to produce it.
