---
id: METAMODEL-Workflow
title: Workflow
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: operational
artifact-kind: authoritative
established-by: [ADR-0033, ADR-0051, ADR-0065, ADR-0068]
---

# Workflow

**Executable orchestration. It sequences Skills and holds no methodology of its
own** (`ADR-0033`).

## What new semantics does this introduce?

**Ordering.** Nothing else in the metamodel expresses that one thing happens
before another.

Every other relationship specified so far is timeless: a Concept is scoped to a
context, an Invariant constrains a Capability, an Artifact has revisions. None
of them can say *first this, then that.*

That is the whole of what Workflow adds — and it is deliberately the whole. A
Workflow containing methodology would be a Skill wearing the wrong name.

## identity

A qualified name within the repository.

## purpose

To separate **what is done** from **the order it is done in**, so that either can
change without the other.

The separation is enforced by subtraction: a Workflow may sequence, branch,
repeat and terminate, and may do nothing else. Any step containing judgement is a
Skill.

## ownership

Framework workflows are owned by Engineering OS; adopting repositories declare
their own and may recompose framework skills into different orders.

## lifecycle owner

`ArtifactRevisionLifecycle`.

**A Workflow is not the same as its execution.** `Workflow Execution` is a
distinct canonical name (`ADR-0057`) and a distinct lifecycle: the Workflow is a
specification that is revised; an execution is an event that happens. This
specification covers the Workflow. **The execution is not modelled**, which is
recorded below.

## authoritative representation

A declaration naming the sequence of Skills, the conditions on branches, and the
Gates it passes through.

## derived representations

- Nodes and ordered edges in the Canonical Knowledge Model.
- A Workflow diagram in the Knowledge Explorer.
- A coverage report: Skills sequenced by no Workflow, Gates in no Workflow.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| has-step | WorkflowStep | one or more |
| passes-through | EngineeringGate | zero or more |
| governed-by | ProcessPolicy | zero or more |
| produces | Artifact | zero or more, via its Skills |

**`has-step` is unordered, and the Workflow is still ordered.** The order lives on
`WorkflowStep.has-position` (`ADR-0068`): the same Skill occupies different
positions in different Workflows, so the position is a fact about the association
rather than about either end.

A Workflow does not relate directly to a Skill. It relates to steps, and steps
execute skills.

## extension points

An adopting repository declares its own workflows and recomposes framework skills
freely. Recomposition is the intended extension mechanism — it is why the
methodology lives in Skills rather than here.

## Debt

**Ordering was the first semantic construct the metamodel could not express**,
and it is resolved (`ADR-0068`). The resolution cost one entity — `WorkflowStep` —
and no extension to `RelationshipType`. Recorded because the next ordered domain
should reach for the same answer rather than rediscovering it.

**Workflow Execution is unmodelled.** `ADR-0057` names it as a canonical concept
and no entity exists. Executions are where Operational Knowledge would enter the
model, which is `ISSUE-0073` again, from a third direction.

**Branch conditions have no vocabulary.** A Workflow may branch; nothing says on
what.
