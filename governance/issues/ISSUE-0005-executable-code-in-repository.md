---
id: ISSUE-0005
title: Whether the Engineering OS ships executable code is undecided
type: question
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M9]
evidence:
  - sources/handoff/ROADMAP.md
  - governance/design/proposed-architecture.md
  - imports/reconstruct-system-knowledge/SKILL.md
resolved-by: null
---

# ISSUE-0005 — Whether this repository ships executable code is undecided

## Statement

The architecture includes `validation/` and `tests/`, and the roadmap includes
"Schemas" and "Scenario tests". These imply a runtime. Nothing states whether
this repository contains runnable code, or only specifications that a target
project implements.

## Why it matters

Determines whether M9 produces scripts or specifications, whether the repository
needs a language toolchain, dependency management and CI, and whether
`ISSUE-0002` may resolve to an executable runner.

## What we know

- `reconstruct-system-knowledge` deliberately defers tooling choice to the
  target ecosystem, listing ROBOT, Jena, OWLAPI, RDFLib and pySHACL as
  possibilities, and warns: "Do not introduce a heavy platform before a simpler
  tool proves insufficient."
- That guidance is about the *target* repository, not this one. The distinction
  was never drawn.

## Options

- **Pure specification** — no code; validation is described and implemented
  per-project. Maximum portability, no enforcement.
- **Reference implementation** — this repository ships validators and a runner
  in one language. Enforceable, adds a dependency and a maintenance burden.
- **Schemas plus thin scripts** — JSON Schema as the contract, small scripts for
  convenience. Middle path.

## Resolution criteria

An ADR stating whether executable code is in scope, and if so which language and
what may depend on it.
