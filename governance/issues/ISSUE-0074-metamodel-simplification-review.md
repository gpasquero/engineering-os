---
id: ISSUE-0074
title: Metamodel simplification review at approximately 75% completion
type: gap
status: deferred
severity: medium
created: 2026-08-02
updated: 2026-08-02
blocks: []
evidence:
  - model/metamodel/ontology/FINDINGS.md
  - model/metamodel/entity-inventory.md
  - governance/adr/ADR-0067-the-relationship-is-the-design-unit.md
resolved-by: null
defers-to: [B1]
debt: architectural
---

# ISSUE-0074 — Metamodel simplification review

> **Scheduled work, deferred by decision** (`ADR-0062`). Not blocking. The
> trigger is a completion threshold, not a contradiction.

## Statement

**When approximately 75% of the metamodel exists, perform a metamodel
simplification review.**

One explicit objective: **identify entity pairs that can be merged without
losing expressive power.**

## Why it matters

The metamodel is being built incrementally, and incremental construction
accumulates accidental complexity — distinctions that exist because the
architecture evolved that way, not because they carry meaning.

`ADR-0067` gives the review its instrument: *what new semantic relationship does
this entity introduce that cannot already be expressed?* Applied retroactively,
that question is what makes merging tractable.

**Doing this at 75% rather than at 100% is deliberate.** At completion, every
merge is a change to a finished thing. Before it, a merge changes what remains
to be built.

## What we know

**`Dimension` / `DimensionSpecification` is the first candidate.** The 1:1
correspondence is a very strong signal. `Dimension` has no authoritative
representation of its own, is functionally determined by its specification, and
carries no property the specification lacks (`FINDINGS.md` #2).

The reviewer's instruction is explicit: **do not force them to remain separate
merely because the architecture originally evolved that way.**

The Specification/Instance split is used more than once — `StateMachineSpecification`
/ `StateMachine` has the same shape and is unspecified. Whether that pair has the
same problem is unknown, and it will be known once both are written.

**Neither premature optimisation nor preserved accidental complexity is
acceptable.** The threshold exists to hold that line.

## Options

Not a choice between answers. The review is the work, and its outcome is a set
of merge or retain decisions, each recorded.

## Resolution criteria

Resolved when the review has been performed and its outcome recorded as ADRs —
one per merge or explicit retention, at minimum for `Dimension` /
`DimensionSpecification`.

**Trigger: approximately 75% of Layer A entities specified.** With 27 entities
currently confirmed, that is roughly 20.
