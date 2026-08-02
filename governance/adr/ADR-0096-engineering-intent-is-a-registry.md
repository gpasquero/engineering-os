---
id: ADR-0096
title: EngineeringIntent is a registry, not a Layer A entity
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0065, ADR-0076, ADR-0085, ADR-0091, ADR-0095]
---

# ADR-0096 — EngineeringIntent is a registry

## Context

`SESSION-0034` was asked to determine whether `EngineeringIntent` belongs in
Layer A or is better represented as a Recommendation specialization, and to bring
back a proposal before implementing anything.

The proposal — `governance/design/PROPOSAL-engineering-intent.md` — recommended
**neither**, and the reviewer accepted that conclusion.

## Decision

**`EngineeringIntent` is a registered vocabulary in the interaction layer. It is
not a Layer A entity, and it is not a specialization of Recommendation.**

> **It is not part of the software knowledge. It is part of an engineering
> session.**

**Do not promote it unless reality forces us to.**

### The criterion this establishes

`EngineeringIntent` passes all three existing admission tests — `ADR-0067`,
`ADR-0076`, `ADR-0065`. The test that decides it was not written until now:

> **A Layer A entity is one whose instances belong in a model. An intent belongs
> to a session.**

Every existing Layer A entity has instances that persist as facts about a system.
No repository would contain `Intent.AddFeature` as a node describing itself. An
intent is the same kind of thing as a query's `subject`: required to ask, and not
part of the answer.

**This criterion now applies to every future candidate**, and it is the fourth
question a proposed entity must answer.

### Why not a Recommendation specialization

A `Recommendation` already carries an `intent` **string**, and that string
describes *the recommendation*, not the developer's goal: `R-change-concept` and
`R-change-implementation` are both *Modify Behavior*.

**Merging them would mean one intent per recommendation**, inverting a
relationship in which an intent selects many.

### What the registry buys

The one genuinely new relationship: **an intent selects plans and
recommendations.** The interaction becomes *state an intent, name a subject*
rather than *pick a plan by its identifier* — which is where `ADR-0095`'s loop
begins.

## Alternatives considered

**A Layer A operational entity.** Rejected. It would be the first entity whose
instances live outside models, breaking the criterion above by its own inventory,
and every future candidate would cite it.

**A Recommendation specialization.** Rejected for inverting the cardinality.

**Nothing — keep passing plan identifiers.** Rejected: the loop's first stage is
Developer Intent, and there is no artifact for it.

## Consequences

### Positive

- **Reversible.** Promoting a registry to an entity is mechanical; demoting an
  entity is not. The cheaper error was chosen deliberately.
- The metamodel stays at 23 entities for a fourth milestone.
- **It writes down a criterion the project had been applying without stating**,
  which is the more durable outcome than the decision itself.

### Negative

- **Intents cannot be related to one another.** *Migrate specialises Refactor* is
  inexpressible, and a vocabulary cannot fix that.
- **Intents cannot be queried as part of a model.** *Which intents touched this
  concept?* has no answer, and if plans become durable records that question will
  arrive.

### Neutral

- No metamodel change. One registry added.

## Compliance

`model/engineering-intents.md` declares the vocabulary and is registered. **No
metamodel entity is added.** Promotion requires a question that a registry cannot
answer.
