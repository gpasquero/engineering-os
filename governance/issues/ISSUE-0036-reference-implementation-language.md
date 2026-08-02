---
id: ISSUE-0036
title: The reference implementation language is deliberately deferred
type: question
status: deferred
severity: medium
created: 2026-08-02
updated: 2026-08-02
blocks: [M9]
defers-to: M9
evidence:
  - governance/adr/ADR-0017-reference-architecture-not-reference-implementation.md
resolved-by: null
---

# ISSUE-0036 — Reference implementation language

## Statement

`ADR-0017` establishes that the architecture must not depend on any specific
implementation language, and **defers the reference implementation language
until architectural stabilization**.

This issue exists so the deferral is visible rather than forgotten. It is
`deferred`, not `open` — nobody should be waiting on it, and nothing before M9
should be blocked by it.

## Why it is deferred rather than answered

Choosing now would couple the architecture to one ecosystem before the
architecture is stable. `ISSUE-0001` may pull adapters toward a different
ecosystem than the compiler would naturally use, and that tension is better
resolved once both are understood.

## What the deferral costs

M2 cannot ship executable tooling. Manifest validation and index generation
cannot be built, so generated projections remain hand-maintained — tracked as
`ISSUE-0037`. That debt grows for as long as this stays deferred, which is the
main argument for not deferring indefinitely.

## What must be true before deciding

- The compiler interface is specified (M2).
- `ISSUE-0001` is resolved, so the adapter ecosystem is known.
- The semantic-web tooling requirements are understood — the strongest options
  live in Java (Jena, OWLAPI, ROBOT) and Python (RDFLib, pySHACL), which may or
  may not match the adapter ecosystem.

## Constraints already fixed by ADR-0017

Whatever is chosen:

- It must implement the stable compiler interface, not define it.
- An adopting repository must not need it installed to read, author or follow
  the methodology.
- It is required only to generate or validate derived artifacts.

## Resolution criteria

An ADR naming the reference implementation language, runtime, dependency manager
and test framework — written when the compiler interface is stable, not before.
