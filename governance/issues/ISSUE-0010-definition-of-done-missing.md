---
id: ISSUE-0010
title: Definition of Done is asserted but never stated
type: gap
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M3]
evidence:
  - sources/handoff/DECISIONS.md
  - imports/principal-engineering-skill/SKILL.md
resolved-by: null
---

# ISSUE-0010 — Definition of Done is asserted but never stated

## Statement

`sources/handoff/DECISIONS.md` records the decision "Knowledge update is part of Done". No
document defines Done.

## Why it matters

The knowledge-update policy in M3 exists to enforce a definition that does not
exist. Without it, "knowledge update is part of Done" is unenforceable and each
session will interpret it differently.

## What we know

Candidate criteria are scattered across the prototypes:

- `principal-engineering` lists six deliverables per change: impact analysis,
  implementation plan, acceptance criteria, traceability, validation report,
  knowledge update report.
- `ontology-driven-development` requires impact analysis to be re-run after
  implementation, and forbids claiming completion without it.
- `reconstruct-system-knowledge` defines ten completion criteria, but for a
  reconstruction *iteration* rather than a change.

These are two different notions of Done — one per change, one per iteration —
and both may be needed.

## Resolution criteria

A document defining Done for a change and Done for a knowledge iteration, as
observable, checkable conditions. Feeds the knowledge-update policy in M3 and
the inherited decision recorded in `governance/inherited-decisions.md`.
