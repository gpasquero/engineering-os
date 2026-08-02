---
id: ADR-0041
title: Dimensions are first-class semantic entities, added by registration
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0057]
related: [ADR-0027, ADR-0031, ADR-0032, ADR-0040, ADR-0043, ISSUE-0059]
---

# ADR-0041 — Dimensions are registered first-class entities

## Context

`ADR-0040` introduced Architectural Dimensions and listed eight as examples.
`ISSUE-0057` recorded that the set was not closed, that four dimensions were
undefined, and that nothing said when a new dimension is justified.

It also recorded an obligation rather than a preference: `ADR-0031` requires
**every extensible concept** to be evaluated for Registry + Specification
modeling, and `ADR-0027` had already answered the analogous question for state
machines with registration rather than enumeration.

## Decision

**Architectural Dimensions are first-class semantic entities.**

> A Dimension is **not merely a taxonomy**. It is a semantic construct that
> defines **one independent axis of classification**.

### Every Dimension defines

- identifier
- purpose
- governed entity types
- value domain
- cardinality
- constraints
- relationships to other dimensions
- authoritative specification

### Dimensions are registered

Engineering OS introduces a **Dimension Registry Specification** (authoritative)
and a generated **Dimension Registry Projection** (derived), following the
Registry Pattern (`ADR-0031`, `ADR-0032`).

> **Future dimensions are added by registration, never by modifying compiler
> logic.**

## Alternatives considered

**A closed enumeration of dimensions.** Rejected on the same grounds as
`ADR-0027` rejected a state machine catalogue: the framework applies to target
domains whose classification needs cannot be anticipated here.

**Dimensions as ordinary vocabularies** in `shared/vocabularies/`. Rejected: a
vocabulary is a set of values. A Dimension has a value domain *and* cardinality,
constraints, governed entity types and relationships to other dimensions. Those
are the properties of an entity, not of a list.

**Fix the four undefined dimensions now and defer the mechanism.** Rejected: it
would answer the smallest of the three problems `ISSUE-0057` recorded and leave
the structural one open.

## Consequences

### Positive

- **"Never by modifying compiler logic" is the strongest form of the Registry
  Pattern's promise so far.** Earlier instances constrained where data lives;
  this one constrains the *implementation*, making extensibility a property the
  compiler cannot quietly withdraw.
- **Fifth instance of the Registry Pattern**, and the first adopted because
  `ADR-0031` obliged it rather than because the shape was noticed again. The
  pattern is now doing work as a rule.
- The eight required fields answer `ISSUE-0057`'s third problem implicitly: a
  dimension is justified when all eight can be filled. An axis with no
  cardinality or no governed entity types is not a dimension.
- Adopting repositories can register domain-specific dimensions without forking
  the framework.

### Negative

- **The four undefined dimensions are not defined by this decision.** Governance
  Status, Ownership, Authority and Visibility become registration work rather
  than answered questions, and the suspected overlap between `Governance Status`
  and `ArtifactRevisionLifecycle` is untouched. `ISSUE-0059`.
- **"Relationships to other dimensions" sits uneasily with `ADR-0040`**, which
  states that dimensions are independent and that a value on one never implies a
  value on another. If dimensions relate, in what sense are they independent?
  The field's semantics are undefined. Also `ISSUE-0059`.
- Another Registry Specification and Projection to author and generate, on top of
  the state machine registry, with no compiler to generate either.

### Neutral

- `ADR-0040`'s eight examples become the first registrations.

## Compliance

No dimension exists without a registration carrying all eight fields. No
compiler change is required to add a dimension. The Dimension Registry follows
the Registry Pattern: the specification is authoritative, the projection is
generated.
