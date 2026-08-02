---
id: METAMODEL-Relationship
title: Relationship
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0042, ADR-0065]
---

# Relationship

**A named, typed, directed association between two semantic entities.**

## identity

The triple of **source, relationship type and target**.

A Relationship has no identity independent of what it connects. Two relationships
with the same triple are the same relationship, regardless of where each was
asserted.

## purpose

To make associations **first-class and therefore inspectable**.

The alternative — associations as properties of the entities they connect — has
been rejected twice in this project's history, both times for the same reason.
`ADR-0042` rejected it for dimension values; the argument generalises:

- A property belongs to one entity; **a relationship belongs to neither.**
- A property cannot be queried without knowing which entity holds it.
- A property cannot carry its own provenance.

> **The graph is the model.** Entities are nodes; the meaning lives in the edges.

## ownership

Owned by the repository asserting it — which may be neither the repository
owning the source nor the one owning the target.

That is the case `ADR-0019` anticipated: a repository importing a Knowledge
Package may assert relationships between imported Concepts and its own, without
modifying either side.

## lifecycle owner

`ArtifactRevisionLifecycle`.

## authoritative representation

An assertion in the semantic model, naming source, type and target.

**A Relationship is asserted, never inferred.** No compiler phase creates
relationships that were not stated. This is `ADR-0044`'s rule — descriptive,
never inferential — raised from Dimensions to the general case, and it is what
keeps the Knowledge Compiler mechanical (`ADR-0061`).

## derived representations

- An edge in the Canonical Knowledge Model.
- An object property assertion in a generated ontology.
- A traversable link in the Knowledge Explorer.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| from | semantic entity | exactly one |
| to | semantic entity | exactly one |
| typed-by | relationship type | exactly one |
| constrained-by | Invariant | zero or more |

**A Relationship connects exactly two entities.** Anything genuinely n-ary is
modelled as an entity with its own relationships — `DimensionAssignment` is
precisely that pattern, and it is why that entity exists rather than a
three-place edge.

## extension points

**Relationship types are registered, not enumerated** — the Registry Pattern
(`ADR-0031`) applied to the vocabulary of edges. An adopting repository
registers domain relationship types without modifying the metamodel.

## Debt

**Relationship types are not themselves specified.** `typed-by` points at a
concept — the relationship type — that has no entity in the inventory. It may
turn out to be a `Concept` in a framework-owned BoundedContext, which would be
elegant, or it may need its own entity. **Deferred: B1 does not require the
answer, and the OWL skeleton will likely force it.**

**Cardinality and directionality constraints have no home.** That a relationship
is one-to-many, or symmetric, or transitive, is stated nowhere. `Invariant` is
the probable owner, and `constrained-by` is written on that assumption.

**Reification cost is unmeasured.** If every association is an instance, the
graph has more Relationship instances than all other entities combined. Whether
that is a problem is an implementation question for B3.
