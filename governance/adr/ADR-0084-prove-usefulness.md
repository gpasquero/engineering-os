---
id: ADR-0084
title: The project enters the prove-usefulness phase; success is measured by the questions it can answer
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0062, ADR-0080, ADR-0081, ADR-0082]
---

# ADR-0084 — Prove usefulness

## Context

`ACCEPT-0025` records that a developer question was transformed into a semantic
answer through the complete pipeline, and that this is **the first working
Engineering OS application** rather than a compiler demonstration.

> **The original hypothesis has been demonstrated.** A repository can be compiled
> into a Canonical Knowledge Model that can answer engineering questions.

## Decision

**The project leaves the "prove the architecture" phase and enters the "prove
usefulness" phase.** These are fundamentally different optimization targets.

### The product metric

> **Success is no longer measured by the sophistication of the metamodel. It is
> measured by the quality of the engineering questions Engineering OS can
> answer.**

### The evaluation criterion

Every proposal is evaluated primarily by one question:

> **Does this allow Engineering OS to answer better engineering questions about
> real software systems?**

**If not, it should probably wait.**

### How this differs from `ADR-0080`

`ADR-0080` asked whether a capability improves a developer's ability to
understand, modify or evolve a real system. This narrows it in two ways that
matter:

- **"better questions"** — not more capability, not more coverage. A capability
  that answers an existing question slightly faster scores lower than one that
  answers a question nobody could ask.
- **"real software systems"** — Engineering OS modelling itself no longer counts
  as evidence.

`ADR-0080` remains the capability test. This is the phase's optimization target,
and it is stricter.

## Alternatives considered

**Continue under `ADR-0080` without declaring a phase.** Rejected. `ADR-0080` did
not stop the metamodel growing by three entities in two sessions, because each
was individually justifiable. A phase change is what makes *not building* the
default.

**Declare the metamodel frozen.** Rejected as too strong and as the wrong
mechanism. `ADR-0085` provides the right one: the metamodel grows when a question
requires it, which is a gate rather than a freeze.

**Set a numeric target — *N* questions answerable.** Rejected. It would optimise
question count, and the metric is explicitly **quality**. Ten shallow questions
are worse than one that reveals something documentation cannot.

## Consequences

### Positive

- **It gives "wait" a default.** Under `ADR-0062` the default was to build; that
  was right while the architecture was unproven and is wrong now.
- The metric is externally checkable. *Which questions can it answer about a real
  system* is answerable by someone who did not build it.
- It makes the roadmap honest: everything not serving a question is deferred,
  including work already begun.

### Negative

- **Foundational work scores badly on this metric.** A query engine, an index or
  a parser answers no question by itself. `ADR-0086` is admitted under this
  decision only because every question will execute through it — the saving
  clause is *enables better questions*, not *is a question*.
- **Most of the existing repository does not obviously pass.** The ontology, the
  graph views and much of the governance corpus answer no engineering question
  about a real system. This decision does not remove them; it stops them growing.

### Neutral

- No artifact changes. What changes is what earns priority.

## Compliance

Every proposal states the engineering question it makes answerable, or newly
answerable **about a real software system**. Proposals that cannot are deferred.
