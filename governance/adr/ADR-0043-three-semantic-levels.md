---
id: ADR-0043
title: Three semantic levels — Metamodel, Model, Classification
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0035, ADR-0037, ADR-0040, ADR-0041, ADR-0042, ISSUE-0061]
---

# ADR-0043 — Three semantic levels

**This is one of the foundations of the Engineering OS Metamodel.**

## Context

`ADR-0040` introduced dimensions, `ADR-0041` made them registered entities, and
`ADR-0042` made classification a relationship rather than a property. Each
decision moved classification further away from the objects being classified,
without naming why that direction is right.

## Decision

Engineering OS explicitly distinguishes **three semantic levels**.

### 1. Metamodel — defines entity *types*

`Artifact` · `Dimension` · `Registry` · `Policy` · `Workflow` · `Skill`

### 2. Model — defines *instances*

`ADR-0040` · `GovernancePolicy` · Compiler Interface Workflow

### 3. Classification — defines *semantic assertions about instances*

*belongs to Layer A* · *is Authoritative* · *is Active* · *owned by
Architecture* · *consumed during Compiler Phase "Parsing"*

### Why

> **This separation prevents classification systems from becoming part of the
> object model itself.**

It also allows dimensions, classifications and semantic assertions to evolve
independently.

**The future Knowledge Graph represents these as distinct node types rather than
flattening them into object properties.**

### How the recent decisions fit

The three levels explain them as one design:

| Decision | Level |
|---|---|
| `Dimension` is an entity type (`ADR-0040`) | 1 — Metamodel |
| A specific dimension is registered (`ADR-0041`) | 2 — Model |
| A Dimension Assignment (`ADR-0042`) | 3 — Classification |

## Relationship to the four semantic layers

**Different axes.** Levels classify *what kind of statement* something is;
layers classify *where in the compilation pipeline* it sits (`ADR-0037`).

Level 1 and Layer A both concern the metamodel, which invites conflation. They
are not the same claim: Layer A says the metamodel is authored in this
repository and defines the language; Level 1 says a statement is about entity
*types* rather than instances or assertions.

The naming risk is recorded as `ISSUE-0061`.

## Alternatives considered

**Two levels — types and instances — with classification as instance
properties.** Rejected: it is exactly the flattening this decision prevents.
Classification would become part of the object model, so changing how something
is classified would mean changing the object.

**Flatten everything into object properties**, as most document systems do.
Rejected: it makes dimensions inseparable from artifacts, contradicting
`ADR-0042`, and produces a graph where an assertion cannot be versioned,
attributed or invalidated on its own.

**More levels** — separating assertions from their provenance, for instance.
Rejected as premature: three levels are what the current decisions require, and
`ADR-0041`'s registration model can carry additional structure without a fourth
level.

## Consequences

### Positive

- **Classification can evolve without touching the object model**, which is what
  `ADR-0041` and `ADR-0042` each assumed separately and neither stated.
- The Knowledge Graph gets distinct node types, so an assertion is a node with
  its own identity — versionable, attributable and refutable, which matches the
  evidence discipline inherited from the prototypes.
- It gives the metamodel its organising principle: entity types at Level 1,
  everything the framework registers at Level 2, everything asserted about them
  at Level 3.

### Negative

- **"Level" and "Layer" are now two ordinal schemes whose first element is the
  metamodel in both.** Given this project's record — six terminology problems in
  fourteen sessions — the risk is not theoretical. `ISSUE-0061`.
- Three node types where a simpler graph would have one, and every traversal now
  crosses levels.
- Level 3 assertions are numerous: one per artifact per dimension. The graph
  grows faster than the corpus does.

### Neutral

- No existing artifact changes. The levels describe what the recent decisions
  already do.

## Compliance

No classification is modelled as a property of the object it classifies. The
Knowledge Graph represents metamodel entities, instances and assertions as
distinct node types. The metamodel is organised by level.
