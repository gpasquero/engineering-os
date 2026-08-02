---
id: ADR-0132
title: A metric may not become primary if it can rise while understanding deteriorates
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0067, ADR-0075, ADR-0084, ADR-0089, ADR-0102, ADR-0116, ADR-0120, ADR-0127, ADR-0128]
---

# ADR-0132 — The metric admission test

## Context

The project has six admission tests, each governing what may be **built**. None
governs what may be **measured** — and the last two sessions showed that a
metric can fail in exactly the way a feature can, while looking like progress.

Coverage held at `1/9` for ten commits while the question a team relied on was
lost. Before that, proposal counts rose across two repositories while
understanding fell. **Both were true numbers reporting the opposite of what had
happened.**

The reviewer supplied the test:

> **Understanding Retention is now the primary longitudinal KPI. Protect it. Do
> not let future aggregate metrics hide it again. Every future metric should be
> evaluated against this question: "Could this metric increase while Engineering
> Understanding deteriorates?" If the answer is yes, it cannot become the
> primary product metric.**

## Decision

**Before a metric becomes primary, ask: *could this metric increase while
Engineering Understanding deteriorates?*** If yes, it may be reported — as
implementation telemetry (`ADR-0127`) — and it may not be primary.

The seventh admission test, and the first that governs measurement rather than
construction.

| Metric | Could it rise while understanding falls? | Status |
|---|---|---|
| proposal count · nodes · edges · predicates | **yes**, trivially | telemetry |
| curated sources | **yes** — observed, 10 → 94 at flat coverage | telemetry |
| maintenance cost | **yes** — cheapest when nothing is preserved | telemetry |
| Question coverage | **yes** — observed, hid a total turnover | **secondary** |
| **Understanding Retention** | **no** — it is defined over what was answerable | **primary** |

**Coverage is demoted, not discarded.** It is the only metric that shows
understanding *growing*; retention only shows it *surviving*. Neither alone is
enough, and **retention decides the verdict**.

## Rationale

The test is cheap and it is decisive: it asks for a **counter-example**, and a
metric for which one exists has already been shown to be capable of lying.

Every metric this project has ever had fails it except one. That is not an
indictment of the metrics — counts were the right thing to report when the
question was *can we acquire anything at all?* It is a statement that the
question changed and the measurements did not follow.

**An aggregate is the specific danger named.** Any score combining coverage with
knowledge would rise on the ten-commit run that lost `EQ-06`. `ADR-0127` already
forbids that combination; this decision generalises the prohibition to metrics
not yet invented.

## Consequences

**Understanding Retention is the primary longitudinal KPI**, and the frozen
suite (`ADR-0129`) is where it is read.

**A metric that fails the test may still be valuable.** Maintenance cost fails it
and is reported at every step, because a preservation fix that made maintenance
cost as much as a rerun would be a real regression — just not a *product* one.

**Retention has a known weakness and it is recorded rather than hidden:** it is
defined over a small baseline, so it is coarse. Its remedy is better coverage,
which is why coverage stays.

## Compliance

- A proposed metric states its answer to the test, with a counter-example if the
  answer is yes.
- No aggregate combines a primary metric with telemetry.
- Verdicts are read from retention; coverage qualifies them.
