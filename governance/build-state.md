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
| ADRs | 36 — 31 accepted, 5 superseded |
| Issues | 55 recorded — 23 open, 31 resolved, 1 deferred |
| Acceptance Records | 7 — `ACCEPT-0001` (trust root) through `ACCEPT-0007` |
| Session journal | 12 entries |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff) |

## What does not exist

**The Metamodel does not exist.** It is now M2's first deliverable (`ADR-0036`).

No executable code, and none is planned before M9 (`ADR-0017`, `ISSUE-0036`).

Nothing in `shared/`, `skills/`, `workflows/`, `model-spec/`, `model/`,
`templates/`, `schemas/`, `validation/`, `tests/`, `adapters/` or `docs/`. None
of the three manifests. No Registry Specification of any kind. **No policies of
any kind.**

## Acceptance status

| Record | Covers |
|---|---|
| `ACCEPT-0001` | Bootstrap corpus at `2b6484f` — trust root, the only retrospective acceptance |
| `ACCEPT-0002` | `SESSION-0006` at `aed6d89` — first under the normal workflow |
| `ACCEPT-0003` | `SESSION-0007` at `d439084` |
| `ACCEPT-0004` | `SESSION-0008` at `51bed77` |
| `ACCEPT-0005` | `SESSION-0009` at `7af8f44` |
| `ACCEPT-0006` | `SESSION-0010` at `a87ce51` |
| `ACCEPT-0007` | `SESSION-0011` at `ef8e067` |

**`ADR-0035`, `ADR-0036`, `ISSUE-0055` and this session's propagation are `Under
Review`**, not `Active`.

## A note for agents reading this repository

**The ADR corpus is history, not specification** (`ADR-0029`). Thirty-six
decisions, five superseded, two partially corrected.

**A new process gate is in force** (`ADR-0035`): every new concept must be
positioned in the Metamodel before a new artifact type is introduced. The
Metamodel does not exist yet, so in practice no new artifact type should be
introduced until it does.

The normative rules will live in `ModelingPolicy`, `GovernancePolicy` and
`ProcessPolicy` artifacts under `shared/policies/`, written in M3. Until then the
ADRs are the only statement of the rules.

## Blocking

| Issue | Blocks |
|---|---|
| `ISSUE-0055` | **M2.** The Metamodel is its first deliverable and the metamodel's location — Layer A or Layer B — is undecided. |
| `ISSUE-0002` | M8 |
| `ISSUE-0006` | M10 |

`ISSUE-0049` gates the state machine specifications and `shared/vocabularies/`
within M2.

## Must be resolved within M2

`ISSUE-0007`, `ISSUE-0011`, `ISSUE-0013`, `ISSUE-0014`, `ISSUE-0015`,
`ISSUE-0018`, `ISSUE-0019`, `ISSUE-0031`, `ISSUE-0048`.

`ISSUE-0031` and `ISSUE-0055` should be resolved **together** — both ask what
Engineering OS's own knowledge contains, from opposite sides.

## Known debt

- **`ISSUE-0037`** — five hand-maintained Registry Projections; no compiler until
  `ISSUE-0036` is un-deferred.
- **`ISSUE-0048`** — no machine-readable correction mechanism. Two corrections
  exist, visible only in prose and the ADR index.
- **`ADR-0029`** — rule text will exist in both ADRs and policies. The divergence
  is intended; intended divergence and accidental drift look identical in a diff.

## Next action

Accept or return this session's work.

Then resolve `ISSUE-0055` with `ISSUE-0031`. Nothing else in M2 can start until
the Metamodel has a home, because `ADR-0036` puts it ahead of the compiler
interface.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Visibility: **public, with no licence file** — `ISSUE-0011`
