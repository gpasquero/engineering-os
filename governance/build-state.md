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
| ADRs | 23 — 18 accepted, 5 superseded |
| Issues | 43 recorded — 22 open, 20 resolved, 1 deferred |
| **Acceptance Records** | **1 — `ACCEPT-0001`, the trust root** |
| Session journal | 6 entries |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff) |

## What does not exist

No executable code, and none is planned before M9 (`ADR-0017`, `ISSUE-0036`).

Nothing has been built in `shared/`, `skills/`, `workflows/`, `model-spec/`,
`model/`, `templates/`, `schemas/`, `validation/`, `tests/`, `adapters/` or
`docs/`. None of the three manifests exist. No governance policy exists — the
first arrives in M3.

## Acceptance status

`ACCEPT-0001` covers the bootstrap corpus at revision `2b6484f` and **nothing
after it** (`ADR-0022`).

**Everything created since that revision is `Under Review`, not `Active`** —
`ADR-0020` through `ADR-0023`, `ACCEPT-0001` itself, `ISSUE-0042`, `ISSUE-0043`,
and this session's propagation edits. They await acceptance by a reviewer other
than their author (`ADR-0023`).

This is the normal workflow operating, not a defect. It is also the first time
the repository has held unaccepted work, which is what the lifecycle exists to
express.

## Blocking

**Nothing blocks M2.** Two issues gate specific deliverables within it:

| Issue | Gates |
|---|---|
| `ISSUE-0043` | `shared/vocabularies/` — four document status vocabularies overlap the revision lifecycle |
| `ISSUE-0042` | The Acceptance Record contract — whether a record requires its own acceptance |

`ISSUE-0002` (M8) and `ISSUE-0006` (M10) block later milestones.

## Must be resolved within M2

`ISSUE-0007`, `ISSUE-0011`, `ISSUE-0013`, `ISSUE-0014`, `ISSUE-0015`,
`ISSUE-0018`, `ISSUE-0019`, `ISSUE-0031`.

## Known debt

- **`ISSUE-0037`** — five hand-maintained projections, because no generator can
  exist until `ISSUE-0036` is un-deferred. Counts drifted once already, in
  `SESSION-0004`, and are now recomputed from the files before each rewrite.

## Next action

Accept this session's work, or return it for revision. Until then the corpus
above `2b6484f` is `Under Review`.

Then M2: the compiler interface specification and `model-spec/` can proceed
immediately; `shared/vocabularies/` waits on `ISSUE-0043`.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Visibility: **public, with no licence file** — `ISSUE-0011`
