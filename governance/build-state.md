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
started, and unblocked.**

M1 is complete.

## What exists

| Area | State |
|---|---|
| Repository architecture | Defined and accepted |
| Documentation system, session protocol | Defined and accepted |
| Vision, principles, glossary | Written |
| Roadmap | M1–M13 |
| ADRs | 17 — 14 accepted, 3 superseded |
| Issues | 37 recorded — 22 open, 14 resolved, 1 deferred |
| Session journal | 4 entries |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff) |

## What does not exist

No executable code of any kind, and none is planned before M9. `ADR-0017`
defers the implementation language until architectural stabilization
(`ISSUE-0036`), so M2 produces a **compiler interface specification** instead of
tooling.

Nothing has been built in `shared/`, `skills/`, `workflows/`, `model-spec/`,
`model/`, `templates/`, `schemas/`, `validation/`, `tests/`, `adapters/` or
`docs/`.

None of the three manifests exist.

## Blocking

**Nothing blocks M2.** Two issues block later milestones: `ISSUE-0002` (M8) and
`ISSUE-0006` (M10).

## Must be resolved within M2

`ISSUE-0007`, `ISSUE-0009`, `ISSUE-0011`, `ISSUE-0013`, `ISSUE-0014`,
`ISSUE-0015`, `ISSUE-0018`, `ISSUE-0019`, `ISSUE-0031`.

`ISSUE-0009` is the most consequential. Since `ADR-0015`, human acceptance is a
hard architectural requirement — an artifact becomes authoritative only when
accepted and committed — yet nothing defines who accepts, on what basis, or what
review consists of. **Nothing currently prevents an agent from committing its
own output and self-certifying it as authoritative.**

## Known debt

`ISSUE-0037` — every governance projection is hand-maintained, because no
generator can exist until `ISSUE-0036` is un-deferred. The register lists five
projections. This is sanctioned by `ADR-0016` as transitional, and grows with
every record added.

## Next action

Begin M2 with `shared/vocabularies/`. Extracting the assertion statuses and the
artifact kinds to single sources closes `ISSUE-0018` and gives everything later
a stable vocabulary to reference.

Then the compiler interface specification, which is the M2 deliverable that
unblocks M9 and is the hardest thing in the milestone — `ADR-0017` records the
risk of specifying seams before an implementation exists to learn from.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Visibility: **public, with no licence file** — `ISSUE-0011`
