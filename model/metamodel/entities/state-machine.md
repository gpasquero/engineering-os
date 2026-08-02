---
id: METAMODEL-StateMachine
title: StateMachine
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0025, ADR-0065, ADR-0067]
related-issues: [ISSUE-0074]
merge-candidate: METAMODEL-StateMachineSpecification
---

# StateMachine

**An instance of a StateMachineSpecification.**

> **This entity fails the `ADR-0067` test.** The specification is written to
> record that finding, not to justify the entity.

## What new semantics does this introduce?

**None.**

Every relationship a StateMachine might declare is already declared by its
StateMachineSpecification:

| Candidate relationship | Already declared by |
|---|---|
| governs an entity type | `StateMachineSpecification.governs` |
| has states | `StateMachineSpecification.declares-states` |
| has transitions | `StateMachineSpecification.declares-transitions` |
| is driven by a Workflow | `StateMachineSpecification.driven-by` |

A StateMachine has no authoritative representation of its own, holds no property
its specification lacks, and stands in a 1:1 functional relation to it.

**This is the same shape as `Dimension` / `DimensionSpecification`**
(`FINDINGS.md` #2), reached independently in a second domain.

## What the second domain showed

The purpose of specifying this pair was to test whether the
Specification/Instance pattern survives independent confirmation. **It did not.**

The pattern is not Specification/Instance. It is **specification only, with the
word "instance" attached to the same thing twice.**

Genuine instantiation exists in both domains — but it is not where the pattern
put it:

| Domain | The specification | The genuine instance |
|---|---|---|
| Dimensions | `DimensionSpecification` | **`DimensionAssignment`** — a particular artifact classified along the axis |
| State machines | `StateMachineSpecification` | **a particular artifact traversing states over time** — unmodelled |

`DimensionAssignment` already exists and is already correct. The state-machine
equivalent would be a *State Machine Execution*, which is Operational Knowledge
and sits outside the model (`ADR-0061`, `ISSUE-0073`).

> **In both domains the middle layer is empty because the real instance is either
> already modelled under a different name, or deliberately outside the model.**

## identity

None of its own. It has the identifier declared by its specification.

## purpose

To be assessed for removal.

Under `ISSUE-0074` this is now the **second confirmed merge candidate**, and the
stronger of the two: `Dimension` could be defended on the grounds that
`DimensionAssignment.along` reads better pointing at an axis than at a document.
`StateMachine` has no such defence — nothing points at it.

## ownership, lifecycle owner, authoritative representation

Its specification's. It has none of its own.

## derived representations

None. Anything derived is derived from the specification.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| specified-by | StateMachineSpecification | exactly one |

**One relationship, and it is the one that makes the entity redundant.**

## extension points

None.

## Debt

**This entity should probably not exist.** Recorded rather than deleted, because
`ISSUE-0074` exists precisely so that removals happen as one considered pass
rather than as opportunistic deletions — and because a third case may yet show
the pattern is sound and these two are the anomalies.

**The finding generalises to `RegistrySpecification`**, which is unspecified and
has the same shape. If it too has no instance half, the conclusion is not that
three entities are redundant but that **`Specification` is a suffix the metamodel
applies where no distinction exists** — and the specifications should simply be
called `Dimension`, `StateMachine` and `Registry`.

That is a larger and better outcome than three merges, and it is exactly what the
simplification review is for.
