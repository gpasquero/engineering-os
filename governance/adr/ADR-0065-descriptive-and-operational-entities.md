---
id: ADR-0065
title: Metamodel entities are either Descriptive or Operational
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0035, ADR-0056, ADR-0062]
---

# ADR-0065 — Descriptive and Operational entities

## Context

Twelve entities into B1, the metamodel is converging toward two families that
have been treated as peers without qualification.

This was raised as **a recommendation, not a blocker** — and taken now for the
reason given: discovering the split after twenty more entities exist would be
expensive, while introducing it at twelve is nearly free.

That reasoning is `ADR-0062`'s test applied honestly. The question is not *is
this needed to build the next entity* but *is this cheaper now than later*, and
for a top-level abstraction the answer is unambiguous.

## Decision

Every Layer A metamodel entity belongs to exactly one of two families.

### Descriptive entities — describe knowledge

They answer *what is true of the modelled world.* They are owned by a
BoundedContext, they have no notion of an engineering activity, and they would
be meaningful in a repository that had no engineering process at all.

BoundedContext · Concept · Capability · Relationship · Invariant · Evidence ·
Actor · Artifact · ArtifactRevision · DimensionSpecification · Dimension ·
DimensionAssignment · StateMachineSpecification · StateMachine · Vocabulary ·
Principle · KnowledgePackage

### Operational entities — describe engineering activity

They answer *what was done, decided or must be done.* They are owned by the
engineering process, they carry provenance about who acted and when, and they
would be meaningless in a repository with no engineering process.

Workflow · Skill · EngineeringGate · AcceptanceRecord · ADR · Issue · Policy

### They are not peers

Both families remain in the same metamodel. They have **different purposes,
different lifecycles and different relationships**, and no specification should
treat them as interchangeable.

The distinction is made explicit as a top-level abstraction so that every entity
declares its family.

## Alternatives considered

**Two separate metamodels.** Rejected: operational entities reference
descriptive ones constantly — an Issue cites Evidence, an ADR establishes a
Principle. Splitting the metamodel would put that relationship across a
boundary.

**Leave them as peers.** Rejected on cost. The split was visible at twelve
entities and would be equally true at thirty-two, by which point every
specification would need revisiting.

**Defer as architectural debt.** The default under `ADR-0062`, and rejected
here: debt is for questions whose answer does not change what is built next.
This one changes the shape of every remaining specification.

## Consequences

### Positive

- **Cheap now, expensive later.** Twelve specifications need a one-line family
  declaration; thirty-two would need re-reading.
- It explains an asymmetry already visible in the specifications. Descriptive
  entities are *owned by a bounded context*; operational entities are *owned by
  the engineering process*. The two ownership sections were diverging without a
  reason being stated.
- It gives the OWL skeleton a top-level class structure rather than a flat list
  of twenty-seven siblings.

### Negative

- **Some entities do not classify cleanly.** `Manifest`, `RegistrySpecification`
  and `ValidationRule` describe structure *about* engineering rather than about
  a domain. They are assigned when specified, not now.
- A third family may prove necessary. Naming two is a claim that the space has
  two regions, and nothing yet tests it.

### Neutral

- No entity changes meaning. Twelve gain a family declaration.

## Compliance

Every Layer A entity specification declares its family. No specification treats
a Descriptive and an Operational entity as interchangeable.
