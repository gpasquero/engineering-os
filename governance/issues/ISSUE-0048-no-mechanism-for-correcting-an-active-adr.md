---
id: ISSUE-0048
title: The documentation system has no mechanism for correcting part of an Active ADR
type: gap
status: open
severity: medium
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/documentation-system.md
  - governance/adr/ADR-0026-artifact-revision-lifecycle.md
  - governance/adr/ADR-0025-every-state-belongs-to-exactly-one-state-machine.md
resolved-by: null
---

# ISSUE-0048 — No mechanism for correcting part of an Active ADR

## Statement

`governance/documentation-system.md` states that an accepted ADR is never
edited, and is superseded by a new ADR. Those are the only two options.

`ADR-0026` needed a third. It corrects the *examples* in `ADR-0025` — the state
machine name `ArtifactLifecycle` becomes `ArtifactRevisionLifecycle` — while
`ADR-0025`'s decision is untouched and remains `Active`.

Superseding would be wrong: it would signal that the state-machine rule was
replaced, when only an illustration was. Editing would violate immutability. So
the correction currently lives only in `ADR-0026`'s prose and in the ADR index.

## Why it matters

A reader arriving at `ADR-0025` directly — from a search, a link, or the
index — sees `ArtifactLifecycle.Active` presented as correct, with nothing in
its front matter indicating otherwise. The `superseded-by` field is the only
machine-readable warning the system has, and it is the wrong one here.

The problem will recur. Long-lived ADRs accumulate small factual corrections
while their decisions stand.

## Options

- **A `corrected-by` front matter field**, listing ADRs that correct part of
  this one. Cheap, machine-readable, and symmetrical with `superseded-by`.
  Requires a matching `corrects` field, and thus another bidirectional link to
  maintain.
- **Treat any correction as a supersession.** Simple and already implemented,
  but it would mark `ADR-0025` superseded over an example, which misinforms more
  than it warns.
- **Allow errata edits to accepted ADRs**, appended and dated. Breaks
  immutability, which is the property that makes the corpus trustworthy.
- **Accept the gap**, relying on the index's Corrections section. Zero cost, and
  it fails exactly the reader who does not come via the index.

The first option is the most consistent with how supersession already works.

## Resolution criteria

An ADR extending the documentation system with a correction mechanism, or
recording a decision to accept the gap and stating why the index is sufficient.
