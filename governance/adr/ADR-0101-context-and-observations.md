---
id: ADR-0101
title: Execution Context out, Execution Observations back; workers never touch the model
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0044, ADR-0061, ADR-0072, ADR-0092, ADR-0098, ADR-0100]
---

# ADR-0101 — Context and observations

## Context

A worker currently receives a task objective and a list of targets. That is not
enough to do the work, and there is **no channel back at all** — which is why the
loop does not close.

> **Execution Observations are now the most important missing artifact.**

## Decision

Two artifacts, forming the complete contract between Engineering OS and any
worker.

### Out: the Execution Context

A worker receives **an execution package, not an objective**:

| Field | Is |
|---|---|
| objective | what this task achieves |
| engineering rationale | why this task exists, from the plan |
| assumptions | what must already be true |
| evidence | the sources the assertions rest on |
| affected CKM nodes | what this task touches, by identifier |
| expected outputs | what the task must produce |
| completion conditions | how the task is known to be done |
| required updates | what should be recorded afterwards |
| **allowed scope** | **what the worker may touch, and nothing else** |

**This package is the contract.** A worker that needs something not in its
context is a worker whose task was under-specified — a defect upstream, not
initiative to be taken downstream.

### Back: Execution Observations

> **Workers never update the Canonical Knowledge Model. Workers emit
> observations.**

An observation is a **claim about what execution found** — an invariant
confirmed or violated, evidence discovered, documentation drift, an assumption
disproved, an unexpected dependency, an architectural concern.

**Engineering OS evaluates observations. Engineering OS decides what enters the
knowledge model.**

### Why the model is write-protected from workers

`ADR-0044` and `ADR-0061`: every edge is asserted, nothing is inferred, and the
compiler is not an intelligence. **A worker writing to the model would make the
model contain probabilistic content**, and every downstream determinism would
inherit it.

The observation channel keeps the model's contents deterministic **without
discarding what execution learned.** An observation is evidence about the world;
whether it becomes knowledge is a decision, and decisions belong to the Director
and its gates.

### Three outcomes, declared per observation kind

| Outcome | Means |
|---|---|
| `record` | may enter the model mechanically |
| `govern` | requires authorization before entering (`ADR-0100`) |
| `reject` | cannot enter; recorded as a finding instead |

**An observation that contradicts an accepted decision is never recorded
mechanically.** That is the case gates exist for.

## Alternatives considered

**Let workers write to the model and validate afterwards.** Rejected. Validation
can check that a written assertion is well-formed; it cannot check that an
*unwritten* one was missing, nor that a written one was invented. **Determinism
is a property of how content was produced.**

**A single free-form observation channel.** Rejected: without declared kinds, the
intake decision becomes interpretation, and interpretation is the thing being
kept out.

**Have the Director re-derive knowledge from the changed repository instead of
accepting observations.** Genuinely attractive — recompilation is deterministic
and needs no channel. Rejected because it loses everything execution learned that
is *not* in the artifacts: a disproved assumption, a concern, a dependency
discovered and worked around. **Recompilation sees the result, not the finding.**

## Consequences

### Positive

- **The loop can close** — the first decision that makes Knowledge Update
  buildable.
- The worker contract becomes explicit, so an under-specified task is a visible
  defect rather than a worker improvising.
- **`allowed scope` gives the system a statement of what a worker may touch**,
  which is the precondition for ever running one unattended.

### Negative

- **Observation kinds are a closed vocabulary**, and execution will find things
  that fit none of them. Those become `reject` and are recorded as findings,
  which is honest and lossy.
- **An observation is a worker's claim**, and a worker may be wrong. The intake
  rules decide what may enter mechanically; they cannot decide what is true.
- Building the context costs a query pass per task, and nothing caches it.

### Neutral

- No entity is added. Observation kinds are a registry.

## Compliance

`compiler/context/` builds execution contexts. `model/observation-kinds.md`
declares the vocabulary and each kind's intake outcome. `compiler/observe/`
evaluates observations and produces a **knowledge-update proposal — never a
model write.**
