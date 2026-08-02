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

**Compiler evolution takes precedence over metamodel expansion** (`ADR-0075`).
Remaining entities are justified by compiler requirement, not by architectural
completeness.

## The product

**The Canonical Knowledge Model** (`ADR-0072`). OWL, the explorer, the graphs and
every register are projections of it. Nothing else is the deliverable.

```sh
python3 tools/compile.py --phases      # the phase contract
python3 tools/compile.py examples/tiny # compile a project
python3 tools/test.py                  # rebuild every test project
```

```text
all 10 project(s) behaved as declared
```

## What exists

| Area | State |
|---|---|
| **`tools/compile.py`** | Six declared phases (`ADR-0073`); **7 features, each declaring input, output, invariants and determinism** |
| **`tests/projects/`** | **10 compiler test projects — 6 pass, 4 must fail.** Determinism checked by compiling twice and comparing |
| **`tools/test.py`** | The regression suite. Every compiler change rebuilds every project |
| **`tools/generate-metamodel-views.py`** | Three generated graph views |
| `examples/tiny/` | The reference end-to-end example, 13 nodes |
| **`model/metamodel/`** | **20 of 26 entities specified.** 4 remain in scope, 2 deferred |
| `model/metamodel/relationship-vocabulary.md` | 18 core types; **63 predicates, all parented**; 2 of 5 required fields machine-readable |
| `model/metamodel/ontology/` | OWL 0.4.0 — 660 triples, 31 classes, 73 object properties |
| ADRs | 75 — 67 accepted, 8 superseded |
| Issues | 74 — **1 open, 51 resolved, 22 deferred as debt** |
| Acceptance Records | 22 |
| Session journal | 27 entries |

### Metamodel progress

| Family | Specified | Remaining |
|---|---|---|
| **Descriptive** | BoundedContext · Artifact · ArtifactRevision · Concept · Capability · RelationshipType · Invariant · Evidence · Actor · Dimension · DimensionAssignment · StateMachineSpecification | `Vocabulary` (soon) · ~~Principle~~ · ~~KnowledgePackage~~ |
| **Operational** | Policy · Workflow · WorkflowStep · Skill · EngineeringGate · AcceptanceRecord · ADR · Issue | — |
| **Unassigned** | none | `ValidationRule` (now) · `Registry` (now) · `Manifest` (soon) |

`Principle` and `KnowledgePackage` are **deferred** (`ADR-0075`): the compiler
compiles no ADRs, and there is one repository.

## What does not exist

No `ValidationRule` entity — the checks live in `resolve()` as Python. No
`Registry` entity — the compiler reads the vocabulary from Markdown by regex. No
manifest, so a project is *whatever is in `model/*.md`*. No lifecycle
enforcement, no acceptance checking, no dimension assignment in the compiler.

**The governance corpus is not compiled.** 192 records, and the Canonical
Knowledge Model covers 13 example nodes plus 10 test projects.

## Blocking

**Nothing blocks B1.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. **Now an architectural violation, not an inconvenience** (`ADR-0072`): a hand-maintained projection is a projection with no model behind it. Four governance indexes, the corrections table and the metamodel ontology are still hand-maintained |

## Architectural debt

**22 deferred issues.**

- **`ISSUE-0073`** — Operational Knowledge. `ADR-0070` draws the boundary: a
  Specification whose instances live outside the repository is where Engineering
  OS stops.
- **`ISSUE-0048`** — `ADR.corrects` specified; six corrections still in a
  hand-maintained table.
- **`ISSUE-0063`** — minimum serialized classification set. The compiler assigns
  no dimensions.

## Debt discovered while building

| Question | Where |
|---|---|
| **441 field declarations required, fewer than a third exist.** Domain, range and cardinality are prose the compiler cannot read | `relationship-vocabulary.md` |
| Only one `ValidationRule` exists and it is hard-coded in `resolve()` | `ADR-0075` |
| Four vocabulary mappings are strained — `produces`, `guarded-by`, `has-position`, `requires` | `relationship-vocabulary.md` |
| No test project exercises the six unspecified entities. **The gap is the map** | `tests/README.md` |
| Transitions and conditions point at things that are not entities; both extrinsic by `ADR-0068`'s test | `FINDINGS.md` |
| Nothing enforces that an acceptance reviewer differs from the author | `acceptance-record.md`, `tests/projects/acceptance` |
| Deferral has no automatic trigger, and two entities were just deferred | `ADR-0075`, `issue.md` |

## Acceptance status

`ACCEPT-0001` (trust root) through `ACCEPT-0022`, covering `SESSION-0006`
through `SESSION-0026`.

**`ADR-0072`–`ADR-0075`, the phase-declaring compiler, `tools/test.py` and the
ten test projects are `Under Review`.**

## Next action

**`ValidationRule` and `Registry`** — the two entities the compiler already
needs, both currently implemented as Python that the model should own.

`ValidationRule` has a concrete first instance ready: *every predicate declares a
registered parent*. Moving it from `resolve()` into the model is the smallest
change that makes the metamodel own its own enforcement.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
