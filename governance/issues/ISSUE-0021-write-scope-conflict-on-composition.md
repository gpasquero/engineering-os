---
id: ISSUE-0021
title: Write scope conflicts when reconstruction composes with implementation
type: risk
status: deferred
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M3]
evidence:
  - imports/reconstruct-system-knowledge/SKILL.md
  - imports/ontology-driven-development-v2/SKILL.md
  - imports/principal-engineering-skill/SKILL.md
resolved-by: null
defers-to: [M3]
debt: architectural
---

# ISSUE-0021 — Write scope conflicts on composition

> **Architectural debt** (`ADR-0062`). Deferred because it is not needed to
> build the next deliverable. Reopen when implementation requires it.

## Statement

`reconstruct-system-knowledge` forbids modifying production source code and
restricts all writes to `model/` and `model/tooling/`. It further forbids
refactoring modules, altering migrations, changing public contracts and fixing
discovered bugs.

`ontology-driven-development` Phase 8 and `principal-engineering` Phase 10 write
production code.

When a workflow chains reconstruction into implementation, write scope must
change mid-run. No document defines when, or by what authority.

## Why it matters

This is a safety issue, not merely a design gap. The reconstruction constraints
exist to guarantee that understanding a system cannot damage it. An agent
running a composed workflow that carries implementation permissions into a
reconstruction phase can silently violate them — for example by "fixing" a bug
it discovered while reading, which the reconstruction rules explicitly forbid.

## What we know

- The constraints are stated per-skill, as prose, with no machine-readable
  declaration.
- The skill contract planned for M2 is the natural place to declare write scope
  as a property that a workflow can enforce at each step.

## Resolution criteria

A write-scope policy in `shared/policies/`, plus a write-scope declaration in
the skill contract, so that scope is a property of the executing step rather
than of the session. Interacts with `ISSUE-0002`, since enforcement depends on
the composition primitive.
