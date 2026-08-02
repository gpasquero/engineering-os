---
id: ISSUE-0009
title: Human-in-the-loop authority and gate approval are undefined
type: question
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2, M3]
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

## Raised by ADR-0015

`ADR-0015` makes human acceptance a **hard architectural requirement**, not only
a methodological preference: *AI-generated content becomes authoritative only
after human acceptance and version control.*

The whole three-tier model of `ADR-0014` rests on the authoritative tier being
trustworthy, and acceptance is what makes it so. This issue is therefore now
load-bearing for the architecture, not just for the gate.

It sharpens what must be answered. Beyond "who lifts a `blocked` gate", the
project must define what **acceptance** means: who accepts, on what basis, and
what review consists of. A commit is the *record* of acceptance, not a
definition of it — and nothing currently stops an agent from committing its own
output and thereby self-certifying it as authoritative.

That gap is the practical risk, and it exists today.

## Resolution criteria

An ADR defining who holds authority for each gate outcome and each class of
model change, and what an agent does when authority is unavailable. Feeds the
autonomy and escalation policy in M3.
