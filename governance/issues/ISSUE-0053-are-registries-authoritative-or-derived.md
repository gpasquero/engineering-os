---
id: ISSUE-0053
title: Whether a Registry is authoritative or derived is contradicted across three ADRs
type: inconsistency
status: open
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0031-registry-pattern.md
  - governance/adr/ADR-0016-governance-is-authoritative-manifests-are-projections.md
  - governance/adr/ADR-0012-executable-framework-and-artifact-taxonomy.md
resolved-by: null
---

# ISSUE-0053 — Is a Registry authoritative or derived?

## Statement

Three `Active` ADRs say different things about the same artifacts.

**`ADR-0031`** — "A Registry is an **authoritative** index of semantic entities."

**`ADR-0016`** — governance documents are authoritative and machine manifests are
**generated projections**; the rule "applies to every other index that restates
content held elsewhere: they are projections, not sources."

**`ADR-0012`** — "wherever possible, manifests are **validated or partially
generated** from repository inspection rather than relying exclusively on manual
maintenance."

`MANIFEST.yaml` and `KNOWLEDGE-MANIFEST.yaml` are registries under `ADR-0031`
and manifests under `ADR-0013`. `BUILD-STATE.yaml` is explicitly a projection.

## Why it matters

All three manifests are M2 deliverables, and the artifact kind determines
everything about how they are built: whether they are hand-authored and accepted,
generated and never edited, or hand-authored and machine-validated.

Getting this wrong means either building a generator for something that should
be authored, or hand-maintaining something that should be generated — the debt
already registered in `ISSUE-0037`.

It is marked `blocking` because it cannot be deferred past the first manifest.

## The reconciliation that probably works

A Registry holds facts **no specification holds** — identity, location,
ownership, status, version. It does not *restate* content held elsewhere, so
`ADR-0016`'s rule about restating indexes does not apply to it.

`governance/issues/index.md` restates issue front matter, so it is a projection.
A registry of state machines records that a machine exists, who owns it and
where its specification lives — facts that exist nowhere else until the registry
asserts them.

Under that reading: **registries are authoritative; indexes that restate are
projections**; and `ADR-0012`'s "validated or partially generated" means
*validated* for registries — a check that every referenced specification exists,
not generation of the registry itself.

This is coherent, and it is not what any of the three ADRs actually says.

## Open sub-questions

- Is `MANIFEST.yaml` authoritative, then? `ADR-0012` implied partial generation.
- Is `BUILD-STATE.yaml` a registry at all, or purely a projection? It records
  status, which the reconciliation above treats as registry content.
- Can one artifact be part authoritative and part generated? The artifact
  taxonomy assigns exactly one kind per artifact.

That last question is the hard one, and the taxonomy currently says no.

## Resolution criteria

An ADR assigning an artifact kind to each of the three manifests and to
registries in general, and stating how `ADR-0016`'s projection rule and
`ADR-0031`'s authoritative-index claim coexist.
