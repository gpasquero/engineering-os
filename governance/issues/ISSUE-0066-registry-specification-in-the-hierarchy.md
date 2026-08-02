---
id: ISSUE-0066
title: Where the Registry Specification sits in the four-stage modeling hierarchy
type: question
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0050-definition-instance-assignment-projection.md
  - governance/adr/ADR-0032-registry-specification-versus-registry-projection.md
  - governance/adr/ADR-0048-dimension-specification-is-a-metamodel-entity.md
resolved-by: null
---

# ISSUE-0066 — Where the Registry Specification sits

## Statement

`ADR-0050` establishes a four-stage hierarchy:

```text
Definition → Instance → Assignment → Projection
```

For dimensions, the Definition stage is occupied by the **Dimension
Specification** and the Projection stage by the **Registry Projection**.

`ADR-0032` established a different artifact: the **Registry Specification**,
which is authoritative and defines registry identity, semantic purpose,
ownership, membership rules, required metadata, constraints, relationships and
extension rules.

**The Registry Specification is not any of the four stages.** It governs the
registry that holds them.

## Why it matters

Both are M2 deliverables. `ADR-0032` pairs Registry Specification with Registry
Projection as specification-and-derived; `ADR-0050` pairs Dimension
Specification with Registry Projection across four stages. The same Projection
now appears in two different pairings, which cannot both be the whole story.

Getting this wrong means either an artifact with no place in the pattern, or a
pattern that quietly has five stages while claiming four.

## Options

- **The Registry Specification is orthogonal to the hierarchy.** The four stages
  describe a *concept*; the registry describes a *collection* of them. Cleanest
  conceptually; means `ADR-0050`'s pattern is not the whole architecture, and
  the two must be related explicitly.
- **A fifth stage**, with the Registry Specification governing the Definition
  stage. `ADR-0050` considered and rejected this "for now" — reopening it would
  make the pattern complete at the cost of the symmetry that makes it memorable.
- **The Registry Specification *is* the Definition stage**, and Dimension
  Specifications are its Instances. This reads naturally — a registry defines
  what may be registered, and each registration instantiates it — but it
  contradicts `ADR-0048`, which places Dimension Specification at Definition and
  Dimension at Instance.
- **The hierarchy applies per concept, and each concept's registry is described
  by its own Registry Specification**, which sits above all four stages.

## The question underneath

**Does the Registry Specification describe a container, or a kind?**

If a container, it is orthogonal and the first option holds. If a kind, the
third option holds and `ADR-0048`'s stage assignment needs revisiting.

`ADR-0032`'s field list — membership rules, extension rules — reads like a
container. But *required metadata* and *constraints* read like a kind.

## Resolution criteria

An ADR placing the Registry Specification relative to the four stages, and
stating whether `ADR-0050`'s pattern is complete or one part of a larger
structure.
