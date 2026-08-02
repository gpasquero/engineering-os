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
| **`model/metamodel/`** | **7 of 22 Layer A entities specified**; inventory reclassified into five categories |
| `LICENSE` | Apache-2.0, canonical text (`ADR-0063`) |
| Repository architecture, documentation system, session protocol | Accepted |
| Roadmap | Six-deliverable build sequence, B1–B6 |
| ADRs | 64 — 56 accepted, 8 superseded |
| Issues | 73 — **1 open, 50 resolved, 22 deferred as debt** |
| Acceptance Records | 17 |
| Session journal | 22 entries |
| Frozen provenance | `imports/`, `sources/` |

### Metamodel progress

| Specified | Remaining |
|---|---|
| Artifact · ArtifactRevision · Concept · Capability · DimensionSpecification · Dimension · DimensionAssignment | RegistrySpecification · StateMachineSpecification · StateMachine · Policy · Workflow · Skill · EngineeringGate · AcceptanceRecord · ADR · Issue · KnowledgePackage · Principle · Vocabulary · Manifest · ValidationRule |

Four concepts were **relocated** out of Layer A as compiler architecture —
Compiler, Projection, RegistryProjection, ValidationResult. One was **rejected**:
`Validation` unqualified, which conflated three things. One is **deferred**:
`Ontology`, pending B2.

## What does not exist

No executable code. No OWL. No Canonical Knowledge Model. No compiler. No
manifests. No policies. Nothing in `shared/`, `skills/`, `workflows/`,
`model-spec/`, `schemas/`, `validation/`, `tests/`, `adapters/` or `docs/`.

## Blocking

**Nothing blocks B1.**

One issue is open, and it is not architectural:

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Five hand-maintained projections — operational debt that B5 discharges |

## Architectural debt

**22 deferred issues.** Reopened when implementation requires them, not on a
schedule.

`ISSUE-0007` was deferred as debt in `SESSION-0021` and **resolved one session
later**, because writing `ArtifactRevision` turned an abstract question about
versioning into a blank field. The deferral was correct and short-lived — which
is the pattern `ADR-0062` predicts.

Nearest to the surface now:

- **`ISSUE-0073`** — "runtime" names both a compiler artifact kind and
  target-system telemetry. Both will appear in the metamodel.
- **`ISSUE-0063`** — the minimum serialized classification set. `DimensionAssignment`
  already had to record it as debt.
- **`ISSUE-0018`** — the inherited evidence model has never been adopted, and
  `Concept` references `Evidence` as an entity that does not exist.

## Debt discovered while building

Four entities are referenced by specifications and absent from the inventory:

| Referenced entity | Referenced by |
|---|---|
| **BoundedContext** | `Concept`, `Capability` — two independent references |
| **Invariant** | `Capability` |
| **Actor** | `Capability` |
| **Evidence** | `Concept` |

`BoundedContext` is referenced twice from independent specifications, which is
the signal it belongs in the next batch.

## Acceptance status

`ACCEPT-0001` (trust root) through `ACCEPT-0017`, covering `SESSION-0006`
through `SESSION-0021`.

**`ADR-0063`, `ADR-0064`, `LICENSE`, the inventory reclassification and the
seven entity specifications are `Under Review`**, not `Active`.

## Next action

**Continue B1.** Next batch in dependency order: `BoundedContext` first — it is
referenced by two existing specifications — then `RegistrySpecification`,
`StateMachineSpecification` and `StateMachine`.

Do not open architectural questions unless they block. Record and continue.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
