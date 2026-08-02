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

**M2 — Foundational contracts, manifests and the compiler interface. Not
started.** The three manifests are blocked; the rest is not.

M1 is complete.

## What exists

| Area | State |
|---|---|
| Repository architecture | Defined and accepted |
| Documentation system, session protocol | Defined and accepted |
| Vision, principles, glossary | Written |
| Roadmap | M1–M13 |
| ADRs | 31 — 26 accepted, 5 superseded |
| Issues | 53 recorded — 25 open, 27 resolved, 1 deferred |
| Acceptance Records | 5 — `ACCEPT-0001` (trust root) through `ACCEPT-0005` |
| Session journal | 10 entries |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff) |

## What does not exist

No executable code, and none is planned before M9 (`ADR-0017`, `ISSUE-0036`).

Nothing in `shared/`, `skills/`, `workflows/`, `model-spec/`, `model/`,
`templates/`, `schemas/`, `validation/`, `tests/`, `adapters/` or `docs/`. None
of the three manifests. No State Machine Registry. **No policies of any kind.**

## Acceptance status

| Record | Covers |
|---|---|
| `ACCEPT-0001` | Bootstrap corpus at `2b6484f` — trust root, the only retrospective acceptance |
| `ACCEPT-0002` | `SESSION-0006` at `aed6d89` — first under the normal workflow |
| `ACCEPT-0003` | `SESSION-0007` at `d439084` |
| `ACCEPT-0004` | `SESSION-0008` at `51bed77` |
| `ACCEPT-0005` | `SESSION-0009` at `7af8f44` |

**`ADR-0030`, `ADR-0031`, `ISSUE-0051`–`ISSUE-0053` and this session's
propagation are `Under Review`**, not `Active`.

## A note for agents reading this repository

**The ADR corpus is history, not specification** (`ADR-0029`). Thirty-one
decisions, five superseded, one partially corrected.

The normative rules will live in `ModelingPolicy`, `GovernancePolicy` and
`ProcessPolicy` artifacts under `shared/policies/`. **Until M3 writes them, no
policy exists**, and the ADRs are the only statement of the rules — the
condition `ADR-0029` exists to end.

## Blocking

| Issue | Blocks |
|---|---|
| `ISSUE-0053` | **The three manifests.** Whether a Registry is `authoritative` or `derived` is contested across `ADR-0031`, `ADR-0016` and `ADR-0012`, and the artifact kind determines how each manifest is built. |
| `ISSUE-0049` | `shared/vocabularies/` and the state machine specifications |
| `ISSUE-0051` | Process policies in M3, and the workflow catalogue in M8 |
| `ISSUE-0002` | M8 |
| `ISSUE-0006` | M10 |

The compiler interface specification, `model-spec/` and the remaining contracts
are unblocked and can start now.

## Must be resolved within M2

`ISSUE-0007`, `ISSUE-0011`, `ISSUE-0013`, `ISSUE-0014`, `ISSUE-0015`,
`ISSUE-0018`, `ISSUE-0019`, `ISSUE-0031`, `ISSUE-0048`.

## Known debt

- **`ISSUE-0037`** — five hand-maintained projections; no generator until
  `ISSUE-0036` is un-deferred.
- **`ADR-0027`** — registration correctness unenforced until validators exist.
- **`ADR-0029`** — rule text will exist in both ADRs and policies. The divergence
  is intended, but intended divergence and accidental drift look identical in a
  diff.

## Next action

Accept or return this session's work.

Then `ISSUE-0053`, which is the only issue blocking a named M2 deliverable.
Meanwhile the compiler interface specification and `model-spec/` need no further
decisions.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Visibility: **public, with no licence file** — `ISSUE-0011`
