---
id: ADR-0080
title: The product is semantic answers to engineering questions
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0059, ADR-0062, ADR-0067, ADR-0072, ADR-0075, ADR-0079]
---

# ADR-0080 — The product is semantic answers

## Context

Twenty-eight sessions have produced a metamodel, a compiler, a validation
system and a regression suite. **None of them is the product.**

> **Engineering OS is not being built to compile Markdown. It is being built to
> become the semantic operating system used by developers and AI agents to
> understand, reason about, evolve and operate software systems.**

## Decision

**Every capability is evaluated against one question:**

> **How does this improve a developer's ability to understand, modify or evolve a
> real software system?**

**If the answer is weak, defer it.**

### The test applies to capabilities; two narrower tests remain

The project now has three admission tests, at three levels, and they compose:

| Test | Governs | From |
|---|---|---|
| *What new semantic relationship does this introduce?* | **entities** | `ADR-0067` |
| *What would the compiler do differently?* | **remaining metamodel entities** | `ADR-0075` |
| **How does this improve a developer's ability to understand, modify or evolve a real system?** | **capabilities** | this decision |

The third is the widest and the strictest. A capability may pass the first two
and fail it, and when it does, **the first two were answering the wrong
question.**

### The compiler's bar is raised

The compiler is mature enough that a new compiler feature is admitted only if it
improves one of three things:

1. **semantic correctness**
2. **developer reasoning**
3. **agent reasoning**

Everything else has a very high bar.

### Agents are a first-class consumer

Not an eventual one. `Actor` already states that a role may be filled by a human,
a system **or an agent**, and treats that as unremarkable. This decision makes
the consequence explicit: **a capability that only a human can use is half a
capability.** Machine-consumable output is part of the deliverable, not a
convenience.

## Alternatives considered

**Leave the objective implicit in the vision document.** Rejected. It has been
implicit for twenty-eight sessions and did not prevent the project from
optimising for metamodel completeness — which `ADR-0075` had to correct once
already, at the level of entities rather than capabilities.

**State it as a principle rather than a decision.** Rejected: a `Principle` in
this framework is *extracted from accepted decisions* (`ADR-0058`), so it must be
a decision first.

**Adopt the test only for new work.** Rejected — it is most useful applied
backwards. Several existing capabilities do not obviously pass, and knowing which
is more valuable than protecting them.

## Consequences

### Positive

- **It gives "defer" a criterion at the capability level**, which `ADR-0062`
  established for architectural questions and nothing established for features.
- It makes the roadmap answerable. Every milestone can be asked which developer
  question it makes answerable.
- **It is the strongest available argument against building more metamodel.**
  Entity twenty-three improves nobody's ability to understand a real system.

### Negative

- **The test is a judgement, and it can be argued either way for most
  infrastructure.** A parser improves reasoning only indirectly, and a strict
  reading would defer all foundational work. The saving clause is *weak*, not
  *indirect* — indirect but load-bearing passes.
- Applied honestly, it puts existing work in question. The metamodel ontology,
  the graph views and parts of the governance corpus would struggle.

### Neutral

- No artifact changes. What changes is what gets built next.

## Compliance

Every proposed capability states the developer question it makes answerable.
Every compiler feature states which of semantic correctness, developer reasoning
or agent reasoning it improves.
