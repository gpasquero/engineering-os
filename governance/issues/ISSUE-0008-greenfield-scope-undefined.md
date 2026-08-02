---
id: ISSUE-0008
title: Whether greenfield development is in scope is undefined
type: question
status: deferred
severity: medium
created: 2026-08-02
updated: 2026-08-02
blocks: [M4]
evidence:
  - imports/reconstruct-system-knowledge/SKILL.md
  - imports/ontology-driven-development-v2/SKILL.md
  - imports/principal-engineering-skill/SKILL.md
resolved-by: null
defers-to: [M4]
debt: architectural
---

# ISSUE-0008 — Whether greenfield development is in scope is undefined

> **Architectural debt** (`ADR-0062`). Deferred because it is not needed to
> build the next deliverable. Reopen when implementation requires it.

## Statement

All three prototypes assume an existing system. `reconstruct-system-knowledge`
reverse-engineers a repository; `ontology-driven-development` changes one;
`principal-engineering` describes "evolving existing software". Nothing states
whether the Engineering OS applies to a system being built from nothing.

## Why it matters

The discovery skills in M4 are built around evidence extraction from an existing
codebase. On a greenfield project there is no evidence to extract, and
`research-domain` and `reconstruct-domain` would need fundamentally different
behavior — or a different skill entirely.

## What we know

- The evidence hierarchy, assertion statuses and drift analysis are all
  meaningless without an implementation to compare against.
- Conversely the ontology, specification and impact-analysis machinery applies
  perfectly well to new work.

## Options

- **Brownfield only** — matches the prototypes; simplest; narrows the audience.
- **Brownfield first, greenfield later** — a named future milestone.
- **Both from the start** — discovery skills gain a mode switch; more design
  work in M4.

## Resolution criteria

An ADR stating the scope, and if greenfield is included, how discovery skills
behave when there is no implementation evidence.
