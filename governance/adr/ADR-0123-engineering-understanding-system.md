---
id: ADR-0123
title: Engineering OS is a continuously improving Engineering Understanding System
status: accepted
date: 2026-08-02
supersedes: ADR-0122
superseded-by: null
resolves: []
related: [ADR-0092, ADR-0094, ADR-0112, ADR-0118, ADR-0120, ADR-0122]
---

# ADR-0123 — An Engineering Understanding System

## Context

`ADR-0122` named the product an **engineering memory**. The reviewer accepted the
direction and corrected the noun:

> **Engineering OS is not simply an Engineering Memory. It is a continuously
> improving Engineering Understanding System.**
>
> **Memory stores. Understanding explains. Guidance recommends. Acquisition
> learns. Drift challenges.** Together they become something larger than memory.

The correction is not cosmetic. **Memory is a storage claim and it is passive.**
A system judged as memory succeeds by retaining; a system judged as
understanding must be able to *explain*, and explanation is falsifiable in a way
retention is not.

## Decision

**Engineering OS is a continuously improving Engineering Understanding System.
It is composed of five verbs, and none of them alone is the product.**

| Verb | Does | Already exists as |
|---|---|---|
| **Acquisition learns** | turns evidence into proposals | Initial · Continuous · Periodic (`ADR-0118`) |
| **Memory stores** | keeps what was curated, with provenance | the Authoritative Engineering Model |
| **Understanding explains** | answers questions nobody re-derived | the CKM and the query engine |
| **Drift challenges** | makes the stored claim defend itself | the Knowledge Drift Report |
| **Guidance recommends** | tells a team what to do next | Recommendations · Plans · the Director |

**Understanding is measured by explanation, not by retention** — which is
`ADR-0120`, and this decision is why that metric is the right one.

## The transition this decision anticipates

The reviewer named the next architectural transition, and it is recorded here
rather than deferred to a later ADR because it changes how every remaining
decision should be judged:

> Until now the guiding question has been **"How do we acquire engineering
> understanding?"** Soon it should become **"How do engineering teams work
> differently once Engineering OS possesses that understanding?"**
>
> **The product is no longer acquisition. Acquisition enables engineering
> guidance. That guidance is what customers ultimately buy.**

Acquisition has consumed twelve milestones and is the part of the system that is
furthest ahead. **Guidance is the part a customer would pay for**, and the
Director, Plans, Recommendations and Skills were all built before there was
enough understanding for them to act on.

## Rationale

The five verbs make a class of imbalance visible that a single noun hid.
Measured against them, the system today is:

| | |
|---|---|
| Acquisition | **strong** — three modes, two stacks, declarative extraction |
| Memory | **strong** — provenance on every assertion, curation governed |
| Drift | **works** — and has already caught the model asserting things a rerun would not |
| Understanding | **weak** — 22 % and 33 % (`ADR-0120`) |
| Guidance | **untested against a real model** — every plan run so far used a model built for the purpose |

**Four of the five verbs feed the fifth, and the fifth is the one nobody has
tried.**

## Consequences

**"Continuously improving" is a claim about the whole system, and the
longitudinal experiment tests it.** `SESSION-0047` ran ten real commits and the
result was **1 of 9 questions answered at t0 and 1 of 9 at t9** — with the model
growing from 39 proposals to 94 curated sources.

**The model stayed current and did not get better.** Under `ADR-0122`'s framing
that reads as success: nothing was lost, everything was maintained. Under this
one it is a failure, because understanding did not improve — and that difference
is the entire argument for the correction.

**Guidance may not be scaled up before understanding is.** Recommending from a
model that answers one question in nine would produce confident advice with no
basis, which is the failure mode this project has been most careful to avoid.

## Compliance

- Architectural proposals state which of the five verbs they serve and which
  they do not.
- No proposal may strengthen Acquisition while leaving Understanding flat
  without saying so explicitly.
- The roadmap is ordered by the weakest verb, not by the most tractable one.
