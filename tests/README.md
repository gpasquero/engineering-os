---
id: TESTS
title: Compiler Test Projects
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0062, ADR-0072, ADR-0073, ADR-0077, ADR-0078]
---

# Compiler Test Projects

**Knowledge repositories are executable test fixtures.**

Each project under `projects/` is a minimal repository exercising one
architectural feature, and declares in `expected.md` what the compiler must do
with it.

```sh
python3 tools/test.py            # every project
python3 tools/test.py acceptance # one
python3 tools/test.py --accept   # rewrite golden outputs from current behaviour
```

**Every fixture verifies six things**: the Canonical Knowledge Model, the OWL,
the Explorer, the graph, a deterministic rebuild, and the expected diagnostics.
Golden outputs live in `<project>/golden/`, so a change to any emitter surfaces
as a diff in every affected fixture.

**Every compiler change rebuilds every project.** A project that should compile
and does not, or that should fail and compiles, is a regression.

## The projects

| Project | Exercises | Outcome |
|---|---|---|
| `relationship-taxonomy` | all four relationship categories in one model | pass |
| `acceptance` | an act conferring `Active` status; the chain terminating at the record | pass |
| `workflow-ordering` | **the same Skill at two positions in one Workflow** | pass |
| `state-machine` | `StateMachineSpecification`, and the absence of `StateMachine` | pass |
| `dimensions` | classification as a relationship, not a property | pass |
| `policies` | `Policy` and `EngineeringGate` — normativity and conditional review | pass |
| `unregistered-predicate` | `VR-0002` — `ADR-0071` is enforced | **fail** |
| `unknown-entity-type` | `VR-0001` — the metamodel constrains which types may exist | **fail** |
| `dangling-reference` | `VR-0003` — every relationship target resolves | **fail** |
| `duplicate-id` | `VR-0004` — node identity is unique | **fail** |
| `self-reference` | `VR-0005` — no containment or revision edge to itself | **fail** |
| `missing-required-relationship` | `VR-0006` — a `WorkflowStep` must declare `executes` | **fail** |
| `malformed-yaml` | `ADR-0078` — structural errors surface at **Parsing**, not Resolution | **fail** |

## Negative fixtures are the point

Seven projects **must fail**, and they carry more weight than the six that pass.

A compiler that accepts everything also passes every positive test. The negative
fixtures are what proves the metamodel is an **executable contract** (`ADR-0072`)
rather than a description, and each names the rule or decision it defends: if
`unregistered-predicate` ever compiles, `VR-0002` has stopped firing and
`ADR-0071` has become decoration.

`malformed-yaml` is the one that proves the **phase boundary**. Its
`relationships` key is a string. Under the old regex parser that was silently an
empty list and the file compiled to a node with no edges — a structural defect
reinterpreted as a valid model (`ADR-0078`).

## What each expectation declares

```yaml
outcome: pass | fail
expected-nodes:      exact node count
expected-edges:      exact edge count
expected-categories: relationship categories that must appear
expected-errors:     substrings that must appear in the failure
expected-phase:      the phase a diagnostic must come from
expected-rule:       the ValidationRule id that must fire
```

`expected-phase` and `expected-rule` are what keep diagnostics honest: a fixture
declares not only *that* compilation fails but **where** and **why**.

Counts are declared, not inferred from what the compiler produced. **That
distinction found a defect on the first run**: `relationship-taxonomy` claimed to
exercise all four categories and had no `semantic` edge, because `has-position`
is a datatype property rather than an edge. A suite that recorded actual output
as expected output would have enshrined the gap.

## Determinism is checked, not assumed

Every passing project is compiled **twice** and the two Canonical Knowledge
Models compared. `ADR-0073` requires each feature to declare a determinism
guarantee; this is where the guarantee is tested rather than trusted.

## A rule caught a defect in a fixture that had passed for two sessions

`VR-0007` — *an `ArtifactRevision` must declare `revision-of`* — was written by
generalising `VR-0006`, not by inspecting any project. It immediately failed
`dimensions`, whose revision had declared no artifact since the fixture was
created.

**Declaring rules as data produced rules that writing conditionals had not.** A
table invites *what else belongs here?*; a function does not.

## Coverage

Every core relationship category is exercised, and every ValidationRule from
`VR-0001` to `VR-0006` has a fixture that makes it fire.

## What is not covered

No project exercises `Vocabulary`, `Registry`, `Manifest`, `Principle` or
`KnowledgePackage`. **The gap is the map** (`ADR-0075`).

**`VR-0007` has no fixture of its own** — it fires only where a project happens
to violate it, which is how it was found and is not the same as being tested.
