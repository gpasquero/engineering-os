---
id: ADR-0105
title: Engineering Discovery is the first engineering workflow, not a preprocessing step
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0072, ADR-0092, ADR-0095, ADR-0098, ADR-0101, ADR-0102]
---

# ADR-0105 — Engineering Discovery is a workflow

## Context

`SESSION-0037` ran the Director against `ai-desk`. **The input was produced by
`grep`** — nodes extracted by hand from the working tree, knowledge reconstructed
by an author reading source.

> **That is a useful validation technique. It is not the intended architecture.**

**The Engineering Director must never operate directly on a source repository.
It operates on an Engineering Model.**

## Decision

**Engineering Discovery is the first engineering workflow executed by Engineering
OS itself** — not a preprocessing step that runs before it.

```text
Repository → Discovery Intent → Discovery Plan → Discovery Task Graph
   → Discovery Workers → Candidate Engineering Model → Engineering Review
   → Authoritative Engineering Model → Compiler → CKM
   → Engineering Director → Continuous Engineering
```

### One execution architecture for the whole lifecycle

> **The only difference between Brownfield and Continuous Engineering is the
> objective. Everything else is identical.**

Plans, Task Graphs, Worker Routing, Governance Gates, Execution Observations,
Knowledge Updates — **the same mechanisms, unchanged.**

Brownfield onboarding is a project Engineering OS manages, and it is the first
one.

### Discovery is an engineering process, not a parser

Its responsibility is to transform an unknown repository into a **Candidate
Engineering Model**. Activities may include source parsing, AST extraction,
dependency and framework discovery, architectural and API and database and
runtime discovery, domain concept and capability extraction, invariant and ADR
and workflow candidates, evidence extraction, and **identification of knowledge
gaps**.

> **None of those become authoritative automatically. They become engineering
> proposals.**

Only after engineering review and acceptance do they become Authoritative
Engineering Knowledge. **Only then does the compiler produce the CKM. Only then
does the Director reason about the system.**

### The separation that is the differentiator

| | Understands |
|---|---|
| **Engineering Discovery** | software |
| **Engineering OS** | engineering |

> **If we blur them, Engineering OS risks becoming another repository-
> understanding system.** Its differentiator is precisely that it reasons over
> engineering knowledge rather than directly over source code.

Discovery workers read source. **Nothing else in the architecture ever does.**

### What this makes of the existing ai-desk model

`external/ai-desk-auth/` was authored by a human-equivalent process reading
source — **a discovery worker operating without the workflow around it.**

It is not invalidated: what it contains is what discovery would propose. What is
missing is the process — the plan that requested it, the gates that reviewed it,
and the record of what was proposed and rejected. **It stands as a hand-made
Candidate Engineering Model that skipped its review.**

## Alternatives considered

**Discovery as a separate tool that emits authoring sources.** Rejected, and it
is what the project was implicitly heading toward. It would mean two execution
architectures — one for understanding a system and one for changing it — and the
onboarding half would have no plans, no gates, no observations and no record of
what it chose not to propose.

**Discovery as a compiler phase.** Rejected. `ADR-0073`'s phases are
deterministic and discovery is irreducibly interpretive: `ADR-0060` already
separates Mechanical from Interpretive Discovery, and putting the interpretive
half inside the compiler would make the compiler an intelligence, which
`ADR-0061` forbids.

**Skip discovery; require repositories to be authored by hand.** Rejected — it is
the current state, it does not scale past one subsystem, and it makes Engineering
OS useless on every system that already exists.

## Consequences

### Positive

- **One execution architecture for the entire software lifecycle.** Everything
  built for continuous engineering applies to onboarding unchanged, which is a
  large amount of leverage from a correction rather than an addition.
- Discovery inherits governance for free: proposals are reviewed by the same
  gates, so **nothing enters the model unreviewed** regardless of where it came
  from.
- It keeps the differentiator explicit and defensible.

### Negative

- **Discovery is by far the largest worker surface the project has contemplated**,
  and every activity listed is a research area. Naming them does not make them
  cheap.
- **Review does not scale.** A candidate model for a 469-file repository could
  propose thousands of assertions, and every one requires human acceptance. **The
  architecture is correct and the review bottleneck is real**, and nothing in
  this decision addresses it.

### Neutral

- No existing artifact changes. `ai-desk-auth` is reclassified, not invalidated.

## Compliance

Discovery is declared as an intent, a plan, task kinds and worker types in the
**existing registries**. **No new execution mechanism is built.** Discovery
output is a Candidate Engineering Model and is never authoritative until
reviewed.
