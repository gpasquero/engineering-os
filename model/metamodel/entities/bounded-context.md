---
id: METAMODEL-BoundedContext
title: BoundedContext
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0035, ADR-0065]
---

# BoundedContext

**A boundary within which a set of terms has one consistent meaning.**

The first entity in the semantic backbone, because `Concept` and `Capability`
were both written referencing it before it existed.

## identity

A name, unique within the repository.

A BoundedContext is **not** a directory, a module, a package or a service. It
may correspond to one, and frequently will, but the correspondence is an
observation about a particular repository, not part of what a BoundedContext is.

## purpose

To make **the scope of a meaning explicit**.

Without it, every Concept name is a global claim. `Policy` means one thing in
governance and another in access control; `Artifact` means one thing here and
another in a build system. A metamodel with no boundaries forces every naming
collision to be resolved by renaming — which is exactly what this project did
eight times before `ADR-0057`.

> **A BoundedContext is what makes two identical names non-conflicting.**

This is the structural counterpart of the Naming Qualification discipline.
`ADR-0057` qualifies names *within* a context; the BoundedContext is what makes
qualification unnecessary *across* contexts.

## ownership

Owned by the repository that declares it. A Knowledge Package may **reference**
a context declared elsewhere, but never redefine one.

## lifecycle owner

`ArtifactRevisionLifecycle`.

## authoritative representation

A declaration in the repository's semantic model, naming the context and its
purpose. Concepts declare their context; the context does not enumerate its
Concepts.

That direction matters: **membership is asserted by the member.** A context that
listed its Concepts would be a hand-maintained projection, and `ISSUE-0037`
records what those cost.

## derived representations

- A grouping node in the Canonical Knowledge Model.
- A top-level navigation boundary in the Knowledge Explorer.
- A namespace or IRI prefix in generated ontologies.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| contains | Concept | zero or more (asserted by the Concept) |
| contains | Capability | zero or more (asserted by the Capability) |
| relates-to | BoundedContext | zero or more, descriptive only |

**`relates-to` is descriptive, never inferential** — the same rule `ADR-0044`
applies to Dimensions. That a context relates to another implies nothing about
the meaning of terms in either.

## extension points

An adopting repository declares any contexts its domain requires. The framework
declares none as mandatory.

## Debt

**The framework's own contexts are undeclared.** This repository plainly has
more than one — governance, the metamodel, compilation — and no declaration
exists for any of them. The entity is specified and unexercised, like `Dimension`
and `DimensionAssignment` before it.

**Context relationships have no vocabulary.** `relates-to` is a placeholder.
Whether contexts need typed relationships is unresolved and does not block B1.

**Whether a Concept may appear in two contexts is unstated.** The classical
answer is that the same *term* may, denoting different Concepts. Nothing here
says so, and `Concept` identity is defined as a qualified name — which implies
it but does not state it.
