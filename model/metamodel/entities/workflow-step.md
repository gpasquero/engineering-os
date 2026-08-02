---
id: METAMODEL-WorkflowStep
title: WorkflowStep
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: operational
artifact-kind: authoritative
established-by: [ADR-0066, ADR-0068]
---

# WorkflowStep

**The reified association between a Workflow and a Skill, carrying its
position.**

## What new semantics does this introduce?

**Position within a sequence** — which is extrinsic, and therefore cannot live on
either end of the association.

The same Skill occupies position 2 in one Workflow and position 5 in another. The
position is not a fact about the Skill, and it is not a fact about the Workflow
as a whole. It is a fact about *this Skill in this Workflow*.

`ADR-0068`'s test settles it mechanically:

> **Can the same target hold two different positions under two different
> sources?** Yes. The order belongs to the association, and by `ADR-0066` an
> association that carries data is an entity.

## identity

The pair of **Workflow and position**.

Not Workflow-and-Skill: a Workflow may legitimately execute the same Skill twice
at different points, and identifying by Skill would make that unrepresentable.

## purpose

To hold ordering without extending `RelationshipType` and without putting a
special case in `Workflow`.

Both resulting relationships — `Workflow → WorkflowStep` and
`WorkflowStep → Skill` — are ordinary and unordered. **The ordering problem
disappears rather than being accommodated.**

## ownership

Owned by the repository owning the Workflow.

## lifecycle owner

`ArtifactRevisionLifecycle`, through its Workflow. A step has no independent
lifecycle: reordering a Workflow is a revision of the Workflow.

## authoritative representation

A declaration within the Workflow naming the position, the Skill executed, and
any condition guarding the step.

**The serialization is nested inside the Workflow; the semantics are not.** This
is the same relationship `DimensionAssignment` has to front matter (`ADR-0045`):
convenient authoring syntax over a first-class relationship. Nesting in the
authoring form does not make the step a property of the Workflow.

## derived representations

- Ordered edges in the Canonical Knowledge Model.
- The Workflow diagram in the Knowledge Explorer.
- Skill-usage reports: which Workflows execute a Skill, and where.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| step-of | Workflow | exactly one |
| executes | Skill | exactly one |
| has-position | ordinal | exactly one |
| guarded-by | condition | zero or one |

## extension points

None. A step is structural; extension happens in the Skill it executes.

## Debt

**Reification costs one entity per ordered association.** This is the second in
the metamodel after `DimensionAssignment`, and a domain with many ordered
relationships will accumulate them. `ADR-0068` accepted that cost explicitly;
whether it becomes a problem is a question for a real Layer B model, not for B1.

**`guarded-by` points at "condition", which is not an entity** — the fifth
instance of the pattern named in `FINDINGS.md` #8. Branch conditions were already
recorded as debt in `Workflow` and this does not change that.

**Position notation is unstated.** Contiguous integers, sparse integers and
fractional insertion keys all behave differently under reordering. Not needed to
finish B1.
