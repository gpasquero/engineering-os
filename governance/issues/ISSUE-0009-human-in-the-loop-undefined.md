---
id: ISSUE-0009
title: Human-in-the-loop authority and gate approval are undefined
type: question
status: resolved
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2, M3]
evidence:
  - imports/ontology-driven-development-v2/SKILL.md
  - imports/reconstruct-system-knowledge/SKILL.md
resolved-by: ADR-0018
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

## Resolution

`ADR-0018`. **Acceptance is a first-class engineering concept, modeled
explicitly.** The question was reframed: it is not about gate authority, it is
about what acceptance *is*.

Authoritative status is determined by an explicit acceptance process, **not by
who created the artifact**. Lifecycle:

```text
Draft → Under Review → Accepted → Active → Superseded → Archived
```

> The state shown here as `Active` was originally named `Authoritative` in
> `ADR-0018`. It was renamed by `ADR-0020`, which supersedes it, to end the
> collision with the artifact kind of the same name (`ISSUE-0038`).

**Acceptance is an engineering decision, not a Git operation. A commit alone
does not make an artifact authoritative** — which corrects the boundary marker
that `ADR-0015` had claimed, and is why `ADR-0018` supersedes it.

Three conditions: explicit reviewer approval; traceability to the motivating
issue, ADR or requirement; successful validation of applicable deterministic
checks.

**Self-certification is prohibited** unless an explicit governance policy
enables it. Engineering OS never assumes an AI agent can accept its own work by
default.

Opened by this answer: `ISSUE-0038` (`authoritative` names two things),
`ISSUE-0039` (the governance policy mechanism does not exist), `ISSUE-0040` (the
existing corpus was self-certified), `ISSUE-0041` (acceptance record undefined).

## Original resolution criteria

An ADR defining who holds authority for each gate outcome and each class of
model change, and what an agent does when authority is unavailable. Feeds the
autonomy and escalation policy in M3.
