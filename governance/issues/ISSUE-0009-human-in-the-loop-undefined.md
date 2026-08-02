---
id: ISSUE-0009
title: Human-in-the-loop authority and gate approval are undefined
type: question
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M3]
evidence:
  - imports/ontology-driven-development-v2/SKILL.md
  - imports/reconstruct-system-knowledge/SKILL.md
resolved-by: null
---

# ISSUE-0009 — Human-in-the-loop authority is undefined

## Statement

The methodology has an implementation gate that can read `blocked`. No document
states who is authorized to unblock it, who approves an ontology change, or what
an agent should do when it reaches a gate it cannot clear.

## Why it matters

A gate with no defined authority is either advisory — in which case an agent
will talk itself past it — or a deadlock. This is the mechanism the whole
methodology rests on, so an undefined escalation path undermines everything
built on top of it.

Closely related to `ISSUE-0020`, which records that the three prototypes already
disagree about autonomy.

## What we know

- `ontology-driven-development` defines the gate values `ready`,
  `ready-with-mitigations`, `blocked`, and lists seven conditions requiring
  `blocked`.
- It does not say who lifts a `blocked` state.
- `reconstruct-system-knowledge` names three narrow conditions for asking the
  user, and otherwise instructs the agent to continue.

## Options

- **Agent-autonomous with recorded justification** — fast, and the gate becomes
  self-certified.
- **Human approval required for `blocked` and for ontology changes** — slower,
  preserves the gate's meaning.
- **Tiered by risk** — approval required only above a severity threshold.

## Resolution criteria

An ADR defining who holds authority for each gate outcome and each class of
model change, and what an agent does when authority is unavailable. Feeds the
autonomy and escalation policy in M3.
