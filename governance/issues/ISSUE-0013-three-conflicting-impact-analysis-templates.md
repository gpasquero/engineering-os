---
id: ISSUE-0013
title: Three conflicting impact-analysis templates were inherited
type: inconsistency
status: deferred
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - imports/ontology-driven-development-v2/templates/impact-analysis.md
  - imports/principal-engineering-skill/templates/impact-analysis.md
  - imports/ontology-driven-development-v2/SKILL.md
resolved-by: null
defers-to: [M2]
debt: architectural
---

# ISSUE-0013 — Three conflicting impact-analysis templates

> **Architectural debt** (`ADR-0062`). Deferred because it is not needed to
> build the next deliverable. Reopen when implementation requires it.

## Statement

Three different definitions of the impact analysis exist, and no document says
which is canonical:

1. `imports/ontology-driven-development-v2/templates/impact-analysis.md` — 190
   lines, full metadata, gate decision, post-implementation review.
2. `imports/principal-engineering-skill/templates/impact-analysis.md` — 24
   lines, a flat heading list.
3. `imports/ontology-driven-development-v2/SKILL.md` sections 4.1–4.12 — twelve
   enumerated analysis categories.

## Why it matters

The impact analysis is the operational core of the methodology. Three
definitions means three different gates, and no way to tell whether an analysis
is complete.

## What we know

The category sets genuinely differ. The `principal-engineering` template has
top-level **Performance** and **Business impact** sections. The twelve
categories in `ontology-driven-development` have neither — performance appears
only as a test type and a verification step, and business impact is absent
entirely.

Template (1) is the most developed and is the only one with a post-implementation
review section.

## Resolution criteria

A single canonical impact-analysis template in `templates/`, with an explicit
category list, adopted by ADR. The ADR must state whether Performance and
Business impact become top-level categories.
