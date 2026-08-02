---
id: ISSUE-0038
title: "authoritative" names both a lifecycle state and an artifact kind
type: inconsistency
status: open
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0018-acceptance-confers-authoritative-status.md
  - governance/adr/ADR-0012-executable-framework-and-artifact-taxonomy.md
  - governance/adr/ADR-0014-three-tier-knowledge-model.md
resolved-by: null
---

# ISSUE-0038 — `authoritative` names two different things

## Statement

Two closed vocabularies now use the same word for different concepts.

**Artifact kind** (`ADR-0012`) — how an artifact is produced:
`authoritative`, `derived`, `runtime`, `cached`.

**Lifecycle state** (`ADR-0018`) — where an artifact stands in the acceptance
process: `Draft`, `Under Review`, `Accepted`, `Authoritative`, `Superseded`,
`Archived`.

`authoritative` appears in both, meaning different things. A draft is already
`authoritative` *in kind* — it is hand-authored source, not generated — while
being `Draft` *in lifecycle*.

## Why it matters

Both become closed vocabularies in `shared/vocabularies/` during M2. Writing
them with a colliding term guarantees that every downstream artifact, schema and
validator inherits the ambiguity.

This is the same class of defect as the overloaded word "skill" resolved in M1
(`ISSUE-0012`) — and that one was caught only because someone asked what
`BOOTSTRAP.md` meant. It is marked `blocking` because the vocabularies are early
M2 deliverables and renaming afterwards is expensive.

## A second, related ambiguity

The lifecycle lists `Accepted` and `Authoritative` as **separate states**, and
nothing says what distinguishes them. `ADR-0018` says acceptance confers
authoritative status, which reads as though they are the same moment.

Plausible readings:

- `Accepted` is the decision; `Authoritative` is the state that follows once the
  acceptance record is committed.
- `Accepted` means approved but not yet published or compiled; `Authoritative`
  means in force.

These are not equivalent, and the difference determines whether an artifact
between the two states is usable by the compiler.

## Options

- Rename the artifact kind — for example `source` or `authored` — leaving
  `authoritative` to the lifecycle.
- Rename the lifecycle state — for example `In Force` or `Active`.
- Keep both and disambiguate by qualifier everywhere. Weakest option; it is what
  the project already had to abandon for "skill".

## Resolution criteria

An ADR fixing both vocabularies with no shared term, and stating precisely what
distinguishes `Accepted` from `Authoritative`. Must precede
`shared/vocabularies/`.
