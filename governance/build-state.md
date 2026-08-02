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

Advancing under `ADR-0062`: **architecture through implementation.** If an
existing decision permits building, build. Stop only for a real contradiction.
New questions that do not block the next deliverable become architectural debt.

## What exists

| Area | State |
|---|---|
| **`model/metamodel/`** | **22 of 28 Layer A entities specified** — past the simplification review threshold |
| **`model/metamodel/ontology/`** | OWL skeleton at 0.3.0 — **496 triples, 33 classes, 52 object properties**, parses clean |
| **`model/metamodel/views/`** | **Three generated graph views.** The first mechanically produced projection in the repository |
| **`tools/`** | `generate-metamodel-views.py` — the first executable code in the repository |
| `LICENSE` | Apache-2.0, canonical text (`ADR-0063`) |
| Repository architecture, documentation system, session protocol | Accepted |
| Roadmap | Six-deliverable build sequence, B1–B6 |
| ADRs | 68 — 60 accepted, 8 superseded |
| Issues | 74 — **1 open, 50 resolved, 23 deferred as debt** |
| Acceptance Records | 20 |
| Session journal | 25 entries |
| Frozen provenance | `imports/`, `sources/` |

### Metamodel progress

| Family | Specified | Remaining |
|---|---|---|
| **Descriptive** | BoundedContext · Artifact · Concept · Capability · RelationshipType · Invariant · Evidence · Actor · ArtifactRevision · DimensionSpecification · Dimension · DimensionAssignment · StateMachineSpecification · StateMachine | Vocabulary · Principle · KnowledgePackage |
| **Operational** | Policy · Workflow · WorkflowStep · Skill · EngineeringGate · AcceptanceRecord · ADR · Issue | — |
| **Unassigned** | none | RegistrySpecification · Manifest · ValidationRule |

**Every specification answers the `ADR-0067` question** — what new semantic
relationship does this introduce that cannot already be expressed? **One entity
answered "none" and says so**: `StateMachine`.

## What does not exist

No Canonical Knowledge Model. No compiler. No manifests. No policy instances.
Nothing in `shared/`, `skills/`, `workflows/`, `model-spec/`, `schemas/`,
`validation/`, `tests/`, `adapters/` or `docs/`.

The OWL skeleton is **hand-written, not compiled**. The graph views **are**
generated.

## Blocking

**Nothing blocks B1.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections — operational debt. **Partly discharged**: `views/` is generated, the four indexes are not |

## Ready to perform

| Work | State |
|---|---|
| **`ISSUE-0074` — metamodel simplification review** | **Trigger met** (22 of 28) and the three graph views it is performed against exist. Two confirmed merge candidates, plus the `Specification` suffix as a general question and the `governs` collision |

## Architectural debt

**23 deferred issues.** Reopened when implementation requires them.

Nearest to the surface:

- **`ISSUE-0074`** — ready to perform, not performed.
- **`ISSUE-0073`** — surfaced a third time, in `Workflow`: Workflow Execution is
  unmodelled, and executions are where Operational Knowledge would enter.
- **`ISSUE-0048`** — `ADR.corrects` is specified; the six corrections still live
  only in a hand-maintained table.

## Debt discovered while building

**In each specification's `Debt` section, in `ontology/FINDINGS.md` for what the
OWL exposed, and in `views/README.md` for what the graphs showed.**

Missing semantic constructs — the class of finding that replaced missing
entities:

| Construct | Status |
|---|---|
| **Ordering** | **Resolved** (`ADR-0068`). Intrinsic or extrinsic; no new construct needed |
| **Transitions** | `declares-transitions` points at a non-entity. Extrinsic by `ADR-0068`'s test, so it should be reified like `WorkflowStep` |
| **Conditions** | `WorkflowStep.guarded-by` and Workflow branches both point at "condition", which has no representation |

Other open items, none blocking:

| Question | Where |
|---|---|
| The metamodel has **no reusable relationship vocabulary** — no relation used 3+ times in the ontology | `views/README.md` #3 |
| `governs` names three different relationships | `views/README.md` #4 |
| `Evidence.supports` has no range; no `Assertion` entity exists | `FINDINGS.md` #4 |
| Nothing enforces that an acceptance reviewer differs from the author | `acceptance-record.md` |
| Nothing detects that a deferred issue's trigger has been met | `issue.md` |
| The framework declares none of its own BoundedContexts, Actors, RelationshipTypes or state machines | four specifications |

## Acceptance status

`ACCEPT-0001` (trust root) through `ACCEPT-0020`, covering `SESSION-0006`
through `SESSION-0024`.

**`ADR-0068`, `StateMachineSpecification`, `StateMachine`, `WorkflowStep`, the
0.3.0 ontology, `tools/` and `views/` are `Under Review`**, not `Active`.

## Next action

**Perform `ISSUE-0074`** — the simplification review, against the graph views
rather than the specifications. The trigger is met and the inputs exist.

Then finish B1: `Vocabulary`, `Principle`, `KnowledgePackage`,
`RegistrySpecification`, `Manifest`, `ValidationRule`.

**`RegistrySpecification` should be written before the review concludes**, or the
review will decide the `Specification` suffix question on two data points when a
third is one specification away.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
