---
id: ISSUE-0064
title: Whether Representation is an independent dimension or a grouping of Semantic Layers
type: question
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0047-three-representations-of-knowledge.md
  - governance/adr/ADR-0037-four-layer-semantic-architecture.md
  - governance/adr/ADR-0039-layers-classify-artifacts-not-directories.md
resolved-by: null
---

# ISSUE-0064 — Representation versus Semantic Layer

## Statement

`ADR-0047` introduces three representations of knowledge. They map onto the four
Semantic Layers almost exactly:

| Representation | Semantic Layer |
|---|---|
| Authoring | A and B |
| Semantic | C |
| Presentation | D |

That makes Representation look like a **coarser partition of the same axis**
rather than an independent one — which under `ADR-0040` would make it a
relationship between dimensions, not a dimension.

## Why it matters

`ADR-0041` requires every dimension to be registered with eight fields, and the
Dimension Registry Specification is M2 work. Registering a redundant axis would
put a duplicate into the registry, and `ISSUE-0061` has just established that
near-duplicate classification schemes are caught before the metamodel names
them, not after.

This is now the **third** scheme in this family — Semantic Layer, Abstraction
Level, Representation — and the second time in two sessions that a new one has
needed checking against an existing one.

## The reading that makes them independent

**Representation applies to cross-cutting artifacts; Semantic Layer does not.**

`ADR-0039` established that governance, tooling, testing and CI/CD have Semantic
Layer `None`. But an ADR plainly has an **Authoring Representation** — it is a
human-editable source artifact — and appears in **Presentation** through the
generated indexes.

If that holds, Representation ranges over strictly more artifacts than Semantic
Layer, and the two are genuinely independent despite the near-alignment on
semantic artifacts.

This reading is coherent and is **not stated in `ADR-0047`**.

## Options

- **Independent dimension**, on the reading above. Registered with eight fields;
  its relationship to Semantic Layer declared descriptively per `ADR-0044`.
- **A grouping of Semantic Layers**, expressed as a relationship rather than a
  dimension. Simpler, and it would mean cross-cutting artifacts have no
  representation — which contradicts the fact that they are authored and
  presented.
- **A dimension over a different entity type.** Representations may classify
  *encodings of knowledge* rather than *artifacts*, in which case the comparison
  with Semantic Layer is a category error and both can stand unchanged.

The third option is worth serious weight: `ADR-0047` calls them "views of the
same knowledge", which is not obviously a property of an artifact at all.

## Resolution criteria

An ADR stating whether Representation is a registered dimension, what entity
type it governs, and how it relates to Semantic Layer under `ADR-0044`'s
descriptive-relationship rule.
