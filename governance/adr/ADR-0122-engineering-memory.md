---
id: ADR-0122
title: Engineering OS is a continuously improving engineering memory
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0080, ADR-0089, ADR-0110, ADR-0112, ADR-0116, ADR-0118, ADR-0120]
---

# ADR-0122 — Engineering memory is the product

## Context

The project has restated its objective seven times, each restatement narrower
and more useful than the last: metamodel completeness → semantic answers →
engineering value → the Engineering Director → autonomy → orchestration →
Brownfield knowledge acquisition.

The reviewer stated the eighth, and it is a statement about **time**:

> **Discovery does not exist to create graphs. Discovery exists so that six
> months later an engineer can ask a difficult question about a system and
> receive an answer that nobody had to rediscover.**
>
> **Optimize every future architectural decision against that outcome.**

Every previous framing describes a *capability*. This one describes a
**duration**, and duration is what none of the architecture has yet been tested
against. The longest-lived model this project has built is a few sessions old.

## Decision

**Engineering OS is a continuously improving engineering memory. Every
architectural decision is judged against whether an answer survives to be given
six months later, without rediscovery.**

Three properties follow, and each forbids something a graph database would
happily allow.

**1. An answer must remain attributable.** Six months on, the engineer's next
question is *how do you know?* An answer without provenance is a rumour, and a
memory of rumours is worse than no memory — this is why every proposal carries
its source, locator, worker and support, and why fabrication is the one
unforgivable defect (`SESSION-0045`).

**2. An answer must be allowed to become wrong.** A memory that cannot be
challenged calcifies into folklore. Periodic Reacquisition exists for exactly
this, and its output is a challenge, never a replacement (`ADR-0118`).

**3. The improvement must be cumulative, not repeated.** *Continuously
improving* means the model is worth more in month six than in month one. A
system that re-derives the same understanding every run has no memory at all —
it has a cache.

## What this makes wrong that previously looked right

**Optimizing Initial Acquisition for speed.** A faster onboarding that
understands less trades the entire product for a number nobody was asking
about. Initial Acquisition is permitted to take hours.

**Measuring a run by what it produced.** `ADR-0120` already demotes counts. This
decision explains why: what matters is not what a run produced but **what a
question can still be answered from, later.**

**Treating curation as overhead.** The curated 72 of 299 is the memory. The
other 227 are observations. Anything that makes curation cheaper by making it
less deliberate is destroying the product to improve a statistic.

## Rationale

The vision is testable, and it is the first framing that is. A memory claim
fails in a way a capability claim cannot: **ask the same question twice, six
months apart, and see whether the second answer cost anything.**

Nothing in the repository measures that today. The two acquisition modes that
would — Continuous and Periodic — have run against exactly one engineering
change, in one repository, over one commit.

## Consequences

**The known gaps are re-ranked by this decision, and the order changes.**

*Why does this system work this way?* becomes the highest-value unanswered
question in the set, above authorization. Rationale is precisely the knowledge
that is expensive to rediscover and that decays fastest — the people who hold it
leave. Authorization can be re-read from the code in an afternoon; **the reason
for a decision made three years ago cannot be re-read from anywhere.**

`EQ-01` scores `no-data` in both benchmarked repositories.

**A longitudinal test is now missing infrastructure, not a nice-to-have.** The
architecture claims cumulative improvement and nothing measures it. Recorded as
the principal gap.

## Compliance

- Architectural proposals state how the decision serves an answer given later,
  not only a capability delivered now.
- No decision may reduce provenance, remove the ability to challenge an
  assertion, or make curation less deliberate.
- The roadmap is ordered by which unanswered questions are most expensive to
  rediscover.
