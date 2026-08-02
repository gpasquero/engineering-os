---
id: ADR-0049
title: Dimensions are a scarce architectural resource, governed by five conditions
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0064]
related: [ADR-0040, ADR-0041, ADR-0047, ADR-0048, ISSUE-0065]
---

# ADR-0049 — Dimensions are a scarce architectural resource

## Context

`ISSUE-0064` asked whether Representation is an independent dimension or a
coarser partition of Semantic Layer. It was the third scheme in that family —
Semantic Layer, Abstraction Level, Representation — and the second in two
sessions needing to be checked against an existing one.

`ADR-0040` had already recorded the risk: the pressure that produced overloaded
terms can equally produce proliferating axes, and the remedy was undefined.

## Decision

**Not every conceptual distinction deserves to become a Dimension.**

A concept becomes a Dimension **only if all five conditions hold**:

1. **It classifies many independent artifact types.**
2. **Its values are orthogonal to other classifications.**
3. **It is expected to evolve independently.**
4. **It is useful for querying, navigation or validation.**
5. **Multiple values can exist across repository artifacts.**

If these are not satisfied, the concept is modelled instead as:

- metadata,
- a property,
- a relationship,
- or a dedicated metamodel entity.

> **Dimensions are a scarce architectural resource. Creating a new Dimension
> requires an ADR.**

The goal is to **prevent the metamodel from becoming an uncontrolled collection
of classification axes**.

## Alternatives considered

**Decide Representation's status directly.** Rejected as the smaller answer:
the question would recur with the next candidate, and the project has already
seen three schemes in this family in two sessions.

**Allow dimensions freely, and prune later.** Rejected: `ADR-0041` makes each
dimension a registered entity with ten fields, and `ADR-0042` makes assignments
graph relationships. A dimension added casually is expensive to remove once
artifacts are assigned along it.

**A softer guideline rather than five hard conditions.** Rejected: a guideline
would be applied by whoever wants the dimension. Requiring an ADR moves the
decision to acceptance, where a reviewer other than the author sees it
(`ADR-0023`).

## Consequences

### Positive

- **The missing test now exists.** `ISSUE-0062`'s question — is `Governance
  Status` distinct from `Lifecycle`? — was unanswerable because there was no
  criterion. Condition 2 is that criterion.
- Creating a dimension requires an ADR, so a new axis is reviewed by someone
  other than whoever wants it.
- Naming three alternatives — metadata, property, relationship, or metamodel
  entity — means rejecting a dimension is not a dead end. The concept still gets
  modelled, just not as an axis.
- Applies to adopting repositories too: a domain cannot inflate the framework's
  classification space casually.

### Negative

- **The five conditions do not answer `ISSUE-0064`'s own question.** They tell
  you how to determine whether Representation is a dimension; someone still has
  to apply them, and the outcome could be either. `ISSUE-0065`.
- Condition 2 — orthogonality — is the hardest to judge and the one most likely
  to be argued. `Governance Status` against `Lifecycle` is exactly the case
  where two people can reasonably disagree about whether two axes are the same.
- An ADR per dimension adds real friction to the initial set of eight.

### Neutral

- No existing dimension is invalidated. The conditions apply from here, and the
  initial set is evaluated in M2.

## Compliance

No dimension exists without an ADR recording it against all five conditions. A
concept failing any condition is modelled as metadata, a property, a
relationship or a metamodel entity — never as a dimension.
