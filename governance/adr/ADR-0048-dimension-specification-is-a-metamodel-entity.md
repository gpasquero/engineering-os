---
id: ADR-0048
title: DimensionSpecification is a first-class metamodel entity; dimensions are instantiated from it
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0062]
related: [ADR-0032, ADR-0041, ADR-0042, ADR-0050, ISSUE-0048, ISSUE-0065]
---

# ADR-0048 — DimensionSpecification is a metamodel entity

## Context

`ADR-0041` made dimensions registered first-class entities with eight declared
fields. `ISSUE-0062` recorded that four of the eight initial dimensions —
Governance Status, Ownership, Authority, Visibility — remained undefined, and
that the question had been deferred through three consecutive issues while the
mechanism was decided three times over.

## Decision

**Dimensions are part of the Engineering OS Metamodel. They must therefore be
specified before they can be instantiated.**

The Dimension Registry registers **Dimension Specifications**.

### A Dimension Specification defines

- identifier
- purpose
- governed entity types
- **value model**
- **assignment semantics**
- cardinality
- constraints
- relationships
- **serialization strategy**
- **validation rules**

**A Dimension Assignment is always an instance of a Dimension Specification.**

### The metamodel entity

**`DimensionSpecification` is a first-class metamodel entity.** The initial
dimensions are created as **instances of that entity**, not embedded into
compiler documentation.

This mirrors the pattern already established:

```text
Registry Specification  →  Registry Projection
Dimension Specification →  Dimension Assignment
```

## Correction to ADR-0041

`ADR-0041`'s decision stands: dimensions are first-class entities added by
registration, never by modifying compiler logic.

Its **field list is superseded**. Eight fields become ten: `value domain`
becomes `value model`; `authoritative specification` is dropped, since the
specification *is* the artifact; and **assignment semantics**, **serialization
strategy** and **validation rules** are added.

This is the **fifth** correction to an `Active` ADR, still visible only in prose
and the ADR index (`ISSUE-0048`). Five is no longer an anomaly.

## Alternatives considered

**Define the four dimensions directly and keep the eight-field schema.**
Rejected: it would answer the smallest question again while leaving dimensions
outside the metamodel, which is where `ADR-0035`'s process gate requires every
concept to be positioned first.

**Keep dimensions as registry entries without a specification entity.** Rejected:
`ADR-0042` makes an assignment an instance of *something*, and without a
specification entity there is nothing for it to instantiate.

**Document the initial dimensions in compiler documentation.** Rejected
explicitly by the decision. It would make the compiler's documentation the source
of semantics, which `ADR-0036` forbids — the compiler compiles *into* the
metamodel, not the other way round.

## Consequences

### Positive

- **The three-session deferral ends by reframing.** The four dimensions are no
  longer "undefined"; they are unwritten instances of a defined entity. That is
  work rather than an open question.
- The three new fields close real gaps: **assignment semantics** gives
  `ADR-0042` something to instantiate, **serialization strategy** gives
  `ADR-0045`'s Human Representation a per-dimension rule, and **validation
  rules** gives `ADR-0042`'s "validation applies to assignments" a home.
- Dimensions become expressible in the metamodel rather than described beside
  it.

### Negative

- **The four dimensions are still not written**, and each now needs evaluating
  against `ADR-0049`'s five conditions before it can be specified at all.
  `ISSUE-0065`.
- Ten fields per dimension is a substantial authoring cost, and the initial set
  is eight dimensions.
- **Fifth correction, no mechanism.** `ISSUE-0048` has been open since
  `SESSION-0008`; a reader of `ADR-0041` still sees eight fields with nothing in
  its front matter to indicate otherwise.

### Neutral

- `ADR-0050` generalizes this specification-to-assignment shape into a pattern
  spanning dimensions, state machines and policies.

## Compliance

No dimension exists without a Dimension Specification. Every Dimension
Assignment instantiates one. No dimension is defined in compiler documentation.
The metamodel defines `DimensionSpecification` as an entity.
