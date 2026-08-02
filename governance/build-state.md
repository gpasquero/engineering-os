---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: exploit-the-model
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**Exploiting the Kubernetes model** (`ADR-0089`). Engineering value is the
optimization target; architecture serves the product.

## What valuable engineering capability became possible

**Engineering OS now produces guidance, not only knowledge.**

```sh
python3 tools/advise.py external/kubernetes-ssa R-change-implementation Artifact.ConflictGo
python3 tools/advise.py external/kubernetes-ssa R-audit-model
python3 tools/ask.py external/kubernetes-ssa Q-assumptions Artifact.MetaV1Types
```

A maintainer about to change `conflict.go` is told what to review, verify,
inspect and investigate — **and every line names the query that produced it.**
Nothing is asserted that a query did not return.

## What exists

| Area | State |
|---|---|
| **`model/recommendations.md`** | **3 recommendations**, composed entirely of semantic queries. No logic in code (`ADR-0091`) |
| **`compiler/recommend/`** | Executes recommendations by executing queries; 6-action closed vocabulary |
| **`tools/advise.py`** | Implements no recommendation. `--json` for agents |
| **`model/finding-kinds.md`** | **8-kind taxonomy ranked by strength** (`ADR-0090`). **No confidence scores anywhere** |
| `model/queries.md` | **17 declared queries** — `Q-assumptions`, `Q-obsolete-decisions`, `Q-stale-implementation` added |
| `compiler/query/` | 5 operators + **`has-path`**, the second gap external validation found |
| `external/kubernetes-ssa/` | 41 nodes, four source classes, **6 findings classified by kind and support** |
| `tests/` | **17 fixtures**, 9 negative, golden outputs, query rows/status/paths |
| Parity | **981 query/subject pairs** across four projects, full fidelity |
| `model/metamodel/` | 23 of 27 entities — **unchanged for two milestones** |
| ADRs | 91 — 83 accepted, 8 superseded |
| Issues | 74 — 1 open, 51 resolved, 22 deferred |
| Acceptance Records | 28 · Session journal | 33 entries |

## The Kubernetes findings, classified

`ADR-0090`. **Kind describes what was found; support describes how well it is
evidenced.**

| Finding | Kind | Rank | Support |
|---|---|---|---|
| A `managedFields` timestamp is not the time that entry last changed | documentation-gap | 5 | confirmed |
| That timestamp is rendered in the conflict message a user reads | observability-gap | 6 | confirmed |
| `ApplyRequiresFieldManager` is asserted by a test and no document | documentation-gap | 5 | confirmed |
| **Nothing constrains `Concept.Conflict`** — found by `Q-assumptions`, not by reading | traceability-gap | 4 | confirmed |
| Whether KEP-2885 and KEP-5958 refine KEP-555 | ambiguous-evidence | 7 | ambiguous |
| Who owns fields set by defaulting | missing-evidence | 8 | unsupported |

**Ranks 1–3 are empty.** No confirmed contradiction, no behavioral or
architectural inconsistency. **The strongest thing this validation found is a
documentation gap**, and saying so is the point of the taxonomy.

## Two external-validation gaps, two domain-neutral corrections

| Gap | Where it belonged | Correction |
|---|---|---|
| An assertion could not cite its exact source | **authoring representation** | uninterpreted `attributes` on nodes |
| *Which artifacts no longer match their design rationale?* was inexpressible | **query language** | `has-path` — filter a row on a property several hops away |

**Neither was about Kubernetes.** Both fixtures mention no domain.

## What does not exist

**No confidence scores, and none will be added** (`ADR-0090`).

**No AI workflow selection.** `ADR-0091` generalises it: the semantic layer
recommends engineering actions and execution engines consume them.

**No `Finding` entity** — no question requires one (`ADR-0085`).

**No second external system.** The metamodel has modelled one domain shape.

## Blocking

**Nothing.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. **Seven registries**, seven hand-maintained sources, zero generated |

## Debt discovered while building

| Question | Where |
|---|---|
| Step order in a recommendation is a judgement with nothing to check it | `recommendations.md` |
| A recommendation inherits the bluntness of its queries — `Q-tests` names a file of 30 tests | `recommendations.md` |
| `R-audit-model`'s empty `applies-to` overloads the field: *no subject* and *any subject* look alike | `recommendations.md` |
| Finding classification is the author's judgement, and the incentive runs the wrong way | `finding-kinds.md` |
| `documentation-gap` and `traceability-gap` overlap | `finding-kinds.md` |
| Test granularity is the file — still the sharpest modelling limitation | `kubernetes-ssa/FINDINGS.md` |

## Next action

**A second external system of a different shape** — PostgreSQL or LLVM
(`ADR-0089` direction). The objective is **architectural diversity, not scale**.

**Aim at ranks 1–3 of the finding taxonomy.** Kubernetes reached rank 5, and the
three strongest kinds have never been used.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
