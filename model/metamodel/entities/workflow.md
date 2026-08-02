---
id: METAMODEL-Workflow
title: Workflow
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: operational
artifact-kind: authoritative
established-by: [ADR-0033, ADR-0051, ADR-0065]
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
| sequences | Skill | one or more, **ordered** |
| passes-through | EngineeringGate | zero or more |
| governed-by | ProcessPolicy | zero or more |
| produces | Artifact | zero or more, via its Skills |

**`sequences` is the metamodel's first ordered relationship.** Every other
relationship is a set; this one is a list, and `RelationshipType` has no field
for that distinction.

## extension points

An adopting repository declares its own workflows and recomposes framework skills
freely. Recomposition is the intended extension mechanism — it is why the
methodology lives in Skills rather than here.

## Debt

**`RelationshipType` cannot express order.** Its five fields — domain, range,
cardinality, constraints, semantics — have no notion of sequence, and `sequences`
needs one. **This is the first relationship the metamodel cannot type**, found by
writing the entity that needs it.

It does not block: the ordering can be carried in the Workflow's own declaration
rather than in the relationship. It does mean the relationship vocabulary is
incomplete, and `RelationshipType` will need either an ordering field or an
explicit statement that ordered relationships are modelled differently.

**Workflow Execution is unmodelled.** `ADR-0057` names it as a canonical concept
and no entity exists. Executions are where Operational Knowledge would enter the
model, which is `ISSUE-0073` again, from a third direction.

**Branch conditions have no vocabulary.** A Workflow may branch; nothing says on
what.
