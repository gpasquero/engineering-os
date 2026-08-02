---
id: ISSUE-0061
title: "Level" and "Layer" are two ordinal schemes whose first element is the metamodel in both
type: risk
status: resolved
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0043-three-semantic-levels.md
  - governance/adr/ADR-0037-four-layer-semantic-architecture.md
resolved-by: ADR-0046
---

# ISSUE-0061 — "Level" and "Layer" are confusable

## Statement

Two ordinal classification schemes now exist, and both begin with the metamodel.

| Scheme | Members |
|---|---|
| **Layers** (`ADR-0037`) | A — Metamodel · B — Repository Knowledge Model · C — Canonical Knowledge Model · D — Derived Projections |
| **Levels** (`ADR-0043`) | 1 — Metamodel · 2 — Model · 3 — Classification |

They are genuinely different axes. Layers classify *where in the compilation
pipeline* something sits. Levels classify *what kind of statement* something is.

But "Layer A — Metamodel" and "Level 1 — Metamodel" invite the reading that
layers and levels are the same scheme counted differently, and "Layer B —
Repository Knowledge Model" against "Level 2 — Model" reinforces it.

## Why it matters

This is recorded before it propagates, which is the discipline `ADR-0035`
established after five collisions were each caught late.

The project's record is the argument: "skill", "authoritative", "state",
"policy", "registry", and "layer" itself — six terminology problems in fourteen
sessions, every one expensive in proportion to how long it went unnoticed.

Both schemes are about to be written into the metamodel, where a reader
encounters them together for the first time.

## What makes this different from the previous six

The earlier cases were **one term with two meanings**, resolved by splitting.
This is **two terms for two genuinely different things**, at risk of being
conflated because they are near-synonyms in English and their first elements
coincide.

The remedy is therefore not a split. It is either a rename, or an explicit
statement of the relationship strong enough that the coincidence stops being
misleading — which `ADR-0043` attempts and this issue records as possibly
insufficient.

## Options

- **Rename one scheme.** Levels could become *semantic tiers*, *abstraction
  levels*, or *statement kinds*; layers could become *pipeline stages*. A rename
  is cheap now and expensive after the metamodel is written.
- **State the relationship in the metamodel**, so the two axes are modelled
  explicitly and their independence is machine-visible rather than prose.
  Consistent with `ADR-0040`: they are two dimensions.
- **Accept the risk**, on the grounds that `ADR-0043` already states the
  distinction. Cheapest, and it relies on every future reader encountering that
  paragraph.

The second is the most consistent with the architecture the project just built:
if levels and layers are independent axes, they are dimensions, and `ADR-0041`
already says how dimensions are declared.

## Resolution

`ADR-0046`. **Both concepts are valid and describe different dimensions.**

- **Level classifies abstraction.**
- **Layer classifies semantic position** in the Engineering OS knowledge
  architecture.

Explicit qualified names are introduced — **Abstraction Level** and **Semantic
Layer** — and future diagrams, specifications and ontology definitions always
use them in full.

> **No renaming is required. Only qualification.**

Neither of the first two options was taken as written. Renaming was rejected
because both words are accurate; formal registration is subsumed rather than
chosen, since they *are* two dimensions under `ADR-0040` and `ADR-0041` already
says how dimensions are declared.

This is the **third application of the same discipline**, after state names
(`ADR-0025`) and normative artifact types (`ADR-0030`). Three ADRs applying one
rule is a rule — it belongs in a `ModelingPolicy` in M3 rather than being
rediscovered a fourth time.
