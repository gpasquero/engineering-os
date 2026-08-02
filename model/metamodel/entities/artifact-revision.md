---
id: METAMODEL-ArtifactRevision
title: ArtifactRevision
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
artifact-kind: authoritative
established-by: [ADR-0026, ADR-0020]
---

# ArtifactRevision

An identifiable version of an Artifact. **The unit that carries lifecycle state
and the unit that is accepted.**

## identity

An ArtifactRevision is identified **within an Artifact identity**, not globally.
An Artifact is an identity that may own many Revisions; a Revision has exactly
one lifecycle state (`ADR-0026`).

**What identifies a revision — commit, content hash or declared version — is
undefined.** `ISSUE-0007`, deferred as architectural debt.

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

## extension points

An adopting repository may **assign additional dimensions** to its revisions.
It may not add lifecycle states — `ArtifactRevisionLifecycle` is a closed
vocabulary, and a new state requires an ADR under `ADR-0025`.

## Recorded while building

`ADR-0026` states that an Artifact "has metadata such as identifier, ownership
and revision history" — but **`Artifact` has no entity specification**, and this
specification refers to it throughout. Writing `ArtifactRevision` before
`Artifact` was the wrong order and is worth noting for the next increment.
