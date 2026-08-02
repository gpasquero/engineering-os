---
id: ADR-0044
title: Dimension independence is not isolation; relationships are descriptive, never inferential
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0059]
related: [ADR-0040, ADR-0041, ADR-0042, ISSUE-0062]
---

# ADR-0044 — Independence is not isolation

## Context

`ADR-0040` stated that dimensions are independent: *a value on one never implies
a value on another*. `ADR-0041` then required every dimension registration to
declare *relationships to other dimensions*.

`ISSUE-0059` recorded that both could not be read strictly, and asked in what
sense dimensions are independent if they relate.

## Decision

**The apparent contradiction comes from confusing independence with isolation.**

- **Dimensions are semantically independent.** Dimension values are not derived
  from one another.
- **Dimensions may define semantic relationships with other dimensions.**
- **These relationships are descriptive, not inferential.**

### Examples

**Compilation Phase** may reference **Semantic Layer**, because certain phases
primarily consume artifacts from particular layers. This does **not** mean that
assigning a Semantic Layer determines a Compilation Phase.

**Artifact Taxonomy** may constrain **Lifecycle** applicability.

**Ownership** may constrain **Governance Policies**.

Relationships describe **compatibility, applicability or constraints**. They
**never imply automatic classification**.

### The rules

- Dimensions remain independent.
- **Dimension relationships are independent semantic entities.**
- **No dimension may derive the value of another dimension unless an explicit
  inference rule exists.**

### Inference Rules

**If Inference Rules are introduced in the future, they become their own
first-class artifact type** rather than being embedded into Dimension
definitions.

## Alternatives considered

**Drop the relationships field** and keep strict independence. Rejected: real
constraints exist between axes — a `runtime` artifact plausibly cannot be
`Active` in the revision sense — and suppressing them would push that knowledge
into validator code, where it could not be registered or reviewed.

**Drop the independence claim** and allow derivation. Rejected: it would make
classification partly implicit, so an artifact's dimension values could not be
read without evaluating rules. That reintroduces exactly the opacity
`ISSUE-0060` was opened about.

**Embed inference in dimension definitions** rather than deferring it to a
separate type. Rejected pre-emptively, and this is the useful part: the decision
fixes *where inference would go* before anyone needs it, which removes the
shortcut of adding a small rule to a dimension and discovering later that it has
become a rules engine.

## Consequences

### Positive

- Both `ADR-0040` and `ADR-0041` are preserved exactly, with no supersession and
  no correction. The contradiction was in the reading.
- **Constraints become declarable and reviewable.** Compatibility and
  applicability are registered facts rather than validator behaviour.
- The pre-commitment on Inference Rules prevents a predictable failure: rules
  accumulating inside dimension definitions until they are a hidden engine.
- Classification stays fully explicit — nothing is derived, so nothing must be
  computed to be read.

### Negative

- **"Descriptive, not inferential" is a distinction that must be policed.** A
  constraint saying `runtime` artifacts cannot be `Active` looks inferential in
  practice: it does not assign a value, but it rules some out. Where description
  ends and inference begins will be argued.
- Dimension relationships are "independent semantic entities", which implies
  another entity type in the metamodel with no specification yet.
- **The four undefined dimensions are still undefined.** `ISSUE-0059` carried
  them from `ISSUE-0057`; they are now carried again into `ISSUE-0062`. That is
  three issues in a row deferring the same question.

### Neutral

- No inference rule exists, and none is required. The decision only fixes where
  one would live.

## Compliance

No dimension derives another's value. Every declared relationship states
compatibility, applicability or constraint — never assignment. No inference
logic is embedded in a dimension definition.
