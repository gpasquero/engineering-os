---
id: ISSUE-0017
title: The three prototype phase models do not reconcile with the skill catalogue
type: inconsistency
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M4]
evidence:
  - imports/principal-engineering-skill/SKILL.md
  - imports/ontology-driven-development-v2/SKILL.md
  - imports/reconstruct-system-knowledge/SKILL.md
  - governance/design/skill-catalog.md
resolved-by: null
---

# ISSUE-0017 — Phase models do not reconcile with the skill catalogue

## Statement

`principal-engineering` defines 12 phases, `ontology-driven-development` 10, and
`reconstruct-system-knowledge` 15 (Phase 0 through Phase 14). The planned skill
catalogue lists 10 skills. None of these map cleanly onto any other.

## Why it matters

M4 through M7 build skills from this material. Without a mapping, content from
37 prototype phases will be re-derived by hand and will drift from its source.

## What we know

Phases with no corresponding skill in `governance/design/skill-catalog.md`:

- **Ontology Review** (`principal-engineering` phase 4) — no `model-ontology`
  skill exists in the catalogue.
- **Implementation Planning** (`principal-engineering` phase 9) — possibly
  folded into `design-change`, but never stated.
- **Confidence Report** and **Counterfactual Review** — cross-cutting quality
  gates in `principal-engineering` with no home at all.
- **Constraint placement**, **knowledge graph model**, **competency questions**
  (`reconstruct-system-knowledge` phases 8–10) — no dedicated skill.

`governance/roadmap.md` provisionally adds `model-ontology` and
`plan-implementation` to close the first two, but this is a proposal, not a
decision.

## Resolution criteria

A phase-to-skill mapping table covering all 37 prototype phases, recorded in
`docs/prototype-migration.md`, with an ADR confirming the final skill list.
