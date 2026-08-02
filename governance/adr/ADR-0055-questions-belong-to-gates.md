---
id: ADR-0055
title: Evaluation questions belong to Gates, not to artifacts
status: accepted
date: 2026-08-02
supersedes: ADR-0038
superseded-by: null
resolves: [ISSUE-0068]
related: [ADR-0035, ADR-0051, ADR-0053, ADR-0054]
---

# ADR-0055 — Questions belong to Gates

## Context

`ADR-0038` required every new artifact type to answer four questions before
acceptance, and treated an unanswerable question as a rejection.

`ISSUE-0068` recorded that its fourth question — *which compiler phase consumes
or produces it* — conflicts with `ADR-0053`: a purely semantic concept may have
no compiler phase, and would be rejected for being exactly what the separation
says it is entitled to be. It also recorded that three gates now overlapped with
no composition rule.

`ADR-0054` then made Gate a first-class concept, which supplies the missing
owner for the questions.

## Decision

**The questions defined by `ADR-0038` are not mandatory for every artifact. They
are conditional.**

> **Every Gate declares which questions apply.**

| Gate | Questions |
|---|---|
| **Metamodel Position Gate** | Which metamodel entity does it instantiate? Which semantic layer owns it? |
| **Compiler Impact Review** | Which compiler phase consumes it? Which compiler phase produces it? |
| **Dimension Review** | Does it satisfy the Dimension criteria? Is another metamodel construct more appropriate? |
| **Acceptance Review** | Is it authoritative? Has it been reviewed? Does it satisfy applicable validation? |

**Questions belong to Gates rather than to artifacts.**

This removes the tension where purely semantic concepts were forced to answer
compiler questions.

## What survives from ADR-0038

The principle that a concept must be *sufficiently defined* before acceptance,
and that an unanswerable applicable question is a rejection rather than a gap to
fill later. The four questions themselves survive — redistributed across the
gates that own them.

**What changes** is universality. A question applies when its gate is triggered,
not to every artifact type unconditionally. `ADR-0038`'s framing predated
`ADR-0053` by four sessions and asked every concept to declare a position in
both architectures.

## Alternatives considered

**Allow `None (Not Applicable)` for question 4**, extending `ADR-0039`'s
precedent. Rejected as the smaller fix: it would let a semantic concept decline
one compiler question while still being asked it, and would leave the three
overlapping gates uncomposed.

**Drop the compiler questions entirely.** Rejected: they are correct questions
for artifacts the compiler genuinely consumes or produces. The defect was
asking them universally, not asking them.

**Compose the three gates into one procedure.** Rejected: `ADR-0054` establishes
that gates are distinct concepts with their own triggering conditions.
Collapsing them would recreate the universal questionnaire under another name.

## Consequences

### Positive

- **The conflict with `ADR-0053` disappears at the source.** A semantic concept
  never encounters a compiler question, because the Compiler Impact Review is not
  triggered for it.
- Gates become self-describing: a gate's questions are part of its own
  definition, under `ADR-0054`'s `evaluation criteria` field.
- The three-gate overlap resolves into a triggering question rather than a
  composition rule — which gates apply, not how they combine.
- **Acceptance Review is named for the first time.** The acceptance process from
  `ADR-0020` and `ADR-0021` was a gate all along; it now sits alongside the
  others.

### Negative

- **Triggering conditions become load-bearing and are undefined.** If a gate
  applies only when triggered, then what triggers it decides what is asked. That
  is now the whole enforcement surface, and `ADR-0054` lists it as a field
  without saying what may appear in one.
- A concept could pass every triggered gate while a gate that *should* have
  triggered did not. Universality was crude but hard to evade.
- Four gates each declaring questions means the full set of questions is no
  longer readable in one place.

### Neutral

- No existing artifact is re-evaluated. The redistribution applies from here.

## Compliance

No question is asked of an artifact except through a Gate that declares it. No
Gate asks questions belonging to an architecture the concept does not
participate in. Every Gate's questions are part of its definition.
