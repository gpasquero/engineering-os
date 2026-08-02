---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: task-graph
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**The Engineering Director** (`ADR-0092`), built stage by stage around the
engineering loop (`ADR-0095`).

## The loop

```text
Developer Intent → Context Acquisition → Engineering Reasoning
   → Engineering Plan → Task Graph → Worker Assignment → Execution
   → Review → Knowledge Update → Continuous Learning ⟲
```

| Stage | State |
|---|---|
| Developer Intent | **registry** — 3 intents (`ADR-0096`) |
| Context Acquisition | compiler + CKM |
| Engineering Reasoning | 17 queries, 3 recommendations |
| Engineering Plan | ✅ 2 plans |
| **Task Graph** | ✅ **this milestone** |
| Worker Assignment | capabilities declared; **routing not built** |
| Execution · Review · Knowledge Update · Continuous Learning | **not built** |

**Five of ten stages exist. The loop does not close** — which is the step that
would make the system improve between one intent and the next.

## The measure

`ADR-0093`. **How much engineering judgment happens before an LLM must think.**

```sh
python3 tools/taskgraph.py external/kubernetes-ssa P-change-implementation Artifact.ConflictGo
```

| Graph | Tasks | mechanical | reasoning | human | Parallelism | Deferred |
|---|---|---|---|---|---|---|
| `Artifact.ConflictGo` | 5 | 3 | 2 | 1 | 1 | 3 |
| `Concept.ManagedFields` | 7 | 2 | 4 | 1 | **2** | 3 |

**An executor receives a task with an objective, dependencies, a completion
condition, the evidence it must produce, and no decisions about ordering.** That
is the largest single transfer of judgement from executor to system the project
has made.

## What exists

| Area | State |
|---|---|
| **`compiler/taskgraph/`** | Derives graphs from plans. **Levels computed, not annotated**; cyclic dependencies rejected |
| **`tools/taskgraph.py`** | Text, `--json` for executors, `--mermaid`. Verified byte-identical across runs |
| **`model/task-kinds.md`** | 6 kinds from plan actions + **2 terminal**: review gate and knowledge update |
| **`model/worker-capabilities.md`** | 6 capabilities, each classed `mechanical`, `reasoning` or `human` |
| **`model/engineering-intents.md`** | 3 intents. **Not a metamodel entity** (`ADR-0096`) |
| `model/plans.md` · `compiler/plan/` | 2 plans, 8 declared parts, explicit `defers` |
| `model/recommendations.md` · `model/queries.md` | 3 recommendations, 17 queries |
| `external/kubernetes-ssa/` | 41 nodes, four source classes, 6 classified findings |
| `tests/` | 17 fixtures, 9 negative, golden outputs |
| Registries | **11** |
| `model/metamodel/` | 23 of 27 entities — **unchanged for four milestones** |

## Capabilities, never workers

A task declares **what capability it requires**. Routing is a separate stage
(`ADR-0097`).

**Every graph terminates in `T-review-gate`, which requires `C-approve` — a
capability no worker of any kind may hold**, because self-certification is
prohibited (`ADR-0023`). By design, and worth stating: the graph ends in a task
nothing can execute automatically.

## What does not exist

**No routing.** Capabilities are declared and nothing matches them to a worker.

**No execution, no review, no knowledge update.** `T-update-knowledge` appears in
every graph as a task and has no executor — **the loop's closure is present as a
node and absent as a capability**, which is more honest than omitting it.

No second external system. No confidence scores, and none will be added.

## Blocking

**Nothing.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. **Eleven registries**, eleven hand-maintained sources, zero generated |

## Debt discovered while building

| Question | Where |
|---|---|
| **A plan action with no declared task kind produces no task**, reported as a diagnostic rather than dropped — but nothing prevents the omission | `ADR-0097` |
| Execution classes are authored judgements — that reading source requires reasoning is plausible and unverified | `worker-capabilities.md` |
| Completion conditions are inherited from the plan and **remain unchecked**; nothing re-runs them | `plans.md`, `ADR-0097` |
| `I-investigate` selects no plan — a real intent with no planning support | `engineering-intents.md` |
| Intent selection is a declared list; adding a plan does not update the intents that should offer it | `engineering-intents.md` |
| Task objectives substitute only `{targets}`, so a task cannot say *why* those targets were selected | `task-kinds.md` |

## Next action

**The first true Engineering Director** — one command from intent to Plan, Task
Graph, Reviews, Suggested Worker Assignment, Verification Strategy and Expected
Knowledge Updates, **with no language model invoked.**

Only then should Claude or Codex receive implementation tasks.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
