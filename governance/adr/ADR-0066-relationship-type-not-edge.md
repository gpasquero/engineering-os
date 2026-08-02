---
id: ADR-0066
title: The metamodel defines RelationshipType, not Relationship
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0042, ADR-0044, ADR-0053, ADR-0065]
---

# ADR-0066 — RelationshipType, not Relationship

## Context

`SESSION-0023` specified `Relationship` as "a named, typed, directed association
between two semantic entities" — an edge, reified as an entity.

Expressing the metamodel as OWL exposed the problem immediately
(`FINDINGS.md` #1). Every association in the skeleton is an
`owl:ObjectProperty`; the metamodel also declared an entity whose purpose was to
represent an association. **Two mechanisms for the same thing, with nothing
saying which is authoritative.**

## Decision

**The metamodel defines the *vocabulary* of relationships. It does not represent
every edge as an entity.**

`Relationship` is replaced by **`RelationshipType`**, which declares:

- **domain** — what may be the source
- **range** — what may be the target
- **cardinality**
- **constraints**
- **semantics** — what the relationship means

Instances of relationships **already exist naturally in the graph**. They do not
need an entity to give them existence.

```text
RelationshipType   defines domain, range, cardinality, constraints, semantics
       ↓
   Compiler
       ↓
 ObjectProperty
       ↓
Relationship instances
```

**This preserves compatibility with OWL while keeping Engineering OS
implementation-independent.** The metamodel names what kinds of edge may exist;
the compiler emits the mechanism a target formalism uses to express them; the
edges themselves are graph structure, not modelled objects.

## Alternatives considered

**Keep `Relationship` as a reified edge.** Rejected. It would mean the Canonical
Knowledge Model contains one entity instance per edge, and — worse — that the
metamodel competes with the representation it compiles to. `ADR-0053` says the
semantic architecture is separate from the compiler architecture; an entity that
duplicates `owl:ObjectProperty` violates that in the other direction.

**Declare `owl:ObjectProperty` the authoritative mechanism and drop the entity.**
Rejected: it would bind Layer A to OWL. `ADR-0017` commits to a reference
architecture, and the metamodel must be expressible in formalisms that are not
OWL.

**Keep both at different abstraction levels.** This was the resolution
`FINDINGS.md` guessed at, and it is nearly this decision — except that naming
the entity `Relationship` while it means *relationship type* is exactly the
class of error `ADR-0057` exists to prevent. **The name was the problem.**

## Consequences

### Positive

- **Entities get lighter and relationships get heavier**, which is the correct
  direction for an ontology-driven architecture.
- `RelationshipType` becomes the natural home for the cardinality and
  directionality constraints that `relationship.md` recorded as homeless debt.
- `typedBy` — which pointed at nothing defined (`FINDINGS.md` #5) — now points at
  `RelationshipType`. **A second finding closes as a consequence of the first.**
- The registry pattern applies cleanly: relationship types are registered, not
  enumerated (`ADR-0031`).

### Negative

- The relationship instances are no longer first-class, so **an individual edge
  cannot carry its own provenance or lifecycle**. Where that is genuinely needed,
  the relationship must be modelled as an entity — which is exactly what
  `DimensionAssignment` already is. That entity is now the precedent for the
  pattern rather than an anomaly.
- An accepted specification is withdrawn one session after acceptance.

### Neutral

- `Relationship` was absent from every inventory this project produced before
  `SESSION-0023`. It existed as a specification for a single session.

## Compliance

`model/metamodel/entities/relationship.md` is replaced by
`relationship-type.md`. The OWL skeleton declares `eos:RelationshipType` and
stops treating edges as class instances.
