---
id: ISSUE-INDEX
title: Issue Index
status: current
created: 2026-08-02
updated: 2026-08-02
related: [ISSUE-0037]
---

# Issue Index

**41 recorded · 24 open · 16 resolved · 1 deferred.** Highest allocated ID:
`ISSUE-0041`.

> **Hand-maintained projection.** Under `ADR-0016` this is a projection of issue
> front matter, which is authoritative. No generator exists yet
> (`ISSUE-0036`), so it is maintained by hand as declared transitional debt —
> registered in `ISSUE-0037`. **These counts drifted once already**, in
> `SESSION-0004`. The issue files win in any disagreement.

## Blocking — the named milestone cannot start

| ID | Title | Blocks |
|---|---|---|
| [0038](ISSUE-0038-authoritative-names-two-things.md) | `authoritative` names both a lifecycle state and an artifact kind | **M2** |
| [0040](ISSUE-0040-existing-corpus-was-self-certified.md) | The entire existing corpus was self-certified | **M2** |
| [0041](ISSUE-0041-acceptance-record-undefined.md) | The acceptance record is undefined | **M2** |
| [0002](ISSUE-0002-composition-primitive-undefined.md) | How a workflow invokes a skill is undefined | M8 |
| [0006](ISSUE-0006-scenario-testing-method-undefined.md) | How a prompt-based methodology is tested is undefined | M10 |

## Open, by milestone

### M2 — Foundational contracts, manifests and the compiler interface

| ID | Title | Type | Severity |
|---|---|---|---|
| [0038](ISSUE-0038-authoritative-names-two-things.md) | `authoritative` names two things | inconsistency | blocking |
| [0040](ISSUE-0040-existing-corpus-was-self-certified.md) | Existing corpus was self-certified | risk | blocking |
| [0041](ISSUE-0041-acceptance-record-undefined.md) | Acceptance record undefined | gap | blocking |
| [0007](ISSUE-0007-versioning-granularity-undefined.md) | Versioning granularity and compatibility policy | question | high |
| [0011](ISSUE-0011-audience-licence-distribution-undefined.md) | Repository is public with no licence | question | high |
| [0013](ISSUE-0013-three-conflicting-impact-analysis-templates.md) | Three conflicting impact-analysis templates | inconsistency | high |
| [0014](ISSUE-0014-model-changes-directory-missing.md) | `model/changes/` absent from the canonical tree | inconsistency | high |
| [0015](ISSUE-0015-path-resolution-ambiguity.md) | Skill-relative and target-relative paths not distinguished | inconsistency | high |
| [0018](ISSUE-0018-assertion-statuses-duplicated.md) | Assertion status vocabulary defined twice | inconsistency | medium |
| [0031](ISSUE-0031-engineering-os-self-model-scope.md) | Self-model scope; `KNOWLEDGE-MANIFEST` overlaps the glossary | gap | medium |
| [0019](ISSUE-0019-evidence-record-defaults-diverge.md) | Two minimum evidence records disagree | inconsistency | low |

### M3 — Shared policies

| ID | Title | Type | Severity |
|---|---|---|---|
| [0010](ISSUE-0010-definition-of-done-missing.md) | Definition of Done asserted but never stated | gap | high |
| [0020](ISSUE-0020-three-conflicting-autonomy-policies.md) | Three incompatible autonomy policies | inconsistency | high |
| [0021](ISSUE-0021-write-scope-conflict-on-composition.md) | Write scope conflicts on composition | risk | high |
| [0039](ISSUE-0039-governance-policy-mechanism-missing.md) | Governance policy mechanism does not exist | gap | high |
| [0027](ISSUE-0027-inherited-decisions-lack-context.md) | Ten inherited decisions have no rationale | gap | medium |

### M4 — Discovery skills

| ID | Title | Type | Severity |
|---|---|---|---|
| [0017](ISSUE-0017-phase-models-do-not-reconcile.md) | Phase models do not reconcile with the skill catalogue | inconsistency | high |
| [0008](ISSUE-0008-greenfield-scope-undefined.md) | Whether greenfield development is in scope | question | medium |
| [0025](ISSUE-0025-skill-decomposition-is-a-name-list.md) | Skill decomposition is only a list of names | gap | medium |

