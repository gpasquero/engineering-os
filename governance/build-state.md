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
| ADRs | 27 — 22 accepted, 5 superseded |
| Issues | 48 recorded — 23 open, 24 resolved, 1 deferred |
| Acceptance Records | 3 — `ACCEPT-0001` (trust root), `ACCEPT-0002`, `ACCEPT-0003` |
| Session journal | 8 entries |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff) |

## What does not exist

No executable code, and none is planned before M9 (`ADR-0017`, `ISSUE-0036`).

Nothing in `shared/`, `skills/`, `workflows/`, `model-spec/`, `model/`,
`templates/`, `schemas/`, `validation/`, `tests/`, `adapters/` or `docs/`. None
of the three manifests. No State Machine Registry. No governance policy — the
first arrives in M3.

## Acceptance status

| Record | Covers | Note |
|---|---|---|
| `ACCEPT-0001` | Bootstrap corpus at `2b6484f` | Trust root; the only retrospective acceptance |
| `ACCEPT-0002` | `SESSION-0006` at `aed6d89` | First acceptance under the normal workflow |
| `ACCEPT-0003` | `SESSION-0007` at `d439084` | — |

**`ADR-0026`, `ADR-0027`, `ISSUE-0046`–`ISSUE-0048` and this session's
propagation are `Under Review`**, not `Active`.

## Blocking

**Nothing blocks M2.** One issue gates two deliverables within it:

| Issue | Gates |
|---|---|
| `ISSUE-0047` | The State Machine Registry and `shared/vocabularies/` — the registry's location overlaps `KNOWLEDGE-MANIFEST.yaml` |

The compiler interface specification, `model-spec/`, the manifests and the
remaining contracts can proceed in parallel.

`ISSUE-0002` (M8) and `ISSUE-0006` (M10) block later milestones.

## Must be resolved within M2

`ISSUE-0007`, `ISSUE-0011`, `ISSUE-0013`, `ISSUE-0014`, `ISSUE-0015`,
`ISSUE-0018`, `ISSUE-0019`, `ISSUE-0031`, `ISSUE-0048`.

## Known debt

- **`ISSUE-0037`** — five hand-maintained projections; no generator can exist
  while `ISSUE-0036` is deferred. Counts are recomputed from the files before
  each index rewrite, after drifting once in `SESSION-0004`.
- **`ISSUE-0046`** — modeling guidelines are declared across scattered ADRs with
  no home document. Two so far, and the set will grow through M3.
- **`ADR-0027` extends the debt**: registration correctness is unenforced until
  validators exist, so a malformed registration is caught only by review.

## Next action

Accept or return this session's work.

Then M2. The compiler interface specification and `model-spec/` are the largest
unblocked deliverables. `ISSUE-0047` should be settled before either the
registry or `shared/vocabularies/` is written.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Visibility: **public, with no licence file** — `ISSUE-0011`
