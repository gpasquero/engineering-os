---
id: METAMODEL-Dimension
title: Dimension
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0040, ADR-0041, ADR-0048, ADR-0049, ADR-0070]
supersedes: METAMODEL-DimensionSpecification
---

# Dimension

**An independent axis of classification.**

> **One entity, not two.** `DimensionSpecification` was merged in by `ADR-0070`:
> a Dimension has no instances that exist independently of the repository, so
> there is nothing for a Specification to be a specification *of*.

## What new semantics does this introduce?

**Orthogonal classification.** The ability to say that an artifact is several
things at once, along axes that do not derive from one another.

`Concept` names meanings and `RelationshipType` names associations; neither can
express that a set of values forms an axis, or that two axes are independent.

## identity

A stable identifier, allocated when the Dimension is accepted, and registered in
the Dimension Registry — a section of `KNOWLEDGE-MANIFEST.yaml` (`ADR-0028`).

## purpose

To let artifacts be classified along several independent axes simultaneously,
rather than forcing every classification into a single hierarchy (`ADR-0040`).

**Dimensions are a scarce architectural resource.** A concept becomes a Dimension
only if all five conditions hold (`ADR-0049`):

1. It classifies many independent artifact types.
2. Its values are **orthogonal to other classifications**.
3. It is expected to evolve independently.
4. It is useful for querying, navigation or validation.
5. Multiple values can exist across repository artifacts.

Otherwise it is modelled as metadata, a property, a relationship, or another
metamodel entity.

**Independence is not isolation** (`ADR-0044`). A Dimension may declare
relationships describing compatibility, applicability or constraints. Those are
**descriptive, never inferential** — no Dimension derives another's value unless
an explicit Inference Rule exists, and Inference Rules, if ever introduced, are
their own first-class artifact type.

## ownership

Framework dimensions are owned by Engineering OS. **An adopting repository may
register its own** without forking the framework (`ADR-0041`).

## lifecycle owner

`ArtifactRevisionLifecycle`.

**A Dimension enters the metamodel only through a Dimension Review**
(`ADR-0051`) — an Engineering Gate producing one of four outcomes: accepted as a
Dimension, or rejected and modelled as metadata, a relationship, or another
metamodel entity.

## authoritative representation

A declaration of ten fields (`ADR-0048`):

identifier · purpose · governed entity types · **value model** · **assignment
semantics** · cardinality · constraints · relationships · **serialization
strategy** · **validation rules**

## derived representations

- An entry in the **Dimension Registry Projection**, generated from the registry.
- Nodes and edges in the Canonical Knowledge Model.
- Filter and grouping axes in the Knowledge Explorer.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| assigns-via | DimensionAssignment | zero or more |
| classifies | entity type | one or more |
| relates-to | Dimension | zero or more, descriptive only |

**`classifies` replaces the former `governs`.** `governs` named three different
relationships across the metamodel — constrains normatively, controls the
lifecycle of, and may classify — and the ontology had already been forced to
rename one occurrence to avoid a clash (`views/README.md` #4). This is the
occurrence that meant *may classify*.

## extension points

**Future dimensions are added by registration, never by modifying compiler
logic** (`ADR-0041`) — the strongest form of the Registry Pattern in the
framework, because it constrains the implementation rather than only the data.

## Debt

**No Dimension has passed a Dimension Review.** Nine candidates exist — Semantic
Layer, Artifact Taxonomy, Lifecycle, Compilation Phase, Abstraction Level,
Governance Status, Ownership, Authority, Visibility — and five are in active use
across the corpus without ever having been tested against the five conditions.

Two are expected to fail. `Compilation Phase` classifies artifacts by when a
compiler touches them, which places a compiler concept in the semantic model
(`ADR-0053`). `Governance Status` appears to duplicate
`ArtifactRevisionLifecycle`, failing the orthogonality condition.

**This specification describes a shape with no instances.** The mechanism is
defined and unexercised.
