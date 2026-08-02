---
id: ISSUE-0004
title: Where the Layer B model tree lives for a target system is undefined
type: question
status: open
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - imports/reconstruct-system-knowledge/SKILL.md
  - imports/reconstruct-system-knowledge/references/repository-structure.md
  - imports/ontology-driven-development-v2/README.md
resolved-by: null
---

# ISSUE-0004 — Where the Layer B `model/` tree lives is undefined

## Statement

All three prototypes assume the knowledge model lives at `model/` inside the
target repository. None considers a system spread across multiple repositories,
or an organization that wants one knowledge model spanning several codebases.

## Why it matters

`model-spec/` is an M2 deliverable and must state where its scaffold is
installed. The answer also determines how traceability references are written:
paths relative to a target repository do not survive a move to a central store.

## What we know

- `reconstruct-system-knowledge` restricts all its writes to `model/` in the
  current working directory.
- `ontology-driven-development` writes to `model/changes/<change-id>/`, a path
  absent from the canonical tree (`ISSUE-0014`).
- `ADR-0006` separated Layer A from Layer B but deliberately did not decide
  placement.

## Options

- **In the target repository** (`model/`) — matches the prototypes; simple;
  co-versioned with the code it describes; breaks for multi-repo systems.
- **Sibling knowledge repository** — supports multi-repo; loses atomic
  co-versioning of code and model.
- **Central knowledge store** for an organization — strongest for cross-system
  questions; heaviest; raises access-control questions.
- **Configurable, with in-repo default** — flexible; every skill must then
  resolve a configured root rather than a fixed path, which interacts with
  `ISSUE-0015`.

## Resolution criteria

An ADR naming the default location, whether it is configurable, and how
traceability references are expressed so they survive relocation.
