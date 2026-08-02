---
id: ADR-0020
title: Artifact taxonomy and revision lifecycle are independent vocabularies
status: accepted
date: 2026-08-02
supersedes: ADR-0018
superseded-by: null
resolves: [ISSUE-0038]
related: [ADR-0012, ADR-0021, ADR-0023, ISSUE-0007, ISSUE-0043]
---

# ADR-0020 — Artifact taxonomy and revision lifecycle are independent

**This is a foundational architectural principle.** It supersedes `ADR-0018`,
whose acceptance decision is carried forward in full; only the lifecycle
vocabulary changes, and the subject of that lifecycle sharpens.

## Context

`ADR-0012` defined an artifact taxonomy including `authoritative`. `ADR-0018`
defined a lifecycle including `Authoritative`. `ISSUE-0038` recorded the
collision: one word naming two concepts, in two closed vocabularies that were
both about to be written to `shared/vocabularies/` in M2.

This is the same class of defect as the overloaded word "skill" resolved in M1 —
which survived undetected through the entire inherited corpus.

## Decision

**The term `authoritative` is split. Two independent vocabularies.**

### Artifact taxonomy — the nature of an artifact

- Authoritative Artifact
- Derived Artifact
- Runtime Artifact
- Cached Artifact

### Revision lifecycle — the lifecycle of a revision

- Draft
- Under Review
- Accepted
- **Active** — renamed from `Authoritative`
- Superseded
- Archived

### The two definitions that matter

**Accepted** — the revision has successfully completed the acceptance process.

**Active** — the accepted revision is the current governing revision for that
artifact.

The distinction is essential because **an accepted revision may immediately
become superseded by a newer accepted revision**. Acceptance is a completed
event; being Active is a current status, and only one revision of an artifact is
Active at a time.

### The invariant

> **An artifact is authoritative because of its taxonomy.
> A revision is Active because of its lifecycle.
> These concepts remain completely independent.**

A hand-authored ontology file is an Authoritative Artifact whether its current
revision is Draft, Active or Archived. A generated index is a Derived Artifact
regardless of any lifecycle state.

## What survives from ADR-0018

The entire acceptance decision:

- Authoritative status is conferred by acceptance, not by authorship and not by
  a commit.
- Acceptance requires explicit reviewer approval, traceability to the motivating
  issue or ADR, and successful validation of all applicable deterministic checks.
- **Self-certification is prohibited** unless an explicit governance policy
  enables it.
- Acceptance is itself knowledge, and traceable.

Also carried forward from `ADR-0015` through `ADR-0018`: authoring is
non-deterministic, compilation is deterministic, AI agents are authors exactly
like human engineers, and a generator may never invoke an agent.

**What changes:** the state `Authoritative` becomes `Active`, and the lifecycle
is explicitly the lifecycle of a **revision** rather than of an artifact.

## Alternatives considered

**Rename the taxonomy term instead** — for example `source` or `authored`.
Rejected: "authoritative artifact" is the more established of the two usages,
appears throughout `ADR-0012` and `ADR-0014`, and carries the tier name in the
three-tier model. Renaming it would touch far more of the corpus.

**Keep both and disambiguate by qualifier.** Rejected: it is precisely what the
project had to abandon for "skill", and a qualifier that must be remembered
everywhere is not a fix.

**Collapse the two into one vocabulary.** Rejected: they answer different
questions and combine freely. Collapsing them would make it impossible to say
that a hand-authored file is currently a draft.

## Consequences

### Positive

- Both vocabularies can now be written to `shared/vocabularies/` without
  inheriting an ambiguity into every schema and validator downstream.
- The two axes combine freely, which is what the model actually needs.
- **`Accepted` versus `Active` closes the second ambiguity `ISSUE-0038` raised**,
  and does so with a real distinction rather than a definition of convenience.

### Negative

- **`revision` becomes load-bearing and is undefined.** The lifecycle applies to
  revisions, and `ADR-0021` requires an "artifact revision" field, but nothing
  says what identifies a revision — a commit, a content hash, a version number.
  Folded into `ISSUE-0007`.
- Every document already written that names `Authoritative` as a lifecycle state
  must be corrected. That is this session's propagation work.
- **The project's own document status vocabularies now overlap this lifecycle.**
  An ADR marked `status: accepted` is, in lifecycle terms, `Active`. Four
  vocabularies exist where one might do — `ISSUE-0043`.

### Neutral

- Third supersession in the acceptance area in two sessions
  (`ADR-0015`→`ADR-0018`→`ADR-0020`). The chain is visible in the supersession
  table, and the depth is honest evidence that this area is still settling.

## Compliance

No document uses `authoritative` as a lifecycle state, and no document uses
`Active` as an artifact kind. Every artifact is classifiable on both axes
independently. Exactly one revision of an artifact is `Active` at a time.
