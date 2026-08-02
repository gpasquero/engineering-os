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
started, and unblocked.**

M1 is complete.

## What exists

| Area | State |
|---|---|
| Repository architecture | Defined and accepted |
| Documentation system, session protocol | Defined and accepted |
| Vision, principles, glossary | Written |
| Roadmap | M1–M13 |
| ADRs | 29 — 24 accepted, 5 superseded |
| Issues | 50 recorded — 23 open, 26 resolved, 1 deferred |
| Acceptance Records | 4 — `ACCEPT-0001` (trust root) through `ACCEPT-0004` |
| Session journal | 9 entries |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff) |

## What does not exist

No executable code, and none is planned before M9 (`ADR-0017`, `ISSUE-0036`).

Nothing in `shared/`, `skills/`, `workflows/`, `model-spec/`, `model/`,
`templates/`, `schemas/`, `validation/`, `tests/`, `adapters/` or `docs/`. None
of the three manifests. No State Machine Registry. **No policies of any kind** —
the first Modeling Policies arrive in M3.

## Acceptance status

| Record | Covers | Note |
|---|---|---|
| `ACCEPT-0001` | Bootstrap corpus at `2b6484f` | Trust root; the only retrospective acceptance |
| `ACCEPT-0002` | `SESSION-0006` at `aed6d89` | First acceptance under the normal workflow |
| `ACCEPT-0003` | `SESSION-0007` at `d439084` | — |
| `ACCEPT-0004` | `SESSION-0008` at `51bed77` | — |

**`ADR-0028`, `ADR-0029`, `ISSUE-0049`, `ISSUE-0050` and this session's
propagation are `Under Review`**, not `Active`.

## A note for agents reading this repository

**The ADR corpus is history, not specification** (`ADR-0029`). Twenty-nine
decisions, five superseded, one partially corrected. Deriving the currently
applicable rules from it is archaeology.

The normative rules will live in Modeling Policies under `shared/policies/`.
**Until M3 writes them, no such policy exists**, and the ADRs are the only
statement of the rules — which is precisely the condition `ADR-0029` exists to
end.

## Blocking

**Nothing blocks M2.**

| Issue | Gates |
|---|---|
| `ISSUE-0049` | `shared/vocabularies/` and the state machine specifications |
| `ISSUE-0050` | `shared/policies/` — blocks M3, not M2 |

The compiler interface specification, `model-spec/`, the manifests and the
remaining contracts can proceed in parallel.

`ISSUE-0002` (M8) and `ISSUE-0006` (M10) block later milestones.

## Must be resolved within M2

`ISSUE-0007`, `ISSUE-0011`, `ISSUE-0013`, `ISSUE-0014`, `ISSUE-0015`,
`ISSUE-0018`, `ISSUE-0019`, `ISSUE-0031`, `ISSUE-0048`.

## Known debt

- **`ISSUE-0037`** — five hand-maintained projections; no generator until
  `ISSUE-0036` is un-deferred.
- **`ADR-0027`** — registration correctness is unenforced until validators exist.
- **`ADR-0029`** — rule text will exist in both ADRs and policies. The divergence
  is intended, but intended divergence and accidental drift look identical in a
  diff.

## Next action

Accept or return this session's work.

Then M2. The compiler interface specification and `model-spec/` are the largest
unblocked deliverables. `ISSUE-0049` should be settled before
`shared/vocabularies/`.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Visibility: **public, with no licence file** — `ISSUE-0011`
