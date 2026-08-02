---
id: ADR-0141
title: The customer lifecycle is the product experience and outranks the compiler architecture
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0073, ADR-0108, ADR-0112, ADR-0118, ADR-0135, ADR-0136, ADR-0140]
---

# ADR-0141 — The customer lifecycle

## Context

The reviewer set out what a customer actually goes through, and ranked it:

```text
Brownfield Repository → Mechanical Discovery → Interpretive Discovery (LLM Skill)
  → Human Curation → Authoritative Engineering Model → Engineering Guidance
  → Continuous Acquisition → Periodic Reacquisition → Drift Analysis → Repeat
```

> **I suspect this lifecycle is eventually more important than the compiler
> architecture itself. It is probably what customers will actually experience.
> Build toward that experience.**

The project's own internal ordering is the compiler's: Authoring → Discovery →
Parsing → Resolution → CKM → Projection (`ADR-0073`). **That sequence is
invisible to a customer**, and it is the one the repository is organised around.

## Decision

**The customer lifecycle is the primary structure of the product. The compiler
phases are an implementation of one of its steps.**

`LIFECYCLE.md` states it, and every stage names what a customer does, what they
get, and what is missing.

**Three consequences follow, and each reorders something.**

**1. A stage nobody has experienced is not built.** *Human Curation* has run only
as a filter function in a script — no person has ever curated a model in this
system. It is the stage every proposal must pass through and the least
developed.

**2. Progress is reported by stage.** *"Continuous Acquisition preserves five of
six predicates"* is implementation. *"After ten commits the team still gets the
same advice on 80 % of untouched subjects"* is a stage of the lifecycle.

**3. The loop is the product, not the pass.** Every stage after the model exists
to return to it. A one-shot onboarding delivers none of the promise
(`ADR-0136`), and the loop is what makes preservation a property rather than a
claim.

## Where the lifecycle stands today

| Stage | State |
|---|---|
| Brownfield Repository | two, chosen for engineering characteristics |
| Mechanical Discovery | **strong** — declarative, two stacks, reproducible |
| Interpretive Discovery | deterministic only; **the LLM skill is `ADR-0140`** |
| **Human Curation** | **weakest — never performed by a human** |
| Authoritative Model | **strong** — provenance, governed, deterministic |
| Engineering Guidance | measured for the first time this session: **80 %** |
| Continuous Acquisition | **strong** — 100 % Understanding Retention |
| Periodic Reacquisition | works |
| Drift Analysis | works — 15 classes, each routed to a plan |
| **Repeat** | **run once, over ten commits** |

## Rationale

The two orderings disagree about what matters, and the disagreement is
informative rather than academic. The compiler's phases are ranked by
*dependency*; the lifecycle is ranked by *what a person does*. Under the first,
curation is a small step between two large ones. Under the second it is **the
only stage where a human decides anything**, and its quality determines
everything downstream.

`ADR-0140` states the onboarding skill's purpose as helping a team *produce the
model faster and with higher quality* — a claim entirely about the curation
stage. **The lifecycle is what makes that a measurable objective rather than a
sentiment.**

## Consequences

**Curation becomes the next area of investment after `ADR-0140`**, and the two
are the same work seen from either end: a better proposer is only better if a
curator can tell.

**The compiler architecture is not demoted in importance, only in primacy.** It
remains how the Authoritative Model is produced and is why the model is
trustworthy. It is not what a customer experiences.

**Documentation leads with the lifecycle.** A reader arriving at this repository
currently meets a metamodel and a compiler. They should meet the loop.

## Compliance

- `LIFECYCLE.md` is maintained as an Authoritative Artifact and names the state
  of every stage.
- Progress reports name the lifecycle stage they advance.
- No stage is declared complete before a human has been through it.
