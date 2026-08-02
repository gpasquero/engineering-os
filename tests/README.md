---
id: TESTS
title: Compiler Test Projects
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0062, ADR-0072, ADR-0073]
---

# Compiler Test Projects

**Knowledge repositories are executable test fixtures.**

Each project under `projects/` is a minimal repository exercising one
architectural feature, and declares in `expected.md` what the compiler must do
with it.

```sh
python3 tools/test.py           # every project
python3 tools/test.py acceptance
```

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
| `unregistered-predicate` | `ADR-0071` is enforced | **fail** |
| `unknown-entity-type` | the metamodel constrains which types may exist | **fail** |
| `dangling-reference` | every relationship target resolves | **fail** |
| `duplicate-id` | node identity is unique | **fail** |

## Negative fixtures are the point

Four projects **must fail**, and they carry more weight than the six that pass.

A compiler that accepts everything also passes every positive test. The negative
fixtures are what proves the metamodel is an **executable contract** (`ADR-0072`)
rather than a description, and each names the decision it defends: if
`unregistered-predicate` ever compiles, `ADR-0071` has become decoration.

## What each expectation declares

```yaml
outcome: pass | fail
expected-nodes:      exact node count
expected-edges:      exact edge count
expected-categories: relationship categories that must appear
expected-errors:     substrings that must appear in the failure
```

Counts are declared, not inferred from what the compiler produced. **That
distinction found a defect on the first run**: `relationship-taxonomy` claimed to
exercise all four categories and had no `semantic` edge, because `has-position`
is a datatype property rather than an edge. A suite that recorded actual output
as expected output would have enshrined the gap.

## Determinism is checked, not assumed

Every passing project is compiled **twice** and the two Canonical Knowledge
Models compared. `ADR-0073` requires each feature to declare a determinism
guarantee; this is where the guarantee is tested rather than trusted.

## Coverage

Across the suite: 11 structural, 9 behavioral, 6 semantic and 4 traceability
edges. Every core relationship category is exercised.

## What is not covered

No project exercises `Vocabulary`, `Principle`, `KnowledgePackage`, `Registry`,
`Manifest` or `ValidationRule` — the six unspecified entities. **The gap is the
map**: those are precisely the entities the compiler cannot yet need, which is
the test `ADR-0075` applies to whether they are needed at all.
