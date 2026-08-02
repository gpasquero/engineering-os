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

> An **Authoritative Artifact**, not a projection (`ADR-0016`). The
> machine-readable `BUILD-STATE.yaml` will be generated from it and from issue
> front matter.

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
| ADRs | 25 — 20 accepted, 5 superseded |
| Issues | 45 recorded — 22 open, 22 resolved, 1 deferred |
| Acceptance Records | 2 — `ACCEPT-0001` (trust root), `ACCEPT-0002` |
| Session journal | 7 entries |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff) |

## What does not exist

No executable code, and none is planned before M9 (`ADR-0017`, `ISSUE-0036`).

Nothing has been built in `shared/`, `skills/`, `workflows/`, `model-spec/`,
`model/`, `templates/`, `schemas/`, `validation/`, `tests/`, `adapters/` or
`docs/`. None of the three manifests exist. No governance policy exists — the
first arrives in M3.

## Acceptance status

| Record | Covers | Status |
|---|---|---|
| `ACCEPT-0001` | Bootstrap corpus at `2b6484f` | Trust root; the only retrospective acceptance |
| `ACCEPT-0002` | `SESSION-0006` decisions at `aed6d89` | First acceptance under the normal workflow |

**`ADR-0024`, `ADR-0025`, `ISSUE-0044`, `ISSUE-0045` and this session's
propagation are `Under Review`**, not `Active`. They await acceptance by a
reviewer other than their author.

## Blocking

**Nothing blocks M2.** Two issues gate `shared/vocabularies/`:

| Issue | Gates |
|---|---|
| `ISSUE-0044` | Whether the state machine is `ArtifactLifecycle` or `RevisionLifecycle` |
| `ISSUE-0045` | Which state machines this repository owns, and how a new one is introduced |

Other M2 work — the compiler interface specification, `model-spec/`, the
manifests, the remaining contracts — can proceed in parallel.

`ISSUE-0002` (M8) and `ISSUE-0006` (M10) block later milestones.

## Must be resolved within M2

`ISSUE-0007`, `ISSUE-0011`, `ISSUE-0013`, `ISSUE-0014`, `ISSUE-0015`,
`ISSUE-0018`, `ISSUE-0019`, `ISSUE-0031`.

## Known debt

- **`ISSUE-0037`** — five hand-maintained projections, because no generator can
  exist until `ISSUE-0036` is un-deferred. Counts drifted once, in
  `SESSION-0004`, and are now recomputed from the files before each rewrite.

## Next action

Accept or return this session's work.

Then M2: the compiler interface specification and `model-spec/` can start
immediately. `shared/vocabularies/` waits on `ISSUE-0044` and `ISSUE-0045`.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Visibility: **public, with no licence file** — `ISSUE-0011`
