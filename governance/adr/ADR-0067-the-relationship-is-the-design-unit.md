---
id: ADR-0067
title: The relationship is the design unit, not the entity
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0030, ADR-0035, ADR-0062, ADR-0066]
---

# ADR-0067 — The relationship is the design unit

## Context

Until now the metamodel has been developed as **a collection of entities**. The
OWL model shows that this is no longer where the design happens.

Entities are becoming increasingly lightweight. Most semantics are moving into
**relationships, constraints, cardinalities, inference and identity.**

This is the expected evolution of an ontology-driven architecture, and it was
visible in the skeleton before it was visible in the specifications: seventeen
classes carrying almost nothing, and twenty-nine properties carrying nearly all
the meaning.

## Decision

**Every new entity specification must answer one question before it is
accepted:**

> **What new semantic relationship does this entity introduce that cannot
> already be expressed?**

**If the answer is "none", the entity is probably redundant.**

The question is recorded in a required section of every entity specification,
named `What new semantics does this introduce?`.

**This question becomes part of the Modeling Policy once Policies are
implemented** (`ADR-0030`). Until then it is enforced by this decision.

## Alternatives considered

**Leave it as guidance in the metamodel README.** Rejected: the project already
has evidence that unenforced guidance drifts. `ISSUE-0037` records a hand-
maintained projection that diverged from its source inside a single session.

**Wait for the Modeling Policy.** Rejected under `ADR-0062`. `Policy` is
unspecified and the next batch of entities is being written now; a rule that
arrives after the entities it governs is worthless. The question is enforced
immediately and relocated later — the relocation is mechanical.

**Make it a hard rejection rule rather than a signal.** Rejected as stated:
"probably redundant" is deliberate. An entity may earn its place by carrying
identity or constraints rather than by introducing an edge, and a hard rule
would force those cases to be argued as exceptions.

## Consequences

### Positive

- **It is a cheap, mechanical check with a sharp failure mode.** An author who
  cannot fill the section has learned something before writing the rest.
- It gives the metamodel a defence against the accumulation this project is
  otherwise structurally prone to — twenty-three sessions have produced sixty-
  seven decisions, and nothing until now has made *removal* a normal outcome.
- It applies retroactively as a review instrument, which is what makes the
  scheduled simplification review (`ISSUE-0074`) tractable.

### Negative

- **Some already-specified entities will fail it.** `Dimension` is the known
  case; there may be others. They are not removed reactively — `ISSUE-0074`
  exists so that removal happens as one considered pass rather than as
  opportunistic deletions.
- The question is answerable dishonestly. A weak relationship can always be
  invented to justify an entity, and nothing detects that.

### Neutral

- The eight properties `ADR-0035` requires become nine.

## Compliance

Every entity specification written after this decision contains a
`What new semantics does this introduce?` section. Specifications written before
it are assessed during the simplification review, not retrofitted.
