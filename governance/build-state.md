---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: M2
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).

## Current milestone

**M2 — The Metamodel, foundational contracts and manifests. Not started, and
blocked.**

M1 is complete. **M3 is unblocked.**

## What exists

| Area | State |
|---|---|
| Repository architecture | Defined and accepted |
| Documentation system, session protocol | Defined and accepted |
| Vision, principles, glossary | Written |
| Roadmap | M1–M13 |
| ADRs | 38 — 32 accepted, 6 superseded |
| Issues | 56 recorded — 22 open, 33 resolved, 1 deferred |
| Acceptance Records | 8 — `ACCEPT-0001` (trust root) through `ACCEPT-0008` |
| Session journal | 13 entries |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff) |

## What does not exist

**The Metamodel does not exist.** It is M2's first deliverable, at
`model/metamodel/`, and it is Layer A (`ADR-0037`).

No executable code, and none is planned before M9 (`ADR-0017`, `ISSUE-0036`).

Nothing in `shared/`, `skills/`, `workflows/`, `model-spec/`, `model/`,
`templates/`, `schemas/`, `validation/`, `tests/`, `adapters/` or `docs/`. None
of the three manifests. No Registry Specification of any kind. **No policies of
any kind.**

## The architecture, in four layers

`ADR-0037` completed it. Every artifact belongs to exactly one layer.

| Layer | Defines | Status here |
|---|---|---|
| **A** — Engineering OS Metamodel | the language | Does not exist; M2's first deliverable |
| **B** — Repository Knowledge Model | a domain in that language | Does not exist |
| **C** — Canonical Knowledge Model | compiler output | Requires a compiler |
| **D** — Derived Projections | Explorer, docs, indexes, packages, validation, search | Five hand-maintained projections only (`ISSUE-0037`) |

## Acceptance status

| Record | Covers |
|---|---|
| `ACCEPT-0001` | Bootstrap corpus at `2b6484f` — trust root, the only retrospective acceptance |
| `ACCEPT-0002` | `SESSION-0006` at `aed6d89` — first under the normal workflow |
| `ACCEPT-0003`–`ACCEPT-0008` | `SESSION-0007` through `SESSION-0012` |

**`ADR-0037`, `ADR-0038`, `ISSUE-0056` and this session's propagation are `Under
Review`**, not `Active`.

## A note for agents reading this repository

**The ADR corpus is history, not specification** (`ADR-0029`). Thirty-eight
decisions, six superseded, two partially corrected.

**Two process gates are in force:**

- Every new concept must be positioned in the Metamodel before a new artifact
  type is introduced (`ADR-0035`). The Metamodel does not exist yet.
- Every new artifact type must answer four questions before acceptance
  (`ADR-0038`): which layer owns it; authoritative or derived; what metamodel
  entity it instantiates; which compiler phase consumes or produces it. **An
  unanswerable question is a rejection.**

## Blocking

| Issue | Blocks |
|---|---|
| `ISSUE-0056` | **M2.** `ADR-0038` requires every artifact type to declare a layer, and `shared/`, `skills/`, `workflows/`, `templates/`, `schemas/` and `governance/` have none. |
| `ISSUE-0002` | M8 |
| `ISSUE-0006` | M10 |

`ISSUE-0049` gates the state machine specifications and `shared/vocabularies/`
within M2.

## Must be resolved within M2

`ISSUE-0007`, `ISSUE-0011`, `ISSUE-0013`, `ISSUE-0014`, `ISSUE-0015`,
`ISSUE-0018`, `ISSUE-0019`, `ISSUE-0048`.

## Known debt

- **`ISSUE-0037`** — five hand-maintained Registry Projections; no compiler until
  `ISSUE-0036` is un-deferred.
- **`ISSUE-0048`** — no machine-readable correction mechanism. Three corrections
  now exist, visible only in the ADR index.
- **`ADR-0038` is failed by the existing corpus** on the day it was written.
  `ISSUE-0056` is that compliance debt.

## Next action

Accept or return this session's work.

Then `ISSUE-0056`. It is the only issue blocking M2, and `ADR-0038` cannot be
applied to anything until the existing directories have layers.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Visibility: **public, with no licence file** — `ISSUE-0011`
