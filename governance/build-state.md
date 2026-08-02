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

## Current milestone

**M2 — Foundational contracts and manifest. Not started, and unblocked.**

M1 is complete.

## What exists

| Area | State |
|---|---|
| Repository architecture | Defined and accepted (`repository-architecture.md`) |
| Documentation system | Defined and accepted (`documentation-system.md`) |
| Session protocol | Defined and accepted (`session-protocol.md`) |
| Vision, principles, glossary | Written |
| Roadmap | M1–M13 |
| ADRs | 10 — 9 accepted, 1 superseded (`ADR-0006` by `ADR-0010`) |
| Issues | 31 recorded — 24 open, 7 resolved |
| Session journal | 2 entries |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff documents) |

## What does not exist

Nothing has been built in `shared/`, `skills/`, `workflows/`, `model-spec/`,
`model/`, `templates/`, `schemas/`, `validation/`, `tests/`, `adapters/` or
`docs/`.

There is no `MANIFEST.yaml` — its purpose is now defined (`ADR-0009`) but the
file itself is an M2 deliverable.

There is no `model/`. This repository will have one, describing Engineering OS
itself, in M11 (`ADR-0010`, `ISSUE-0031`).

## Blocking

**Nothing blocks M2.** `ISSUE-0003` and `ISSUE-0004` were resolved by
`ADR-0009` and `ADR-0010`.

Two issues block later milestones: `ISSUE-0002` (M8) and `ISSUE-0006` (M10).

Eight issues must be resolved *within* M2: `ISSUE-0005`, `ISSUE-0007`,
`ISSUE-0013`, `ISSUE-0014`, `ISSUE-0015`, `ISSUE-0018`, `ISSUE-0019`,
`ISSUE-0030`.

`ISSUE-0005` (does the repository ship executable code?) is the most urgent of
these: `ADR-0009` requires build pipelines, documentation generators and
generated manifest sections, all of which imply executable tooling. It should be
decided before the manifest schema is written.

## Next action

Begin M2 with `shared/vocabularies/`. Extracting the twelve assertion statuses
to a single source closes `ISSUE-0018` and gives every later artifact a stable
vocabulary to reference.

Then resolve `ISSUE-0005` and `ISSUE-0030`, both of which constrain the manifest
schema.

## Repository state

- Branch: `feat/repository-bootstrap`
- Remote: `github.com/gpasquero/engineering-os`
