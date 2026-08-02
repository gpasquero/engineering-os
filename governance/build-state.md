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
| **`model/metamodel/`** | **12 of 27 Layer A entities specified** — the semantic backbone is complete |
| **`model/metamodel/ontology/`** | **First OWL skeleton.** 273 triples, 17 classes, parses clean |
| `LICENSE` | Apache-2.0, canonical text (`ADR-0063`) |
| Repository architecture, documentation system, session protocol | Accepted |
| Roadmap | Six-deliverable build sequence, B1–B6 |
| ADRs | 65 — 57 accepted, 8 superseded |
| Issues | 73 — **1 open, 50 resolved, 22 deferred as debt** |
| Acceptance Records | 18 |
| Session journal | 23 entries |
| Frozen provenance | `imports/`, `sources/` |

### Metamodel progress

Entities now declare a **family** (`ADR-0065`): descriptive entities describe
knowledge; operational entities describe engineering activity. They are not
peers.

| Family | Specified | Remaining |
|---|---|---|
| **Descriptive** | BoundedContext · Artifact · Concept · Capability · Relationship · Invariant · Evidence · Actor · ArtifactRevision · DimensionSpecification · Dimension · DimensionAssignment | StateMachineSpecification · StateMachine · Vocabulary · Principle · KnowledgePackage |
| **Operational** | **none** | Policy · Workflow · Skill · EngineeringGate · AcceptanceRecord · ADR · Issue |
| **Unassigned** | none | RegistrySpecification · Manifest · ValidationRule |

**All twelve specified entities are descriptive.** The operational family is
entirely unbuilt — which is the strongest evidence available that `ADR-0065`'s
split is real rather than imposed.

Four concepts were **relocated** out of Layer A as compiler architecture —
Compiler, Projection, RegistryProjection, ValidationResult. One was **rejected**:
`Validation` unqualified, which conflated three things. One is **deferred**:
`Ontology`, pending B2.

## What does not exist

No executable code. No Canonical Knowledge Model. No compiler. No manifests. No
policies. Nothing in `shared/`, `skills/`, `workflows/`, `model-spec/`,
`schemas/`, `validation/`, `tests/`, `adapters/` or `docs/`.

The OWL skeleton is **hand-written, not compiled**, and covers less than half the
metamodel.

## Blocking

**Nothing blocks B1.**

One issue is open, and it is not architectural:

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections — operational debt that B5 discharges. **The OWL skeleton is now the sixth.** |

## Architectural debt

**22 deferred issues.** Reopened when implementation requires them, not on a
schedule.

Nearest to the surface now:

- **`ISSUE-0018`** — the inherited evidence model. `Evidence` is now specified
  and reconstructs the prototypes' directness ranking without adopting their
  confidence scoring, status model or aggregation rules.
- **`ISSUE-0073`** — "runtime" names both a compiler artifact kind and
  target-system telemetry. `Evidence` ranks runtime observation as the *most
  direct* kind while `ADR-0061` places Operational Knowledge outside the model.
  **This contradiction has now surfaced**, as predicted, and does not block:
  a citation can reference an observation the model does not own.
- **`ISSUE-0063`** — the minimum serialized classification set. Now has a second
  witness: `DimensionAssignment.hasValue` has a per-dimension range that plain
  OWL cannot express.

## Debt discovered while building

**Recorded in each specification's `Debt` section, and in
`model/metamodel/ontology/FINDINGS.md` for what the OWL exposed.**

Open questions carried forward, none blocking:

| Question | Where |
|---|---|
| `Relationship` competes with OWL's own object-property mechanism for representing edges | `FINDINGS.md` #1 |
| `Dimension` may carry no data its specification does not already carry | `FINDINGS.md` #2 |
| `Evidence.supports` has no range; no `Assertion` entity exists | `FINDINGS.md` #4 |
| `Relationship.typedBy` points at nothing defined | `relationship.md`, `FINDINGS.md` #5 |
| The framework declares none of its own BoundedContexts or Actors, though it plainly has both | `bounded-context.md`, `actor.md` |
| Whether Markdown or OWL is authoritative once the compiler exists | `FINDINGS.md` |
| The ontology namespace is a documented placeholder | `FINDINGS.md` |

## Acceptance status

`ACCEPT-0001` (trust root) through `ACCEPT-0018`, covering `SESSION-0006`
through `SESSION-0022`.

**`ADR-0065`, the five new entity specifications, the family declarations, the
OWL skeleton and `FINDINGS.md` are `Under Review`**, not `Active`.

## Next action

**Continue B1 with the operational family**, which is where the metamodel is now
entirely blank: `Policy`, `Workflow`, `Skill`, `EngineeringGate`,
`AcceptanceRecord`, `ADR`, `Issue`.

`ADR-0065` predicts these will differ structurally from everything specified so
far — different ownership, different lifecycle, provenance about who acted.
Writing them is the test of whether the split holds.

Do not open architectural questions unless they block. Record and continue.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
