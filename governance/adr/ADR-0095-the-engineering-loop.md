---
id: ADR-0095
title: The architecture is the engineering loop; every stage is a deterministic artifact
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0061, ADR-0072, ADR-0092, ADR-0093, ADR-0094]
---

# ADR-0095 — The engineering loop

## Context

`ADR-0092` named the Engineering Director and sketched a nine-step loop. **Four
of its steps exist.** The architecture is still organised around the compiler
that produced the first four.

> **The next objective is no longer "better plans".**

## Decision

**The architecture is designed around the complete engineering cycle**, and the
Canonical Knowledge Model sits at its centre:

```text
Developer Intent → Context Acquisition → Engineering Reasoning
   → Engineering Plan → Task Graph → Worker Assignment → Execution
   → Review → Knowledge Update → Continuous Learning ⟲
```

| Stage | State |
|---|---|
| Developer Intent | **registry** (`ADR-0096`) |
| Context Acquisition | the compiler and the CKM |
| Engineering Reasoning | queries and recommendations |
| Engineering Plan | `ADR-0094` |
| **Task Graph** | **`ADR-0097` — this milestone** |
| Worker Assignment | declared capability requirements; routing not built |
| Execution | not built |
| Review | not built |
| Knowledge Update | **not built — the loop does not close** |
| Continuous Learning | not built |

**Everything else should now start appearing around plans**, not inside them.

### The rule that must hold across every stage

> **Every stage before Execution is deterministic.** A language model enters at
> Execution and nowhere earlier.

Stages after Execution — Review, Knowledge Update — return to determinism: they
consume observations and update the model mechanically.

### Domain independence is a property of reasoning, not of knowledge

> **Optimize for engineering reasoning that remains identical regardless of
> domain.**
>
> **Every new external system should require adding knowledge, never changing
> reasoning. If reasoning changes, investigate whether the abstraction is wrong
> before extending it.**

This is now a test, not an aspiration. Kubernetes required two corrections and
**neither was to reasoning** — one was the authoring format, one the query
language. A third external system that forces a reasoning change is evidence of a
wrong abstraction, and must be investigated as one.

## Alternatives considered

**Keep improving plans.** Rejected — the reason for the decision. A better plan
is a better artifact in a loop that does not turn.

**Build Execution next, since it is where the value is visible.** Rejected: an
executor with no task graph receives a plan and must decide sequencing, which
moves judgement back into the LLM and inverts `ADR-0092`.

**Close the loop first — build Knowledge Update before Task Graph.** Genuinely
tempting, because the loop's closure is what makes the system learn. Rejected on
dependency: there are no observations to consume until something executes, and
nothing executes until tasks exist.

## Consequences

### Positive

- **Six missing stages become a roadmap rather than an absence.**
- It makes the deterministic boundary checkable per stage instead of per
  component.
- The domain-independence rule turns each external validation into a test of the
  abstraction rather than only of coverage.

### Negative

- **The loop's closure is still the last thing that will be built**, and it is
  the step that makes the system improve. Everything before it produces a better
  static tool.
- **Six unbuilt stages is a large commitment stated in one decision.** Naming
  them does not make them cheap, and the estimate is unknown.

### Neutral

- No artifact changes. What changes is what the architecture is organised around.

## Compliance

Every milestone names the loop stage it advances. **No stage before Execution
invokes a language model.** An external system that forces a reasoning change
opens an investigation into the abstraction before any extension is made.
