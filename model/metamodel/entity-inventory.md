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

Every candidate entity, classified by whether it belongs to the Layer A semantic
metamodel at all.

**The early inventory conflated four different things.** Appearing in
`ADR-0035`'s list is not evidence that a concept is a semantic entity.

## Confirmed Layer A entities

Belong to the semantic metamodel. **Grouped by family** (`ADR-0065`), and within
the descriptive family the semantic backbone is listed first, since almost every
remaining entity derives from it.

### Descriptive — the semantic backbone

| # | Entity | Purpose | Established by | Spec |
|---|---|---|---|---|
| 1 | **BoundedContext** | A boundary within which a set of terms has one consistent meaning | `ADR-0035` | [✓](entities/bounded-context.md) |
| 2 | **Artifact** | A stable logical identity that owns many revisions | `ADR-0026`, `ADR-0064` | [✓](entities/artifact.md) |
| 3 | **Concept** | A named unit of meaning within a bounded context | `ADR-0035` | [✓](entities/concept.md) |
| 4 | **Capability** | Something a system can do, externally visible | `ADR-0035` | [✓](entities/capability.md) |
| 5 | **Relationship** | A named, typed, directed association between two semantic entities | `ADR-0042` | [✓](entities/relationship.md) |
| 6 | **Invariant** | A condition that must hold, stated independently of what enforces it | `ADR-0035` | [✓](entities/invariant.md) |
| 7 | **Evidence** | A reference to an observable fact, cited in support of an assertion | `ADR-0060`, `ADR-0061` | [✓](entities/evidence.md) |
| 8 | **Actor** | A role that interacts with a system's Capabilities | `ADR-0035` | [✓](entities/actor.md) |

### Descriptive — remaining

| # | Entity | Purpose | Established by | Spec |
|---|---|---|---|---|
| 9 | **ArtifactRevision** | An immutable revision of an Artifact; the unit accepted and the unit carrying lifecycle state | `ADR-0026`, `ADR-0064` | [✓](entities/artifact-revision.md) |
| 10 | **DimensionSpecification** | Defines one independent axis of classification | `ADR-0048` | [✓](entities/dimension-specification.md) |
| 11 | **Dimension** | An instance of a DimensionSpecification | `ADR-0041` | [✓](entities/dimension.md) |
| 12 | **DimensionAssignment** | The relationship classifying an artifact along a dimension | `ADR-0042` | [✓](entities/dimension-assignment.md) |
| 13 | **StateMachineSpecification** | Defines a state machine and its vocabulary | `ADR-0027` | — |
| 14 | **StateMachine** | An instance of a StateMachineSpecification | `ADR-0025` | — |
| 15 | **Vocabulary** | A closed enumeration with exactly one definition | `ADR-0008` | — |
| 16 | **Principle** | A semantic relationship emerging from accepted knowledge. **Not an artifact** | `ADR-0058` | — |
| 17 | **KnowledgePackage** | A published interface between repositories | `ADR-0019` | — |

### Operational

**None specified.** The entire family is unbuilt.

| # | Entity | Purpose | Established by | Spec |
|---|---|---|---|---|
| 18 | **Policy** | A normative rule motivated by Principles — `GovernancePolicy`, `ModelingPolicy`, `ProcessPolicy` | `ADR-0029`, `ADR-0030` | — |
| 19 | **Workflow** | Executable orchestration; sequences skills, holds no methodology | `ADR-0033` | — |
| 20 | **Skill** | A composable unit of methodology with an explicit contract | `governance/glossary.md` | — |
| 21 | **EngineeringGate** | An Engineering Process reviewing the introduction or modification of a concept | `ADR-0054` | — |
| 22 | **AcceptanceRecord** | The act conferring `Active` status on a revision | `ADR-0021` | — |
| 23 | **ADR** | A recorded architectural decision | `ADR-0002` | — |
| 24 | **Issue** | A recorded unknown | `ADR-0003` | — |

### Family unassigned

Recorded by `ADR-0065` as not classifying cleanly. Each describes structure
*about* engineering rather than about a domain. **Assigned when specified.**

| # | Entity | Purpose | Established by | Spec |
|---|---|---|---|---|
| 25 | **RegistrySpecification** | Defines a registry: identity, membership rules, extension rules | `ADR-0032` | — |
| 26 | **Manifest** | A root declaration of composition, status or semantics | `ADR-0013` | — |
| 27 | **ValidationRule** | A constraint a semantic model must satisfy | `ADR-0048` | — |

**12 of 27 specified — and all twelve are descriptive.**

## Compiler-architecture concepts

**Not Layer A semantic entities.** They belong to the compiler architecture, and
`ADR-0053` states that the metamodel contains no compiler concepts. They appear
in `ADR-0035`'s early inventory and are relocated here.

| Concept | Belongs to |
|---|---|
| **Compiler** | Compiler architecture (`ADR-0014`, `ADR-0061`) |
| **Projection** | Compilation hierarchy (`ADR-0052`) |
| **RegistryProjection** | Compilation hierarchy (`ADR-0032`) |
| **ValidationResult** | Compiler or operational output |

They will be specified where the Knowledge Compiler specification is written
(B4), not here.

## Tooling concepts

Neither semantic nor compiler-architectural. Implementation.

| Concept | Note |
|---|---|
| **Validator** | The program executing ValidationRules. Language-dependent (`ADR-0017`, `ISSUE-0036`) |

## Undefined candidates

Named somewhere, with no definition and no decision establishing them as
entities.

| Candidate | Status |
|---|---|
| **Ontology** | Named in `ADR-0035`. OWL is an inherited decision awaiting an ADR (`ISSUE-0027`). Deferred to B2, where the first OWL ontologies define what one is |

## Rejected candidates

| Candidate | Why rejected |
|---|---|
| **Validation** *(unqualified)* | Conflated three distinct things: `ValidationRule` (semantic), `ValidationResult` (compiler or operational), `Validator` (tooling). Removed from the inventory rather than defined |

## Recorded while building

**`Validation` is the eighth term this project has had to split**, after
"skill", "authoritative", "state", "policy", "registry", "layer/level" and
"level/process". It was caught before being specified rather than after —
`ADR-0057`'s Naming Qualification doing its work.

**Three entities relocated, one rejected, one deferred.** Of `ADR-0035`'s twenty
named entities, five do not belong in the Layer A metamodel. That inventory was
written before `ADR-0053` drew the semantic/compiler boundary.

**Five entities were added by writing specifications, not by analysis.**
`BoundedContext`, `Invariant`, `Evidence` and `Actor` were referenced by
specifications before they existed in any list. `Relationship` was absent from
every list this project produced in twenty-two sessions and is arguably the most
fundamental entity in the metamodel — the graph is the model, and nothing named
the edge.

**All twelve specified entities are descriptive.** The operational family is
entirely unbuilt, which is not an accident: the descriptive entities are what
`ADR-0065` calls the language, and the operational ones describe activity
performed *on* things described in that language. The build order followed the
dependency without anyone stating it, and `ADR-0065` is that statement arriving
after the fact.
