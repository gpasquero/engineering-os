---
id: DESIGN-README
title: Design Notes
status: current
created: 2026-08-02
updated: 2026-08-02
---

# Design Notes

Working proposals. **Not decisions.**

A document here has been thought about but not accepted. Nothing in this
directory is binding. When a proposal is accepted it becomes an ADR in
`governance/adr/` and a specification elsewhere; the design note may then be
left in place as history.

This separation exists because Principle 9 requires current state and proposed
state to be kept apart — including for this repository's own design.

## Contents

| File | Status |
|---|---|
| `proposed-architecture.md` | Superseded in part by `ADR-0006` and `ADR-0008`, which split `shared/` three ways and separated Layer A from Layer B. Retained as the origin of the seven-directory sketch. |
| `skill-catalog.md` | Ten skill names with no definitions. Recorded as incomplete in `ISSUE-0025`; likely missing skills recorded in `ISSUE-0017`. |
| `workflow-catalog.md` | Six workflow names. Conflicts with two other change-type taxonomies — see `ISSUE-0016`. |

All three were inherited at the pre-M1 handoff and moved here from the former
root-level `design/` directory by `ADR-0004`. They are **not** frozen
provenance — unlike `imports/` and `sources/`, they may be edited as the design
evolves. Their original form is in git history.
