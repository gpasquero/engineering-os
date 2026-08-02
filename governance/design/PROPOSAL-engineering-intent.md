---
id: PROPOSAL-ENGINEERING-INTENT
title: Proposal — where EngineeringIntent belongs
status: accepted
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0065, ADR-0076, ADR-0085, ADR-0091, ADR-0092]
decision-required-from: Project Owner
resolved-by: ADR-0096
---

# Proposal — where `EngineeringIntent` belongs

> **ACCEPTED as recommended** — `ADR-0096`. The reviewer confirmed that
> `EngineeringIntent` should not become a Layer A entity: it is part of an
> engineering session, not of the software knowledge. **Do not promote it unless
> reality forces us to.**

**Requested before implementation.** Nothing in this proposal had been built when
it was written.

The question: is `EngineeringIntent` a **Layer A entity**, or is it better
represented as a **specialization of Recommendation**?

## What it would be

A vocabulary describing **why the developer entered the system** — Add Feature,
Modify Behavior, Investigate Bug, Refactor, Migrate, Improve Performance, Improve
Security, Remove Capability.

Explicitly **not** a description of software.

## The three tests the project already has

| Test | From | Verdict |
|---|---|---|
| What new semantic relationship does this introduce? | `ADR-0067` | **passes** — `intent selects recommendation`, which nothing expresses today |
| Is it meaningful without a compiler? | `ADR-0076` | **passes** — *I want to investigate a bug* is meaningful with no software at all |
| Which family? | `ADR-0065` | **operational** — it describes engineering activity, not the modelled world |

**All three pass.** On the project's existing criteria, `EngineeringIntent` is
admissible as a Layer A operational entity.

## The test that decides it, and is not yet written

Every existing Layer A entity has instances that **persist as facts in a
Canonical Knowledge Model**. A repository declares its Workflows, its Skills, its
Gates; they are part of what is known about it.

**An intent is not a fact about a system. It is an input to one interaction.**

> **Proposed criterion: a Layer A entity is one whose instances belong in a
> model. An intent belongs to a session.**

It is the same kind of thing as a query's `subject` — required to ask, and not
part of the answer. No repository would contain `Intent.AddFeature` as a node
describing itself.

### The counter-argument, stated fairly

`ADR-0094` makes an Engineering Plan an **authoritative artifact**, and a plan
records the intent it came from. So an intent *does* persist — inside a plan.

**That is persistence as a field, not as an entity.** `subject` persists in a
plan too, and nobody proposes a `Subject` entity. A thing recorded *about* an
artifact is not thereby a node in the graph.

Two facts would change this. **Both are answerable and neither has been asked:**

- If a question needs *which intents touched this concept?*, intents must be
  queryable, and then they are entities (`ADR-0085`).
- If two intents need to relate to each other — *Migrate specialises Refactor* —
  a vocabulary cannot express it and an entity must.

## The recommendation

**Neither of the two options offered. A third.**

### Not a Layer A entity — yet

It would be the first entity whose instances live outside models, and admitting
it would weaken the boundary that has kept the metamodel at 23 entities across
two external validations.

### Not a specialization of Recommendation

They are different things, and merging them loses a distinction that is already
doing work:

| | Answers | Cardinality |
|---|---|---|
| **Intent** | *why am I here?* | one per interaction |
| **Recommendation** | *what should I look at for this subject?* | many per intent |

A `Recommendation` already carries an `intent` **string** — *"I want to change
this implementation"*. That string is a **description of the recommendation**,
not a classification of the developer's goal. `R-change-concept` and
`R-change-implementation` are both *Modify Behavior*.

**Collapsing them would mean one intent per recommendation**, which inverts the
relationship: an intent should select recommendations, not be one.

### Proposed: a registry, beside Recommendation

`REG-engineering-intents` — a registered vocabulary in the **interaction layer**,
where queries, recommendations and plans already live.

```yaml
engineering-intents:
  - id: I-modify-behavior
    label: Modify behaviour
    question-form: What am I changing, and what depends on it?
    selects-plans: [P-change-implementation, P-change-concept]
    selects-recommendations: [R-change-implementation, R-change-concept]
```

**What this buys:**

- The **new relationship** — *intent selects plans and recommendations* — which
  is the one thing that genuinely does not exist today.
- The interaction becomes *state an intent, name a subject* rather than *pick a
  recommendation by its identifier*, which is the entry point `ADR-0092`'s loop
  begins from.
- It costs no metamodel change and is reversible. **Promoting a registry to an
  entity later is cheap; demoting an entity is not.**

**What it does not buy:**

- Intents cannot be related to one another.
- Intents cannot be queried as part of a model.

**Both are acceptable until a question needs them**, and `ADR-0085` says the
question comes first.

## What would change the recommendation

| If | Then |
|---|---|
| a question asks about intents as model content | it becomes a Layer A operational entity |
| intents need to specialise one another | the same |
| plans need to record intent with its own identity and lifecycle | the same |
| **none of the above within two milestones** | the registry was correct and stays |

## Cost of being wrong

**Registry, wrongly:** the interaction layer holds a vocabulary that should have
been a node. Promotion is mechanical — declare the entity, migrate the registry,
the questions that motivated it define the relationships.

**Entity, wrongly:** Layer A contains something no model instantiates, the
criterion *entities belong in models* is broken by its own inventory, and every
future candidate cites it. **This is the more expensive error**, which is why the
proposal takes the reversible option.

## Awaiting decision

**Nothing has been implemented.** The Engineering Planning Engine built this
session takes a **plan identifier and a subject**, which is exactly what the
registry option would sit in front of — so either decision can be adopted without
rework.
