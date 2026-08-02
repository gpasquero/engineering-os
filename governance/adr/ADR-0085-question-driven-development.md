---
id: ADR-0085
title: Work begins with questions, not entities
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0062, ADR-0067, ADR-0075, ADR-0080, ADR-0084]
---

# ADR-0085 — Question-driven development

## Context

Twenty-nine sessions have produced twenty-three metamodel entities. **Almost all
of them began as "we need another entity."**

`SESSION-0029` ran the other way round and the difference was measurable: asking
*which tests must change?* and *which specifications become inconsistent?*
produced answers **without a `Test` entity or a `Specification` entity**, both of
which the inventory would have eventually justified.

## Decision

**Work begins with a question.**

```text
Engineering Question
        ↓
Required semantic capability
        ↓
Metamodel extension        (only if necessary)
        ↓
Compiler support
        ↓
Explorer support
        ↓
Regression test
```

**Do not begin with:** *we need another entity.*

**Begin with:** *what engineering question cannot yet be answered?*

### The order is the decision

Every step after the first is conditional on the one before it. **"Only if
necessary" is the load-bearing clause**, and it is placed third deliberately:
between naming the capability and building anything, there is a step whose usual
answer is *no*.

### It ends at a regression test, not at code

A question that cannot be expressed as a fixture is not answered — it is
demonstrated. `tests/projects/` is where the difference is recorded (`ADR-0072`).

### This is a core principle

`ADR-0058` holds that Principles are extracted from accepted decisions rather
than authored. This decision is written so that principle has something to
extract.

## Alternatives considered

**Keep entity-driven development with a stricter admission test.** Rejected —
`ADR-0067` and `ADR-0075` are already that, and both fire *after* someone has
decided an entity is wanted. They filter; they do not redirect.

**Require a question only for metamodel changes.** Rejected as too narrow. The
compiler, the Explorer and the query engine all grew without any question
demanding them, and the discipline is worth more where it is inconvenient.

**Maintain a backlog of questions.** Deferred rather than rejected — useful, and
it is a mechanism rather than a decision. The unanswered question from
`SESSION-0029` is currently recorded in a README, which does not scale.

## Consequences

### Positive

- **It converts the metamodel from a goal into a consequence.** Entities are
  built when a question needs them, which is what `ADR-0084`'s metric requires.
- The unanswered question becomes the unit of planning, and one already exists:
  *which AI workflow should execute?*
- **It makes negative results cheap and visible.** "This question needs no new
  entity" is now a normal, recordable outcome instead of an absence.

### Negative

- **Questions can be reverse-engineered to justify an entity.** Nothing prevents
  writing the question that the entity you wanted answers, and nothing detects
  it. The defence is that the question must be about a **real software system**
  (`ADR-0084`), which is harder to fabricate.
- Some genuinely foundational work has no question. It is admitted under
  `ADR-0084`'s *enables better questions* clause, and each such admission is a
  judgement.

### Neutral

- No existing artifact changes.

## Compliance

Every proposal names the engineering question that motivates it. Every metamodel
extension states which question required it and why no existing construct
sufficed. Every answered question has a regression fixture.
