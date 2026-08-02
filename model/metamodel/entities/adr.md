---
id: METAMODEL-ADR
title: ADR
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: operational
artifact-kind: authoritative
established-by: [ADR-0002, ADR-0058, ADR-0065]
---

# ADR

**A recorded architectural decision.**

## What new semantics does this introduce?

**Supersession** — and it is genuinely distinct from revision.

`ArtifactRevision` already expresses that a thing changed. Supersession expresses
that **a different decision replaced this one while this one remains readable and
true of its own moment.** A superseded ADR is not a stale revision; it is a
correct record of what was decided then.

Two further relationships are new:

- **`resolves`** — a decision answering a recorded unknown. The pair with
  `Issue.resolved-by` is what makes the knowledge base auditable.
- **`establishes`** — the source from which Principles are extracted
  (`ADR-0058`).

## identity

A stable sequential identifier, never reused.

## purpose

To make the reasoning behind an architecture **survive the people who did it**.

The rule that gives this force: **an accepted ADR is never edited.** It is
superseded by a new ADR, with `superseded-by` set on the original and
`supersedes` on the replacement. Both directions are mandatory, which makes the
chain traversable in either direction and mechanically checkable.

> **An ADR with no `Alternatives considered` section is a note, not a decision
> record.** A decision is defined by what it rejected.

## ownership

Owned by the repository making the decision. An imported Knowledge Package
carries decisions as provenance; they do not become local decisions.

## lifecycle owner

`ArtifactRevisionLifecycle`, with one qualification: an ADR's normal terminal
state is `Superseded` rather than `Archived`, and a superseded ADR stays
readable indefinitely.

## authoritative representation

A record naming the context, the decision, **the alternatives considered**, the
consequences — positive, negative and neutral — and compliance.

## derived representations

- Decision nodes in the Canonical Knowledge Model.
- The supersession graph.
- Extracted Principles (`ADR-0058`) — mechanical extraction of a declaration, not
  recognition of a pattern (`ADR-0060`).
- The decision index.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| supersedes | ADR | zero or more |
| superseded-by | ADR | zero or one |
| resolves | Issue | zero or more |
| establishes | Principle | zero or more |
| corrects | ADR | zero or more |

**`corrects` is not `supersedes`.** A correction fixes an error in an ADR whose
decision remains `Active` — six exist, visible only in a hand-maintained table in
the ADR index (`ISSUE-0048`).

## extension points

An adopting repository records its own decisions. The structure is fixed;
`Alternatives considered` is not optional.

## Debt

**`corrects` has no machine-readable mechanism** (`ISSUE-0048`). Six corrections
exist and all six live in a table maintained by hand — which is `ISSUE-0037`
again. Specifying the relationship here is the first step; making the front
matter carry it is B5.

**`establishes` has never been exercised.** No Principle has been extracted from
any of the sixty-seven ADRs. `Principle` is unspecified.

**An ADR is thinner than it appears.** Remove supersession, correction and
resolution, and what remains is an Artifact with a required section. Under
`ADR-0067` it passes — those three relationships are real and unavailable
elsewhere — but it passes on its relationships alone, which is exactly the
lightening `ADR-0067` describes.
