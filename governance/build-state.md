---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: M2
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current milestone

**M2 — The Metamodel, foundational contracts and manifests. Not started, and
blocked.**

M1 is complete. **M3 is unblocked.**

## What exists

| Area | State |
|---|---|
| Repository architecture | Defined and accepted |
| Documentation system, session protocol | Defined and accepted |
| Vision, principles, glossary | Written |
| Roadmap | M1–M13 |
| ADRs | 59 — 51 accepted, 8 superseded |
| Issues | 71 recorded — 23 open, 47 resolved, 1 deferred |
| Acceptance Records | 15 — `ACCEPT-0001` (trust root) through `ACCEPT-0015` |
| Session journal | 20 entries |
| Frozen provenance | `imports/` (3 prototypes), `sources/` (requirements, archives, original handoff) |

## What does not exist

**The Metamodel does not exist.** It is M2's first deliverable, at
`model/metamodel/`.

No executable code, and none is planned before M9 (`ADR-0017`, `ISSUE-0036`).

Nothing in `shared/`, `skills/`, `workflows/`, `model-spec/`, `model/`,
`templates/`, `schemas/`, `validation/`, `tests/`, `adapters/` or `docs/`. None
of the three manifests. No Registry Specification. **No policies of any kind.**

## The architecture

**Semantic Layers** — every *semantic* artifact belongs to exactly one
(`ADR-0037`, corrected by `ADR-0039`):

| Layer | Defines | Status here |
|---|---|---|
| **A** — Engineering OS Metamodel | the language | Does not exist; M2's first deliverable |
| **B** — Repository Knowledge Model | a domain in that language | Does not exist |
| **C** — Canonical Knowledge Model | compiler output | Requires a compiler |
| **D** — Derived Projections | Explorer, docs, indexes, packages, validation, search | Five hand-maintained projections only |

**Cross-Cutting Infrastructure** — Governance, Tooling, Automation, Validation,
Testing, CI/CD. Orthogonal to the layers; Semantic Layer `None`. **Everything
this repository currently contains outside `imports/` and `sources/` is
governance.**

**Layers classify artifacts, not directories** (`ADR-0039`). Repository layout is
an implementation concern.

**Architectural Dimensions** (`ADR-0040`, `ADR-0041`) — artifacts are classified
along several independent axes simultaneously. Dimensions are registered
entities, added without changing compiler logic.

**Dimension Assignments** (`ADR-0042`) — classification is a *relationship*, not
a property. Artifacts do not contain dimension values.

**Abstraction Levels** (`ADR-0043`, `ADR-0046`) — Metamodel (types), Model
(instances), Classification (assertions). A different axis from Semantic Layers;
both names are always qualified.

**Three representations of knowledge** (`ADR-0047`) — Semantic (the canonical
graph), Authoring (human-editable sources), Presentation (generated views). The
compiler maintains semantic equivalence across them; they are different views of
the same knowledge, not different knowledge.

**Front matter is interchange syntax** (`ADR-0045`), not the semantic model.

**Two orthogonal hierarchies** (`ADR-0052`). Semantic:
`Definition → Instance → Assignment`. Compilation: `Authoritative Semantic
Model → Canonical Knowledge Model → Projection`.

**Semantic architecture is separate from compiler architecture** (`ADR-0053`).
The metamodel defines what exists; the compiler defines how it is transformed.

**Dimensions are scarce** (`ADR-0049`) — five conditions, and creating one
requires an ADR.

## Acceptance status

| Record | Covers |
|---|---|
| `ACCEPT-0001` | Bootstrap corpus at `2b6484f` — trust root, the only retrospective acceptance |
| `ACCEPT-0002` | `SESSION-0006` at `aed6d89` — first under the normal workflow |
| `ACCEPT-0003`–`ACCEPT-0015` | `SESSION-0007` through `SESSION-0019` |

**`ADR-0057`–`ADR-0059`, `ISSUE-0071` and this session's propagation are `Under
Review`**, not `Active`.

## A note for agents reading this repository

**The ADR corpus is history, not specification** (`ADR-0029`). **Fifty-nine
decisions**, eight superseded, five partially corrected.

`ADR-0056` now explains why: ADRs record how content came to be; **Policies**
hold the rules; **Gates** are the processes. None exists yet.

**Gates are now a first-class concept** (`ADR-0054`), and **questions belong to
Gates rather than to artifacts** (`ADR-0055`). A gate applies when triggered;
its questions are part of its definition.

| Gate | Asks |
|---|---|
| Metamodel Position Gate | metamodel entity, semantic layer |
| Compiler Impact Review *(future)* | consuming and producing compiler phases |
| Dimension Review | the five Dimension criteria; is another construct better? |
| Acceptance Review | authoritative? reviewed? validation satisfied? |

**Triggering conditions are now the entire enforcement surface**, and nothing
says what may appear in one.

**Names are qualified** (`ADR-0057`): a concept's canonical name includes its
architectural dimension whenever ambiguity is possible. Short names remain valid
informally.

**Principles are not artifacts** (`ADR-0058`) — they are semantic entities the
compiler extracts. **Engineering OS maximizes discovered knowledge**
(`ADR-0059`).

## Blocking

| Issue | Blocks |
|---|---|
| `ISSUE-0071` | **M2 and M9.** How discovered knowledge is produced. `ADR-0058` says the compiler *extracts* Principles and `ADR-0059` says it discovers patterns and semantic clusters — while `ADR-0020` requires determinism and forbids a generator invoking an agent. Either discovery is algorithmic, or the determinism rule needs qualifying. |
| `ISSUE-0063` | The minimum classifications every artifact must serialize. `ADR-0038` says what must be knowable; `ADR-0045` says what may be visible; nothing connects them. |
| `ISSUE-0002` | M8 |
| `ISSUE-0006` | M10 |

## Must be resolved within M2

`ISSUE-0007`, `ISSUE-0011`, `ISSUE-0013`, `ISSUE-0014`, `ISSUE-0015`,
`ISSUE-0018`, `ISSUE-0019`, `ISSUE-0048`, `ISSUE-0049`.

## Known debt

- **`ISSUE-0037`** — five hand-maintained Registry Projections; no compiler until
  `ISSUE-0036` is un-deferred.
- **`ISSUE-0048`** — no machine-readable correction mechanism. **Five
  corrections** now exist, visible only in the ADR index. Open since
  `SESSION-0008`.

## Next action

Accept or return this session's work.

Then `ISSUE-0071`. It is the only issue blocking a named M2 deliverable, and it
decides how much of `ADR-0059`'s ambition the compiler can carry. The reading
recorded in the issue — that deterministic discovery is compilation and
non-deterministic discovery is authoring — would preserve every existing rule,
but it would also place the most ambitious discoveries outside the compiler.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Visibility: **public, with no licence file** — `ISSUE-0011`
