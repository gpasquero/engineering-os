---
id: METAMODEL-DimensionSpecification
title: DimensionSpecification
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0048, ADR-0041, ADR-0049]
---

# DimensionSpecification

Defines **one independent axis of classification**. Not merely a taxonomy — a
semantic construct (`ADR-0041`).

**Dimensions must be specified before they can be instantiated** (`ADR-0048`).

## identity

A stable identifier, allocated when the specification is accepted. Registered in
the Dimension Registry, which is a section of `KNOWLEDGE-MANIFEST.yaml`
(`ADR-0028`).

## purpose

To let artifacts be classified along several independent axes simultaneously,
rather than forcing every classification into a single hierarchy (`ADR-0040`).

Dimensions are **a scarce architectural resource**. A concept becomes a
Dimension only if all five conditions hold (`ADR-0049`):

1. It classifies many independent artifact types.
2. Its values are **orthogonal to other classifications**.
3. It is expected to evolve independently.
4. It is useful for querying, navigation or validation.
5. Multiple values can exist across repository artifacts.

Otherwise it is modelled as metadata, a property, a relationship, or another
metamodel entity.

## ownership

Framework dimensions are owned by Engineering OS. **An adopting repository may
register its own** without forking the framework (`ADR-0041`).

## lifecycle owner

`ArtifactRevisionLifecycle`. A DimensionSpecification is an authoritative
artifact and follows the normal acceptance workflow.

**It enters the metamodel only through a Dimension Review** (`ADR-0051`) — an
Engineering Gate producing one of four outcomes: accepted as a Dimension, or
rejected and modelled as metadata, a relationship, or another metamodel entity.

## authoritative representation

A specification declaring ten fields (`ADR-0048`):

identifier · purpose · governed entity types · **value model** · **assignment
semantics** · cardinality · constraints · relationships · **serialization
strategy** · **validation rules**

## derived representations

- An entry in the **Dimension Registry Projection**, generated from the registry.
- Nodes and edges in the Canonical Knowledge Model.

## relationships

| Relationship | Target | Notes |
|---|---|---|
| instantiated-by | Dimension | the axis itself |
| governs | ArtifactType | which types it may classify |
| relates-to | DimensionSpecification | **descriptive, never inferential** |

**Independence is not isolation** (`ADR-0044`). Dimension values are never
derived from one another, but a dimension may declare relationships describing
**compatibility, applicability or constraints**. They never imply automatic
classification. No dimension derives another's value unless an explicit
Inference Rule exists — and Inference Rules, if ever introduced, are their own
first-class artifact type.

## extension points

**Future dimensions are added by registration, never by modifying compiler
logic** (`ADR-0041`). This is the strongest form of the Registry Pattern in the
framework: it constrains the *implementation*, not only where data lives.

## Recorded while building

**No dimension has been specified yet.** Nine candidates exist — Semantic Layer,
Artifact Taxonomy, Lifecycle, Compilation Phase, Abstraction Level, Governance
Status, Ownership, Authority, Visibility — and none has passed a Dimension
Review, though five are in active use across the corpus.

Two are expected to fail. `Compilation Phase` classifies artifacts by when a
compiler touches them, which puts a compiler concept in the semantic model
(`ADR-0053`). `Governance Status` appears to duplicate
`ArtifactRevisionLifecycle`, failing condition 2.
