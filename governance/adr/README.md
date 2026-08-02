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

> **This corpus is history, not specification** (`ADR-0029`). ADRs explain *why*
> a rule exists; the rule that must be followed lives in a Policy under
> `shared/policies/`. Agents consume policies; humans read ADRs for rationale.

**Highest allocated ID: `ADR-0050`.** IDs are sequential and never reused.

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
- **`ADR-0026`** — the lifecycle belongs to a Revision; an Artifact is an
  identity with no lifecycle of its own.
- **`ADR-0027`** — state machines are registered, not enumerated.
- **`ADR-0029`** — ADRs explain *why*; Policies define the rule. Agents consume
  policies, humans read ADRs. **Read this before treating any ADR as a
  specification.**
- **`ADR-0031`** — the **Registry Pattern**. A registry indexes; specifications
  live separately. Evaluate every extensible concept against it.
- **`ADR-0032`** — a Registry **Specification** is authoritative; a Registry
  **Projection** is derived. Read with `ADR-0031`.
- **`ADR-0035`** — the **Engineering OS Metamodel**: the ontology of the
  framework itself, and its semantic backbone. **Position every new concept in
  it before introducing a new artifact type.**
- **`ADR-0036`** — the Canonical Knowledge Model is a graph **conforming to the
  Metamodel**. The Metamodel is the contract between authoring and compilation.
- **`ADR-0037`** — the **four-layer semantic architecture**. Every artifact
  belongs to exactly one of A (metamodel), B (repository knowledge model),
  C (canonical model), D (projections).
- **`ADR-0038`** — **four questions** every new artifact type must answer before
  acceptance.
- **`ADR-0039`** — layers classify **artifacts, not directories**. Governance
  and infrastructure are cross-cutting, not layers.
- **`ADR-0040`** — **Architectural Dimensions**. Artifacts are classified along
  multiple independent axes; the metamodel models them explicitly.
- **`ADR-0042`** — artifacts are classified by **Dimension Assignments**, not by
  embedded values.
- **`ADR-0043`** — **three Abstraction Levels**: Metamodel, Model,
  Classification. Read with `ADR-0037`; levels are not layers.
- **`ADR-0045`** — **front matter is interchange syntax**, not the semantic
  model.
- **`ADR-0047`** — **three representations of knowledge**, with the compiler
  responsible for semantic equivalence across them.
- **`ADR-0049`** — **dimensions are a scarce architectural resource**. Five
  conditions; creating one requires an ADR.
- **`ADR-0050`** — the **`Definition → Instance → Assignment → Projection`**
  hierarchy. Evaluate every extensible concept against it.
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
| [ADR-0014](ADR-0014-three-tier-knowledge-model.md) | Knowledge compiler over a three-tier knowledge model | **superseded by ADR-0037** | ISSUE-0034 |
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
| [ADR-0026](ADR-0026-artifact-revision-lifecycle.md) | **The lifecycle belongs to a Revision** | accepted | ISSUE-0044 |
| [ADR-0027](ADR-0027-state-machine-registration-model.md) | **State machines are registered, not enumerated** | accepted | ISSUE-0045 |
| [ADR-0028](ADR-0028-state-machine-registry-lives-in-knowledge-manifest.md) | The State Machine Registry is a section of `KNOWLEDGE-MANIFEST.yaml` | accepted | ISSUE-0047 |
| [ADR-0029](ADR-0029-modeling-policy-is-a-first-class-artifact-type.md) | **Modeling Policy is a first-class artifact type** | accepted | ISSUE-0046 |
| [ADR-0030](ADR-0030-normative-artifact-taxonomy.md) | **A taxonomy for normative artifacts** | accepted | ISSUE-0050 |
| [ADR-0031](ADR-0031-registry-pattern.md) | **Registry Pattern** | accepted | — |
| [ADR-0032](ADR-0032-registry-specification-versus-registry-projection.md) | **Registry Specification versus Registry Projection** | accepted | ISSUE-0053 |
| [ADR-0033](ADR-0033-process-policy-governs-workflow.md) | A `ProcessPolicy` governs a Workflow | accepted | ISSUE-0051 |
| [ADR-0034](ADR-0034-knowledge-explorer-is-a-per-repository-projection.md) | The Knowledge Explorer is a per-repository projection | accepted | ISSUE-0052 |
| [ADR-0035](ADR-0035-engineering-os-metamodel.md) | **The Engineering OS Metamodel** | accepted | ISSUE-0054 |
| [ADR-0036](ADR-0036-canonical-model-conforms-to-the-metamodel.md) | **The Canonical Knowledge Model conforms to the Metamodel** | accepted | — |
| [ADR-0037](ADR-0037-four-layer-semantic-architecture.md) | **The four-layer semantic architecture** | accepted | ISSUE-0031, ISSUE-0055 |
| [ADR-0038](ADR-0038-four-questions-for-every-new-artifact-type.md) | **Four questions for every new artifact type** | accepted | — |
| [ADR-0039](ADR-0039-layers-classify-artifacts-not-directories.md) | **Layers classify artifacts, not directories** | accepted | ISSUE-0056 |
| [ADR-0040](ADR-0040-architectural-dimensions.md) | **Architectural Dimensions** | accepted | — |
| [ADR-0041](ADR-0041-dimensions-are-registered-first-class-entities.md) | Dimensions are registered first-class entities | accepted | ISSUE-0057 |
| [ADR-0042](ADR-0042-dimension-assignments.md) | **Dimension Assignments** | accepted | ISSUE-0058 |
| [ADR-0043](ADR-0043-three-semantic-levels.md) | **Three semantic levels** | accepted | — |
| [ADR-0044](ADR-0044-independence-is-not-isolation.md) | Independence is not isolation | accepted | ISSUE-0059 |
| [ADR-0045](ADR-0045-human-representation-and-front-matter-as-interchange-syntax.md) | **Front matter is interchange syntax** | accepted | ISSUE-0060 |
| [ADR-0046](ADR-0046-abstraction-level-and-semantic-layer.md) | Abstraction Level and Semantic Layer | accepted | ISSUE-0061 |
| [ADR-0047](ADR-0047-three-representations-of-knowledge.md) | **Three representations of knowledge** | accepted | — |
| [ADR-0048](ADR-0048-dimension-specification-is-a-metamodel-entity.md) | `DimensionSpecification` is a metamodel entity | accepted | ISSUE-0062 |
| [ADR-0049](ADR-0049-dimensions-are-a-scarce-architectural-resource.md) | **Dimensions are a scarce architectural resource** | accepted | ISSUE-0064 |
| [ADR-0050](ADR-0050-definition-instance-assignment-projection.md) | **Definition → Instance → Assignment → Projection** | accepted | — |

