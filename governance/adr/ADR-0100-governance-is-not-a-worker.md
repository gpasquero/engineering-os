---
id: ADR-0100
title: Human review is a governance gate, not a worker
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0021, ADR-0023, ADR-0054, ADR-0097, ADR-0099]
---

# ADR-0100 — Governance is not a worker

## Context

Every task graph terminates in `T-review-gate`, requiring `C-approve` — a
capability **no worker may hold**, because self-certification is prohibited
(`ADR-0023`).

The obvious next move is to declare a `HumanReviewer` worker type. **That would
be wrong.**

## Decision

> **Workers perform work. Governance authorizes change. Those responsibilities
> never merge.**

**Human review is a Governance Gate**, not a worker type.

| | Does | Declares | Produces |
|---|---|---|---|
| **Worker** | performs a task | capabilities provided | outputs and observations |
| **Gate** | authorizes a change | the rule it enforces | an authorization |

**No worker type provides `C-approve`.** The capability exists so that a task can
require it and no assignment can satisfy it — which is the correct outcome, not a
gap.

### Why the distinction matters

**Because policy attaches to gates and not to work.** *A reviewer must not be the
author* (`ADR-0023`), *acceptance confers Active status* (`ADR-0021`) — these
constrain **who may authorize**, not who may act. Modelling review as work would
put policy on a worker type, where the next worker type would not inherit it.

It also protects the boundary in the direction that will be pushed hardest: **if
review is work, a sufficiently good model can do it.** If review is governance,
capability is irrelevant — authority is the question, and no model has any.

### Relationship to the Layer A entity

The metamodel has an `EngineeringGate` entity (`ADR-0054`). **These are different
things at different layers**, and the shared word is deliberate:

- `EngineeringGate` (Layer A) models a gate **a described system has**.
- A Governance Gate (registry) is a gate **the Director enforces at runtime**.

A repository could model the Director's gates using the entity. Neither is
derived from the other, and conflating them would put runtime concerns in the
metamodel — which `ADR-0053` forbids.

## Alternatives considered

**A `HumanReviewer` worker type.** Rejected — the reason for the decision.

**Drop `C-approve` and let gates be implicit.** Rejected: the capability is what
makes the unsatisfiable task visible in the graph, and an implicit gate is one
nobody sees skipped.

**Allow a worker to *prepare* an approval for a human to sign.** Rejected as the
subtle version of the same merge. A prepared approval is an approval whose
judgement was made elsewhere.

## Consequences

### Positive

- **Policy has one place to attach**, and it is the place that already carries
  the project's governance decisions.
- The boundary survives better models rather than eroding as they improve.
- **A skipped gate is visible** as an unsatisfied task requirement.

### Negative

- **Every graph ends in something automation cannot complete.** That is by
  design and it means no end-to-end run ever finishes without a person.
- Two things are called gates, at two layers, and readers will conflate them
  despite the note above.

### Neutral

- No entity is added. Governance gates are a registry.

## Compliance

`model/governance-gates.md` declares gates and the rules they enforce. **No
worker type provides `C-approve`**, and a task requiring it is reported as
awaiting authorization rather than as unassignable.
