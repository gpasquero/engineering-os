---
id: REG-engineering-questions-source
title: The Engineering Question Set
status: current
created: 2026-08-02
updated: 2026-08-02
---

# The Engineering Question Set

> **Engineering understanding is the product metric.** Entities discovered,
> predicates extracted, graph size and proposal count are implementation
> metrics (`ADR-0120`).

Registered as `REG-engineering-questions`.

## What this file is

Nine questions an engineer actually asks about a system they do not know. The
product metric is **the percentage of them Engineering OS can answer about a
given repository**.

**The set was authored by the reviewer, not by the implementer.** That is a
governance property, not a courtesy. A metric whose author also builds the thing
being measured will drift toward what the thing already does — which is the same
conflict `ADR-0023` forbids for acceptance.

**The implementer may not add a question they know passes.** New questions are
proposed with their expected answer *unknown*, and are added by the reviewer.

## Levels

Every question here is a **Repository Question** — asked about one system.
`ADR-0126` records a second level, **Organization Questions** (*which systems
implement customer identity? where is this business rule enforced?*), and
records that it is **not to be built yet**.

`level: repository` is declared on all nine so that the day a second level
exists, nothing has to be reinterpreted.

## How a question is scored

Each question names the declared queries that would answer it, and the subject
types it is asked about. Against a given repository:

| State | Meaning |
|---|---|
| `answered` | rows returned for at least `threshold` of eligible subjects |
| `partial` | rows returned, but for fewer |
| `no-data` | a query exists and returns nothing anywhere in this model |
| `no-query` | **no declared query addresses the question at all** |

`no-data` and `no-query` are different findings. The first says the model is
thin; the second says Engineering OS never learned to ask.

## The questions

```yaml
engineering-questions:

  - id: EQ-01-why
    question: Why does this system work this way?
    level: repository
    author: Project Owner
    matters-because: >
      The first question a new engineer asks, and the one existing documentation
      answers worst. A system whose rationale is lost is a system nobody may
      safely change.
    answered-by: [Q-rationale]
    subject-types: [Invariant, Concept, Capability]
    threshold: 0.25

  - id: EQ-02-enforced-rules
    question: What business rules are actually enforced?
    level: repository
    author: Project Owner
    matters-because: >
      A rule that is documented and not enforced is a liability; a rule enforced
      and not documented is a trap. Only the model can hold both halves.
    answered-by: [Q-constraints]
    subject-types: [Capability, Concept]
    threshold: 0.25

  - id: EQ-03-safe-to-change
    question: What could safely be changed?
    level: repository
    author: Project Owner
    matters-because: >
      The question every estimate depends on. A node nothing depends on is
      cheap to change, and knowing which nodes those are is worth more than any
      count of nodes.
    answered-by: [Q-impact]
    subject-types: [Artifact, Concept, Capability]
    threshold: 0.5

  - id: EQ-04-unsafe-to-change
    question: What cannot safely be changed?
    level: repository
    author: Project Owner
    matters-because: >
      The inverse is not the same question. Something may be depended upon
      widely and still be safe; something may have one dependent and be load
      bearing. Impact plus the invariants that guard it is the answer.
    answered-by: [Q-impact, Q-constraints]
    subject-types: [Artifact, Concept, Capability]
    threshold: 0.5

  - id: EQ-05-decisions-that-matter
    question: Which architectural decisions still matter?
    level: repository
    author: Project Owner
    matters-because: >
      A decision record corpus nobody prunes becomes a corpus nobody reads.
      Which decisions still govern something live is answerable from the model
      and from nowhere else.
    # Mixed in the first draft, and caught by `tools/check-questions.py` rather
    # than by a person — the third instance of the same authoring error.
    # `Q-rationale` is per-subject; pairing it with a model-wide query would let
    # the model-wide one answer for every ADR.
    answered-by: [Q-obsolete-decisions]
    subject-types: [ADR]
    threshold: 0.25

  - id: EQ-06-affected-capabilities
    question: Which capabilities would be affected by this feature?
    level: repository
    author: Project Owner
    matters-because: >
      The planning question. It is the one question a Director must answer
      before it may route work at all.
    answered-by: [Q-impact, Q-dependents]
    subject-types: [Capability]
    threshold: 0.5

  - id: EQ-07-protecting-invariants
    question: Which invariants protect this behavior?
    level: repository
    author: Project Owner
    matters-because: >
      Changing behaviour without knowing which guarantees cover it is how
      regressions become incidents.
    answered-by: [Q-constraints]
    subject-types: [Capability, Artifact]
    threshold: 0.25

  - id: EQ-08-authorization
    question: Who is allowed to perform this operation?
    level: repository
    author: Project Owner
    matters-because: >
      In any multi-tenant or regulated system this is a correctness question,
      not an operational one. It is also the question the first two benchmark
      repositories both failed completely.
    answered-by: []
    subject-types: [Artifact, Capability]
    threshold: 0.25

  - id: EQ-09-unsupported-assumptions
    question: Which engineering assumptions are currently unsupported?
    level: repository
    author: Project Owner
    matters-because: >
      An assumption nothing supports is the cheapest defect to find and the most
      expensive to discover late.
    # `Q-assumptions` was listed here in the first draft and does not belong:
    # it asks what ONE artifact depends on, which is a different question, and
    # pairing it with a model-wide query let a mixed mapping score 216/216.
    answered-by: [Q-unsupported]
    subject-types: [Invariant, Concept, Capability]
    threshold: 0.25
```

## Thresholds are declared, and they are not ambitious

`0.25` means *a quarter of eligible subjects produce an answer*. That is a low
bar, chosen deliberately: **the first measurements should be embarrassing rather
than flattering**, and a bar that the current system clears everywhere would
measure nothing.

Raising a threshold is a reviewer decision, like adding a question.
