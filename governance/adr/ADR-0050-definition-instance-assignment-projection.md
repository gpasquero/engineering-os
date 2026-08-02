---
id: ADR-0050
title: The Definition → Instance → Assignment → Projection modeling hierarchy
status: superseded
date: 2026-08-02
supersedes: null
superseded-by: ADR-0052
resolves: []
related: [ADR-0027, ADR-0031, ADR-0032, ADR-0041, ADR-0042, ADR-0048, ISSUE-0066]
---

# ADR-0050 — The Definition → Instance → Assignment → Projection hierarchy

**This is a core modeling pattern of the metamodel.** Future extensible concepts
are evaluated against it before new modeling structures are introduced.

## Context

The project has arrived at the same shape repeatedly and named it in pieces: the
Registry Pattern (`ADR-0031`), the registry/projection split (`ADR-0032`), state
machine registration (`ADR-0027`), dimension registration (`ADR-0041`),
assignments (`ADR-0042`) and dimension specifications (`ADR-0048`).

Each was decided on its own merits. Together they are one recurring hierarchy.

## Decision

Engineering OS has a recurring modeling hierarchy that appears across the entire
framework:

```text
Definition
    ↓
Instance
    ↓
Assignment
    ↓
Projection
```

### Examples

| Definition | Instance | Assignment | Projection |
|---|---|---|---|
| Dimension Specification | Dimension | Dimension Assignment | Registry Projection |
| State Machine Specification | State Machine | State Assignment | State Registry Projection |
| Policy Specification | Policy | Policy Assignment *(future, if needed)* | Policy Registry Projection |

**This hierarchy is an explicit metamodel pattern.** Future extensible concepts
are evaluated against it before introducing new modeling structures.

## Alternatives considered

**Leave the shape implicit across six decisions.** Rejected: `ADR-0028` had
already recorded that three independent arrivals at a shape were "close to a
principle", and `ADR-0031` named that one. This is the same argument at a larger
scale — the pattern now spans dimensions, state machines and policies.

**Treat it as an extension of the Registry Pattern.** Rejected as too narrow. The
Registry Pattern concerns indexing and specification; this hierarchy adds the
*instance* and *assignment* stages, which is where classification actually
happens.

**A five-stage hierarchy including the registry itself.** Rejected for now — but
this is where the pattern is least settled. `ADR-0032`'s Registry Specification
governs a registry, which is not obviously any of the four stages.
`ISSUE-0066`.

## Consequences

### Positive

- **A uniform semantic architecture across the framework.** Once the four stages
  are known, every extensible concept is understood the same way — which matters
  most for agents, who otherwise learn a bespoke structure per concept.
- It gives `ADR-0038`'s and `ADR-0049`'s gates something concrete to test
  against: a new concept either fits the four stages or explains why it does not.
- **The Policy row is a prediction, not a description.** `Policy Assignment` is
  marked *future, if needed* — the pattern says where it would go before anyone
  needs it, the same pre-commitment `ADR-0044` made for Inference Rules.
- Sixth arrival at a recurring shape, and the second to be named as a pattern
  rather than applied again.

### Negative

- **Where the Registry Specification sits is unclear.** `ADR-0032` made it an
  authoritative artifact governing a registry — identity, membership rules,
  extension rules. It is not the Definition stage, which is occupied by the
  Dimension or State Machine Specification. `ISSUE-0066`.
- Four stages per concept is a real structural cost, and not every concept will
  need all four — the Policy row already has a conditional stage.
- A pattern stated as universal invites forcing concepts into it. `ADR-0049`'s
  five conditions guard dimensions specifically; nothing yet guards the
  hierarchy from being applied where it does not fit.

### Neutral

- No existing decision changes. The hierarchy names what six decisions already
  do.

## Compliance

Every extensible concept is evaluated against the four stages before a new
modeling structure is introduced. A concept that does not fit records why. The
metamodel documents the hierarchy as a pattern.
