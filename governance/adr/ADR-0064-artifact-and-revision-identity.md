---
id: ADR-0064
title: Artifact and ArtifactRevision identity; Git is provenance, not identity
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0007]
related: [ADR-0026, ADR-0020, ADR-0017]
---

# ADR-0064 — Artifact and ArtifactRevision identity

## Context

`ISSUE-0007` had been open since `SESSION-0001` as an abstract question about
versioning granularity. `SESSION-0021` turned it concrete: writing the
`ArtifactRevision` specification produced a field that had to say *undefined*.

`ACCEPT-0001` had used a commit SHA as a pragmatic choice for the trust root,
explicitly not a decision.

## Decision

**An Artifact has a stable logical identifier.**

**An ArtifactRevision has an immutable revision identifier scoped to its
Artifact.**

ArtifactRevision identity is therefore the **pair**:

```text
(artifact-id, revision-id)
```

### The revision identifier

- must be **immutable**;
- must be **unique within the Artifact**;
- **must not require Git**;
- **may** be mapped to a Git commit, content digest or external revision
  identifier;
- must not assume that any one storage or version-control implementation is
  universal.

> **A Git commit SHA is provenance, not identity.**

## Alternatives considered

**Git commit SHA as identity.** Rejected: it makes the knowledge model
unusable outside Git, and `ADR-0017` requires the architecture to depend on no
specific implementation. It also identifies a *repository state*, not a
revision of one artifact.

**Content digest as identity.** Rejected as identity, permitted as a mapping. A
digest changes on a whitespace edit, so two revisions differing only in
formatting would be distinct — and an identical file authored twice would
collide.

**A single global revision identifier.** Rejected: scoping to the Artifact is
what makes revision numbers readable and stable, and a global counter would
couple unrelated artifacts.

## Consequences

### Positive

- **`ArtifactRevision` becomes specifiable.** The field that had to say
  *undefined* now has an answer.
- The knowledge model works under any storage: Git, a document store, or a
  system that has neither.
- Separating identity from provenance means an acceptance record can cite both —
  *which revision* and *where it came from* — without conflating them.
- `ACCEPT-0001`'s use of a commit SHA is retroactively correct: it was recording
  provenance.

### Negative

- **Who allocates a revision identifier, and when, is not stated.** Authors will
  need a convention, and nothing yet provides one. Recorded as debt rather than
  decided.
- Two identifiers where systems usually have one, and the mapping to Git must be
  maintained somewhere.

## Compliance

No artifact is identified by a Git SHA alone. Every ArtifactRevision is
identified by the pair `(artifact-id, revision-id)`. Provenance is recorded
separately from identity.
