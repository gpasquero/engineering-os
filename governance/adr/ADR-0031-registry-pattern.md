---
id: ADR-0031
title: Registry Pattern
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0013, ADR-0027, ADR-0028, ADR-0030, ISSUE-0052, ISSUE-0053]
---

# ADR-0031 — Registry Pattern

**This is one of the core architectural patterns of Engineering OS.**

## Context

The project has independently rediscovered the same shape several times:

| Instance | Recorded in |
|---|---|
| Skills indexed by a manifest, specifications in `skills/` | `ADR-0013` |
| State machines registered rather than enumerated | `ADR-0027` |
| The registry indexes and relates; specifications are separate artifacts | `ADR-0028` |
| Policies will follow the same structure | `ADR-0029`, `ADR-0030` |

`ADR-0028` recorded the shape as "close to a principle" and said it **should be
named as one when the fourth appears**. It has appeared.

## Decision

Engineering OS adopts the **Registry Pattern**.

**A Registry is an authoritative index of semantic entities.**

**A Registry never contains the complete specification.** It references
independently versioned specifications.

### The division of answers

| The Registry answers | The Specification answers |
|---|---|
| what exists | complete semantics |
| where it lives | constraints |
| relationships | examples |
| ownership | rationale |
| status | evolution |
| version | |

### The evaluation rule

**Every extensible concept in Engineering OS should be evaluated to determine
whether it should be modeled as Registry + Specification**, rather than
embedding complete definitions inside manifests or indexes.

Candidates include skills, workflows, state machines, policies, contracts,
vocabularies, ontology modules, capabilities, invariants and Knowledge Packages.

### Consumers

The Registry Pattern is to be one of the primary concepts exposed by the future
**Knowledge Explorer**, allowing users to navigate registries independently from
the specifications they reference. The Knowledge Explorer is named here for the
first time and is not yet defined — `ISSUE-0052`.

## Alternatives considered

**Leave the shape implicit.** Rejected: it recurred four times and would recur
again, each time re-argued from scratch. `ADR-0028` had already flagged the cost
of not naming it.

**Embed complete definitions in manifests.** Rejected — this is the anti-pattern
the principle exists to prevent. It produces manifests that grow without bound,
cannot be versioned per entity, and force a reader to load everything to learn
anything. `ADR-0009` recorded exactly this risk for `MANIFEST.yaml` before
`ADR-0013` split it.

**Specifications only, with no registry.** Rejected: without an index there is
no answer to "what exists", and discovery would require scanning the filesystem —
which is the manual enumeration `ADR-0027` rejected.

## Consequences

### Positive

- **Minimizes duplication.** Identity and location live in one place; semantics
  live in another. Neither restates the other.
- **Enables modular evolution.** A specification can be versioned and revised
  without touching the registry, and the registry can record status changes
  without reopening the specification.
- **Provides a consistent navigation model for humans and AI agents.** Once the
  pattern is known, every extensible concept is navigable the same way — which
  matters most for agents, who otherwise learn a bespoke traversal per concept.
- It gives `ADR-0031`'s successors a decision procedure: for any new extensible
  concept, ask whether it splits into Registry and Specification.

### Negative

- **"Authoritative index" sits uneasily beside `ADR-0016` and `ADR-0012`.**
  `ADR-0016` made indexes *projections*, generated from authoritative sources.
  `ADR-0012` said manifests should be generated or validated from repository
  inspection. This ADR calls a Registry authoritative. The three can be
  reconciled — a Registry holds facts no specification holds, so it does not
  merely restate — but the boundary is not drawn, and all three manifests are M2
  deliverables. `ISSUE-0053`.
- Two artifacts per concept instead of one, and a reader must follow a reference
  to learn what something means. The cost falls on anyone reading a registry
  expecting an answer.
- The evaluation rule creates real work: every extensible concept must be
  assessed, and some will not split cleanly.

### Neutral

- No existing design changes. `ADR-0013`, `ADR-0027` and `ADR-0028` were already
  instances; naming the pattern makes them consistent rather than coincidental.

## Compliance

No registry contains a complete specification. No specification duplicates what
the registry holds — identity, location, ownership, status, version. Every new
extensible concept is evaluated against this pattern before being modeled
another way.
