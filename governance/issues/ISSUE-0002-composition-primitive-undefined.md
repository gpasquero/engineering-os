---
id: ISSUE-0002
title: The mechanism by which a workflow invokes a skill is undefined
type: question
status: deferred
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M8]
evidence:
  - sources/handoff/DECISIONS.md
  - governance/design/workflow-catalog.md
  - imports/principal-engineering-skill/SKILL.md
resolved-by: null
defers-to: [M8]
debt: architectural
---

# ISSUE-0002 — The composition primitive is undefined

> **Architectural debt** (`ADR-0062`). Deferred because it is not needed to
> build the next deliverable. Reopen when implementation requires it.

## Statement

`sources/handoff/DECISIONS.md` asserts "Workflows orchestrate skills" and "Skills are
composable". No document states *how*. There is no described mechanism by which
one unit invokes another, passes inputs, or receives outputs.

## Why it matters

Determines whether `workflows/` contains prose that a human or agent follows by
reading, or executable definitions that a runner interprets. These produce
completely different artifacts. M8 cannot start without an answer.

It also shapes the skill contract in M2, because a contract's I/O signature is
only meaningful if something can act on it.

## What we know

- `principal-engineering` is effectively an early workflow: it names twelve
  phases in prose and expects the reading agent to follow them in order.
- No inherited prototype invokes another prototype.
- The answer may be runtime-dependent, which couples this to `ISSUE-0001`.

## Options

- **Prose sequencing** — a workflow document instructs the agent to apply skills
  in order. Zero machinery, no enforcement, no validation.
- **Sub-agent delegation** — each skill runs as a separate agent invocation with
  a defined I/O contract. Enforceable, runtime-dependent.
- **Executable runner** — a script interprets workflow definitions. Strongest
  guarantees, requires this repository to ship code (`ISSUE-0005`).
- **Progressive disclosure** — the workflow inlines skill content by reference at
  read time.

## Resolution criteria

An ADR naming the primitive, its I/O convention, and how a workflow step failure
is handled.
