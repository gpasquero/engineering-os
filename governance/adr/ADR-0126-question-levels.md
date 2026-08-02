---
id: ADR-0126
title: Engineering Questions exist at repository and organization level; only the first is built
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0116, ADR-0119, ADR-0120, ADR-0125]
---

# ADR-0126 — Question levels

## Context

`ADR-0120` made the Engineering Question Set the product metric. All nine
questions are asked about **one system**.

The reviewer named a second level and, in the same breath, forbade building it:

> **Repository Questions** — why is this implemented this way? what breaks if I
> change this? which invariant protects this behavior?
>
> **Organization Questions** — which systems implement customer identity? which
> repositories depend on this capability? where is this business rule enforced?
> which architectural decisions affect this initiative?
>
> **Keep the current Repository Question Set as the first layer. Do not expand
> yet.**

## Decision

**Engineering Questions are declared at a level. `repository` is the only level
built.**

All nine existing questions declare `level: repository`. The `organization`
level is recorded and **not implemented**.

**The deferral is the decision.** Organization Questions would be cheap to write
and impossible to answer: they require several systems modelled at once, and the
project has two models, built at different times, that have never been loaded
together.

Writing them now would move the product metric **downward by nine** and teach
nothing that is not already known.

## Rationale

This is `ADR-0116` applied to the metric itself: *will this materially improve
the experience of an engineering team on a real Brownfield system?* An
organization question answered by nothing improves no one's experience.

Declaring the field now costs one line per question and means **the day a second
level exists, nothing has to be reinterpreted**. Retrofitting a level onto a
metric whose history is already recorded would make every past measurement
ambiguous.

## What would justify building the second level

**Two or more Authoritative Engineering Models, maintained, in the same
installation.** Not two benchmark runs — two *maintained* models, because an
organization question crosses systems and a stale model on either side gives a
confidently wrong answer about which system implements what.

Engineering OS has never held two models at once. **That, not the questions, is
the missing capability**, and it is the honest form of the requirement.

## Consequences

**The product metric remains a per-repository number**, and the comparison
between repositories stays a comparison, never a total.

**`ADR-0125` and this decision point at the same missing thing from opposite
directions.** One says a repository is only an evidence source; the other says an
organization is more than one system. **Both are waiting on the model becoming
something an installation holds several of.**

## Compliance

- Every registered question declares `level`.
- `organization` questions are not added until two maintained models coexist.
- Measurements are reported per repository and never summed.
