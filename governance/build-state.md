---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: M1
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

## Current milestone

**M1 — Repository architecture and documentation system. Complete.**

## What exists

| Area | State |
|---|---|
| Repository architecture | Defined and accepted (`repository-architecture.md`) |
| Documentation system | Defined and accepted (`documentation-system.md`) |
| Session protocol | Defined and accepted (`session-protocol.md`) |
| Vision, principles, glossary | Written |
| Roadmap | Restructured into M1–M11, mapped from the inherited ten deliveries |
| ADRs | 8 accepted (`ADR-0001` … `ADR-0008`) |
| Issues | 28 recorded — 23 open, 5 resolved |
| Session journal | 1 entry |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff documents) |

## What does not exist

Nothing has been built in `shared/`, `skills/`, `workflows/`, `model-spec/`,
`templates/`, `schemas/`, `validation/`, `tests/`, `adapters/` or `docs/`.
Those directories are specified in `governance/repository-architecture.md` but
are deliberately not created until they hold real content.

There is no `MANIFEST.yaml`. There are no skills, no policies, no contracts and
no vocabularies. This is intentional: M1 was scoped to the memory layer only.

## Blocking the next milestone

M2 **cannot start** until these two are resolved. Both are decisions for the
project owner; neither is inferable from the inherited documents, and assuming
an answer would propagate through every later milestone.

| Issue | Question |
|---|---|
| `ISSUE-0003` | What is `MANIFEST.yaml` — registry, version lock, capability index, or distribution manifest? |
| `ISSUE-0004` | Where does the Layer B `model/` tree live — in the target repository, a sibling, or a central store? |

Six further issues must be resolved *within* M2: `ISSUE-0007`, `ISSUE-0013`,
`ISSUE-0014`, `ISSUE-0015`, `ISSUE-0018`, `ISSUE-0019`.

`ISSUE-0001` (runtime target) is **no longer** an M2 blocker. `ADR-0007` fixed
the runtime-neutral boundary, which defers the question to M11.

## Next action

Resolve `ISSUE-0003` and `ISSUE-0004`, each as an ADR. Then begin M2.

## Repository state

- Branch: `feat/repository-bootstrap`
- Not yet committed; `main` has no commits
