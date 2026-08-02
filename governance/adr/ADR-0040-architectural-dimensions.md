---
id: ADR-0040
title: Architectural Dimensions — artifacts are classified along multiple independent axes
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0012, ADR-0020, ADR-0035, ADR-0037, ADR-0038, ADR-0039, ISSUE-0057, ISSUE-0058]
---

# ADR-0040 — Architectural Dimensions

**This is a foundational modeling rule.** It prevents future conceptual overload
and allows the architecture to scale without inventing artificial exceptions.

## Context

`ADR-0039` resolved `ISSUE-0056` by recognising that governance artifacts are
orthogonal to the semantic layers rather than belonging to one of them.

That resolution generalizes. The project has hit the same shape repeatedly: a
single classification asked to do several jobs, then split when it failed —
"skill", "authoritative", "state", "policy", "registry", and now "layer".

Each was treated as a naming problem. It was a **dimensionality** problem.

## Decision

Engineering OS introduces the concept of **Architectural Dimensions**:
independent classification axes, along which artifacts are classified
**simultaneously**.

Examples:

- Semantic Layer
- Artifact Taxonomy
- Lifecycle
- Governance Status
- Ownership
- Authority
- Visibility
- Compilation Phase

**Every artifact may be classified simultaneously along multiple independent
dimensions.**

### Worked examples

**An ADR:**

| Dimension | Value |
|---|---|
| Dimension | Governance |
| Artifact Type | Authoritative Artifact |
| Lifecycle | Active |
| Owner | Architecture |
| Visibility | Public |
| Compiler Phase | Input |
| **Layer** | **None (Not Applicable)** |

**A Workflow Specification:**

| Dimension | Value |
|---|---|
| Dimension | Semantic |
| Layer | B |
| Artifact Type | Authoritative Artifact |
| Lifecycle | Active |
| Owner | Domain |
| Compiler Phase | Input |

### The rule

**The Engineering OS Metamodel models these dimensions explicitly, rather than
trying to force every classification into a single hierarchy.**

## Alternatives considered

**A single classification hierarchy.** Rejected — it is what produced
`ISSUE-0056`. Forcing governance into a semantic layer was only necessary
because there was one axis available, and the same pressure produced five
earlier terminology splits.

**Ad-hoc classification per artifact type.** Rejected: without shared axes, two
artifacts cannot be compared, filtered or navigated together — which is what the
Knowledge Explorer and every Registry Projection depend on.

**Fix the dimension set now.** Deferred rather than rejected. The list above is
examples, and `ADR-0027` already established registration-over-enumeration for
an analogous case. `ISSUE-0057`.

## Consequences

### Positive

- **This is the general form of a fix the project has applied five times
  locally.** Every previous collision was resolved by splitting an overloaded
  term; dimensions name why the term was overloaded in the first place.
- **The architecture scales without exceptions.** A new classification need is a
  new dimension, not a distortion of an existing one.
- **`ADR-0038`'s four questions become a projection of the dimension set.** Which
  layer, authoritative or derived, and which compiler phase are values along
  Semantic Layer, Artifact Taxonomy and Compilation Phase. The questions were an
  early, partial view of this.
- Registry Projections and the Knowledge Explorer gain a navigation model:
  filter and group along any dimension.

### Negative

- **Every artifact now carries several classifications**, and each is a claim
  that can be wrong. More machinery, more to keep true.
- **Four of the eight named dimensions have no definition here** — Governance
  Status, Ownership, Authority, Visibility. "Governance Status" in particular
  looks like it overlaps `ArtifactRevisionLifecycle`. `ISSUE-0057`.
- **Nothing says when a new dimension is justified.** The same pressure that
  produced overloaded terms can produce proliferating axes, and the remedy for
  that is not itself defined.
- Classification must travel with the artifact for the compiler to use it, which
  is unresolved — `ISSUE-0058`.

### Neutral

- No existing classification changes. Semantic Layer, Artifact Taxonomy and the
  revision lifecycle become dimensions rather than standalone schemes.

## Compliance

No classification is forced into an unrelated hierarchy. Every dimension is
independent: a value on one never implies a value on another. The metamodel
models dimensions explicitly.