### M8 — Workflows

| ID | Title | Type | Severity |
|---|---|---|---|
| [0002](ISSUE-0002-composition-primitive-undefined.md) | The composition primitive is undefined | question | blocking |
| [0016](ISSUE-0016-three-change-type-taxonomies.md) | Three incompatible change-type taxonomies | inconsistency | high |

### M9 — Schemas, validation and the reference implementation

| ID | Title | Type | Severity |
|---|---|---|---|
| [0037](ISSUE-0037-hand-maintained-projections-are-debt.md) | Hand-maintained projections are transitional debt | risk | high |

### M10 — Scenario tests

| ID | Title | Type | Severity |
|---|---|---|---|
| [0006](ISSUE-0006-scenario-testing-method-undefined.md) | How to test a prompt-based methodology | question | blocking |

### M11 — Engineering OS self-model

| ID | Title | Type | Severity |
|---|---|---|---|
| [0031](ISSUE-0031-engineering-os-self-model-scope.md) | Scope of Engineering OS's own `model/` | gap | medium |

### M12 — Documentation, adapters and v1

| ID | Title | Type | Severity |
|---|---|---|---|
| [0001](ISSUE-0001-runtime-target-undefined.md) | The agent runtime target is undefined | question | high |
| [0011](ISSUE-0011-audience-licence-distribution-undefined.md) | Audience, licence and distribution model | question | high |

## Deferred

| ID | Title | Defers to |
|---|---|---|
| [0036](ISSUE-0036-reference-implementation-language.md) | Reference implementation language | M9 |

## Resolved

| ID | Title | Resolved by |
|---|---|---|
| [0003](ISSUE-0003-manifest-purpose-undefined.md) | Purpose and schema of `MANIFEST.yaml` | `ADR-0009` → `ADR-0013` |
| [0004](ISSUE-0004-model-tree-location-undefined.md) | Location of the Layer B model tree | `ADR-0010` |
| [0005](ISSUE-0005-executable-code-in-repository.md) | Whether the repository ships executable code | `ADR-0012` |
| [0009](ISSUE-0009-human-in-the-loop-undefined.md) | Human-in-the-loop authority — answered as acceptance | `ADR-0018` |
| [0012](ISSUE-0012-skill-term-overloaded.md) | The term "skill" is overloaded | `governance/glossary.md` |
| [0022](ISSUE-0022-bootstrap-versus-product-identity.md) | Bootstrap package versus product | `ADR-0001` |
| [0023](ISSUE-0023-reading-order-omitted-vision.md) | Reading order omitted the vision | `ADR-0002` |
| [0024](ISSUE-0024-shared-directory-undifferentiated.md) | `shared/` was undifferentiated | `ADR-0008` |
| [0026](ISSUE-0026-os-and-prototype-share-identity.md) | A prototype claims to be the entire OS | `governance/glossary.md` |
| [0028](ISSUE-0028-issue-index-drifts.md) | The issue index is maintained by hand | `ADR-0016` |
| [0029](ISSUE-0029-knowledge-package-format-undefined.md) | Knowledge Package format | `ADR-0019` |
| [0030](ISSUE-0030-manifest-serves-two-audiences.md) | Manifest audiences — answered as three manifests | `ADR-0013` |
| [0032](ISSUE-0032-implementation-language-and-toolchain.md) | Implementation language and toolchain | `ADR-0017` |
| [0033](ISSUE-0033-determinism-boundary.md) | Determinism boundary | `ADR-0015` → `ADR-0018` |
| [0034](ISSUE-0034-canonical-model-versus-model-directory.md) | `model/` — authoritative input or compiled output | `ADR-0014` |
| [0035](ISSUE-0035-build-state-manifest-overlaps-governance.md) | `BUILD-STATE.yaml` duplicates `governance/` | `ADR-0016` |
