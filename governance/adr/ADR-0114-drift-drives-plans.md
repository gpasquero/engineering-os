---
id: ADR-0114
title: Each drift class routes to an Engineering Plan; a drift report is a work queue
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0091, ADR-0094, ADR-0096, ADR-0101, ADR-0112]
---

# ADR-0114 — Drift drives plans

## Context

The first real Knowledge Drift Report produced **238 items in four classes**, and
every one is a proposal requiring review.

**A report nobody can act on is worse than no report**, because it converts a
known gap into a false sense of coverage — a risk `ADR-0112` recorded and did not
address.

> **Different drift classes should drive different Engineering Plans.**

## Decision

**Every drift class routes to an Engineering Plan.** A drift report stops being a
document and becomes **a work queue**.

| Drift class | Plan | Because the right response is |
|---|---|---|
| `D-unsupported-assertion` | `P-review-unsupported` | **retract or re-evidence** — the evidence may have moved, or the system may have changed |
| `D-implementation-without-knowledge` | `P-discover` | extend the model over what exists |
| `D-knowledge-without-implementation` | `P-verify-capability` | confirm the capability exists, or retract the claim |
| `D-invariant-without-enforcement` | `P-establish-enforcement` | find the enforcement point, or record that none exists |
| `D-conflicting-interpretation` | `P-resolve-conflict` | a human decides; no rule can |
| `D-obsolete-rationale` | `P-change-concept` | the decision behind it no longer stands |
| `D-boundary-change` · `D-architectural-drift` | `P-change-capability` | the structure moved |
| `D-business-rule-drift` | `P-change-concept` | the domain moved |
| `D-missed-incremental-update` | `P-review-unsupported` | continuous acquisition did not keep up, and the maintained model is now suspect |
| `D-stale-provenance` · `D-missing-evidence` | `P-discover` | the citation, not the claim, is what failed |
| `D-new-knowledge` · `D-dependency-change` | *none* | additive; curation alone suffices |
| `D-unexplained-divergence` | *none* | **by definition unroutable** |

### Routing is declared, not inferred

The mapping lives in `model/drift-categories.md` beside the classes themselves.
Adding a class without a route is a visible omission rather than a silent one.

### Two classes route nowhere, deliberately

`D-new-knowledge` and `D-dependency-change` are **additive** — curation accepts
or declines them and no engineering work follows.

`D-unexplained-divergence` is the residual, and **a route for it would be a
guess.** It escalates to a human by having nowhere else to go.

### A routed drift item is not a task

It produces **a plan**, and a plan defers what it cannot decide (`ADR-0094`). The
routing says *what kind of work this is*, not *what to do*.

## Alternatives considered

**One plan for all drift.** Rejected — it is the current state. *Review this
drift* is not actionable, and the four classes in the first report need four
different first steps.

**Route by severity.** Rejected under `ADR-0090`: severity is a score, and the
useful distinction is **kind**, not magnitude. One `D-unsupported-assertion` may
matter more than 123 `D-implementation-without-knowledge`.

**Generate plans automatically for every item.** Rejected: 238 items would
produce 238 plans, which is a work queue nobody can face. **Routing says which
plan applies; instantiating it is a curation decision.**

## Consequences

### Positive

- **The drift report becomes actionable**, which is the difference between a
  capability and a report.
- It connects two halves of the system that had never touched: acquisition
  produces drift, and direction consumes it.
- **`P-review-unsupported` finally exercises the retraction path**, which exists
  and has never fired.

### Negative

- **Three plans are named and do not exist** — `P-review-unsupported`,
  `P-verify-capability`, `P-establish-enforcement`. The routing is declared
  ahead of its targets, and a route to a missing plan is a broken promise until
  they are written.
- **Routing is a judgement.** That `D-invariant-without-enforcement` calls for
  finding an enforcement point rather than retracting the invariant is an
  engineering opinion encoded as data, and the opposite is defensible.

### Neutral

- No metamodel change. Routing is a field on an existing registry.

## Compliance

`model/drift-categories.md` declares a `routes-to` field per class. A class with
no route states why. **A drift item produces a plan, never a task.**
