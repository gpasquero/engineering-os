---
id: ISSUE-0056
title: The methodology artifacts have no layer under the four-layer architecture
type: gap
status: resolved
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0037-four-layer-semantic-architecture.md
  - governance/adr/ADR-0038-four-questions-for-every-new-artifact-type.md
  - governance/adr/ADR-0010-repository-local-knowledge-ownership.md
resolved-by: ADR-0039
---

# ISSUE-0056 — The methodology artifacts have no layer

## Statement

`ADR-0037` requires that **every artifact belongs to exactly one layer**, and
defines four:

| Layer | Contains |
|---|---|
| A | the Engineering OS Metamodel |
| B | a repository's knowledge model |
| C | the compiler-generated canonical model |
| D | derived projections |

Under `ADR-0010`, "Layer A" meant the methodology: `shared/`, `skills/`,
`workflows/`, `templates/`, `schemas/`. `ADR-0037` redefines Layer A as the
Metamodel alone.

**Those directories now have no layer.** Neither does `governance/`.

## Why it matters

`ADR-0038` makes "which layer owns it?" the first of four questions that must be
answerable before any new artifact type is accepted. **The project cannot answer
it for the artifacts it already has** — a rule that the existing corpus fails on
the day it is written.

It is marked `blocking` because M2 delivers contracts, manifests and the
metamodel, and each must declare a layer under `ADR-0038`.

## The candidate readings

**They are Layer B instances.** The metamodel has entities `Skill`, `Workflow`,
`Policy`, `Capability`. A concrete skill *instantiates* the `Skill` entity, and
instances belong to a repository's knowledge model. Engineering OS's own skills
would then be Layer B artifacts of the Engineering OS repository.

Coherent, and it explains why the metamodel lists those entities at all. But it
makes the methodology part of one repository's domain knowledge, which sits
oddly with adopters consuming it.

**They are Layer A, broadly construed** — Layer A being "what Engineering OS
owns and ships", of which the metamodel is the semantic core. Preserves the
intuition that the methodology is the framework, but weakens `ADR-0037`'s clean
statement that Layer A *is* the metamodel.

**A fifth layer for the methodology.** Honest, and it contradicts "this completes
the architecture".

**`governance/` is outside the layers entirely** — project memory rather than
semantic content. Plausible on its own terms, but then "every artifact belongs
to exactly one layer" is false as stated.

The first reading is the most consistent with the metamodel's entity list, and
the most surprising in its consequences.

## Resolution

`ADR-0039`. **All four readings above were wrong, because the question was.**

> **The problem comes from assigning layers to directories. Layers do not own
> directories. Layers own semantic artifacts.**

A directory may legitimately contain artifacts of multiple layers. Repository
layout is an **implementation** concern; the semantic layer is an
**architectural** one. **The compiler classifies artifacts, not folders.**

`governance/` is **orthogonal** to the semantic layers. ADRs, Issues, Acceptance
Records and Sessions are governance artifacts — inputs to the Engineering OS
*process*, not part of the semantic model of a target domain. The same applies to
`tests/`, `scripts/`, `tooling/`, `ci/` and editor configuration.

Two kinds of thing are now distinguished:

- **Semantic Layers** — A, B, C, D.
- **Cross-Cutting Infrastructure** — Governance, Tooling, Automation,
  Validation, Testing, CI/CD.

These intersect the semantic layers but are not themselves layers. The ambiguity
is resolved **without forcing unrelated artifacts into the semantic
architecture**.

`ADR-0037`'s universality claim is corrected: every *semantic* artifact belongs
to exactly one layer; cross-cutting artifacts belong to none. `ADR-0038`'s
question 1 accepts `None (Not Applicable)` as a valid answer.

Generalized by `ADR-0040` into Architectural Dimensions.

Opened by this answer: `ISSUE-0057` (the dimension and infrastructure sets are
examples) and `ISSUE-0058` (how an artifact declares its classification, now
that paths no longer imply it).
