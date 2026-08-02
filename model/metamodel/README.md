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

**First increment.** The entity inventory is complete; entity specifications are
being written one at a time. `entity-inventory.md` records which exist.

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
└── entities/              one specification per entity
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

## What this is not

Not OWL, yet. The first OWL ontologies are the next deliverable, and this
inventory is what they will formalize. Authoring in readable Markdown first
keeps `ADR-0017`'s guarantee intact — authoritative artifacts stay usable
without executing the compiler — while the OWL serialization is designed.
