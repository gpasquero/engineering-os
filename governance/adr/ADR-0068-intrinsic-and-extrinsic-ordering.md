---
id: ADR-0068
title: Ordering is intrinsic or extrinsic, and needs no new semantic construct
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0042, ADR-0057, ADR-0066, ADR-0067]
---

# ADR-0068 — Intrinsic and extrinsic ordering

## Context

`Workflow.sequences` is ordered. `RelationshipType` declares domain, range,
cardinality, constraints and semantics — and **none of them is sequence**
(`FINDINGS.md` #7).

The instruction was explicit: **do not extend `RelationshipType` with special
cases.** Do not solve the Workflow case. Determine whether ordering is a property
of a RelationshipType, a constraint attached to one, or a separate semantic
construct — and solve ordered relationships as a general capability, because
many future domains will require it and Workflow is simply the first to reveal
it.

## The question dissolved

It is none of the three, because **"ordering" names two different things.**

Once separated, each already has a mechanism, and neither is a property of a
RelationshipType.

### The diagnostic test

> **Can the same target hold two different positions under two different
> sources?**

That question is mechanical, and it separates the two cases completely.

### Intrinsic ordering — the order belongs to the ordered things

**No.** The order is a property of the entities themselves, identical everywhere
they appear.

`EvidenceKind` is ordered by directness: runtime observation outranks source,
which outranks documentation, which outranks inference. That ranking does not
change depending on who cites the evidence.

**Mechanism: a comparable property.** `directnessRank` is a datatype property and
that is the entire implementation. It already exists in the ontology and required
no construct when it was written.

### Extrinsic ordering — the order belongs to the association

**Yes.** The same Skill occupies position 2 in one Workflow and position 5 in
another. The position is not a fact about the Skill.

So the position is data carried by the association — and `ADR-0066` already
decided what to do with an association that carries data:

> **Where an individual association genuinely needs its own identity, provenance
> or lifecycle, it is modelled as an entity.** `DimensionAssignment` is exactly
> that, and it is the precedent for the pattern rather than an anomaly.

**Mechanism: reify the association.** `Workflow --sequences--> Skill` becomes
`Workflow --has-step--> WorkflowStep --executes--> Skill`, with the position on
the step. Both resulting relationships are ordinary and unordered.

## Decision

**`RelationshipType` is not extended.** It gains no ordering field, no sequence
flag, and no special case.

**Ordering is classified before it is modelled:**

| | Intrinsic | Extrinsic |
|---|---|---|
| The order is a fact about | the ordered entities | the association |
| Same target, different positions? | no | yes |
| Mechanism | a comparable property | reify the association (`ADR-0066`) |
| Requires a new construct | no | no |

**Both cases were already solvable.** The gap was that one word covered both, so
neither mechanism looked applicable.

## Alternatives considered

**An `ordered` flag on `RelationshipType`.** Rejected, and it is the option the
instruction warned against. It would declare an order without providing anywhere
to store it: the positions still have to live somewhere, and the only candidates
are the targets (wrong for the extrinsic case) or the edges (which `ADR-0066`
says are structure, not data-carrying objects). **The flag would state a problem
rather than solve one.**

**Ordering as a constraint attached to a RelationshipType.** Rejected for the
same reason. "These edges are totally ordered" is checkable only once the order
is representable, so the constraint presupposes the mechanism it was meant to
replace.

**A separate `Ordering` or `Sequence` construct.** Rejected as unnecessary once
the split is made — and it is the option most at risk of over-engineering.
Introducing a construct for a capability that two existing mechanisms already
cover would add a metamodel entity that fails `ADR-0067`'s own test.

**Solve the Workflow case with a list on the Workflow.** Rejected as the special
case the instruction prohibited.

## Consequences

### Positive

- **A general capability, resolved with no new construct.** The answer applies to
  policy precedence, severity, compiler phase order and any future ordered
  domain, without any of them needing a decision.
- The diagnostic test is mechanical and can be applied by an author or a checker
  without judgement.
- **`DimensionAssignment` is confirmed as a pattern rather than an exception.**
  It is now one of two reified associations, arrived at independently.
- `RelationshipType` stays small, which is what keeps it usable.

### Negative

- **One new entity: `WorkflowStep`.** Reification always costs an entity, and the
  cost is paid per ordered association. A domain with many ordered relationships
  will accumulate them.
- The intrinsic case is easy to get wrong in the direction that is expensive to
  fix: an author who puts a position on the target must reify later, and by then
  instances exist.

### Neutral

- **"Ordering" is the ninth term this project has had to split**, after "skill",
  "authoritative", "state", "policy", "registry", "layer/level", "level/process"
  and "validation". It is the second caught before being built rather than after.

## Compliance

`Workflow.sequences` is replaced by `has-step` and the `WorkflowStep` entity. No
specification declares a relationship ordered; ordered associations are reified
and ordered entities carry a comparable property.
