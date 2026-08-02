---
id: ADR-0133
title: Knowledge, Understanding and Guidance Preservation are three different product properties
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0123, ADR-0127, ADR-0128, ADR-0130, ADR-0136, ADR-0136]
---

# ADR-0133 — Three preservation properties

## Context

`ADR-0127` separated knowledge from understanding. The reviewer extended the
separation to a third property and made all three **preservation** questions:

> **Knowledge Preservation** — *do we still know the same facts?*
> **Understanding Preservation** — *can we still explain the system?*
> **Guidance Preservation** — *can we still safely direct engineering work?*
>
> Engineering OS will eventually need to preserve all three. **Today only the
> second has been measured.**

## Decision

**Three preservation properties, measured separately and never substituted for
one another.**

| Property | Asks | Measured by | Today |
|---|---|---|---|
| **Knowledge Preservation** | do we still know the same facts? | assertions retained across evolution | **not measured** |
| **Understanding Preservation** | can we still explain the system? | Understanding Retention (`ADR-0128`) | **measured — 100 %** |
| **Guidance Preservation** | can we still safely direct engineering work? | plans still derivable and still correct | **not measured** |

**They can diverge in every direction, and each divergence is a distinct
product failure:**

- knowledge preserved, understanding lost — **observed**: every fact from `t0`
  was still in the model while `EQ-06` went unanswered for nine commits;
- understanding preserved, guidance lost — a model that explains the system but
  can no longer produce a plan a team may act on;
- guidance preserved, understanding lost — **the most dangerous**: confident
  recommendations derived from an explanation that no longer holds.

## Rationale

The third property is the one a customer experiences, and it is the one nothing
observes. A team does not notice that a predicate stopped being emitted. **They
notice that the advice stopped being right**, and by then the cause is several
months old.

Naming it now, unmeasured, is deliberate. `ADR-0136` separates Acquisition from
Guidance as products, and Guidance is the weakest verb (`ADR-0123`). **A
preservation property that is named and empty is a better statement of the gap
than a metric invented before the thing it measures exists.**

## Consequences

**Knowledge Preservation is trivially measurable and is not yet measured.** It is
the retention of assertions rather than of answers, and the current maintenance
path never removes anything — retraction is governed and has never fired — so
the expected reading is 100 % and it would be a weak result. **A metric whose
answer is known in advance is not urgent**, and it is recorded rather than built.

**Guidance Preservation blocks nothing today and constrains the next phase.**
Before Engineering Guidance is scaled up, it needs its own longitudinal reading —
*would this plan still be correct ten commits later?* — because guidance that
degrades silently is worse than no guidance.

**Only the measured property may be claimed.** Reports say *Understanding
Preservation: 100 %*, never *preservation: 100 %*.

## Compliance

- The three properties are named separately in every report that mentions
  preservation.
- No property's measurement is presented as evidence for another.
- Guidance is not scaled up before Guidance Preservation has a reading.
