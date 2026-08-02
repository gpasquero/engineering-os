---
id: ADR-0013
title: Three manifests separated by responsibility and lifecycle
status: accepted
date: 2026-08-02
supersedes: ADR-0009
superseded-by: null
resolves: [ISSUE-0030]
related: [ADR-0011, ADR-0012, ISSUE-0031, ISSUE-0034, ISSUE-0035]
---

# ADR-0013 — Three manifests separated by responsibility and lifecycle

## Context

`ISSUE-0030` asked whether one manifest schema serves both this repository and
adopting repositories, or whether two are needed.

The answer is neither. The question had the wrong axis: the problem is not
*audience*, it is **responsibility and lifecycle**.

`ADR-0009` bundled fifteen concerns into a single `MANIFEST.yaml` and recorded
as a negative consequence the risk of it becoming "a god-file that accumulates
every unresolved concern". That risk is now addressed structurally rather than
by discipline.

## Decision

There are **three manifests**, each with a single responsibility and a distinct
lifecycle.

### `MANIFEST.yaml` — architectural manifest

Project composition, enabled modules, extension points, build pipelines,
artifact taxonomy, generators, plugins, repository capabilities.

**Lifecycle: stable.** Deliberately independent of day-to-day implementation
progress. It should change rarely.

### `BUILD-STATE.yaml` — implementation state

Milestones, implementation progress, blockers, active work, completed work,
pending work, references to the ADRs and issues affecting delivery.

**Lifecycle: continuous.** Expected to change constantly.

### `KNOWLEDGE-MANIFEST.yaml` — knowledge model manifest

Ontology modules, vocabularies, knowledge packages, graph modules, bounded
contexts, capabilities, invariants, state machines, glossary modules, semantic
dependencies.

**Lifecycle: per domain change.** Changes when the meaning of the system
changes.

### Root discoverability

`MANIFEST.yaml` remains the root machine entry point and **declares the other
two**. `ADR-0009`'s governing property — everything in the repository is
discoverable from `MANIFEST.yaml` — is preserved transitively rather than
abandoned.

> This last point is a derivation, not something stated in the answer to
> `ISSUE-0030`. If the intent was three independent roots with no single entry
> point, this clause needs correcting.

## What changes from ADR-0009

`ADR-0009` is superseded. Its identity claim survives in full: a manifest here
describes **architecture and composition**, is the equivalent of `package.json`
or `Cargo.toml` for Engineering OS composition, and is explicitly not a
dependency lock file, package-manager manifest or distribution descriptor.

What changes is the scope of `MANIFEST.yaml`. Its fifteen concerns are
redistributed: ontology modules move to `KNOWLEDGE-MANIFEST.yaml`; implementation
progress moves to `BUILD-STATE.yaml`; architecture, artifact taxonomy, pipelines,
generators, plugins and capabilities remain.

## Alternatives considered

**One schema with all sections optional.** Rejected: a schema permissive enough
to validate both a framework and an adopter validates almost nothing, and it
leaves architecture and daily progress churning in the same file.

**One schema with a declared project kind** (`framework` versus `adopter`).
Rejected, despite being the option `ISSUE-0030` judged most likely correct. It
solves the audience problem while leaving the lifecycle problem untouched — a
single file would still mix content that changes yearly with content that
changes hourly.

**Two schemas, one per audience.** Rejected for the same reason, plus it
duplicates every shared section.

The decisive argument for three is **rate of change**. Architecture changes
rarely, implementation state changes continuously, and semantics change when the
domain changes. Binding them into one file guarantees that the stable content is
churned by the volatile content, which is how a manifest becomes a source of
architectural drift rather than a defence against it.

## Consequences

### Positive

- Single responsibility per manifest; each can be validated against a schema
  that actually constrains it.
- `BUILD-STATE.yaml` churn never touches architectural declarations, so the
  history of `MANIFEST.yaml` stays reviewable.
- Under `ADR-0012`, each manifest can be independently validated or partially
  generated from repository inspection. `BUILD-STATE.yaml` in particular is
  largely derivable — milestones from the roadmap, blockers from issue front
  matter — which is the concrete route to closing `ISSUE-0028`.
- The audience question dissolves: an adopting repository has the same three
  manifests, with sections it does not use left empty.

### Negative

- **Three files must stay consistent with each other**, and cross-manifest
  references need rules that do not yet exist. Three single-responsibility files
  are better than one god-file, but they are not free.
- **`BUILD-STATE.yaml` overlaps `governance/` directly** — `build-state.md`,
  `issues/index.md` and `roadmap.md` already hold exactly this content. Which is
  authoritative and which is derived is unresolved and must be settled before
  either is built: `ISSUE-0035`.
- **`KNOWLEDGE-MANIFEST.yaml` overlaps `model/` and `governance/glossary.md`.**
  It lists "glossary modules" while the project's glossary currently lives in
  `governance/`. This compounds `ISSUE-0031`.
- It strains `ADR-0004`, which kept the root minimal so that memory lived in
  `governance/`. Three root manifests are YAML machine artifacts rather than
  memory documents, so the letter holds — but `BUILD-STATE.yaml` is memory by
  any honest reading, which is exactly what `ISSUE-0035` must resolve.

### Neutral

- Manifest versioning depends on `ISSUE-0007`.

## Compliance

No manifest contains content owned by another. Architectural declarations never
appear in `BUILD-STATE.yaml`; implementation progress never appears in
`MANIFEST.yaml`; semantic declarations appear only in
`KNOWLEDGE-MANIFEST.yaml`. A section that must be duplicated across manifests is
a signal that the responsibility split is wrong.
