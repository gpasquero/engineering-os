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
started, and fully unblocked.**

M1 is complete. **M3 is also unblocked.**

## What exists

| Area | State |
|---|---|
| Repository architecture | Defined and accepted |
| Documentation system, session protocol | Defined and accepted |
| Vision, principles, glossary | Written |
| Roadmap | M1–M13 |
| ADRs | 34 — 29 accepted, 5 superseded |
| Issues | 54 recorded — 23 open, 30 resolved, 1 deferred |
| Acceptance Records | 6 — `ACCEPT-0001` (trust root) through `ACCEPT-0006` |
| Session journal | 11 entries |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff) |

## What does not exist

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

**`ADR-0032`–`ADR-0034`, `ISSUE-0054` and this session's propagation are `Under
Review`**, not `Active`.

## A note for agents reading this repository

**The ADR corpus is history, not specification** (`ADR-0029`). Thirty-four
decisions, five superseded, two partially corrected.

The normative rules will live in `ModelingPolicy`, `GovernancePolicy` and
`ProcessPolicy` artifacts under `shared/policies/`. **Until M3 writes them, no
policy exists**, and the ADRs are the only statement of the rules — the
condition `ADR-0029` exists to end.

## Blocking

**Nothing blocks M2 or M3.** For the first time since M1, no issue blocks a
named deliverable.

Two issues gate specific work within M2:

| Issue | Gates |
|---|---|
| `ISSUE-0049` | State machine specifications and `shared/vocabularies/` |
| `ISSUE-0054` | Anything depending on the metamodel |

`ISSUE-0002` blocks M8; `ISSUE-0006` blocks M10.

## Must be resolved within M2

`ISSUE-0007`, `ISSUE-0011`, `ISSUE-0013`, `ISSUE-0014`, `ISSUE-0015`,
`ISSUE-0018`, `ISSUE-0019`, `ISSUE-0031`, `ISSUE-0048`.

## Known debt

- **`ISSUE-0037`** — five hand-maintained Registry Projections; no compiler until
  `ISSUE-0036` is un-deferred. `ADR-0032` now names what they are, and notes
  their Registry Specifications do not exist either.
- **`ISSUE-0048`** — no machine-readable correction mechanism. Two corrections
  now exist (`ADR-0025`←`ADR-0026`, `ADR-0031`←`ADR-0032`), both visible only in
  prose and the ADR index.
- **`ADR-0029`** — rule text will exist in both ADRs and policies. The divergence
  is intended, but intended divergence and accidental drift look identical in a
  diff.

## Next action

Accept or return this session's work.

Then begin M2. The compiler interface specification and `model-spec/` are the
largest deliverables and have no remaining decision dependencies.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Visibility: **public, with no licence file** — `ISSUE-0011`
