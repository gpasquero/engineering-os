---
id: ADR-0098
title: Orchestration is the objective; the Engineering Director owns the loop
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0092, ADR-0093, ADR-0095, ADR-0097]
---

# ADR-0098 — Orchestration is the objective

## Context

Five of the loop's ten stages exist, and all five produce **artifacts**. Nothing
**runs** the loop: a plan and a graph are produced and then handed to whoever
asked.

> **The next objective is no longer planning. It is orchestration.**

## Decision

**The Engineering Director owns the loop. Workers execute only individual
tasks.**

```text
Developer Intent → Engineering Director → Engineering Plan → Task Graph
   → Worker Assignment → Execution → Execution Observations
   → Knowledge Update → Repository Evolution ⟲
```

Every stage except **Execution** belongs to the Director and is deterministic.

### The primary architectural KPI

`ADR-0093` asked how much engineering judgment happens before an LLM must think.
This sharpens it to a measurable boundary:

> **How much engineering judgment happens before the first LLM token is
> generated?**

- **Every deterministic decision moved upstream is progress.**
- **Every probabilistic decision moved downstream is progress.**

Counts of entities, registries, queries, plans and task graphs are **no longer
reported as progress**. They are inventory.

### What this forbids

**A worker never receives an intent, a plan or a graph.** It receives one task
and its context (`ADR-0101`).

**A worker never decides what to do next.** Sequencing belongs to the graph, and
the graph belongs to the Director.

## Alternatives considered

**Improve plans further.** Rejected — plans are adequate and nothing consumes
them.

**Build Execution first, since it is where value becomes visible.** Rejected: an
executor with no assignment, context or observation channel is a language model
holding a document, which is what the architecture exists to avoid.

**Let the Director be a language model coordinating deterministic tools.**
Rejected, and it is the industry-standard shape. It inverts `ADR-0092`: the
coordination decisions — what to do, in what order, who can do it, what counts as
done — are exactly the judgement being moved upstream. **A probabilistic
coordinator makes every downstream determinism cosmetic.**

## Consequences

### Positive

- **The KPI is measurable and adversarial to hand-waving.** Any decision left to
  a worker is visible as a decision not made upstream.
- It gives the remaining five stages one owner instead of five components.
- **It makes the loop's closure a requirement of the Director**, not an optional
  final feature.

### Negative

- **The Director becomes the largest component and the one most able to
  accumulate special cases.** Nothing yet constrains its growth the way registries
  constrain the compiler.
- **The KPI can be satisfied by making tasks smaller** rather than by deciding
  more, and nothing distinguishes the two.

### Neutral

- No artifact changes. What changes is what owns them.

## Compliance

Every milestone reports the KPI. **No worker receives more than one task and its
context.** No stage before Execution invokes a language model.
