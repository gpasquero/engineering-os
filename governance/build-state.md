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

## The product

**The Canonical Knowledge Model** (`ADR-0072`), now a Layer A entity in its own
right (`ADR-0076`). Everything else is a projection.

```sh
python3 tools/compile.py --phases       # the phase contract
python3 tools/compile.py examples/tiny  # compile a project
python3 tools/test.py                   # rebuild every fixture, check goldens
```

```text
all 13 project(s) behaved as declared
```

## What exists

| Area | State |
|---|---|
| **`compiler/`** | **Modular**: `discovery` · `parser` · `resolver` · `validator` · `ckm` · `emitters/{json,owl,mermaid,explorer}` · `runtime`. **9 features**, each declaring input phase, output phase, invariants and determinism |
| **`compiler/parser/`** | **Real YAML parsing, schema-validated before resolution** (`ADR-0078`). Structural errors surface at Parsing, never at Resolution |
| **`compiler/validator/`** | **6 rule kinds executing 7 declared rules.** No check is authored in Python |
| **`compiler/emitters/explorer/`** | **Five semantic queries**: relationships with explanations, provenance, derived-from closure, impact, acceptance history |
| **`model/metamodel/validation-rules.md`** | `VR-0001`–`VR-0007`, each with a rationale |
| **`tests/`** | **13 fixtures — 6 pass, 7 must fail.** Golden outputs for all four emitters; deterministic rebuild checked |
| `tools/compile.py` | **Orchestration only.** 42 lines, no compiler logic |
| **`model/metamodel/`** | **22 of 27 entities specified** |
| `model/metamodel/ontology/` | OWL 0.4.0 — 660 triples, 31 classes, 73 object properties |
| ADRs | 79 — 71 accepted, 8 superseded |
| Issues | 74 — **1 open, 51 resolved, 22 deferred as debt** |
| Acceptance Records | 23 |
| Session journal | 28 entries |

### Metamodel progress

| Family | Specified | Remaining |
|---|---|---|
| **Descriptive** | BoundedContext · Artifact · ArtifactRevision · Concept · Capability · RelationshipType · Invariant · Evidence · Actor · Dimension · DimensionAssignment · StateMachineSpecification · **CanonicalKnowledgeModel** | `Vocabulary` · ~~Principle~~ · ~~KnowledgePackage~~ |
| **Operational** | Policy · Workflow · WorkflowStep · Skill · EngineeringGate · AcceptanceRecord · ADR · Issue · **ValidationRule** | — |
| **Unassigned** | none | `Registry` · `Manifest` |

**Both entities added this session were demanded by the implementation**, which
is `ADR-0075` working: the product had no specification, and seven checks existed
as Python the model should own.

## What does not exist

No `Registry` entity — the compiler still reads the relationship vocabulary out
of Markdown with a regex. No `Manifest` — a project is still *whatever is in
`model/*.md`*. No `Vocabulary` — closed enumerations are bare strings.

No lifecycle enforcement, no acceptance checking, no dimension assignment in the
compiler. **Provenance records a path, not a revision** (`ADR-0064` wants
`(artifact-id, revision-id)`), and the Explorer's provenance query says so.

**The governance corpus is still not compiled.** 202 records; the Canonical
Knowledge Model covers 13 example nodes and 13 test projects.

## Blocking

**Nothing blocks B1.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections — an architectural violation under `ADR-0072`. Four governance indexes, the corrections table, the metamodel ontology, **and now the parser schemas**, which nothing checks against the specifications they encode |

## Architectural debt

**22 deferred issues.** Nearest to the surface: `ISSUE-0073` (Operational
Knowledge), `ISSUE-0048` (`ADR.corrects` has no mechanism), `ISSUE-0063`
(minimum serialized classification set).

## Debt discovered while building

| Question | Where |
|---|---|
| Provenance carries a source path, not a revision | `canonical-knowledge-model.md` |
| **Scope is undefined** — identity is *(scope, assertion set)* and nothing defines a scope. `Manifest` would | `canonical-knowledge-model.md` |
| The compatibility policy is written and unexercised; nothing diffs two models | `canonical-knowledge-model.md` |
| `VR-0007` has no fixture of its own; it fired where a project happened to violate it | `tests/README.md` |
| Severity is declared and unused; `warning` has no behaviour | `validation-rules.md` |
| A rule naming an unimplemented kind aborts compilation — the strictest choice, unexamined | `validation-rule.md` |
| Rules are not individually versioned | `validation-rules.md` |
| **441 field declarations required by `ADR-0074`; fewer than a third exist.** Domain, range and cardinality are prose | `relationship-vocabulary.md` |
| Schemas are a new hand-maintained projection | `ADR-0078` |

## Acceptance status

`ACCEPT-0001` (trust root) through `ACCEPT-0023`, covering `SESSION-0006`
through `SESSION-0027`.

**`ADR-0074` and `ADR-0076`–`ADR-0079`, the modular compiler, declarative
validation, schema-validated parsing, the semantic Explorer, the golden-output
suite and the two new entity specifications are `Under Review`.**

`ADR-0074` was written in `SESSION-0027` and was **not named in `ACCEPT-0023`'s
scope**, so it is carried forward rather than assumed accepted.

## Next action

**`Registry`**, the last entity the compiler already needs. It would replace the
regex that reads `relationship-vocabulary.md`, and would give the vocabulary,
the rules and the dimension registry one mechanism instead of three ad-hoc
readers.

Then `Manifest` and `Vocabulary`, and B1's entity work is done.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
