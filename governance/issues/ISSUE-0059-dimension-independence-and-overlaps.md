---
id: ISSUE-0059
title: Dimension independence conflicts with declared inter-dimension relationships, and four dimensions overlap
type: inconsistency
status: open
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0040-architectural-dimensions.md
  - governance/adr/ADR-0041-dimensions-are-registered-first-class-entities.md
  - governance/adr/ADR-0020-artifact-taxonomy-and-revision-lifecycle-are-independent.md
resolved-by: null
---

# ISSUE-0059 — Dimension independence versus declared relationships

## Statement

Two problems, both about how dimensions relate to one another.

### 1. Independence contradicts the registration schema

`ADR-0040` states that dimensions are **independent**: *"a value on one dimension
never implies a value on another."*

`ADR-0041` requires every dimension registration to declare **"relationships to
other dimensions"**.

If dimensions relate, in what sense are they independent? Either the field
expresses something weaker than implication — and nothing says what — or
independence is not the property `ADR-0040` claims.

### 2. Four dimensions are undefined, and appear to overlap

`Governance Status` · `Ownership` · `Authority` · `Visibility` have no
definition.

**`Governance Status` looks like `Lifecycle` under another name.**
`ArtifactRevisionLifecycle` already has `Draft`, `Under Review`, `Accepted`,
`Active`, `Superseded`, `Archived` — which is governance status. Two dimensions
naming one axis is the exact failure `ADR-0040` was written to prevent,
appearing inside `ADR-0040`.

**`Ownership` and `Authority` may also be one axis.** `ADR-0040`'s worked example
gives `Owner: Architecture` and no `Authority` value at all.

## Why it matters

`ADR-0041` makes dimensions registered entities, and the Dimension Registry
Specification is M2 work. It cannot be written while two of its eight fields are
in tension and half its initial registrations are undefined.

`ADR-0020` established the precedent that matters here: the artifact taxonomy
and the revision lifecycle were shown to be genuinely independent axes that
happened to share a label. The question for `Governance Status` and `Lifecycle`
is whether the same holds, or whether they are one axis with two names.

## Open sub-questions

- What kind of relationship can a dimension declare, if not implication?
  Constraint? Applicability? Derivation?
- Is `Governance Status` distinct from `ArtifactRevisionLifecycle`, and if so,
  what does it range over?
- Are `Ownership` and `Authority` one dimension or two? The distinction between
  *who owns a thing* and *who may change it* is real in principle — but nothing
  says it is intended here.
- Does `Visibility` range over artifacts, over projections, or over both?

## Resolution criteria

An ADR reconciling independence with declared relationships, and defining or
eliminating the four dimensions. Must precede the Dimension Registry
Specification.
