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
| **`model/metamodel/`** | **19 of 27 Layer A entities specified.** Both families present; the operational family is complete |
| **`model/metamodel/ontology/`** | OWL skeleton at 0.2.0 — **433 triples, 30 classes, 45 object properties**, parses clean |
| `LICENSE` | Apache-2.0, canonical text (`ADR-0063`) |
| Repository architecture, documentation system, session protocol | Accepted |
| Roadmap | Six-deliverable build sequence, B1–B6 |
| ADRs | 67 — 59 accepted, 8 superseded |
| Issues | 74 — **1 open, 50 resolved, 23 deferred as debt** |
| Acceptance Records | 19 |
| Session journal | 24 entries |
| Frozen provenance | `imports/`, `sources/` |

### Metamodel progress

| Family | Specified | Remaining |
|---|---|---|
| **Descriptive** | BoundedContext · Artifact · Concept · Capability · RelationshipType · Invariant · Evidence · Actor · ArtifactRevision · DimensionSpecification · Dimension · DimensionAssignment | StateMachineSpecification · StateMachine · Vocabulary · Principle · KnowledgePackage |
| **Operational** | **complete** — Policy · Workflow · Skill · EngineeringGate · AcceptanceRecord · ADR · Issue | — |
| **Unassigned** | none | RegistrySpecification · Manifest · ValidationRule |

**Every entity specification now answers one question before acceptance**
(`ADR-0067`): *what new semantic relationship does this entity introduce that
cannot already be expressed?* If the answer is "none", the entity is probably
redundant.

Four concepts were **relocated** out of Layer A as compiler architecture. One was
**rejected**: `Validation` unqualified. One is **deferred**: `Ontology`, pending
B2. One was **withdrawn one session after acceptance**: `Relationship`, replaced
by `RelationshipType` (`ADR-0066`).

## What does not exist

No executable code. No Canonical Knowledge Model. No compiler. No manifests. No
policy instances. Nothing in `shared/`, `skills/`, `workflows/`, `model-spec/`,
`schemas/`, `validation/`, `tests/`, `adapters/` or `docs/`.

The OWL skeleton is **hand-written, not compiled**.

## Blocking

**Nothing blocks B1.**

One issue is open, and it is not architectural:

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections — operational debt that B5 discharges. The OWL skeleton is the sixth |

## Scheduled

| Work | Trigger |
|---|---|
| **`ISSUE-0074` — metamodel simplification review** | ~75% of Layer A specified, i.e. about 20 of 27. **One entity away.** First candidate: `Dimension` / `DimensionSpecification` |

## Architectural debt

**23 deferred issues.** Reopened when implementation requires them, not on a
schedule.

Nearest to the surface:

- **`ISSUE-0074`** — the simplification review, one entity from its trigger.
- **`ISSUE-0073`** — surfaced twice in one session, in `Evidence` (runtime
  observation ranked most direct while Operational Knowledge sits outside the
  model) and in `Workflow` (Workflow Execution is unmodelled). Stepped over both
  times.
- **`ISSUE-0048`** — `ADR.corrects` is now specified as a relationship, and the
  six existing corrections still live only in a hand-maintained table.

## Debt discovered while building

**Recorded in each specification's `Debt` section, and in
`model/metamodel/ontology/FINDINGS.md` for what the OWL exposed** — eight
findings across two checkpoints.

Open, none blocking:

| Question | Where |
|---|---|
| `RelationshipType` cannot express **order**, and `Workflow.sequences` needs it | `FINDINGS.md` #7 |
| `EngineeringGate.holds` and `.produces` point at *question* and *outcome*, neither an entity | `FINDINGS.md` #8 |
| `Evidence.supports` has no range; no `Assertion` entity exists | `FINDINGS.md` #4 |
| `DimensionAssignment.hasValue` has a per-dimension range plain OWL cannot express | `FINDINGS.md` #6 |
| Nothing enforces that an acceptance reviewer differs from the author | `acceptance-record.md` |
| Nothing detects that a deferred issue's trigger has been met | `issue.md` |
| The framework declares none of its own BoundedContexts, Actors or RelationshipTypes | `bounded-context.md`, `actor.md`, `relationship-type.md` |
| Whether Markdown or OWL is authoritative once the compiler exists | `FINDINGS.md` |

## Acceptance status

`ACCEPT-0001` (trust root) through `ACCEPT-0019`, covering `SESSION-0006`
through `SESSION-0023`.

**`ADR-0066`, `ADR-0067`, `ISSUE-0074`, `RelationshipType`, the seven operational
specifications and the 0.2.0 ontology are `Under Review`**, not `Active`.

## Next action

**Continue B1.** Five descriptive entities remain — `StateMachineSpecification`,
`StateMachine`, `Vocabulary`, `Principle`, `KnowledgePackage` — plus the three
unassigned.

**`StateMachineSpecification` / `StateMachine` should be written next**, because
they have the same Specification/Instance shape as `Dimension` /
`DimensionSpecification`. Writing them is what makes the simplification review
answerable: if the pair has the same problem, the pattern is in question
everywhere; if it does not, `Dimension` is the anomaly.

Do not open architectural questions unless they block. Record and continue.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
