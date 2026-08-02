---
id: ISSUE-0012
title: The term "skill" is overloaded and self-contradictory
type: inconsistency
status: resolved
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - sources/handoff/BOOTSTRAP.md
  - governance/design/skill-catalog.md
  - governance/design/proposed-architecture.md
resolved-by: governance/glossary.md
---

# ISSUE-0012 — The term "skill" is overloaded

## Statement

`sources/handoff/BOOTSTRAP.md` states "This is NOT a collection of Claude skills", while
`governance/design/proposed-architecture.md` centres the architecture on a `skills/`
directory and `governance/design/skill-catalog.md` lists ten skills. One word carries two
meanings: a unit of methodology, and a vendor packaging format.

## Why it matters

This was the highest-priority inconsistency in the repository. Every document
about composition, contracts and adapters uses the word, and readers were
resolving it inconsistently.

## Resolution

`governance/glossary.md` defines both meanings and fixes the default:

- **Skill (methodology unit)** — the meaning used throughout this repository.
- **Agent-runtime skill** — a distribution artifact produced by `adapters/`.

Unqualified, "skill" means the methodology unit. `ADR-0007` reinforces this by
confining runtime packaging to `adapters/`.

The remaining question — which runtimes are packaged — is `ISSUE-0001`, and is
a separate matter from the terminology.
