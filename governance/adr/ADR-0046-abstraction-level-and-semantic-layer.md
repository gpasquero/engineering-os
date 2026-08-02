---
id: ADR-0046
title: Abstraction Level and Semantic Layer are qualified names for two distinct dimensions
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0061]
related: [ADR-0025, ADR-0030, ADR-0037, ADR-0043]
---

# ADR-0046 — Abstraction Level and Semantic Layer

## Context

`ADR-0043` introduced three semantic levels — Metamodel, Model, Classification —
alongside `ADR-0037`'s four semantic layers. `ISSUE-0061` recorded that both are
ordinal schemes whose first element is the metamodel, and that the coincidence
invites reading them as one scheme counted differently.

It was raised **before** propagating, which is the discipline `ADR-0035`
established after five collisions were each caught late.

## Decision

**Level and Layer are both valid concepts. They describe different dimensions.**

- **Level classifies abstraction.**
- **Layer classifies semantic position in the Engineering OS knowledge
  architecture.**

They remain separate. Explicit names are introduced:

> **Abstraction Level**
>
> **Semantic Layer**

Future diagrams, specifications and ontology definitions **always use the
qualified names**.

**No renaming is required. Only qualification.**

This follows the same design discipline previously applied to State Machines
(`ADR-0025`) and Policies (`ADR-0030`).

## Alternatives considered

**Rename one scheme** — *semantic tiers*, *statement kinds*, *pipeline stages*.
Rejected: both words are correct for what they describe, and renaming would
discard accurate terminology to solve a problem that qualification solves.

**Model both as registered dimensions with formal independence** — the option
`ISSUE-0061` judged most consistent. Not rejected so much as subsumed: they *are*
two dimensions under `ADR-0040`, and `ADR-0044` already establishes that
independent dimensions may relate descriptively. Qualification is what the naming
question needed; registration follows from `ADR-0041` regardless.

**Accept the risk**, relying on `ADR-0043`'s prose. Rejected: it depends on every
future reader encountering one paragraph, and the project's record makes that a
poor bet.

## Consequences

### Positive

- **Third application of the same discipline**, after state names (`ADR-0025`)
  and normative artifact types (`ADR-0030`). Qualification has now resolved
  three classification-naming problems without discarding a single accurate
  term.
- Cheap. Nothing is renamed, no document is invalidated, and the fix is
  available immediately.
- Both terms keep meaning what they mean, so neither scheme has to be explained
  as a historical accident.

### Negative

- **Qualification is a discipline, not a mechanism.** Nothing prevents an
  unqualified "layer" or "level" appearing in prose, and no validator will catch
  it until M9.
- The corpus already contains unqualified uses. They are not wrong, but they are
  now less precise than the rule requires.

### Neutral

- **Three ADRs now apply the same naming discipline.** That is a rule, not three
  decisions, and it belongs in a `ModelingPolicy` (`ADR-0029`) in M3 rather than
  being rediscovered a fourth time.

## Compliance

Diagrams, specifications and ontology definitions use **Abstraction Level** and
**Semantic Layer** in full. No document uses "level" or "layer" unqualified
where either could be meant.
