---
id: ISSUE-0014
title: model/changes/ is written to but absent from the canonical model tree
type: inconsistency
status: deferred
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - imports/ontology-driven-development-v2/SKILL.md
  - imports/reconstruct-system-knowledge/references/repository-structure.md
resolved-by: null
defers-to: [M2]
debt: architectural
---

# ISSUE-0014 — `model/changes/` is absent from the canonical model tree

> **Architectural debt** (`ADR-0062`). Deferred because it is not needed to
> build the next deliverable. Reopen when implementation requires it.

## Statement

`ontology-driven-development` writes its impact analysis to
`model/changes/<change-id>/impact-analysis.md`.

The canonical Layer B tree in
`imports/reconstruct-system-knowledge/references/repository-structure.md`
defines fifteen top-level directories — `research/`, `analysis/`, `domain/`,
`ontology/`, `validation/`, `graph/`, `engineering/`, `specs/`,
`traceability/`, `architecture/`, `playbooks/`, `loops/`, `prompts/`,
`tooling/`, `generated/` — and none of them is `changes/`.

The two prototypes disagree on the artifact contract.

## Why it matters

`model-spec/` is an M2 deliverable and must define one tree. Change records are
a first-class artifact of the methodology, so their location cannot be left
implicit.

## Options

- **Add `changes/` as a sixteenth top-level directory** — matches how
  `ontology-driven-development` already behaves.
- **Place change records under `analysis/`** — the tree already has
  `analysis/reports/`, and an impact analysis is arguably analysis.
- **Place them under `traceability/`** — change records are the link between
  intent and evidence.

## Resolution criteria

An ADR fixing the canonical Layer B tree, including where change records live,
recorded in `model-spec/`.
