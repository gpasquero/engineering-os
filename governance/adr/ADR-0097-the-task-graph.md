---
id: ADR-0097
title: The Task Graph is derived deterministically from the plan and declares required capabilities
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0092, ADR-0093, ADR-0094, ADR-0095]
---

# ADR-0097 — The Task Graph

## Context

An Engineering Plan states what to do and in what order. **An executor still has
to decide what a unit of work is, what blocks what, what may run in parallel, and
who can do it** — and every one of those is judgement that `ADR-0093` wants moved
out of the executor.

## Decision

**A TaskGraph is derived deterministically from an Engineering Plan.** Every node
declares five things:

| Field | States |
|---|---|
| **objective** | what this task achieves |
| **dependencies** | which tasks must complete first |
| **completion conditions** | how to know it is done |
| **evidence produced** | what should exist afterwards |
| **required worker capabilities** | what kind of worker can perform it |

### Capabilities, not workers

A task declares **what capability it requires**, never which worker performs it.
Routing — matching capabilities to Claude, Codex, a script or a human — is a
**separate stage** (`ADR-0095`) and is not built here.

The reason is the same one `ADR-0081` gave for the CKM: a task bound to a worker
is a task that must be rewritten when the worker changes.

### Execution classes

Each capability declares whether it is **mechanical**, requires **reasoning**, or
requires **human authority**. That classification is what later lets the system
decide which tasks need an LLM, which do not, and which need approval.

> **Claude, Codex or another model should receive a Task, never an Intent.**

### Parallelism is derived, not declared

Tasks with no dependency path between them may run concurrently. The graph
computes **levels** — sets of tasks whose dependencies are all satisfied at the
same depth — so concurrency is a property of the graph rather than an annotation
someone maintains.

### Still completely deterministic

No language model participates. A TaskGraph is a pure function of a plan, which
is a pure function of the model.

## Alternatives considered

**Let the executor derive tasks from the plan.** Rejected — it moves sequencing
and decomposition back into the LLM, which is the inversion `ADR-0092` forbids.

**Declare task graphs as data, like plans.** Rejected: a task graph is *derived
from* a plan, and declaring both would let them disagree. What is declared is the
**task kind per plan action** — the mechanism — and the graph is computed.

**Bind tasks to workers now.** Rejected as premature and as coupling. Routing is
its own stage and needs capabilities to exist first.

**Emit a flat task list.** Rejected: the dependencies are the point. A list
loses parallelism and blocking, which are two of the four things an executor
would otherwise have to decide.

## Consequences

### Positive

- **An executor receives a task with an objective, a completion condition and no
  decisions to make about ordering.** That is the largest single transfer of
  judgement from executor to system the project has made.
- Parallelism and blocking become computed facts, so *what can start now* is
  answerable.
- **Capability requirements make the LLM boundary visible per task**, rather than
  per system.

### Negative

- **Task kinds are a declared mapping from plan actions**, so a plan action with
  no declared kind produces no task — a silent omission unless something checks
  it.
- **Completion conditions are inherited from the plan and remain unchecked.**
  Nothing re-runs them after execution, and nothing will until the loop closes.
- **Capability requirements are authored judgements.** Declaring that *inspect*
  requires reasoning rather than mechanism is an assertion no evidence supports.

### Neutral

- No entity is added. Task kinds and worker capabilities are registries.

## Compliance

`model/task-kinds.md` and `model/worker-capabilities.md` declare the mechanism.
`compiler/taskgraph/` derives graphs. **No language model participates**, and no
task names a worker.
