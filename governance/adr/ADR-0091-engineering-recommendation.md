---
id: ADR-0091
title: Engineering Recommendation — guidance derived from semantic queries, never hardcoded
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0079, ADR-0084, ADR-0086, ADR-0089]
---

# ADR-0091 — Engineering Recommendation

## Context

The query engine answers questions. **Questions produce knowledge;
recommendations produce engineering guidance**, and the difference is the
difference between a knowledge base and a tool.

```text
Question:        What breaks if I change this Concept?

Recommendation:  Before changing this Concept —
                   review these ADRs
                   inspect these tests
                   validate these invariants
                   update these artifacts
```

## Decision

**An Engineering Recommendation is declared as data and composed entirely of
semantic queries.**

Each step names an **action**, a **query** that finds what the action applies to,
and **why**. Executing a recommendation executes its queries against a subject.

> **Recommendations are always explainable by the underlying semantic queries.**
> Every item in a recommendation traces to a declared query and a path in the
> model. Nothing is asserted that a query did not find.

**Recommendation logic is never hardcoded.** Same split as `ADR-0077` for rules,
`ADR-0083` for registries and `ADR-0086` for questions: the engine holds
mechanism, the model holds meaning.

### Not AI workflow selection

The unanswered question *which AI workflow should execute?* is **not** solved by
adding a `Trigger`. It is a special case of a more general concept.

**The semantic layer recommends engineering actions. Execution engines consume
them.**

| Consumer | Executes the recommendation by |
|---|---|
| a developer | doing the work |
| an AI agent | running a workflow |
| a CI pipeline | gating a change |

**This keeps Engineering OS independent of any particular AI runtime**, which is
the same commitment `ADR-0066`, `ADR-0068`, `ADR-0077` and `ADR-0081` made about
formalisms.

### What a recommendation may not do

- **It may not add knowledge.** If a step's query returns nothing, the step
  reports nothing. A recommendation never fills a gap with advice.
- **It may not rank by confidence** (`ADR-0090`).
- **It may not contain domain logic.** A recommendation about Kubernetes is a
  recommendation whose *subject* is Kubernetes, composed of domain-neutral
  queries.

## Alternatives considered

**Hardcode recommendations in the CLI.** Rejected — the reason for the decision,
and the same mistake `ask.py` made before `ADR-0086`.

**Implement AI workflow selection directly.** Rejected as premature and as
narrowing. It would bind the product to one consumer, and the general concept
covers it.

**Generate recommendations with a language model.** Rejected, and it is the most
tempting alternative. A generated recommendation cannot be traced to a query or a
path, which forfeits the one property that makes this trustworthy —
`ADR-0061`: the compiler is not an intelligence.

**Derive recommendations automatically from impact analysis.** Rejected as too
clever: *what is affected* is not *what you should do about it*, and collapsing
them would hide the judgement in the traversal.

## Consequences

### Positive

- **The first capability that produces engineering guidance rather than
  knowledge**, which is `ADR-0089`'s criterion applied.
- Recommendations are reviewable artifacts: a bad one is visible as a bad step,
  and fixable as data.
- **Agents and humans consume the same output.** Machine-consumable guidance is
  part of the deliverable, not an adapter.

### Negative

- **A recommendation is only as good as its queries.** If `Q-tests` names a file
  rather than a test — as it does in the Kubernetes model — the recommendation
  inherits that bluntness and looks more authoritative than the query it wraps.
- **Ordering steps is a judgement encoded as data with nothing to check it.**
  Declaring *review decisions before inspecting tests* asserts an engineering
  practice that no evidence supports.

### Neutral

- No entity is added. Recommendations are a registry (`ADR-0085`: no question
  requires an entity yet).

## Compliance

`model/recommendations.md` declares recommendations and is registered.
`compiler/recommend/` executes them by executing queries. No recommendation logic
exists in code, and no recommendation asserts anything a query did not return.
