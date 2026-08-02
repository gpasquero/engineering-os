---
id: ADR-0092
title: The product is an Engineering Director; Engineering OS reasons, LLMs execute
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0061, ADR-0079, ADR-0080, ADR-0084, ADR-0089, ADR-0091]
---

# ADR-0092 — The Engineering Director

## Context

Recommendations were the closest the project has come to its original vision, and
they are **not the destination**.

> **The final product is not a repository compiler. Not an ontology editor. Not a
> semantic query engine. Not a recommendation engine.**

## Decision

**The product is an Engineering Director**: a system that continuously
understands the software system, plans engineering work, coordinates AI workers,
validates their results, and maintains the engineering knowledge of the system
over time.

**Everything else exists to support that role.**

### The reasoning loop

Recommendations are **one step inside a much larger loop**:

```text
Developer Intent → Engineering Goal → Reasoning → Engineering Plan
   → Recommendations → Execution Plan → AI Workers → Verification
   → Knowledge Update ⟲
```

The loop closes. Verification updates the Canonical Knowledge Model, and the next
intent reasons over what the last execution produced.

**Keep that target visible in every architectural decision.**

### The separation that must not be merged

```text
Developer → Engineering OS → Engineering Plan → Task Graph
          → Claude / Codex / other workers → Implementation
          → Verification → CKM update
```

> **Engineering OS reasons. LLMs execute.**
>
> **Engineering OS remains deterministic. LLMs remain probabilistic executors.**

This is `ADR-0061` — *the Knowledge Compiler is not an intelligence* — restated
as a product architecture. It was a constraint on compilation; it is now the
division of labour of the whole system.

**No LLM participates in producing an Engineering Plan.** A plan derived by a
language model could not be traced to a query or a path, which forfeits the
property that makes any of this trustworthy.

### The Explorer is no longer the primary interface

`ADR-0079` made the Explorer the primary interface to the Canonical Knowledge
Model. **The Engineering Director is now the primary interface**, and the
Explorer becomes **one tool the Director uses during reasoning** rather than the
user's destination.

`ADR-0079` is **not superseded**: the Explorer remains a projection, never a
source of truth, and remains the place a human inspects provenance and paths. Its
position in the product changes; its architecture does not.

## Alternatives considered

**Keep optimizing the semantic compiler.** Rejected — the compiler is adequate
and has needed no metamodel change for two milestones. Further compiler work now
optimises a component nobody is waiting on.

**Let an LLM produce plans and use the model to check them.** Rejected, and it is
the most tempting alternative because it would work sooner. A checked guess is
still a guess: the model can verify that a stated fact is supported, but not that
a *missing* step was missing. **Determinism is not a quality of the output, it is
a property of how the output was produced.**

**Treat recommendations as the product and stop.** Rejected. A recommendation
answers *what to look at*; an engineer needs *what to do, in what order, and how
to know it worked*.

## Consequences

### Positive

- **It gives every future decision one direction to be judged against**, which is
  what `ADR-0089` asked for and did not supply.
- The deterministic/probabilistic boundary is now architectural rather than
  incidental, so it can be violated visibly.
- **It makes the loop's closure a requirement.** Verification feeding the CKM is
  the step that turns a tool into a system that learns, and nothing has built it.

### Negative

- **The gap between here and the vision is very large.** Of nine steps in the
  loop, three exist. Naming the destination makes the distance measurable and
  the current state look thinner than it did.
- **"Engineering Director" invites scope that the deterministic constraint
  forbids.** Much of what a director does is judgement no model can derive, and
  each of those is a place someone will want to insert an LLM.

### Neutral

- No artifact changes. `ADR-0079` is amended in position, not in substance.

## Compliance

Every milestone states which step of the loop it advances. **No component that
produces an Engineering Plan may invoke a language model.** LLM integration
enters only after plans exist, and only as an executor of them.
