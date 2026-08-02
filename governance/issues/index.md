---
id: ISSUE-INDEX
title: Issue Index
status: current
created: 2026-08-02
updated: 2026-08-02
related: [ISSUE-0028]
---

# Issue Index

**31 recorded · 24 open · 7 resolved.** Highest allocated ID: `ISSUE-0031`.

> This index is maintained by hand and can drift from the issue files, which are
> authoritative. Tracked as `ISSUE-0028`; a generator or validation rule is
> planned for M9.

## Blocking — the named milestone cannot start

| ID | Title | Blocks |
|---|---|---|
| [0002](ISSUE-0002-composition-primitive-undefined.md) | How a workflow invokes a skill is undefined | M8 |
| [0006](ISSUE-0006-scenario-testing-method-undefined.md) | How a prompt-based methodology is tested is undefined | M10 |

**M2 is unblocked.** `ISSUE-0003` and `ISSUE-0004` were resolved by `ADR-0009`
and `ADR-0010`.

## Open, by milestone

### M2 — Foundational contracts and manifest

| ID | Title | Type | Severity |
|---|---|---|---|
| [0005](ISSUE-0005-executable-code-in-repository.md) | Whether the repository ships executable code | question | high |
| [0007](ISSUE-0007-versioning-granularity-undefined.md) | Versioning granularity and compatibility policy | question | high |
| [0013](ISSUE-0013-three-conflicting-impact-analysis-templates.md) | Three conflicting impact-analysis templates | inconsistency | high |
| [0014](ISSUE-0014-model-changes-directory-missing.md) | `model/changes/` absent from the canonical tree | inconsistency | high |
| [0015](ISSUE-0015-path-resolution-ambiguity.md) | Skill-relative and target-relative paths not distinguished | inconsistency | high |
| [0030](ISSUE-0030-manifest-serves-two-audiences.md) | `MANIFEST.yaml` serves two audiences | question | high |
| [0011](ISSUE-0011-audience-licence-distribution-undefined.md) | Repository is public with no licence | question | high |
| [0018](ISSUE-0018-assertion-statuses-duplicated.md) | Assertion status vocabulary defined twice | inconsistency | medium |
| [0019](ISSUE-0019-evidence-record-defaults-diverge.md) | Two minimum evidence records disagree | inconsistency | low |

### M3 — Shared policies

| ID | Title | Type | Severity |
|---|---|---|---|
| [0009](ISSUE-0009-human-in-the-loop-undefined.md) | Human-in-the-loop authority and gate approval | question | high |
| [0010](ISSUE-0010-definition-of-done-missing.md) | Definition of Done asserted but never stated | gap | high |
| [0020](ISSUE-0020-three-conflicting-autonomy-policies.md) | Three incompatible autonomy policies | inconsistency | high |
| [0021](ISSUE-0021-write-scope-conflict-on-composition.md) | Write scope conflicts on composition | risk | high |
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

### M9 — Schemas and validation

| ID | Title | Type | Severity |
|---|---|---|---|
| [0028](ISSUE-0028-issue-index-drifts.md) | The issue index is maintained by hand | risk | low |

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

### M13 — Knowledge Packages and federation

| ID | Title | Type | Severity |
|---|---|---|---|
| [0029](ISSUE-0029-knowledge-package-format-undefined.md) | Knowledge Package format and federation protocol | question | high |

## Resolved

| ID | Title | Resolved by |
|---|---|---|
| [0003](ISSUE-0003-manifest-purpose-undefined.md) | Purpose and schema of `MANIFEST.yaml` | `ADR-0009` |
| [0004](ISSUE-0004-model-tree-location-undefined.md) | Location of the Layer B model tree | `ADR-0010` |
| [0012](ISSUE-0012-skill-term-overloaded.md) | The term "skill" is overloaded | `governance/glossary.md` |
| [0022](ISSUE-0022-bootstrap-versus-product-identity.md) | Bootstrap package versus product | `ADR-0001` |
| [0023](ISSUE-0023-reading-order-omitted-vision.md) | Reading order omitted the vision | `ADR-0002` |
| [0024](ISSUE-0024-shared-directory-undifferentiated.md) | `shared/` was undifferentiated | `ADR-0008` |
| [0026](ISSUE-0026-os-and-prototype-share-identity.md) | A prototype claims to be the entire OS | `governance/glossary.md` |
