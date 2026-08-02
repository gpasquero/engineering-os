---
id: ADR-0053
title: Semantic architecture and compiler architecture are separate
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0035, ADR-0036, ADR-0038, ADR-0040, ADR-0047, ADR-0052, ISSUE-0068]
---

# ADR-0053 — Semantic architecture is separate from compiler architecture

**This is a foundational principle.** It prevents implementation concerns from
leaking into the ontology, and ontology concerns from constraining compiler
implementation unnecessarily.

## Context

`ADR-0052` split one hierarchy into two because it mixed a semantic concern with
a compilation concern. That was the second time in two sessions that a decision
needed unmixing — `ADR-0044` had done the same for independence and isolation.

The mixing was not an accident of drafting. Nothing said the two architectures
were separate.

## Decision

Engineering OS **explicitly separates semantic architecture from compiler
architecture**.

> **The metamodel defines what exists. The compiler defines how it is
> transformed.**
>
> **Neither embeds concepts belonging to the other.**

### The consequence for every new concept

Every future concept introduced into Engineering OS first answers:

1. **Is this a semantic concept?**
2. **Is this a compilation concept?**
3. **Is it both?**

**Only concepts that genuinely belong to both worlds appear in both
architectures, and their correspondence is explicit rather than implicit.**

## Alternatives considered

**One unified architecture.** Rejected: it is what produced `ISSUE-0066`. A
single structure forces every concept to take a position in a pipeline it may
have nothing to do with.

**Separate them by convention rather than principle.** Rejected: `ADR-0050` was
written by people who understood both concerns and still mixed them. A
convention would not have caught it.

**Allow implicit correspondence** where a concept appears in both. Rejected:
implicit correspondence is how `Registry Projection` came to occupy two
positions at once. Requiring it to be explicit is what makes the duplication
visible.

## Consequences

### Positive

- **The metamodel can stabilize while the compiler evolves**, and vice versa.
  This is the same property `ACCEPT-0011` identified for the object model and
  classification model, now applied one level up.
- It gives `ADR-0036`'s statement — the metamodel is *the contract between*
  authoring and compilation — a reason to be true rather than a convenient
  framing.
- **It immediately does work.** Two current dimension candidates look like
  compilation concepts wearing semantic clothing:
  - **Compilation Phase** (`ADR-0040`) classifies artifacts by when a compiler
    touches them. A dimension is a metamodel entity, so this puts a compilation
    concept in the semantic model.
  - **Representation** (`ADR-0047`) enumerates Semantic, Authoring and
    Presentation — which `ADR-0052` has just placed in the compilation
    hierarchy.

  Both go to the Dimension Review (`ADR-0051`) with a specific objection rather
  than a general doubt.

### Negative

- **`ADR-0038`'s fourth question now conflicts with this principle.** It requires
  every new artifact type to answer *which compiler phase consumes or produces
  it*, and treats an unanswerable question as a rejection. A purely semantic
  concept may have no compiler phase — and would be rejected for being exactly
  what this ADR says it is entitled to be. `ISSUE-0068`.
- **Three gates now govern new concepts**: position in the metamodel
  (`ADR-0035`), four questions (`ADR-0038`), and these three questions. They
  overlap, and nothing states how they compose.
- Judging "is it both?" will be contested. Anything the compiler reads has a
  compilation aspect in some sense, and the principle depends on that sense
  being narrower than "the compiler touches it".

### Neutral

- No existing artifact moves. What changes is which architecture describes it.

## Compliance

No semantic concept is defined in terms of compiler behaviour. No compiler
concept appears in the metamodel except by explicit correspondence. Every new
concept records which of the three questions it answers.
