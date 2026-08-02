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

> This is an **authoritative** governance document, not a projection
> (`ADR-0016`). The machine-readable `BUILD-STATE.yaml` will be generated from
> it and from issue front matter.

## Current milestone

**M2 — Foundational contracts, manifests and the compiler interface. Not
started, and blocked.**

M1 is complete.

## What exists

| Area | State |
|---|---|
| Repository architecture | Defined and accepted |
| Documentation system, session protocol | Defined and accepted |
| Vision, principles, glossary | Written |
| Roadmap | M1–M13 |
| ADRs | 19 — 15 accepted, 4 superseded |
| Issues | 41 recorded — 24 open, 16 resolved, 1 deferred |
| Session journal | 5 entries |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff) |

## What does not exist

No executable code, and none is planned before M9 (`ADR-0017`, `ISSUE-0036`).

Nothing has been built in `shared/`, `skills/`, `workflows/`, `model-spec/`,
`model/`, `templates/`, `schemas/`, `validation/`, `tests/`, `adapters/` or
`docs/`. None of the three manifests exist.

**No acceptance records exist**, and no mechanism defines them.

## Blocking M2

All three follow from `ADR-0018`, which made acceptance architectural.

| Issue | Question |
|---|---|
| `ISSUE-0038` | `authoritative` names both a lifecycle state and an artifact kind. Both vocabularies are early M2 deliverables; renaming afterwards is expensive. |
| `ISSUE-0041` | What an acceptance record is — fields, location, artifact kind, and whether condition 3 can be satisfied before validation tooling exists. |
| `ISSUE-0040` | Every artifact here was self-certified and has no acceptance record, including `ADR-0018` itself. Depends on `ISSUE-0041`. |

`ISSUE-0002` (M8) and `ISSUE-0006` (M10) block later milestones.

## Must be resolved within M2

`ISSUE-0007`, `ISSUE-0011`, `ISSUE-0013`, `ISSUE-0014`, `ISSUE-0015`,
`ISSUE-0018`, `ISSUE-0019`, `ISSUE-0031`.

## Known debt and compliance gaps

- **`ISSUE-0040`** — the repository does not satisfy `ADR-0018`. The
  authoritative tier currently rests on nothing, because nothing in it was
  accepted by anyone other than its author.
- **`ISSUE-0037`** — five hand-maintained projections, because no generator can
  exist until `ISSUE-0036` is un-deferred. The counts in
  `governance/issues/index.md` already drifted once, in `SESSION-0004`.
- **`ISSUE-0039`** — the governance policy mechanism that `ADR-0018` names as
  the only route to automated acceptance does not exist.

## Next action

Resolve `ISSUE-0041` first — it is the dependency for `ISSUE-0040`, and until an
acceptance record exists there is nowhere to record that anything was accepted.

Then `ISSUE-0038`, before `shared/vocabularies/` is written.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Visibility: **public, with no licence file** — `ISSUE-0011`
