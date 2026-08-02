---
id: ISSUE-INDEX
title: Issue Index
status: current
created: 2026-08-02
updated: 2026-08-02
related: [ISSUE-0037]
---

# Issue Index

**74 recorded · 1 open · 50 resolved · 23 deferred.** Highest allocated ID:
`ISSUE-0074`.

> **Hand-maintained projection.** Under `ADR-0016` this is a projection of issue
> front matter, which is authoritative. No generator exists yet (`ISSUE-0036`),
> so it is maintained by hand as declared transitional debt — registered in
> `ISSUE-0037`. **These counts drifted once already**, in `SESSION-0004`; they
> are now computed from the files before each rewrite. The issue files win in
> any disagreement.

## Open

One issue is open.

| ID | Title | Why open |
|---|---|---|
| [0037](ISSUE-0037-hand-maintained-projections-are-debt.md) | Hand-maintained projections | Operational debt; B5 discharges it |

## Architectural debt

**22 issues deferred under `ADR-0062`.** Each is a real question that does not
block the next deliverable. They are reopened when implementation requires them,
not on a schedule.

| ID | Title | Reopen at |
|---|---|---|
| [0073](ISSUE-0073-operational-knowledge-versus-evidence-hierarchy.md) | "runtime" names two things; Operational Knowledge versus the evidence hierarchy | **B1** — surfaced in `Evidence` and `Workflow`; stepped over, not resolved |
| [0074](ISSUE-0074-metamodel-simplification-review.md) | Metamodel simplification review — identify entity pairs that can merge | **B1** — triggers at ~20 of 27 entities |
| — | *`ISSUE-0007` was deferred here and resolved one session later by `ADR-0064`, because building `ArtifactRevision` turned it into a blank field* | — |
| [0072](ISSUE-0072-how-artifacts-declare-principles.md) | How an artifact declares the Principles it establishes | B1–B3 |
| [0063](ISSUE-0063-minimum-serialized-classifications.md) | Minimum serialized classification set | B3 |
| [0049](ISSUE-0049-state-machine-specification-location.md) | Where state machine specifications live | B1 |
| [0048](ISSUE-0048-no-mechanism-for-correcting-an-active-adr.md) | No correction mechanism for an `Active` ADR | B3 |
| [0018](ISSUE-0018-assertion-statuses-duplicated.md) | Assertion status vocabulary defined twice | B2 |
| [0019](ISSUE-0019-evidence-record-defaults-diverge.md) | Two minimum evidence records disagree | B2 |
| [0013](ISSUE-0013-three-conflicting-impact-analysis-templates.md) | Three conflicting impact-analysis templates | M5 |
| [0014](ISSUE-0014-model-changes-directory-missing.md) | `model/changes/` absent from the canonical tree | M5 |
| [0015](ISSUE-0015-path-resolution-ambiguity.md) | Skill-relative versus target-relative paths | M4 |
| [0027](ISSUE-0027-inherited-decisions-lack-context.md) | Ten inherited decisions have no rationale | B2 (OWL) |
| [0010](ISSUE-0010-definition-of-done-missing.md) | Definition of Done never stated | M3 |
| [0020](ISSUE-0020-three-conflicting-autonomy-policies.md) | Three incompatible autonomy policies | M3 |
| [0021](ISSUE-0021-write-scope-conflict-on-composition.md) | Write scope conflicts on composition | M3 |
| [0008](ISSUE-0008-greenfield-scope-undefined.md) | Whether greenfield is in scope | M4 |
| [0017](ISSUE-0017-phase-models-do-not-reconcile.md) | Phase models versus the skill catalogue | M4 |
| [0025](ISSUE-0025-skill-decomposition-is-a-name-list.md) | Skill decomposition is a name list | M4 |
| [0002](ISSUE-0002-composition-primitive-undefined.md) | The composition primitive | M8 |
| [0016](ISSUE-0016-three-change-type-taxonomies.md) | Three change-type taxonomies | M8 |
| [0006](ISSUE-0006-scenario-testing-method-undefined.md) | How to test a prompt-based methodology | M10 |
| [0001](ISSUE-0001-runtime-target-undefined.md) | The agent runtime target | M12 |
| [0036](ISSUE-0036-reference-implementation-language.md) | Reference implementation language | **B5** |

## Resolved

