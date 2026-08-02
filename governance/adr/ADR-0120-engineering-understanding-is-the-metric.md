---
id: ADR-0120
title: Engineering understanding is the product metric; entity counts are implementation metrics
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0023, ADR-0084, ADR-0086, ADR-0089, ADR-0116, ADR-0119]
---

# ADR-0120 — Engineering understanding is the product metric

## Context

Every measurement this project has published is a count of something it
produced: 299 proposals, 453 proposals, 23 entities, 691 relationships, 76
maintained nodes.

The second benchmark made the problem impossible to ignore. `wa-b2b` produced
**453 proposals** — the largest model Engineering OS has ever built — and could
not answer why anything is the way it is, or who is allowed to do anything.

**By every metric the project had, that run was its best result.**

The reviewer named the correction:

> **The percentage of useful engineering questions that Engineering OS can
> answer is becoming a much more meaningful product metric than entities
> discovered, predicates extracted, graph size, proposal count. Those remain
> implementation metrics. Engineering understanding is the product metric.**

## Decision

**The product metric is the percentage of the registered Engineering Question
Set that Engineering OS can answer about a repository.**

`model/engineering-questions.md`, registered as `REG-engineering-questions`,
declares nine questions. Each names the queries that would answer it, the
subject types it is asked about, and a threshold. `tools/measure.py` scores a
compiled model against all nine.

Counts are not forbidden. **They are demoted**, and must never be reported as a
result on their own.

**Four outcomes, and two of them are distinct findings that may never be
merged:**

| | |
|---|---|
| `answered` · `partial` | how much of the model supports the question |
| **`no-data`** | a query exists and this model cannot answer it — **evidence about the repository** |
| **`no-query`** | nothing declared even attempts the question — **evidence about Engineering OS** |

`no-query` is a **constant**. It says the same thing about every repository, so
it can never accumulate into the repeated evidence `ADR-0119` requires. Only
`no-data` can.

## The set is authored by the reviewer

**The implementer may not add a question they know passes.**

A metric whose author also builds the thing measured will drift toward what the
thing already does. This is the same conflict `ADR-0023` forbids for acceptance,
and it applies with more force here, because a metric is easier to bend than an
approval.

Thresholds are deliberately low — a quarter of eligible subjects. **The first
measurements should be embarrassing rather than flattering.**

## Rationale

The metric earns its place immediately by being unflattering in a *useful*
direction:

```text
wa-b2b     2/9   22%      453 nodes
ai-desk    3/9   33%       76 nodes
```

**The six-times-larger model understands less.** No count could have said that;
this one says it in two lines.

It also produces `ADR-0119`'s repeated evidence automatically, which was
previously a judgement call: `EQ-01` and `EQ-05` return `no-data` in both
repositories, and both need the same missing thing — decisions connected to what
they established.

## Consequences

**Measuring exposed two defects in the measurement.** The first version scored
`EQ-09` at `216/216` because its query is declared `subject: none` and returns
the same rows whatever subject it is handed. The second scored a mixed mapping
the same way.

> **A metric is a query too, and it must be validated like one.** Both defects
> flattered the product, which is the direction metric defects always take.

**Existing reports are not retracted.** Counts published before this decision
were accurate; they were merely answering an implementation question. Benchmark
reports from now on lead with the question score.

**Sessions are judged by movement in this number.** A session that adds entities
and moves it by nothing has produced implementation, not product.

## Compliance

- `model/engineering-questions.md` is the only source of the question set.
- `tools/measure.py` implements no question and reports `no-data` and
  `no-query` separately.
- Benchmark reports state the question score before any count.
- A question is added, and a threshold raised, only by the reviewer.
