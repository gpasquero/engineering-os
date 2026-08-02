---
id: ISSUE-0026
title: A prototype skill claims to be the entire operating system
type: inconsistency
status: resolved
severity: medium
created: 2026-08-02
updated: 2026-08-02
blocks: [M1]
evidence:
  - imports/principal-engineering-skill/SKILL.md
  - sources/handoff/HANDOFF.md
resolved-by: governance/glossary.md
---

# ISSUE-0026 — A prototype claims to be the entire operating system

## Statement

The `principal-engineering` prototype describes itself in its own frontmatter as
an "End-to-end engineering operating system for evolving existing software".

This repository is also called the Engineering Operating System. The
relationship between the two was never stated: is the prototype the system, a
component of it, or a superseded draft of it?

## Why it matters

A future session reading the prototype could reasonably conclude that the work
is already done, or that the prototype is the authoritative specification rather
than an input.

## Resolution

`governance/glossary.md` fixes the term: **Engineering OS** means this
repository and its full contents, never any single skill within it.

`sources/handoff/HANDOFF.md` already framed all three prototypes as "inputs, not final designs",
and `ADR-0005` freezes them as provenance.

The architectural reading is recorded in `governance/repository-architecture.md`
and in the M1 session log: `principal-engineering` is best understood as an
early draft of the **workflow layer**, not as a peer skill. Confirming that
reading is part of `ISSUE-0017`.
