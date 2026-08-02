---
id: METAMODEL-Issue
title: Issue
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: operational
artifact-kind: authoritative
established-by: [ADR-0003, ADR-0062, ADR-0065]
---

# Issue

**A recorded unknown.**

## What new semantics does this introduce?

**Blocking, and deferral.**

An Issue is the only entity that can state *this is not known, and here is what
that prevents.* Nothing else in the metamodel represents absent knowledge at all
— every other entity asserts something.

- **`blocks`** — a dependency on knowledge that does not exist yet.
- **`defers-to`** — an unknown deliberately carried as debt to a named future
  point (`ADR-0062`).

**This is the thinnest passing entity in the metamodel**, and the honest reading
is that it passes on `blocks` and `defers-to` alone. `resolved-by` is merely the
inverse of `ADR.resolves` and introduces nothing.

## identity

A stable sequential identifier, never reused.

## purpose

To make **not knowing** a first-class, recorded state.

The governing rule (`ADR-0003`): **if information is missing, create an issue
instead of assuming.** An Issue is the mechanism that makes an assumption
expensive enough to notice.

## Deferral is a status, not a failure

`ADR-0062` added `deferred`, and it changed what the register is for.

An issue is deferred when its answer **does not change what gets built next**. It
is reopened when implementation requires it — not on a schedule.

The evidence that this works is `ISSUE-0007`: deferred in `SESSION-0021`,
resolved in `SESSION-0022`, because writing `ArtifactRevision` turned a
nineteen-session abstract question into a blank field.

## ownership

Owned by the repository recording the unknown.

## lifecycle owner

Its own state machine — `open`, `deferred`, `resolved` — which is **not**
`ArtifactRevisionLifecycle`. An issue is not accepted; it is answered.

Every state belongs to exactly one state machine (`ADR-0027`), and this is a case
where the general artifact lifecycle does not apply.

## authoritative representation

A record naming: the statement, why it matters, what is known, the candidate
options, and the resolution criteria.

> **Do not silently pick an option.** An Issue that states a preferred answer as
> fact has stopped being a record of an unknown.

## derived representations

- Nodes in the Canonical Knowledge Model, linked to what they block.
- The open-issue register and the debt register.
- A staleness report: deferred issues whose trigger condition has been met.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| blocks | Artifact, deliverable or entity | zero or more |
| defers-to | deliverable | zero or one |
| resolved-by | ADR | zero or more |
| evidenced-by | Evidence | zero or more |

## extension points

An adopting repository records its own unknowns. The states are closed.

## Debt

**No mechanism detects that a deferral's trigger has been met.** Twenty-two
issues are deferred, each naming a condition for reopening, and reopening depends
entirely on someone noticing. **`ISSUE-0073` surfaced in `SESSION-0023` because a
specification happened to touch it**, not because anything checked.

This is mechanical and belongs to B5.

**Six issues were resolved by rejecting all their options**, on the grounds that
the options shared a wrong assumption. Nothing in this specification records that
outcome. It is the most valuable thing the register has produced and it is
invisible in the model.

**The three states are not declared as a Vocabulary**, and the state machine has
no `StateMachineSpecification`. Both entities exist for exactly this.
