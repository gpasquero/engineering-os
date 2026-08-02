---
id: METAMODEL-Dimension
title: Dimension
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0040, ADR-0041, ADR-0048]
---

# Dimension

**An independent axis of classification**, instantiated from a
[DimensionSpecification](dimension-specification.md).

## identity

The identifier declared by its DimensionSpecification. A Dimension does not have
an identity separate from the specification that defines it — it is the axis
that specification describes.

## purpose

To let artifacts be classified along several independent axes simultaneously
rather than being forced into a single hierarchy (`ADR-0040`).

**Independence is not isolation** (`ADR-0044`). Dimension values are never
derived from one another, but a Dimension may declare relationships describing
compatibility, applicability or constraints. Those relationships are
**descriptive, never inferential** — they never imply automatic classification.

No Dimension derives another's value unless an explicit Inference Rule exists,
and Inference Rules, if ever introduced, are their own first-class artifact type.

## ownership

Framework dimensions are owned by Engineering OS. **An adopting repository may
register its own** without forking the framework (`ADR-0041`).

## lifecycle owner

`ArtifactRevisionLifecycle`, through its DimensionSpecification.

A Dimension enters the metamodel **only through a Dimension Review**
(`ADR-0051`) — an EngineeringGate producing one of four outcomes: accepted as a
Dimension, or rejected and modelled as metadata, a relationship, or another
metamodel entity.

## authoritative representation

None of its own. A Dimension is manifested by its DimensionSpecification, which
declares the ten fields `ADR-0048` requires.

## derived representations

- An entry in the **Dimension Registry Projection**, generated from the registry
  section of `KNOWLEDGE-MANIFEST.yaml` (`ADR-0028`).
- Nodes and edges in the Canonical Knowledge Model.
- Filter and grouping axes in the Knowledge Explorer.

## relationships

| Relationship | Target | Notes |
|---|---|---|
| specified-by | DimensionSpecification | exactly one |
| assigns-via | DimensionAssignment | zero or more |
| governs | ArtifactType | which types it may classify |
| relates-to | Dimension | descriptive only, never inferential |

## extension points

**Future dimensions are added by registration, never by modifying compiler
logic** (`ADR-0041`) — the strongest form of the Registry Pattern in the
framework, because it constrains the implementation rather than only the data.

## Debt

**No Dimension has passed a Dimension Review.** Nine candidates exist and five
are in active use across the corpus — Semantic Layer, Artifact Taxonomy,
Lifecycle, Compilation Phase, Abstraction Level — without ever having been
tested against the five conditions that now govern them.

Two are expected to fail. `Compilation Phase` classifies artifacts by when a
compiler touches them, which places a compiler concept in the semantic model
(`ADR-0053`). `Governance Status` appears to duplicate
`ArtifactRevisionLifecycle`, failing the orthogonality condition.

**This specification therefore describes a shape with no instances.** That is a
real state and worth naming: the mechanism is defined and unexercised.
