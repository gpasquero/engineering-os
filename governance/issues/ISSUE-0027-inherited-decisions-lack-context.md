---
id: ISSUE-0027
title: Ten inherited decisions are accepted but have no recorded rationale
type: gap
status: deferred
severity: medium
created: 2026-08-02
updated: 2026-08-02
blocks: [M3]
evidence:
  - sources/handoff/DECISIONS.md
  - governance/inherited-decisions.md
resolved-by: null
defers-to: [M3]
debt: architectural
---

# ISSUE-0027 — Inherited decisions have no recorded rationale

> **Architectural debt** (`ADR-0062`). Deferred because it is not needed to
> build the next deliverable. Reopen when implementation requires it.

## Statement

The pre-M1 `sources/handoff/DECISIONS.md` recorded ten decisions as bare bullet points, with no
context, no alternatives considered, and no consequences.

Two of them commit the project to a specific semantic technology stack — "OWL
models semantics" and "SHACL validates graph instances" — without recording what
else was considered.

## Why it matters

An undocumented decision is re-litigated by every session that encounters a
reason to doubt it. It also cannot be evaluated: there is no way to tell whether
a decision still holds when its premises change, because the premises were never
written down.

## What we know

- The decisions are binding. They are answers whose reasoning was not preserved,
  not open questions.
- Two are already converted: `ADR-0001` (repository-first) and, in effect,
  `ADR-0008` (shared policies over duplicated text).
- The full status table is in `governance/inherited-decisions.md`.

## Resolution criteria

An ADR for each remaining inherited decision, written before the milestone that
depends on it, with real alternatives and consequences. Decision 10 additionally
depends on `ISSUE-0010`, since it references a Definition of Done that does not
exist.
