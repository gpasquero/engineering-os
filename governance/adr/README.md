---
id: ADR-INDEX
title: Decision Index
status: current
created: 2026-08-02
updated: 2026-08-02
---

# Architecture Decision Records

A decision that is not recorded here will be re-litigated. Write the ADR in the
same session the decision is made.

**Highest allocated ID: `ADR-0013`.** IDs are sequential and never reused.

## Foundational

`ADR-0011` — **Engineering OS is a knowledge compiler.** It governs the design
of generators, validators, visualizers, plugins and every future extension
mechanism. Read it before designing anything that produces an artifact.

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
| [ADR-0011](ADR-0011-engineering-os-is-a-knowledge-compiler.md) | **Engineering OS is a knowledge compiler** | accepted | — |
| [ADR-0012](ADR-0012-executable-framework-and-artifact-taxonomy.md) | Executable framework with a typed artifact taxonomy | accepted | ISSUE-0005 |
| [ADR-0013](ADR-0013-three-manifests-by-responsibility.md) | Three manifests separated by responsibility and lifecycle | accepted | ISSUE-0030 |

## Supersessions

**`ADR-0010` supersedes `ADR-0006`.** The two-layer distinction and `model-spec/`
survive; the claim that this repository never contains a live `model/` does not.

**`ADR-0013` supersedes `ADR-0009`.** The identity claim survives in full — a
manifest describes architecture and composition and is not a dependency lock
file. What changes is scope: fifteen concerns are redistributed across three
manifests with different lifecycles.

Superseded ADRs are retained as the record of what was believed before. Read the
superseding ADR for the current rule.

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
