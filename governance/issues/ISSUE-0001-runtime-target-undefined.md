---
id: ISSUE-0001
title: The agent runtime target of the Engineering OS is undefined
type: question
status: deferred
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M12]
evidence:
  - sources/handoff/BOOTSTRAP.md
  - imports/reconstruct-system-knowledge/SKILL.md
  - imports/reconstruct-system-knowledge/README.md
  - imports/ontology-driven-development-v2/README.md
resolved-by: null
defers-to: [M12]
debt: architectural
---

# ISSUE-0001 — The agent runtime target is undefined

> **Architectural debt** (`ADR-0062`). Deferred because it is not needed to
> build the next deliverable. Reopen when implementation requires it.

## Statement

`sources/handoff/BOOTSTRAP.md` states "This is NOT a collection of Claude skills". All three
inherited prototypes are nonetheless Claude Code skills: `SKILL.md` files with
`name` / `description` / `argument-hint` frontmatter, whose READMEs instruct the
reader to copy them into `~/.claude/skills/`.

It is not established which runtimes the Engineering OS targets, or whether it
targets one at all.

## Why it matters

Determines whether `adapters/` holds one entry or several, what M11 must
produce, and how users actually invoke the methodology.

## What we know

- `ADR-0007` decided the *boundary*: the core is runtime-neutral and packaging
  is confined to `adapters/`. This removed the block on M2 and M3.
- The targets themselves remain undecided.

## Options

- **Claude Code only** — simplest, matches the prototypes, contradicts the
  letter of `sources/handoff/BOOTSTRAP.md`.
- **Multiple agent runtimes** (Claude Code, AGENTS.md, MCP) — matches the stated
  intent, multiplies M11 work.
- **Runtime-agnostic documentation only**, with no packaging — purest reading of
  "not a collection of skills", worst adoption ergonomics.

## Resolution criteria

An ADR naming the supported runtimes and the priority order among them.
