---
id: METAMODEL-Artifact
title: Artifact
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
artifact-kind: authoritative
established-by: [ADR-0026, ADR-0064]
---

# Artifact

**A stable logical identity that owns many Revisions.** An Artifact is not a
file and not a version — it is the thing that persists while its revisions
change.

## identity

**A stable logical identifier** (`ADR-0064`). It does not change when the
artifact is revised, moved, renamed or reorganised.

It is not a path. `ADR-0039` established that repository layout is an
implementation concern, so an identifier derived from a location would change
when the location did.

## purpose

To separate *what a thing is* from *which version of it currently governs*.

**An Artifact has no lifecycle of its own.** It has metadata: identifier,
ownership, revision history. Only its revisions transition through states
(`ADR-0026`).

> "What state is this artifact in?" is a **malformed question**. Ask for the
> state of a revision, or for which revision is `Active`.

## ownership

Owned by the repository that owns its domain (`ADR-0010`). Knowledge is
repository-local; there is no central artifact registry across repositories.

## lifecycle owner

**None.** This is the defining negative property. Lifecycle belongs to
`ArtifactRevision`.

## authoritative representation

An Artifact has no representation of its own. It is manifested by its revisions,
each of which has an Authoring Representation (`ADR-0047`).

An Artifact with no revisions is a well-formed but empty identity.

## derived representations

- A node in the Canonical Knowledge Model, linked to its revisions.
- An entry in whatever registry indexes artifacts of its type.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| owns | ArtifactRevision | one to many |
| has-active-revision | ArtifactRevision | zero or one |
| instantiates | ArtifactType | exactly one |
| classified-by | DimensionAssignment | zero or more |

**`has-active-revision` is zero-or-one, not exactly-one.** An artifact whose
revisions are all `Draft` has no governing revision, and that is a legitimate
state.

## extension points

An adopting repository defines its own ArtifactTypes and assigns its own
dimensions. It does not change what an Artifact is.

## Debt

**Who allocates an artifact identifier, and when, is not stated** (`ADR-0064`).
Authors need a convention and none exists. Recorded rather than decided, per
`ADR-0062`.
