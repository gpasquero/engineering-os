---
id: ISSUE-0025
title: Skill decomposition is recorded as complete but is only a list of names
type: gap
status: open
severity: medium
created: 2026-08-02
updated: 2026-08-02
blocks: [M4]
evidence:
  - sources/handoff/BUILD-STATE.md
  - governance/design/skill-catalog.md
  - governance/design/workflow-catalog.md
resolved-by: null
---

# ISSUE-0025 — Skill decomposition is a name list, not a decomposition

## Statement

The pre-M1 `sources/handoff/BUILD-STATE.md` listed "Skill decomposition" under **Completed**.

`governance/design/skill-catalog.md` is ten bare names with no inputs, outputs,
preconditions, postconditions, or statement of responsibility.
`governance/design/workflow-catalog.md` is six bare names.

## Why it matters

Recording incomplete work as complete is a memory defect: a future session
reading the build state would skip the work believing it done. This is the
failure mode the documentation system exists to prevent, and it was present in
the inherited state.

M4 through M7 depend on real skill definitions.

## What we know

- A name list is a useful starting point and should not be discarded; it is
  preserved in `governance/design/` as a working proposal.
- `ISSUE-0017` shows the list is also incomplete — at least `model-ontology` and
  `plan-implementation` are missing, and several prototype phases have no home.

## Resolution criteria

A skill contract per skill, conforming to the contract defined in M2: inputs,
outputs, preconditions, postconditions, policies consumed, artifacts produced,
write scope. The catalogue is only complete when every prototype phase maps to a
skill (`ISSUE-0017`).
