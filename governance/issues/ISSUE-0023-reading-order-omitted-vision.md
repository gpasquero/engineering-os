---
id: ISSUE-0023
title: The mandated reading order omitted the vision and design documents
type: gap
status: resolved
severity: medium
created: 2026-08-02
updated: 2026-08-02
blocks: [M1]
evidence:
  - sources/handoff/AGENTS.md
  - sources/handoff/BOOTSTRAP.md
resolved-by: ADR-0002
---

# ISSUE-0023 — The mandated reading order omitted the vision

## Statement

The pre-M1 `sources/handoff/AGENTS.md` mandated reading four files in order: `sources/handoff/HANDOFF.md`,
`sources/handoff/DECISIONS.md`, `sources/handoff/ROADMAP.md`, `sources/handoff/BUILD-STATE.md`.

It omitted `sources/handoff/BOOTSTRAP.md`, which carried the strongest normative statements in
the repository — "this is NOT a prompt library", "knowledge is the primary
artifact" — and omitted `governance/design/` entirely.

## Why it matters

An agent following the mandated order would begin work without the project's
core constraints, and would be most likely to violate exactly the rules stated
in the omitted file.

## Resolution

`ADR-0002` establishes typed documents with an explicit reading order, and
`governance/session-protocol.md` defines an eleven-step start sequence in which
`vision.md` is second and `glossary.md` is fourth — before any document that
uses the vocabulary it defines.

`AGENTS.md` is rewritten to point at the session protocol rather than restating
a list that can drift from it.
