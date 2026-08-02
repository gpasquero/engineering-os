---
id: ISSUE-0056
title: The methodology artifacts have no layer under the four-layer architecture
type: gap
status: open
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0037-four-layer-semantic-architecture.md
  - governance/adr/ADR-0038-four-questions-for-every-new-artifact-type.md
  - governance/adr/ADR-0010-repository-local-knowledge-ownership.md
resolved-by: null
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

## Resolution criteria

An ADR assigning a layer to `shared/`, `skills/`, `workflows/`, `templates/`,
`schemas/` and `governance/`, or amending `ADR-0037`'s claim that every artifact
belongs to exactly one layer. Must precede the M2 contracts, since each must
declare its layer.
