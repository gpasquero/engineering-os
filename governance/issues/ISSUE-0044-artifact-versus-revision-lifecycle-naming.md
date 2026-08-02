---
id: ISSUE-0044
title: ArtifactLifecycle conflicts with ADR-0020's revision framing
type: inconsistency
status: resolved
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0025-every-state-belongs-to-exactly-one-state-machine.md
  - governance/adr/ADR-0020-artifact-taxonomy-and-revision-lifecycle-are-independent.md
resolved-by: ADR-0026
---

# ISSUE-0044 — `ArtifactLifecycle` versus the revision framing

## Statement

`ADR-0020` was explicit that the lifecycle applies to a **revision**, not to an
artifact:

> "the lifecycle is explicitly the lifecycle of a **revision** rather than of an
> artifact"

It made the point deliberately, because exactly one revision of an artifact is
`Active` at a time while the artifact itself persists across many revisions.

`ADR-0025` names the state machine **`ArtifactLifecycle`**, with
`ArtifactLifecycle.Active` as its example.

## Why it matters

`shared/vocabularies/` is an M2 deliverable and will encode this state machine
under whichever name is chosen. The name will appear in every schema, contract
and validator downstream, and in every skill that models lifecycles in a target
domain.

It is not merely cosmetic. If the machine is named `ArtifactLifecycle`, a reader
will reasonably conclude that an *artifact* is `Active` — which contradicts
`ADR-0020`'s central distinction, since an artifact with three revisions has
one `Active` revision and two `Superseded` ones simultaneously.

## Options

- **`RevisionLifecycle`** — consistent with `ADR-0020`. The states then attach
  to the thing that actually transitions.
- **`ArtifactLifecycle`, with states applying to the artifact's current
  revision.** Matches the name given in `ADR-0025`, and reads naturally, but
  requires the reader to remember an implicit indirection.
- **Both, as distinct machines** — an artifact-level machine (`Draft`,
  `Published`, `Retired`) and a revision-level one. Only justified if artifacts
  genuinely have states independent of their revisions, which has not been
  shown.

The first is the most consistent with what is already decided. The name in
`ADR-0025` was given among examples rather than as a definitive inventory
(`ISSUE-0045`), which suggests it was illustrative.

## Resolution

`ADR-0026`. **`ADR-0020` is correct — the lifecycle belongs to a Revision.**

- An **Artifact** is an *identity* that may own many Revisions.
- A **Revision** has exactly one lifecycle state.
- **The Artifact itself has no lifecycle.** It has metadata: identifier,
  ownership, revision history. Only revisions transition.

The machine is named after the entity that owns it:
`ArtifactRevisionLifecycle.Draft`, `.UnderReview`, `.Accepted`, `.Active`,
`.Superseded`, `.Archived`.

Neither option listed above was taken as written. The first would have kept the
implicit indirection; the third (`RevisionLifecycle`) drops the entity prefix and
breaks the naming rule, since other kinds of revision will exist.

`ADR-0026` also **corrects the examples in `ADR-0025`** without superseding it —
that ADR's rule is untouched. The documentation system has no mechanism for a
partial correction, which is recorded as `ISSUE-0048`.

The identity/revision distinction is now a **core modeling guideline** applying
to every versioned object in Engineering OS.
