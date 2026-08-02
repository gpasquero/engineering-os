---
id: METAMODEL-ArtifactRevision
title: ArtifactRevision
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0026, ADR-0020, ADR-0064]
---

# ArtifactRevision

An identifiable version of an Artifact. **The unit that carries lifecycle state
and the unit that is accepted.**

## identity

**The pair `(artifact-id, revision-id)`** (`ADR-0064`).

An Artifact has a stable logical identifier. An ArtifactRevision has an
**immutable revision identifier scoped to its Artifact** — unique within the
Artifact, not globally.

The revision identifier:

- must be **immutable**;
- must be **unique within the Artifact**;
- **must not require Git**;
- **may** be mapped to a Git commit, content digest or external revision
  identifier;
- must not assume any one storage or version-control implementation is
  universal.

> **A Git commit SHA is provenance, not identity.**

`ACCEPT-0001` used a commit SHA for the trust root as a pragmatic choice,
explicitly not a decision. Under `ADR-0064` that reading is retroactively
correct: it was recording provenance.

## purpose

To separate *what a thing is* from *which version of it currently governs*.

An Artifact persists across many Revisions and **has no lifecycle of its own** —
only metadata: identifier, ownership, revision history. "What state is this
artifact in?" is a malformed question (`ADR-0026`).

## ownership

Owned by the Artifact it revises. An Artifact is owned by the repository that
owns its domain (`ADR-0010`).

## lifecycle owner

**`ArtifactRevisionLifecycle`** (`ADR-0020`, `ADR-0026`):

```text
Draft → Under Review → Accepted → Active → Superseded → Archived
```

- **Accepted** — the revision has completed the acceptance process.
- **Active** — the accepted revision is the current governing revision.

The distinction matters because an accepted revision may immediately become
superseded by a newer accepted revision. **Exactly one revision of an Artifact
is `Active` at a time.**

## authoritative representation

The artifact file itself, in its Authoring Representation (`ADR-0047`). Human
readable and editable without executing the compiler (`ADR-0017`).

Lifecycle state is **not a property of the revision**. It is a
DimensionAssignment relating the revision to the `ArtifactRevisionLifecycle`
dimension (`ADR-0042`), serialized into front matter as interchange syntax
(`ADR-0045`).

## derived representations

- A node in the Canonical Knowledge Model, with its assignments as graph edges.
- Entries in Registry Projections that index it.
- Whatever the Knowledge Explorer and documentation render from those.

## relationships

| Relationship | Target | Notes |
|---|---|---|
| revises | Artifact | many revisions per artifact identity |
| supersedes / superseded-by | ArtifactRevision | forms the supersession chain |
| accepted-by | AcceptanceRecord | exactly one for an `Active` revision |
| classified-by | DimensionAssignment | zero or more |
| has-provenance | external revision reference | zero or more — Git commit, content digest |

## extension points

An adopting repository may **assign additional dimensions** to its revisions.
It may not add lifecycle states — `ArtifactRevisionLifecycle` is a closed
vocabulary, and a new state requires an ADR under `ADR-0025`.

## Debt

**Who allocates a revision identifier, and when, is not stated** (`ADR-0064`).
Recorded rather than decided, per `ADR-0062`.

`SESSION-0021` noted that this specification was written before `Artifact`,
which it references throughout. [`Artifact`](artifact.md) now exists, and the
identity field that had to say *undefined* is answered.
