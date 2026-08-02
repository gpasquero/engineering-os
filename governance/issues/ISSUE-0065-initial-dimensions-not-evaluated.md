---
id: ISSUE-0065
title: The initial dimension candidates have not been evaluated against the five conditions
type: gap
status: open
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0049-dimensions-are-a-scarce-architectural-resource.md
  - governance/adr/ADR-0048-dimension-specification-is-a-metamodel-entity.md
  - governance/adr/ADR-0047-three-representations-of-knowledge.md
resolved-by: null
---

# ISSUE-0065 — The initial dimensions have not been evaluated

## Statement

`ADR-0049` establishes that a concept becomes a Dimension only if all five
conditions hold, and that **creating a Dimension requires an ADR**.

Nine candidates exist and **none has been evaluated**:

| Candidate | Source | Status |
|---|---|---|
| Semantic Layer | `ADR-0037`, `ADR-0040` | In use, never tested |
| Artifact Taxonomy | `ADR-0012`, `ADR-0040` | In use, never tested |
| Lifecycle | `ADR-0020`, `ADR-0040` | In use, never tested |
| Compilation Phase | `ADR-0040` | In use, never tested |
| Abstraction Level | `ADR-0043`, `ADR-0046` | In use, never tested |
| Governance Status | `ADR-0040` | Undefined; suspected duplicate of Lifecycle |
| Ownership | `ADR-0040` | Undefined |
| Authority | `ADR-0040` | Undefined; suspected duplicate of Ownership |
| Visibility | `ADR-0040` | Undefined |
| Representation | `ADR-0047` | Never classified |

## Why it matters

`ADR-0048` requires a Dimension Specification with ten fields before any
dimension can be instantiated, and the Dimension Registry is M2 work. Writing
specifications for concepts that fail `ADR-0049`'s test would put duplicate axes
into the registry on its first day — the exact failure both ADRs exist to
prevent.

Five candidates are already in active use across the corpus without ever having
been tested against the conditions that now govern them.

## Reading against condition 2

Condition 2 is orthogonality, and it is where the open questions concentrate.

**`Governance Status` most likely fails.** `ArtifactRevisionLifecycle` already
ranges over `Draft`, `Under Review`, `Accepted`, `Active`, `Superseded`,
`Archived` — which is governance status. Two axes over one value space are not
orthogonal.

**`Authority` may fail against `Ownership`.** `ADR-0040`'s worked example gives
an `Owner` value and no `Authority` value at all, which suggests one axis was
intended.

**`Representation` is genuinely uncertain.** It aligns almost exactly with
Semantic Layer for semantic artifacts, but `ADR-0039` gives cross-cutting
artifacts no layer while they plainly have an Authoring Representation. If it
ranges over strictly more artifacts, it is orthogonal; if it ranges over
*encodings* rather than artifacts, the comparison is a category error and both
stand. `ADR-0047` does not say.

These are readings offered for evaluation, not determinations.

## Resolution criteria

An ADR per surviving dimension, each recording the five conditions, plus an
explicit decision to model the failures as metadata, properties, relationships
or metamodel entities. Must precede the Dimension Registry.
