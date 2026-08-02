---
id: ADR-0047
title: Three representations of knowledge, with the compiler responsible for semantic equivalence
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0017, ADR-0036, ADR-0037, ADR-0042, ADR-0045, ISSUE-0064]
---

# ADR-0047 — Three representations of knowledge

**This is a foundational principle.** It explains how Engineering OS can
simultaneously optimize for human authoring, machine reasoning and generated
documentation **without duplicating semantics**.

## Context

`ADR-0042` made classification a graph relationship. `ADR-0045` then established
that front matter is a serialization of those relationships rather than the
relationships themselves. Both decisions describe the same underlying idea — one
body of knowledge, encoded differently for different purposes — without naming
it.

## Decision

Engineering OS distinguishes **three representations of knowledge**.

### 1. Semantic Representation

The **canonical graph**.

### 2. Authoring Representation

The **human-editable source artifacts**.

### 3. Presentation Representation

**Generated views**: the Knowledge Explorer, documentation, search indexes,
registry projections.

### The compiler's obligation

> **The compiler is responsible for maintaining semantic equivalence across
> these representations.**

**The representations are different views of the same knowledge, not different
knowledge.**

## Why this matters

Each representation is optimized for a different consumer — a human editing a
file, a machine reasoning over a graph, a reader browsing a generated view. The
usual cost of that is duplicated semantics, and duplicated semantics drift.

Naming them as *views* rather than *copies*, and making equivalence the
compiler's responsibility, is what avoids the duplication rather than managing
it.

## Alternatives considered

**One representation, optimized for a compromise.** Rejected: a format good for
graph reasoning is poor for hand-editing, and vice versa. The compromise would be
worse than either for both.

**Multiple representations with no equivalence obligation.** Rejected — this is
the default failure. Without an owner for equivalence, the three drift and
"which one is right" becomes a per-question judgement.

**Treat the authoring representation as primary and the others as exports.**
Tempting, and close to how the repository works today, but rejected: it would
make the graph a derived convenience rather than the semantic representation, and
`ADR-0036` requires the canonical model to be what conformance is measured
against.

## Consequences

### Positive

- **`ADR-0045` stops being a special case.** Front matter as interchange syntax
  is one instance of a general rule, not an exception carved out to rescue
  `ADR-0017`.
- **Semantic equivalence is an obligation with an owner.** A projection that
  loses meaning is a compiler defect, not an accepted limitation — which makes
  it testable.
- Each representation can be optimized honestly for its consumer, because none
  of them has to serve all three.

### Negative

- **Semantic equivalence is a strong claim and is currently unverifiable.** No
  compiler exists, and nothing defines what equivalence means operationally —
  round-trip fidelity, information preservation, or something weaker.
- Three representations to keep aligned, with the alignment guaranteed by
  software that has not been written.
- **The relationship to Semantic Layers is unclear.** Authoring maps onto Layers
  A and B, Semantic onto Layer C, Presentation onto Layer D — which makes
  Representation look like a coarser partition of the same axis rather than an
  independent one. `ISSUE-0064`.

### Neutral

- No artifact changes. The principle names what `ADR-0042` and `ADR-0045`
  already do.

## Compliance

No knowledge exists in one representation that is absent from the others by
design. Every representation is generated from or serialized to the semantic
representation. A discrepancy between representations is a compiler defect.
