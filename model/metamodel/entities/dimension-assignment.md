---
id: METAMODEL-DimensionAssignment
title: DimensionAssignment
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0042, ADR-0045]
---

# DimensionAssignment

**The explicit semantic relationship by which an artifact is classified.**

> **Artifacts do not contain dimension values** (`ADR-0042`).

```text
Artifact → DimensionAssignment → Dimension → Dimension Value
```

## identity

The triple of **subject, dimension and revision**: which artifact revision is
classified, along which dimension, at which revision of the assignment itself.

An assignment is versioned independently of the artifact it classifies. That is
the whole point of the entity: **reclassifying an artifact does not touch the
artifact.**

## purpose

To make classification a *relationship* rather than a *property*, so that:

- assignments are versioned;
- **assignments change without changing artifact identity**;
- dimensions evolve independently;
- **validation applies to assignments, not to artifacts**.

A constraint violation therefore names the relationship that is wrong, not a
file.

## ownership

Owned by the repository owning the artifact being classified.

## lifecycle owner

`ArtifactRevisionLifecycle`. An assignment is itself versioned and, being
authoritative, follows the normal acceptance workflow.

## authoritative representation

A **Human Representation**: a canonical serialization of the assignment,
exposed so the repository stays understandable without executing the compiler
(`ADR-0045`).

```text
DimensionAssignment → Canonical Serialization → Artifact Front Matter
```

> **Front matter is an interchange syntax, not the semantic model.** The
> compiler reconstructs the relationship from the serialization; the
> relationship exists independently of it.

## derived representations

- A **graph relationship** in the Canonical Knowledge Model — an edge, not
  embedded metadata.
- Filters, groupings and facets in Registry Projections and the Knowledge
  Explorer.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| classifies | ArtifactRevision | exactly one |
| along | Dimension | exactly one |
| has-value | value from the Dimension's value model | per the Dimension's cardinality |

## extension points

An adopting repository assigns any Dimension registered in its own or the
framework's registry. It does not extend what an assignment *is*.

## Debt

**The minimum set of classifications that must be serialized is unstated**
(`ISSUE-0063`). `ADR-0045` says an artifact *may* expose *selected*
classifications; nothing connects that to what must be knowable. An artifact can
satisfy `ADR-0045` while serializing nothing.

**Nothing checks that a serialization matches its assignment.** `ADR-0045` says
the relationship exists independently of the serialization, so a serialization
can be incomplete without being wrong — but whether it can be *stale* is
unaddressed.

**Assignment identity depends on assignments being versioned**, which requires
the revision-allocation convention that `ADR-0064` left open.
