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
| 5 | **RelationshipType** | Declares that a kind of association may exist: domain, range, cardinality, constraints, semantics | `ADR-0042`, `ADR-0066` | [✓](entities/relationship-type.md) |
| 6 | **Invariant** | A condition that must hold, stated independently of what enforces it | `ADR-0035` | [✓](entities/invariant.md) |
| 7 | **Evidence** | A reference to an observable fact, cited in support of an assertion | `ADR-0060`, `ADR-0061` | [✓](entities/evidence.md) |
| 8 | **Actor** | A role that interacts with a system's Capabilities | `ADR-0035` | [✓](entities/actor.md) |

### Descriptive — remaining

| # | Entity | Purpose | Established by | Spec |
|---|---|---|---|---|
| 9 | **ArtifactRevision** | An immutable revision of an Artifact; the unit accepted and the unit carrying lifecycle state | `ADR-0026`, `ADR-0064` | [✓](entities/artifact-revision.md) |
| 10 | **Dimension** | An independent axis of classification, holding the ten fields `ADR-0048` requires | `ADR-0041`, `ADR-0070` | [✓](entities/dimension.md) |
| 11 | **DimensionAssignment** | The relationship classifying an artifact along a dimension | `ADR-0042` | [✓](entities/dimension-assignment.md) |
| 12 | **StateMachineSpecification** | Defines a state machine: states, transitions, what it governs | `ADR-0027`, `ADR-0070` | [✓](entities/state-machine-specification.md) |
| 13 | **Vocabulary** | A closed enumeration with exactly one definition | `ADR-0008` | — |
| 14 | **Principle** | A semantic relationship emerging from accepted knowledge. **Not an artifact** | `ADR-0058` | — |
| 15 | **KnowledgePackage** | A published interface between repositories | `ADR-0019` | — |

### Operational

**Complete.** All seven specified, as the test of whether `ADR-0065`'s split is
real. It held — see `ontology/FINDINGS.md`.

| # | Entity | Purpose | Established by | Spec |
|---|---|---|---|---|
| 16 | **Policy** | A normative rule motivated by Principles — `GovernancePolicy`, `ModelingPolicy`, `ProcessPolicy` | `ADR-0029`, `ADR-0030` | [✓](entities/policy.md) |
| 17 | **Workflow** | Executable orchestration; sequences skills, holds no methodology | `ADR-0033` | [✓](entities/workflow.md) |
| 18 | **Skill** | A composable unit of methodology with an explicit contract | `ADR-0033` | [✓](entities/skill.md) |
| 19 | **EngineeringGate** | An Engineering Process reviewing the introduction or modification of a concept | `ADR-0054` | [✓](entities/engineering-gate.md) |
| 20 | **AcceptanceRecord** | The act conferring `Active` status on a revision | `ADR-0021` | [✓](entities/acceptance-record.md) |
| 21 | **ADR** | A recorded architectural decision | `ADR-0002` | [✓](entities/adr.md) |
| 22 | **Issue** | A recorded unknown | `ADR-0003` | [✓](entities/issue.md) |
| 23 | **WorkflowStep** | The reified association between a Workflow and a Skill, carrying its position | `ADR-0068` | [✓](entities/workflow-step.md) |

### Family unassigned

Recorded by `ADR-0065` as not classifying cleanly. Each describes structure
*about* engineering rather than about a domain. **Assigned when specified.**

| # | Entity | Purpose | Established by | Spec |
|---|---|---|---|---|
| 24 | **Registry** | Identity, membership rules, extension rules. **Not `RegistrySpecification`** — a registry has no independent existence (`ADR-0070`) | `ADR-0032`, `ADR-0070` | — |
| 25 | **Manifest** | A root declaration of composition, status or semantics | `ADR-0013` | — |
| 26 | **ValidationRule** | A constraint a semantic model must satisfy | `ADR-0048` | — |

**20 of 26 specified.** The simplification review is **complete** (`ISSUE-0074`,
resolved by `ADR-0070`).

The criterion was not structural similarity but **independent existence**: does a
Specification define something whose instances may exist outside Engineering OS?

| Outcome | Why |
|---|---|
| `StateMachine` **removed**, `StateMachineSpecification` kept | Instances exist — runtime executions, outside the repository. The redundant half was the phantom middle layer, not the Specification |
| `DimensionSpecification` **merged** into `Dimension` | No independent existence, so nothing is being specified *for* anything |
| `RegistrySpecification` **renamed** `Registry` | Same, decided before the entity was written |

**Two opposite directions**, which structural similarity could not have
distinguished. Two entities disappear and **no expressible statement is lost**
(`ADR-0069`).

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
specifications before they existed in any list. `RelationshipType` was absent from
every list this project produced in twenty-two sessions, and the meaning of the
metamodel is now converging on it — the graph is the model, and nothing named the
vocabulary of its edges.

**The build order followed the family boundary before anyone had named it.** The
first twelve entities specified were all descriptive; `ADR-0065` arrived after
the fact, which is a better outcome than inventing the distinction — the evidence
preceded the decision.

**Writing the operational family tested it, and it held.** All seven are owned by
the engineering process rather than by a BoundedContext, all seven carry
provenance about who acted, and two have lifecycles that are not
`ArtifactRevisionLifecycle` — `AcceptanceRecord` has none at all.

**The `Specification` suffix survived, and the pattern did not.** The conclusion
`SESSION-0025` was heading toward — that `Specification` is applied where no
distinction exists — would have deleted the one specification that is real and
kept the empty halves. The independence criterion inverted it.

**`Relationship` existed for exactly one session.** Specified in `SESSION-0023`,
replaced by `RelationshipType` in `SESSION-0024` because the OWL checkpoint showed
it competing with the mechanism it would compile to. It was the shortest-lived
artifact in the project, and the first withdrawn because building revealed the
error rather than because analysis predicted it.
