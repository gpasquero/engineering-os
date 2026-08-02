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
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

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
| ADRs | 40 — 34 accepted, 6 superseded |
| Issues | 58 recorded — 23 open, 34 resolved, 1 deferred |
| Acceptance Records | 9 — `ACCEPT-0001` (trust root) through `ACCEPT-0009` |
| Session journal | 14 entries |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff) |

## What does not exist

**The Metamodel does not exist.** It is M2's first deliverable, at
`model/metamodel/`.

No executable code, and none is planned before M9 (`ADR-0017`, `ISSUE-0036`).

Nothing in `shared/`, `skills/`, `workflows/`, `model-spec/`, `model/`,
`templates/`, `schemas/`, `validation/`, `tests/`, `adapters/` or `docs/`. None
of the three manifests. No Registry Specification. **No policies of any kind.**

## The architecture

**Semantic Layers** — every *semantic* artifact belongs to exactly one
(`ADR-0037`, corrected by `ADR-0039`):

| Layer | Defines | Status here |
|---|---|---|
| **A** — Engineering OS Metamodel | the language | Does not exist; M2's first deliverable |
| **B** — Repository Knowledge Model | a domain in that language | Does not exist |
| **C** — Canonical Knowledge Model | compiler output | Requires a compiler |
| **D** — Derived Projections | Explorer, docs, indexes, packages, validation, search | Five hand-maintained projections only |

**Cross-Cutting Infrastructure** — Governance, Tooling, Automation, Validation,
Testing, CI/CD. Orthogonal to the layers; Semantic Layer `None`. **Everything
this repository currently contains outside `imports/` and `sources/` is
governance.**

**Layers classify artifacts, not directories** (`ADR-0039`). Repository layout is
an implementation concern.

**Architectural Dimensions** (`ADR-0040`) — artifacts are classified along
several independent axes simultaneously, not forced into one hierarchy.

## Acceptance status

| Record | Covers |
|---|---|
| `ACCEPT-0001` | Bootstrap corpus at `2b6484f` — trust root, the only retrospective acceptance |
| `ACCEPT-0002` | `SESSION-0006` at `aed6d89` — first under the normal workflow |
| `ACCEPT-0003`–`ACCEPT-0009` | `SESSION-0007` through `SESSION-0013` |

**`ADR-0039`, `ADR-0040`, `ISSUE-0057`, `ISSUE-0058` and this session's
propagation are `Under Review`**, not `Active`.

## A note for agents reading this repository

**The ADR corpus is history, not specification** (`ADR-0029`). Forty decisions,
six superseded, **four partially corrected**.

**Two process gates are in force:**

- Position every new concept in the Metamodel before introducing a new artifact
  type (`ADR-0035`). The Metamodel does not exist yet.
- Answer four questions before accepting a new artifact type (`ADR-0038`):
  layer, artifact kind, metamodel entity, compiler phase. `None (Not
  Applicable)` is a valid layer for cross-cutting artifacts; a genuinely
  undetermined answer is a rejection.

## Blocking

| Issue | Blocks |
|---|---|
| `ISSUE-0057` | **M2.** The dimension set is examples, and four dimensions are undefined. The metamodel must model them. |
| `ISSUE-0058` | **M2.** How an artifact declares its classification, now that paths no longer imply it. Every contract depends on it. |
| `ISSUE-0002` | M8 |
| `ISSUE-0006` | M10 |

## Must be resolved within M2

`ISSUE-0007`, `ISSUE-0011`, `ISSUE-0013`, `ISSUE-0014`, `ISSUE-0015`,
`ISSUE-0018`, `ISSUE-0019`, `ISSUE-0048`, `ISSUE-0049`.

## Known debt

- **`ISSUE-0037`** — five hand-maintained Registry Projections; no compiler until
  `ISSUE-0036` is un-deferred.
- **`ISSUE-0048`** — no machine-readable correction mechanism. **Four
  corrections** now exist, visible only in the ADR index.

## Next action

Accept or return this session's work.

Then `ISSUE-0057` and `ISSUE-0058` together — both are about how dimensions
work, and the second's answer depends on which dimensions exist.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Visibility: **public, with no licence file** — `ISSUE-0011`
