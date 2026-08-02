---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: engineering-planning
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**The Engineering Director** (`ADR-0092`). Engineering OS reasons; LLMs execute,
and the two responsibilities are never merged.

## The measure

`ADR-0093`. **How much engineering judgment happens before an LLM must think.**
Entity, ADR, compiler-feature and query counts are inventory, not progress.

| Plan | Subject | Derived | Deferred |
|---|---|---|---|
| `P-change-implementation` | `Artifact.ConflictGo` | **10** | 3 |
| `P-change-implementation` | `Artifact.MetaV1Types` | 6 | 3 |
| `P-change-concept` | `Concept.ManagedFields` | 14 | 3 |

**Deferred items are enumerated, never counted.** *This plan cannot tell you
whether the change is source-compatible for existing callers* is information;
*3 deferrals* is a metric.

## What valuable engineering capability became possible

**A deterministic Engineering Plan, derived entirely from the model.**

```sh
python3 tools/plan.py external/kubernetes-ssa P-change-implementation Artifact.ConflictGo
python3 tools/plan.py external/kubernetes-ssa P-change-concept Concept.ManagedFields --reasoning
```

Objective · assumptions · reasoning chain · ordered actions · dependencies ·
required reviews · expected evidence · completion conditions · **derived and
deferred judgment**.

**No language model participates.** Every action names the query and
recommendation that produced it.

### The plan surfaced the model's own gap as an unmet precondition

Planning a change to `conflict.go` leaves one completion condition unchecked:

```text
[ ] The constraints on this artifact are known and were reviewed.   [Q-assumptions]
[x] At least one test validates this artifact.                      [Q-tests]
```

That is the traceability gap found last session — nothing constrains
`Concept.Conflict` — **arriving unprompted as a reason the work is not ready to
start.** The same plan against `Artifact.MetaV1Types` checks that box and leaves
the other unchecked.

## What exists

| Area | State |
|---|---|
| **`model/plans.md`** | **2 plans**, declared. Phases, dependencies, reviews, evidence, completion, explicit `defers` |
| **`compiler/plan/`** | Derives plans by executing queries and recommendations. Stable topological phase order; cyclic dependencies rejected |
| **`tools/plan.py`** | Implements no plan. `--reasoning` prints the full chain; `--json` for executors |
| `model/recommendations.md` · `compiler/recommend/` | 3 recommendations, 6-action vocabulary |
| `model/queries.md` · `compiler/query/` | 17 queries, 6 operators |
| `model/finding-kinds.md` | 8-kind taxonomy. **No confidence scores anywhere** |
| `external/kubernetes-ssa/` | 41 nodes, four source classes, 6 classified findings |
| `tests/` | 17 fixtures, 9 negative, golden outputs |
| Parity | **981 query/subject pairs**, four projects, full fidelity |
| `model/metamodel/` | 23 of 27 entities — **unchanged for three milestones** |
| Registries | **8** — entity types, predicates, core types, rules, queries, recommendations, plans, finding kinds |

## Awaiting decision

**`EngineeringIntent`** — `governance/design/PROPOSAL-engineering-intent.md`.
**Not implemented**, as directed.

The proposal recommends **neither** offered option. Not a Layer A entity: it
would be the first whose instances live outside models. Not a Recommendation
specialization: that inverts the relationship, since an intent should *select*
recommendations rather than be one. **A registry beside them**, because
promoting a registry later is cheap and demoting an entity is not.

## What does not exist

Of the nine steps in `ADR-0092`'s loop, **four exist**: Reasoning, Engineering
Plan, Recommendations, and the model the first three read.

**No Engineering Goal, no Execution Plan, no Task Graph, no AI workers, no
Verification, and no Knowledge Update.** The loop does not close, which is the
step that would make this a system that learns.

No second external system. No confidence scores, and none will be added.

## Blocking

**Nothing.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. **Eight registries**, eight hand-maintained sources, zero generated |

## Debt discovered while building

| Question | Where |
|---|---|
| Phase order and `requires` are judgements encoded as data with nothing to check them | `plans.md` |
| **`defers` is authored, not derived.** Nothing detects a decision neither derived nor deferred | `plans.md` |
| Completion conditions are checkable in principle and unchecked in practice — nothing re-runs a plan | `plans.md` |
| A plan inherits every weakness of its queries and presents it with more authority | `ADR-0094` |
| The judgment measure is gameable by inflating `derived` with trivia | `ADR-0093` |

## Next action

**The Project Owner's decision on `EngineeringIntent`**, then the second external
system — PostgreSQL or LLVM, for architectural diversity rather than scale.

**Aim at ranks 1–3 of the finding taxonomy.** Kubernetes reached rank 5; the
three strongest kinds have never been used.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
