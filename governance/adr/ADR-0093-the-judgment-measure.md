---
id: ADR-0093
title: Success is measured by how much engineering judgment happens before an LLM must think
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0061, ADR-0084, ADR-0089, ADR-0090, ADR-0092]
---

# ADR-0093 — The judgment measure

## Context

The project has measured itself by entities, ADRs, compiler features and
queries. **All four are counts of what was built, not of what the system can
do.**

## Decision

**Measure how much engineering judgment Engineering OS can perform before an LLM
needs to think.**

> **That number should continuously increase.**

### Made concrete

An Engineering Plan reports two counts:

| | Is |
|---|---|
| **derived** | a fact or action the plan states **because a query returned it** |
| **deferred** | a decision the plan **explicitly hands to a human or an executor** |

The measure is `derived` against `deferred`, **and both must be enumerated**. A
plan that silently omits a decision scores well and is worse than one that names
it.

### What makes this honest

**Deferred items are listed individually, not counted.** *This plan defers 4
decisions* is a metric; *this plan cannot tell you whether the ownership rule
change is source-compatible* is information.

**Deferring is not failure.** Much of engineering judgement is genuinely not
derivable, and `ADR-0092` forbids inventing it. A plan that defers correctly is
better than one that guesses.

### What this replaces

Counts of entities, ADRs, compiler features and queries **stop being reported as
progress**. They remain in the build state as inventory.

## Alternatives considered

**Measure tokens or LLM calls saved.** Rejected: it measures a consumer's
implementation rather than this system's capability, and would improve by making
plans longer.

**Measure plan completeness against a human-written plan.** Rejected as
unavailable — nobody writes those for these systems — and as the wrong target.
Matching a human plan is not the same as reducing what the human must decide.

**A single score.** Rejected under `ADR-0090`. Two enumerated lists carry
information a ratio destroys, and the ratio invites optimising the denominator.

## Consequences

### Positive

- **It makes deferral visible and cheap to state**, which is the behaviour
  `ADR-0092`'s determinism constraint requires.
- It gives every future capability a direction: move an item from deferred to
  derived, or state a new deferral honestly.
- **The measure is computed by the system about itself**, from the same queries
  that produce the plan.

### Negative

- **It is gameable by inflating `derived`.** Listing eight trivially derived
  facts scores better than one hard one, and nothing weights them.
- **Some decisions should never be derived.** A plan that eventually defers
  nothing would be a plan that has started guessing, so the number must not be
  maximised without limit — and the decision states no limit.

### Neutral

- No artifact changes. What changes is what the build state reports as progress.

## Compliance

Every Engineering Plan reports its derived and deferred items, both enumerated.
The build state reports the measure and stops reporting entity and feature counts
as progress.
