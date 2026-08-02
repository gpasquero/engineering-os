---
id: METAMODEL-Concept
title: Concept
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0035]
---

# Concept

**A named unit of meaning within a bounded context.** The thing an Ontology
defines, a Glossary names, and a Capability is expressed in terms of.

## identity

A **qualified name within a bounded context**. The same word in two bounded
contexts is two Concepts — that is what a bounded context is for.

Qualification follows `ADR-0057`: the canonical name includes its dimension
wherever ambiguity is possible.

## purpose

To make domain meaning explicit and addressable, so that assertions, invariants
and specifications refer to something rather than to a word.

A Concept is the unit at which the inherited epistemic discipline applies:
**every material assertion about a Concept carries a status and a confidence**,
and disagreement between sources is recorded rather than resolved by preference.

## ownership

Owned by the bounded context that defines it, in the repository that owns that
domain (`ADR-0010`). Engineering OS's own concepts — Artifact, Dimension, Gate —
are Concepts of the Engineering OS domain.

## lifecycle owner

`ArtifactRevisionLifecycle`, through the artifact that defines it. A Concept
does not have an independent lifecycle: it changes when its defining artifact is
revised.

## authoritative representation

A definition within an Ontology or Glossary artifact, carrying:

- canonical name
- definition
- bounded context
- synonyms and overloaded meanings
- examples and non-examples
- source evidence

## derived representations

- A node in the Canonical Knowledge Model.
- An OWL class, property or individual, once B2 establishes the mapping.
- Entries in search indexes, cross-reference indexes and the Knowledge Explorer.

## relationships

| Relationship | Target | Notes |
|---|---|---|
| defined-in | BoundedContext | exactly one |
| relates-to | Concept | typed by the ontology, not by this metamodel |
| expressed-in | Capability, Invariant, Specification | zero or more |
| evidenced-by | Evidence | the traceability chain |

## extension points

Every adopting repository defines its own Concepts. This is the primary
extension surface of the entire framework — Layer B is largely Concepts and
their relationships.

## Debt

**`BoundedContext` is referenced and is not an entity in the inventory.** The
inherited prototypes treat bounded contexts as central; the metamodel does not
yet name one. Recorded rather than added, per `ADR-0062` — but it is the most
likely next entity.

**`Evidence` is likewise referenced and absent.** The inherited evidence model
(`imports/reconstruct-system-knowledge/references/evidence-model.md`) has never
been adopted (`ISSUE-0018`).

**The Concept-to-OWL mapping is undefined**, and is the substance of B2.
