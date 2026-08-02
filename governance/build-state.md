---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: B1
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**B1 — Engineering OS Metamodel. In progress.**

Advancing under `ADR-0062`: **architecture through implementation.**

## The pipeline runs

```sh
python3 tools/compile.py examples/tiny
```

```text
[metamodel] 20 entity types, 67 registered predicates
[discover]  13 authoring sources
[parse]     13 nodes
[resolve]   OK — 16 edges, all types and predicates valid
[emit]      canonical-knowledge-model.json, model.ttl, graph.md, explorer.html
```

**The metamodel is load-bearing.** Phase 3 reads `model/metamodel/` and rejects
a model that violates it — verified by breaking the example three ways and
confirming all three are caught.

## What exists

| Area | State |
|---|---|
| **`examples/tiny/`** | **First end-to-end pipeline.** 13 nodes → Canonical Knowledge Model, OWL, graph, HTML explorer |
| **`tools/compile.py`** | The Knowledge Compiler — discover, parse, resolve, emit |
| **`tools/generate-metamodel-views.py`** | Three generated graph views |
| **`model/metamodel/`** | **20 of 26 Layer A entities specified.** Simplification review complete |
| **`model/metamodel/relationship-vocabulary.md`** | 18 core types + inverses; **every predicate has a registered parent** |
| `model/metamodel/ontology/` | OWL 0.4.0 — **660 triples, 31 classes, 73 object properties** |
| `LICENSE` | Apache-2.0 (`ADR-0063`) |
| ADRs | 71 — 63 accepted, 8 superseded |
| Issues | 74 — **1 open, 51 resolved, 22 deferred as debt** |
| Acceptance Records | 21 |
| Session journal | 26 entries |

### Metamodel progress

| Family | Specified | Remaining |
|---|---|---|
| **Descriptive** | BoundedContext · Artifact · ArtifactRevision · Concept · Capability · RelationshipType · Invariant · Evidence · Actor · Dimension · DimensionAssignment · StateMachineSpecification | Vocabulary · Principle · KnowledgePackage |
| **Operational** | Policy · Workflow · WorkflowStep · Skill · EngineeringGate · AcceptanceRecord · ADR · Issue | — |
| **Unassigned** | none | Registry · Manifest · ValidationRule |

**26 confirmed entities, down from 28, with no expressible statement lost.**
`StateMachine` removed and `DimensionSpecification` merged — in **opposite
directions**, decided by independent existence rather than structural similarity
(`ADR-0070`).

## What does not exist

No manifests. No policy instances. No `Principle` extraction. No lifecycle
enforcement, no dimension assignment, no acceptance checking in the compiler.
Nothing in `shared/`, `skills/`, `workflows/`, `schemas/`, `validation/`,
`tests/`, `adapters/` or `docs/`.

The metamodel OWL is hand-written. The views, the CKM and its four projections
are generated.

## Blocking

**Nothing blocks B1.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. **Substantially discharged**: `views/` and all `examples/tiny/build/` output are generated; the four governance indexes are not |

## Architectural debt

**22 deferred issues.**

- **`ISSUE-0073`** — Operational Knowledge. `ADR-0070` now draws the boundary
  from a new direction: a Specification whose instances live outside the
  repository is exactly where Engineering OS stops.
- **`ISSUE-0063`** — minimum serialized classification set. The compiler assigns
  no dimensions at all.
- **`ISSUE-0048`** — `ADR.corrects` specified; six corrections still in a
  hand-maintained table.

## Debt discovered while building

| Question | Where |
|---|---|
| Eighteen core relationship types is a seed; some will prove unused | `relationship-vocabulary.md` |
| Four mappings are strained — `produces`, `guarded-by`, `has-position`, `requires` | `relationship-vocabulary.md` |
| No core type declares a cardinality or constraint convention | `relationship-vocabulary.md` |
| Nothing enforces that a new predicate declares a parent — a natural first `ValidationRule` | `ADR-0071` |
| **Transitions** and **conditions** both point at things that are not entities; both extrinsic by `ADR-0068`'s test | `FINDINGS.md` |
| `Evidence.supports` has no range; no `Assertion` entity | `FINDINGS.md` #4 |
| Nothing enforces that an acceptance reviewer differs from the author | `acceptance-record.md` |
| The framework declares none of its own BoundedContexts, Actors or RelationshipTypes | four specifications |

## Acceptance status

`ACCEPT-0001` (trust root) through `ACCEPT-0021`, covering `SESSION-0006`
through `SESSION-0025`.

**`ADR-0069`, `ADR-0070`, `ADR-0071`, the normalization, the relationship
vocabulary, `tools/compile.py` and `examples/tiny/` are `Under Review`.**

## Next action

**Extend the pipeline before extending the metamodel.**

Six entities remain — `Vocabulary`, `Principle`, `KnowledgePackage`, `Registry`,
`Manifest`, `ValidationRule` — and four of them are things the compiler needs
rather than things the model lacks. `ValidationRule` in particular now has a
concrete first instance: *every predicate must declare a registered parent*.

Specifying them against a running pipeline will be sharper than specifying them
against prose, which is the whole argument of `ADR-0062`.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
