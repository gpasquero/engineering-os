---
id: METAMODEL
title: Engineering OS Metamodel
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
artifact-kind: authoritative
---

# Engineering OS Metamodel

**Semantic Layer A.** The ontology of Engineering OS itself.

> Its purpose is not to describe software systems. Its purpose is to describe
> **how Engineering OS describes software systems** (`ADR-0035`).

Every adopting repository owns its own knowledge model (Layer B), **expressed
using this metamodel**. Adopters never modify it — they instantiate it
(`ADR-0037`).

## Status

**12 of 27 entities specified**, all of them descriptive. The operational family
(`ADR-0065`) is entirely unbuilt. `entity-inventory.md` records the current state.

This is being built under `ADR-0062`: where an existing decision permits
building, we build, and open questions that do not block the next deliverable
are recorded as architectural debt rather than as blockers.

## What an entity specification contains

Every metamodel entity declares eight properties (`ADR-0035`):

| Property | States |
|---|---|
| identity | how an instance is identified |
| purpose | what the entity is for |
| ownership | who owns instances |
| lifecycle owner | which state machine governs its revisions |
| authoritative representation | how it is authored |
| derived representations | what the compiler produces from it |
| relationships | how it relates to other entities |
| extension points | how an adopting repository extends it |

## Structure

```text
model/metamodel/
├── README.md              this file
├── entity-inventory.md    all entities, with specification status
├── entities/              one specification per entity
└── ontology/              the OWL skeleton, and what writing it exposed
```

## Conventions in force

- **Canonical names are qualified** by their architectural dimension where
  ambiguity is possible (`ADR-0057`). Short names are informal.
- **The semantic hierarchy is `Definition → Instance → Assignment`**
  (`ADR-0052`). Projection belongs to the compilation hierarchy, not here.
- **The metamodel contains no compiler concepts** (`ADR-0053`). It defines what
  exists; the compiler defines how it is transformed.
- **Classification is a relationship, not a property** (`ADR-0042`). Entities do
  not carry dimension values; Dimension Assignments relate them.
- **Every entity declares its family** — descriptive or operational (`ADR-0065`).
  The two are not peers and no specification treats them as interchangeable.

## The OWL skeleton

`ontology/engineering-os-metamodel.ttl` expresses the specified entities as OWL,
and was written deliberately **before** the metamodel was complete. Reading the
specifications as class definitions exposed a missing superclass, an entity that
may be redundant, and two relationships pointing at nothing defined — see
`ontology/FINDINGS.md`.

Markdown remains the authoring form, which keeps `ADR-0017`'s guarantee intact:
authoritative artifacts stay usable without executing the compiler. **Which of
the two is authoritative is not yet decided**, and maintaining both by hand is
the cost `ISSUE-0037` describes.
