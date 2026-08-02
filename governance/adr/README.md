---
id: ADR-INDEX
title: Decision Index
status: current
created: 2026-08-02
updated: 2026-08-02
related: [ISSUE-0037]
---

# Architecture Decision Records

A decision that is not recorded here will be re-litigated. Write the ADR in the
same session the decision is made.

**Highest allocated ID: `ADR-0025`.** IDs are sequential and never reused.

> This index table is a hand-maintained projection of ADR front matter. It is
> listed in the transitional-debt register, `ISSUE-0037`.

## Foundational

Read these before designing anything that produces an artifact:

- **`ADR-0014`** — Engineering OS is a knowledge compiler over a three-tier
  knowledge model.
- **`ADR-0020`** — artifact taxonomy and revision lifecycle are independent;
  acceptance confers `Active` status.
- **`ADR-0023`** — governance is self-hosting but never self-certifying.
- **`ADR-0025`** — every state belongs to exactly one state machine. A modeling
  rule for the whole Engineering OS, not only for this repository.
- **`ADR-0017`** — reference architecture, not reference implementation.
- **`ADR-0019`** — Knowledge Packages are a published interface.

## Index

| ID | Title | Status | Resolves |
|---|---|---|---|
| [ADR-0001](ADR-0001-repository-is-persistent-memory.md) | The repository is the persistent memory of the project | accepted | ISSUE-0022 |
| [ADR-0002](ADR-0002-typed-documents-with-stable-ids.md) | Knowledge is recorded as typed documents with stable IDs | accepted | ISSUE-0023 |
| [ADR-0003](ADR-0003-in-repo-issue-tracking.md) | Open questions are tracked as in-repository Markdown issues | accepted | — |
| [ADR-0004](ADR-0004-governance-directory-as-memory-layer.md) | Persistent memory lives in `governance/` | accepted | — |
| [ADR-0005](ADR-0005-frozen-provenance-directories.md) | `imports/` and `sources/` are frozen provenance | accepted | — |
| [ADR-0006](ADR-0006-two-layer-architecture.md) | Separate the product layer from the model artifact layer | **superseded by ADR-0010** | — |
| [ADR-0007](ADR-0007-runtime-neutral-core-with-adapter-boundary.md) | Runtime-neutral core with an adapter boundary | accepted | — |
| [ADR-0008](ADR-0008-shared-layer-three-way-split.md) | Split `shared/` into contracts, policies and vocabularies | accepted | ISSUE-0024 |
| [ADR-0009](ADR-0009-manifest-is-the-root-composition-manifest.md) | `MANIFEST.yaml` is the root composition manifest | **superseded by ADR-0013** | ISSUE-0003 |
| [ADR-0010](ADR-0010-repository-local-knowledge-ownership.md) | Knowledge is repository-local; environments federate | accepted | ISSUE-0004 |
| [ADR-0011](ADR-0011-engineering-os-is-a-knowledge-compiler.md) | Engineering OS is a knowledge compiler | **superseded by ADR-0014** | — |
| [ADR-0012](ADR-0012-executable-framework-and-artifact-taxonomy.md) | Executable framework with a typed artifact taxonomy | accepted | ISSUE-0005 |
| [ADR-0013](ADR-0013-three-manifests-by-responsibility.md) | Three manifests separated by responsibility and lifecycle | accepted | ISSUE-0030 |
| [ADR-0014](ADR-0014-three-tier-knowledge-model.md) | **Knowledge compiler over a three-tier knowledge model** | accepted | ISSUE-0034 |
| [ADR-0015](ADR-0015-authoring-is-non-deterministic-compilation-is-deterministic.md) | Authoring is non-deterministic; compilation is deterministic | **superseded by ADR-0018** | ISSUE-0033 |
| [ADR-0016](ADR-0016-governance-is-authoritative-manifests-are-projections.md) | Governance is authoritative; manifests are projections | accepted | ISSUE-0028, ISSUE-0035 |
| [ADR-0017](ADR-0017-reference-architecture-not-reference-implementation.md) | **Reference architecture, not reference implementation** | accepted | ISSUE-0032 |
| [ADR-0018](ADR-0018-acceptance-confers-authoritative-status.md) | Acceptance confers authoritative status | **superseded by ADR-0020** | ISSUE-0009 |
| [ADR-0019](ADR-0019-knowledge-packages-are-a-published-interface.md) | **Knowledge Packages are a published interface** | accepted | ISSUE-0029 |
| [ADR-0020](ADR-0020-artifact-taxonomy-and-revision-lifecycle-are-independent.md) | **Artifact taxonomy and revision lifecycle are independent** | accepted | ISSUE-0038 |
| [ADR-0021](ADR-0021-acceptance-record-specification.md) | Acceptance Record specification | accepted | ISSUE-0041 |
| [ADR-0022](ADR-0022-bootstrap-acceptance-establishes-the-trust-root.md) | Bootstrap acceptance establishes the trust root | accepted | ISSUE-0040 |
| [ADR-0023](ADR-0023-governance-is-self-hosting-never-self-certifying.md) | **Governance is self-hosting but never self-certifying** | accepted | ISSUE-0039 |
| [ADR-0024](ADR-0024-acceptance-terminates-at-the-acceptance-record.md) | The acceptance process terminates at the Acceptance Record | accepted | ISSUE-0042 |
| [ADR-0025](ADR-0025-every-state-belongs-to-exactly-one-state-machine.md) | **Every state belongs to exactly one state machine** | accepted | ISSUE-0043 |

## Supersessions

| Superseded | By | What changed |
|---|---|---|
| `ADR-0006` | `ADR-0010` | The two-layer distinction and `model-spec/` survive; the claim that this repository never contains a live `model/` does not. |
| `ADR-0009` | `ADR-0013` | Nothing was wrong. The identity claim survives in full; only the scope of `MANIFEST.yaml` narrows as concerns redistribute across three manifests. |
| `ADR-0011` | `ADR-0014` | The compiler principle survives entirely. What is added is the three-tier distinction that made `model/`'s status unambiguous. |
| `ADR-0015` | `ADR-0018` | The determinism principle survives. What changes is the boundary marker: a commit no longer confers authoritative status — acceptance does. |
| `ADR-0018` | `ADR-0020` | The acceptance decision survives in full. What changes is the lifecycle vocabulary: the state `Authoritative` is renamed `Active`, and the lifecycle applies to a revision rather than an artifact. |

Superseded ADRs are retained as the record of what was believed before. Read the
superseding ADR for the current rule.

The acceptance chain `ADR-0015` → `ADR-0018` → `ADR-0020` is three deep in two
sessions. That depth is honest evidence that this area is still settling, not a
defect in the mechanism.

## Rules

- An **accepted** ADR is never edited. Supersede it with a new ADR and set
  `superseded-by` on the original and `supersedes` on the replacement.
- An ADR with no **Alternatives considered** section is a note, not a decision
  record.
- If an ADR resolves an issue, it lists the issue in `resolves`, and that issue
  names the ADR in `resolved-by`. Both directions are mandatory.
- Use `_template.md`.

## Pending

Ten pre-M1 decisions are accepted but undocumented. See
`governance/inherited-decisions.md` and `ISSUE-0027`.
