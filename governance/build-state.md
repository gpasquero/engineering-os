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

> Under `ADR-0013` a `BUILD-STATE.yaml` manifest will hold this content in
> machine form. Which of the two is authoritative is unresolved — `ISSUE-0035`.
> Until then, this document is authoritative.

## Current milestone

**M2 — Foundational contracts and manifests. Not started, and blocked.**

M1 is complete.

## What exists

| Area | State |
|---|---|
| Repository architecture | Defined and accepted |
| Documentation system, session protocol | Defined and accepted |
| Vision, principles, glossary | Written |
| Roadmap | M1–M13 |
| ADRs | 13 — 11 accepted, 2 superseded (`ADR-0006`→`ADR-0010`, `ADR-0009`→`ADR-0013`) |
| Issues | 35 recorded — 26 open, 9 resolved |
| Session journal | 3 entries |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff) |

## What does not exist

No executable code of any kind. No language, runtime, dependency manager, test
framework or CI. `ADR-0012` commits the project to being an executable
framework, but nothing has been implemented and no toolchain is chosen
(`ISSUE-0032`).

Nothing has been built in `shared/`, `skills/`, `workflows/`, `model-spec/`,
`model/`, `templates/`, `schemas/`, `validation/`, `tests/`, `adapters/` or
`docs/`.

None of the three manifests exist. Their responsibilities are defined
(`ADR-0013`); the files are M2 deliverables.

## Blocking M2

| Issue | Question |
|---|---|
| `ISSUE-0032` | What language and toolchain? Nothing executable can be built without it, and M2 now contains generated and validated artifacts. |
| `ISSUE-0034` | Is `model/` authoritative input, or the compiled canonical model? `model-spec/` cannot be designed until this is settled. |

Both follow from `ADR-0011` and `ADR-0012` and are decisions for the project
owner.

## Must be resolved within M2

`ISSUE-0007`, `ISSUE-0011` (licence), `ISSUE-0013`, `ISSUE-0014`, `ISSUE-0015`,
`ISSUE-0018`, `ISSUE-0019`, `ISSUE-0031`, `ISSUE-0033`, `ISSUE-0035`.

The two most structurally significant are `ISSUE-0035` (does `BUILD-STATE.yaml`
or `governance/` own the project's status?) and `ISSUE-0033` (where determinism
stops and agent work begins).

## Next action

Resolve `ISSUE-0032` and `ISSUE-0034`, each as an ADR. Then begin M2 with
`shared/vocabularies/` — extracting the assertion statuses and the new artifact
kinds to single sources closes `ISSUE-0018` and gives everything later a stable
vocabulary.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Visibility: **public, with no licence file** — `ISSUE-0011`, raised to `high`
  because default copyright makes public code legally unreusable