## Supersessions

| Superseded | By | What changed |
|---|---|---|
| `ADR-0006` | `ADR-0010` | The two-layer distinction and `model-spec/` survive; the claim that this repository never contains a live `model/` does not. |
| `ADR-0009` | `ADR-0013` | Nothing was wrong. The identity claim survives in full; only the scope of `MANIFEST.yaml` narrows as concerns redistribute across three manifests. |
| `ADR-0011` | `ADR-0014` | The compiler principle survives entirely. What is added is the three-tier distinction that made `model/`'s status unambiguous. |
| `ADR-0015` | `ADR-0018` | The determinism principle survives. What changes is the boundary marker: a commit no longer confers authoritative status — acceptance does. |
| `ADR-0018` | `ADR-0020` | The acceptance decision survives in full. What changes is the lifecycle vocabulary: the state `Authoritative` is renamed `Active`, and the lifecycle applies to a revision rather than an artifact. |
| `ADR-0014` | `ADR-0037` | The knowledge-compiler principle and all three tiers survive, renamed layers B, C and D. What is added is Layer A, the Metamodel, above them. |

Superseded ADRs are retained as the record of what was believed before. Read the
superseding ADR for the current rule.

The acceptance chain `ADR-0015` → `ADR-0018` → `ADR-0020` is three deep in two
sessions. That depth is honest evidence that this area is still settling, not a
defect in the mechanism.

## Corrections

Distinct from supersession: the ADR's decision stands, but a detail within it is
wrong. There is no front-matter mechanism for this — `ISSUE-0048`.

| Corrected | By | What |
|---|---|---|
| `ADR-0025` | `ADR-0026` | Examples only. `ArtifactLifecycle` should read `ArtifactRevisionLifecycle`. The state-machine rule is untouched and remains `Active`. |
| `ADR-0010` | `ADR-0037` | Layer terminology only. `ADR-0010` used "Layer A" for the methodology; Layer A is now the Metamodel. Its decision — knowledge is repository-local, environments federate — is untouched and remains `Active`. |
| `ADR-0041` | `ADR-0048` | The field list. Eight fields become ten: `value domain` becomes `value model`, `authoritative specification` is dropped, and assignment semantics, serialization strategy and validation rules are added. The registration decision is untouched and remains `Active`. |
| `ADR-0037` | `ADR-0039` | The universality claim. "Every artifact belongs to exactly one layer" should read: every *semantic* artifact does; cross-cutting artifacts belong to none. The four layers are untouched and remain `Active`. |
| `ADR-0031` | `ADR-0032` | The opening definition. "A Registry is an authoritative index" should read: a Registry *Specification* is authoritative; a Registry *Projection* is the derived index. The pattern is untouched and remains `Active`. |

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
