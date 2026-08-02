---
id: METAMODEL-AcceptanceRecord
title: AcceptanceRecord
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: operational
artifact-kind: authoritative
established-by: [ADR-0021, ADR-0023, ADR-0024, ADR-0065]
---

# AcceptanceRecord

**The act that confers `Active` status on an ArtifactRevision.**

## What new semantics does this introduce?

**Authority.** It is the only entity that changes another entity's state.

Every other relationship in the metamodel describes or constrains. This one
*does* something: before it, a revision is `Under Review`; after it, `Active`.

> **Acceptance confers Active status. Commits do not** (`ADR-0018`, `ADR-0020`).

That is the relationship nothing else can express, and it is the reason the
project has an acceptance model at all.

## identity

A stable identifier, allocated sequentially and never reused.

## purpose

To make the transition to `Active` **an act by a named party**, rather than a
side effect of writing a file.

Three conditions must hold (`ADR-0021`): reviewer approval, traceability, and
applicable deterministic validation. **Self-certification is prohibited**
(`ADR-0023`) — author and reviewer must be different parties.

## The chain terminates here

**An AcceptanceRecord is never itself subject to an additional AcceptanceRecord**
(`ADR-0024`). It derives its authority from the decision it records.

This is the base case, not an exception, and it has one consequence worth
stating plainly: **an AcceptanceRecord is the single artifact that nothing else
checks.** The `reviewer` field must therefore always name a real, askable party.

The trust root is `ACCEPT-0001`.

## ownership

Owned by the repository whose revisions it accepts. **Acceptance never crosses
repositories** — an imported Knowledge Package carries its own acceptance
history and does not confer status locally.

## lifecycle owner

**None.** An AcceptanceRecord does not transition. It is written once and stands,
because a record of an act cannot later become a different act.

This is the only entity in the metamodel with no lifecycle owner, and the
asymmetry is the point.

## authoritative representation

A record naming the accepted revision, the reviewer, the decision, the rationale,
and evidence that each of the three conditions was satisfied.

## derived representations

- Edges in the Canonical Knowledge Model, from record to accepted revision.
- The acceptance history of any artifact.
- An unaccepted-revision report: revisions `Under Review` with no record.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| accepts | ArtifactRevision | one or more |
| reviewed-by | Actor | exactly one |
| cites | Evidence | zero or more |
| decides | accepted or returned | exactly one |

**`reviewed-by` is exactly one**, and it must not be the author. Governance is
self-hosting but never self-certifying (`ADR-0023`).

## extension points

An adopting repository may add conditions. **It may not remove the three**, and
may not permit self-certification.

## Debt

**Nothing enforces that reviewer and author differ.** The rule is stated in
`ADR-0023` and checked by nobody. It is mechanically checkable — both parties are
recorded — and is a natural first ValidationRule.

**`decides` points at a two-value enumeration that is not a Vocabulary.**
`Vocabulary` is specified as an entity for exactly this and is not yet used.

**Acceptance of an acceptance is prevented by decision, not by structure.**
Nothing in the model makes `ACCEPT-0019 accepts ACCEPT-0018` unrepresentable. It
is prohibited in prose.
