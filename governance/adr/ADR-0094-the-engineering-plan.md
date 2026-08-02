---
id: ADR-0094
title: The Engineering Plan is an authoritative artifact derived deterministically from the model
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0072, ADR-0086, ADR-0091, ADR-0092, ADR-0093]
---

# ADR-0094 — The Engineering Plan

## Context

`ADR-0091` produced recommendations: *what to look at*. An engineer needs **what
to do, in what order, and how to know it worked.**

## Decision

**An Engineering Plan is an authoritative engineering artifact**, derived
entirely from the Canonical Knowledge Model, containing:

| Part | Is |
|---|---|
| **objective** | what the plan achieves, for a named subject |
| **assumptions** | what must already be true, each from a query |
| **reasoning chain** | every query run, its subject, what it returned, and why |
| **ordered actions** | grouped into phases, each action from a recommendation step |
| **dependencies** | which phases require which, declared |
| **required reviews** | checkpoints, each with the query that populates it |
| **expected evidence** | what should exist afterwards that does not now |
| **completion conditions** | checkable statements, each backed by a query |

> **Every action in a plan is explainable through semantic queries.** A plan
> states nothing a query did not return.

### Plans are declared, not coded

Same split as rules (`ADR-0077`), registries (`ADR-0083`), questions
(`ADR-0086`) and recommendations (`ADR-0091`): the engine holds **mechanism**,
the model holds **meaning**. Adding a plan is a data change.

### No language model participates

`ADR-0092`. A plan is deterministic, and **determinism is a property of how the
output was produced**, not of how it reads.

### A plan reports its own judgment measure

`ADR-0093`. Every plan enumerates what it **derived** and what it **defers**.
Deferred items are stated individually and are not failures.

### A plan is an artifact, not an entity

`ADR-0085` admits an entity only when a question requires it. A plan is produced,
read and executed; **no question yet asks the model about plans.** When one does
— *which plans touched this concept?* — that question justifies the entity.

## Alternatives considered

**Generate the plan from the recommendation directly, with no separate
declaration.** Rejected: a recommendation has no notion of order, dependency,
completion or evidence, and inferring them from step order would encode
engineering practice in the engine.

**Let the executor decide order.** Rejected — ordering is exactly the judgement
`ADR-0093` wants moved from the executor into the system.

**Emit a task graph directly.** Rejected as premature. A task graph is an
*execution* artifact; the plan is the engineering artifact it derives from, and
collapsing them would bind planning to one executor.

## Consequences

### Positive

- **The first artifact that tells an engineer what to do**, and the first whose
  every line is traceable to a query and a path.
- It gives `ADR-0093` something to measure and `ADR-0092`'s loop its fourth step.
- Being declared, a bad plan is visible as bad data and fixable without code.

### Negative

- **Phase order and dependencies are judgements encoded as data with nothing to
  check them.** The same debt recommendations carry, one level up and with more
  authority.
- **A plan inherits every weakness of its queries.** `Q-tests` names a file of 30
  tests in the Kubernetes model; the plan will present that as an action.
- **Completion conditions are checkable in principle and unchecked in practice.**
  Nothing yet re-runs a plan to see whether it completed.

### Neutral

- No entity is added. Plans are a registry.

## Compliance

`model/plans.md` declares plans and is registered. `compiler/plan/` derives them
by executing queries and recommendations. **No plan asserts anything a query did
not return, and no language model participates in producing one.**
