---
id: ADR-0039
title: Semantic layers classify artifacts, not directories; governance and infrastructure are cross-cutting
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0056]
related: [ADR-0037, ADR-0038, ADR-0040, ISSUE-0048, ISSUE-0057, ISSUE-0058]
---

# ADR-0039 — Layers classify artifacts, not directories

## Context

`ADR-0037` established four semantic layers and stated that **every artifact
belongs to exactly one layer**. `ADR-0038` made "which layer owns it?" the first
mandatory question for any new artifact type.

`ISSUE-0056` recorded that `shared/`, `skills/`, `workflows/`, `templates/`,
`schemas/` and `governance/` had no layer, so the rule was failed by the corpus
on the day it was written. It offered four candidate readings, all of which
forced those directories into the semantic architecture somehow.

All four were wrong, because the question was.

## Decision

**The problem comes from assigning layers to directories.**

> **Layers do not own directories. Layers own semantic artifacts.**

A directory may legitimately contain artifacts belonging to multiple layers.

- **The repository layout is an implementation concern.**
- **The semantic layer is an architectural concern.**

**Therefore the compiler must classify artifacts, not folders.**

```text
model/metamodel/      → Layer A
model/domain/         → Layer B
generated/canonical/  → Layer C
site/                 → Layer D
```

### Governance is orthogonal

`governance/` contains artifacts that are **orthogonal to the semantic layers**.
ADRs, Issues, Acceptance Records and Sessions are **governance artifacts**: they
are inputs to the Engineering OS *process*, not part of the semantic model of a
target domain.

**Governance belongs to no semantic layer.**

The same applies to `tests/`, `scripts/`, `tooling/`, `ci/` and editor
configuration. These support the Engineering OS process but are not part of the
semantic knowledge stack.

### Two kinds of thing

**Semantic Layers** — A (Metamodel), B (Repository Knowledge Model),
C (Canonical Knowledge Model), D (Derived Projections).

**Cross-Cutting Infrastructure** — Governance, Tooling, Automation, Validation,
Testing, CI/CD.

**These dimensions intersect the semantic layers but are not themselves layers.**

This resolves the ambiguity **without forcing unrelated artifacts into the
semantic architecture**.

## Correction to ADR-0037

`ADR-0037`'s four layers stand entirely. Its universality claim — "every
artifact in Engineering OS belongs to exactly one layer" — is corrected to:
**every *semantic* artifact belongs to exactly one layer; cross-cutting
artifacts belong to none.**

This is the **fourth** correction to an `Active` ADR, still visible only in prose
and the ADR index (`ISSUE-0048`).

## Clarification to ADR-0038

`ADR-0038`'s question 1 remains mandatory, and **`None (Not Applicable)` is a
valid answer** for cross-cutting artifacts. An artifact whose layer is genuinely
undetermined is still a rejection; one that is genuinely orthogonal is not.

The negative consequence `ADR-0038` recorded — that the project could not answer
question 1 for its own artifacts — is discharged.

## Alternatives considered

The four readings recorded in `ISSUE-0056`:

**The methodology artifacts are Layer B instances.** Rejected. It conflates
*instantiating a metamodel entity* with *being domain knowledge*. A concrete
skill does instantiate the `Skill` entity, but that makes it an instance of the
language, not a description of some repository's domain.

**Layer A broadly construed as "what Engineering OS ships".** Rejected: it
dissolves the precision `ADR-0037` had just gained, returning Layer A to the
vague "the methodology" meaning it was redefined away from.

**A fifth layer for the methodology.** Rejected: infrastructure is not a
semantic layer, because it does not compile into anything. Adding it would make
"layer" mean two different things — the failure this project has hit five times.

**Governance outside the layers.** Accepted, and **generalized**: not only
governance, but all cross-cutting infrastructure.

## Consequences

### Positive

- **The ambiguity is resolved without distorting the architecture.** No artifact
  is forced into a semantic layer it does not belong to.
- **Repository layout is decoupled from architecture.** Directories can be
  reorganized without changing what anything means — which is what makes the
  layout an implementation decision rather than a commitment.
- `ADR-0038`'s first question becomes answerable for every artifact in the
  repository.
- The compiler's job is sharpened: it classifies artifacts, so classification
  must travel with the artifact rather than being inferred from its path.

### Negative

- **The directory contracts in `repository-architecture.md` are now
  implementation guidance, not architecture.** That document is the most-read
  structural artifact in the project, and its organising principle has just been
  demoted. It must say so explicitly or it will keep being read as normative.
- **The compiler must be told each artifact's classification.** Path-based
  inference is no longer sufficient, so classification has to be declared —
  in front matter, in a registry, or both. `ISSUE-0058`.
- **The cross-cutting list is examples, not a closed set.** Governance, Tooling,
  Automation, Validation, Testing, CI/CD — nothing says whether more exist or
  how one is added. `ISSUE-0057`.

### Neutral

- No artifact changes location. Only what its location means.

## Compliance

No artifact's semantic layer is inferred from its directory. Every semantic
artifact declares exactly one layer; every cross-cutting artifact declares
`None`. No document states that a directory *is* a layer.
