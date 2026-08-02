---
id: METAMODEL-INVENTORY
title: Metamodel Entity Inventory
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
artifact-kind: authoritative
---

# Metamodel Entity Inventory

Every entity Engineering OS defines, with the decision that established it and
whether its specification exists.

**25 entities. 2 specified.**

## Artifact and lifecycle

| Entity | Purpose | Established by | Spec |
|---|---|---|---|
| **ArtifactType** | The kind of a thing the framework manages | `ADR-0035` | — |
| **ArtifactRevision** | An identifiable version of an artifact; the unit that is accepted and that carries lifecycle state | `ADR-0026` | [✓](entities/artifact-revision.md) |
| **AcceptanceRecord** | The act conferring `Active` status on a revision | `ADR-0021` | — |
| **ADR** | A recorded architectural decision, with context, alternatives and consequences | `ADR-0002` | — |
| **Issue** | A recorded unknown: question, inconsistency, gap or risk | `ADR-0003` | — |

## Classification

| Entity | Purpose | Established by | Spec |
|---|---|---|---|
| **DimensionSpecification** | Defines one independent axis of classification | `ADR-0048` | [✓](entities/dimension-specification.md) |
| **Dimension** | An instance of a DimensionSpecification | `ADR-0041` | — |
| **DimensionAssignment** | The relationship classifying an artifact along a dimension | `ADR-0042` | — |
| **Vocabulary** | A closed enumeration with exactly one definition | `ADR-0008` | — |
| **StateMachine** | The owner of a state vocabulary; every state belongs to exactly one | `ADR-0025` | — |

## Registry

| Entity | Purpose | Established by | Spec |
|---|---|---|---|
| **RegistrySpecification** | Defines a registry: identity, membership rules, extension rules | `ADR-0032` | — |
| **Manifest** | A root declaration of a project's composition, status or semantics | `ADR-0013` | — |

## Normative

| Entity | Purpose | Established by | Spec |
|---|---|---|---|
| **Principle** | A semantic relationship emerging from accepted architectural knowledge. **Not an artifact** | `ADR-0058` | — |
| **Policy** | A normative rule motivated by one or more Principles | `ADR-0029`, `ADR-0030` | — |
| **Gate** | An Engineering Process reviewing the introduction or modification of a concept | `ADR-0054` | — |

## Engineering

| Entity | Purpose | Established by | Spec |
|---|---|---|---|
| **Skill** | A composable unit of methodology with an explicit contract | `governance/glossary.md` | — |
| **Workflow** | Executable orchestration; sequences skills, holds no methodology | `ADR-0033` | — |
| **Capability** | *Named in `ADR-0035`; no definition exists in this project yet* | `ADR-0035` | — |

## Semantic

| Entity | Purpose | Established by | Spec |
|---|---|---|---|
| **Ontology** | *Named in `ADR-0035`; no definition exists in this project yet* | `ADR-0035` | — |
| **Concept** | *Named in `ADR-0035`; no definition exists in this project yet* | `ADR-0035` | — |
| **KnowledgePackage** | A published interface between repositories; a stable projection of the canonical model | `ADR-0019` | — |

## Compilation boundary

These four are **named in `ADR-0035` but belong to the compiler architecture**,
not the semantic one (`ADR-0053`). Whether they appear in the metamodel at all
is unresolved and deferred as architectural debt.

| Entity | Purpose | Established by |
|---|---|---|
| **Compiler** | The deterministic semantic compiler | `ADR-0014`, `ADR-0061` |
| **Projection** | A derived artifact produced from the canonical model | `ADR-0052` |
| **RegistryProjection** | The generated index of registered entities | `ADR-0032` |
| **Validation** | *Named in `ADR-0035`; no definition exists yet* | `ADR-0035` |

## Recorded while building

Three entities — **Capability**, **Concept**, **Validation** — were named in
`ADR-0035`'s inventory and have never been defined anywhere in the project.
`SESSION-0017` recorded this: writing the metamodel is design work, not
transcription.

**Ontology** is named but undefined here while OWL is an inherited decision
awaiting an ADR (`ISSUE-0027`).

The four compilation-boundary entities create a tension with `ADR-0053`, which
says the metamodel contains no compiler concepts. Recorded as debt rather than
resolved, per `ADR-0062`.
