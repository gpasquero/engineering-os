---
id: ADR-0116
title: The admission test is whether it improves a team's experience on a real Brownfield system
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0067, ADR-0075, ADR-0084, ADR-0089, ADR-0102]
---

# ADR-0116 — The product-experience test

## Context

The project has five admission tests, each narrower than the last. All five ask
about **capability**. None asks about **use**.

> **The architecture is now sufficiently mature that the product itself should
> become the primary design driver.**

## Decision

**Before starting a new architectural subsystem, ask:**

> **Will this materially improve the experience of an engineering team using
> Engineering OS on a real Brownfield system?**

**If the answer is no, defer it.**

### The ladder, complete

| Test | Governs | From |
|---|---|---|
| What new semantic relationship does this introduce? | entities | `ADR-0067` |
| What would the compiler do differently? | metamodel entities | `ADR-0075` |
| Does this answer better questions about real systems? | capabilities | `ADR-0084` |
| What valuable engineering capability became possible? | milestones | `ADR-0089` |
| Does it remove a decision from a worker? | infrastructure | `ADR-0102` |
| **Will a team on a real Brownfield system notice?** | **subsystems** | this decision |

**Each earlier test can be passed by something nobody uses.** This one cannot,
and it is the first to mention a team rather than a system.

### The product, restated

> The product is **a persistent engineering understanding of a software system**
> — acquired once, maintained continuously, periodically challenged against
> reality, and used to direct every future engineering decision.

**Not a compiler for engineering knowledge. Not an engineering knowledge graph.**

### What the next demonstrations must answer

Onboarding a 500 KLOC production system · preserving understanding for months ·
detecting real architectural erosion · multiple engineers collaborating through
the maintained model · Claude and Codex as interchangeable workers in one
process.

**These are now more valuable than additional compiler features.**

## Alternatives considered

**Keep `ADR-0089` as the widest test.** Rejected: *valuable engineering
capability* is satisfied by a capability no team would reach for, and several
existing ones plausibly are.

**Require a named user.** Rejected as unmeetable today — the project has one
reviewer and no engineering team — and it would block work that is genuinely
foundational.

**Rank subsystems by expected value.** Rejected under `ADR-0090`: a ranking is a
score, and *defer* is a binary decision.

## Consequences

### Positive

- **It makes "no" the default for infrastructure**, which is what a maturing
  architecture needs and what five capability tests could not deliver.
- It names the demonstrations that matter, so a milestone can be judged against
  something outside this repository.

### Negative

- **The test is unfalsifiable without a real team.** *Would a team notice?* is
  answered by the same person who proposes the work, and that person has never
  used this system on someone else's repository under time pressure.
- **It will refuse correct architecture.** Some of what this project built —
  the parity check, the failure taxonomy — no team would notice, and each was
  worth building. The test is right in aggregate and wrong in specific cases,
  and there is no rule for telling which is which.

### Neutral

- No artifact changes. What changes is what may be started.

## Compliance

Every proposed subsystem answers the question. **Scale, longevity, erosion
detection, collaboration and worker interchangeability are the demonstrations
that count.**
