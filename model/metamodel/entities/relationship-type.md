---
id: METAMODEL-RelationshipType
title: RelationshipType
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0042, ADR-0065, ADR-0066, ADR-0071, ADR-0074]
supersedes: METAMODEL-Relationship
---

# RelationshipType

**A declaration that a kind of association may exist**, and what it means.

> **The metamodel defines the vocabulary of relationships. It does not represent
> every edge as an entity** (`ADR-0066`).

## What new semantics does this introduce?

The **typing of edges.** Without it, the graph has edges and no statement of
which edges are legitimate, what they mean, or how many may exist.

Nothing else in the metamodel can express that. `Invariant` states conditions
about the modelled world; `RelationshipType` states the shape of the model
itself.

## identity

A qualified name — the name of the relationship, plus the BoundedContext in
which it is declared.

`contains` in one context and `contains` in another are different relationship
types, and `BoundedContext` is what makes that non-conflicting.

## purpose

To carry the semantics that entities have stopped carrying.

Entities are becoming lightweight; the meaning is moving into relationships,
constraints and cardinalities (`ADR-0067`). `RelationshipType` is where that
meaning lives.

**`RelationshipType` is the type system of the knowledge graph** (`ADR-0074`).
The compiler already depends on it: `resolve()` rejects a model whose predicates
have no registered parent, which is type-checking by another name.

A RelationshipType declares seven fields:

| Declares | Required | States |
|---|---|---|
| **semantic definition** | yes | what the relationship means |
| **parent relationship** | yes | the core type it specializes (`ADR-0071`) |
| **domain** | yes | what may be the source |
| **range** | yes | what may be the target |
| **cardinality** | yes | how many, from each end |
| **inference rules** | optional | what may be derived from an instance |
| **validation rules** | optional | what the compiler must check |

**Inference is optional and never implicit.** `ADR-0044` holds: relationships are
descriptive unless an explicit rule exists. The field gives the exception a place
to be declared and keeps the compiler mechanical (`ADR-0061`).

## Relationship instances are not entities

**Instances already exist naturally in the graph.** They are structure, not
modelled objects, and they do not need an entity to give them existence.

```text
RelationshipType   definition · parent · domain · range · cardinality · rules
       ↓
   Compiler
       ↓
 ObjectProperty          (or whatever the target formalism uses)
       ↓
Relationship instances
```

This keeps Engineering OS **implementation-independent** while remaining
compatible with OWL: the metamodel names what kinds of edge may exist, and the
compiler emits the mechanism a given formalism uses to express them.

**Where an individual association genuinely needs its own identity, provenance
or lifecycle, it is modelled as an entity.** `DimensionAssignment` is exactly
that, and it is the precedent for the pattern rather than an anomaly. The test
is whether the association carries data of its own — not whether it feels
important.

## ownership

Framework relationship types are owned by Engineering OS. **An adopting
repository registers its own** without modifying the metamodel.

## lifecycle owner

`ArtifactRevisionLifecycle`.

## authoritative representation

A declaration in the semantic model naming the seven fields above.

**Relationship instances are asserted, never inferred** (`ADR-0044`). A
RelationshipType may declare that a relationship is symmetric or transitive —
that is a statement about the type. Whether a compiler materialises the implied
edges is a compiler concern (`ADR-0053`) and does not make those edges
authored.

## derived representations

- An `owl:ObjectProperty` with `rdfs:domain`, `rdfs:range` and cardinality
  restrictions, in a generated ontology.
- Edge-type definitions in the Canonical Knowledge Model.
- Traversal affordances in the Knowledge Explorer.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| has-domain | entity type | one or more |
| has-range | entity type | one or more |
| scoped-to | BoundedContext | exactly one |
| constrained-by | Invariant | zero or more |
| specialises | RelationshipType | zero or one |

## extension points

**Relationship types are registered, not enumerated** (`ADR-0031`) — which is
what makes the metamodel extensible without being modifiable. An adopting
repository declares the relationships its domain has; it never adds an entity to
Layer A.

## Debt

**Seven fields for sixty-three predicates is 441 declarations, and fewer than a
third exist.** `relationship-vocabulary.md` records which are declared and which
are outstanding; the gap is stated rather than hidden.

Every predicate has a **parent** and a **semantic definition**. Almost none has a
formally declared domain, range or cardinality — those live in prose in the
entity relationship tables, which is where the compiler cannot read them.

**Cardinality notation is prose.** "Zero or more", "exactly one". A formal
notation is needed before the compiler can check anything, and is not needed to
finish B1.

**Whether `domain` and `range` may name a RelationshipType** — relationships
between relationships — is unaddressed. Nothing in B1 requires it.