| ID | Title | Resolved by |
|---|---|---|
| [0003](ISSUE-0003-manifest-purpose-undefined.md) | Purpose and schema of `MANIFEST.yaml` | `ADR-0009` → `ADR-0013` |
| [0004](ISSUE-0004-model-tree-location-undefined.md) | Location of the Layer B model tree | `ADR-0010` |
| [0005](ISSUE-0005-executable-code-in-repository.md) | Whether the repository ships executable code | `ADR-0012` |
| [0009](ISSUE-0009-human-in-the-loop-undefined.md) | Human-in-the-loop authority — answered as acceptance | `ADR-0018` → `ADR-0020` |
| [0012](ISSUE-0012-skill-term-overloaded.md) | The term "skill" is overloaded | `governance/glossary.md` |
| [0022](ISSUE-0022-bootstrap-versus-product-identity.md) | Bootstrap package versus product | `ADR-0001` |
| [0023](ISSUE-0023-reading-order-omitted-vision.md) | Reading order omitted the vision | `ADR-0002` |
| [0024](ISSUE-0024-shared-directory-undifferentiated.md) | `shared/` was undifferentiated | `ADR-0008` |
| [0026](ISSUE-0026-os-and-prototype-share-identity.md) | A prototype claims to be the entire OS | `governance/glossary.md` |
| [0028](ISSUE-0028-issue-index-drifts.md) | The issue index is maintained by hand | `ADR-0016` |
| [0029](ISSUE-0029-knowledge-package-format-undefined.md) | Knowledge Package format | `ADR-0019` |
| [0030](ISSUE-0030-manifest-serves-two-audiences.md) | Manifest audiences — answered as three manifests | `ADR-0013` |
| [0032](ISSUE-0032-implementation-language-and-toolchain.md) | Implementation language and toolchain | `ADR-0017` |
| [0033](ISSUE-0033-determinism-boundary.md) | Determinism boundary | `ADR-0015` → `ADR-0020` |
| [0034](ISSUE-0034-canonical-model-versus-model-directory.md) | `model/` — authoritative input or compiled output | `ADR-0014` |
| [0035](ISSUE-0035-build-state-manifest-overlaps-governance.md) | `BUILD-STATE.yaml` duplicates `governance/` | `ADR-0016` |
| [0038](ISSUE-0038-authoritative-names-two-things.md) | `authoritative` named two things | `ADR-0020` |
| [0039](ISSUE-0039-governance-policy-mechanism-missing.md) | Governance policy mechanism | `ADR-0023` |
| [0040](ISSUE-0040-existing-corpus-was-self-certified.md) | Existing corpus was self-certified | `ADR-0022` → `ACCEPT-0001` |
| [0041](ISSUE-0041-acceptance-record-undefined.md) | Acceptance record undefined | `ADR-0021` |
| [0042](ISSUE-0042-acceptance-record-regress.md) | Acceptance Record regress | `ADR-0024` |
| [0043](ISSUE-0043-document-status-vocabularies-overlap-lifecycle.md) | Status vocabularies overlap the lifecycle | `ADR-0025` |
| [0044](ISSUE-0044-artifact-versus-revision-lifecycle-naming.md) | Artifact versus revision lifecycle naming | `ADR-0026` |
| [0045](ISSUE-0045-state-machine-inventory-not-fixed.md) | State machine inventory not fixed | `ADR-0027` |
| [0046](ISSUE-0046-modeling-guidelines-have-no-home.md) | Modeling guidelines have no home | `ADR-0029` |
| [0047](ISSUE-0047-state-machine-registry-location.md) | State Machine Registry location | `ADR-0028` |
| [0050](ISSUE-0050-policy-is-overloaded.md) | "policy" named three artifact kinds | `ADR-0030` |
| [0051](ISSUE-0051-process-policy-overlaps-workflows.md) | `ProcessPolicy` versus Workflow | `ADR-0033` |
| [0052](ISSUE-0052-knowledge-explorer-undefined.md) | Knowledge Explorer undefined | `ADR-0034` |
| [0053](ISSUE-0053-are-registries-authoritative-or-derived.md) | Registry authoritative or derived | `ADR-0032` |
| [0054](ISSUE-0054-metamodel-undefined.md) | The Engineering OS metamodel was undefined | `ADR-0035` |
| [0031](ISSUE-0031-engineering-os-self-model-scope.md) | Engineering OS self-model scope | `ADR-0037` |
| [0055](ISSUE-0055-metamodel-location-and-distribution.md) | Where the Metamodel lives | `ADR-0037` |
| [0056](ISSUE-0056-existing-artifacts-have-no-layer.md) | Methodology artifacts had no layer | `ADR-0039` |
| [0057](ISSUE-0057-dimension-set-is-not-fixed.md) | The dimension set was not fixed | `ADR-0041` |
| [0058](ISSUE-0058-how-artifacts-declare-classification.md) | How artifacts declare classification | `ADR-0042` |
| [0059](ISSUE-0059-dimension-independence-and-overlaps.md) | Dimension independence versus relationships | `ADR-0044` |
| [0060](ISSUE-0060-where-dimension-assignments-are-authored.md) | Where assignments are authored | `ADR-0045` |
| [0061](ISSUE-0061-level-and-layer-are-confusable.md) | "Level" and "Layer" confusable | `ADR-0046` |
| [0062](ISSUE-0062-four-dimensions-still-undefined.md) | Four dimensions undefined | `ADR-0048` |
| [0064](ISSUE-0064-representation-versus-semantic-layer.md) | Representation versus Semantic Layer | `ADR-0049` |
| [0065](ISSUE-0065-initial-dimensions-not-evaluated.md) | Dimension candidates not evaluated | `ADR-0051` |
| [0066](ISSUE-0066-registry-specification-in-the-hierarchy.md) | Registry Specification in the hierarchy | `ADR-0052` |
| [0067](ISSUE-0067-dimension-review-artifact-type.md) | Dimension Review artifact type | `ADR-0054` |
| [0068](ISSUE-0068-compiler-phase-question-conflicts-with-separation.md) | Compiler-phase question versus separation | `ADR-0055` |
| [0069](ISSUE-0069-level-and-process-reused.md) | "Level" and "Process" reused | `ADR-0057` |
| [0070](ISSUE-0070-are-principles-a-first-class-artifact-type.md) | Are Principles an artifact type? | `ADR-0058` |
| [0071](ISSUE-0071-how-discovered-knowledge-is-produced.md) | How discovered knowledge is produced | `ADR-0060` |
| [0011](ISSUE-0011-audience-licence-distribution-undefined.md) | Licence and audience | `ADR-0063` |
| [0007](ISSUE-0007-versioning-granularity-undefined.md) | Artifact and revision identity | `ADR-0064` |
