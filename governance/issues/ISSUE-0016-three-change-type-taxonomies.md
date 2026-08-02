---
id: ISSUE-0016
title: Three incompatible taxonomies of change type were inherited
type: inconsistency
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M8]
evidence:
  - governance/design/workflow-catalog.md
  - imports/ontology-driven-development-v2/SKILL.md
resolved-by: null
---

# ISSUE-0016 — Three incompatible change-type taxonomies

## Statement

Three different classifications of "kind of change" exist:

1. `governance/design/workflow-catalog.md` — **six** workflows: feature, bug, behavior
   change, refactoring, integration, architecture evolution.
2. `ontology-driven-development` special workflows — **four**: new capability,
   bug, behavior change, refactoring. No integration, no architecture evolution.
3. `ontology-driven-development` Phase 1 classification — **eleven** types: new
   capability, bug, behavior change, refactoring, performance, security, data
   migration, integration, operational change, documentation, infrastructure.

There is also a naming collision: the catalogue says "Feature", the skill says
"New capability".

## Why it matters

M8 builds one workflow per change type. Three taxonomies means the workflow set
is undefined. It also affects `understand-request` in M4, which must classify an
incoming request into whichever taxonomy is canonical.

## What we know

Taxonomies (1) and (3) serve different purposes and may both be legitimate:
classification (3) is a *description* of a request, which may carry several
labels at once; workflow selection (1) picks *one* path to follow. Taxonomy (2)
appears simply to be incomplete relative to (1).

## Resolution criteria

A single closed vocabulary in `shared/vocabularies/change-types.yaml`, with an
explicit statement of whether classification and workflow selection use the same
set, and a mapping between them if they do not.
