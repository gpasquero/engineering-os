---
id: ISSUE-0057
title: The set of Architectural Dimensions is examples, and four of them are undefined
type: gap
status: resolved
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0040-architectural-dimensions.md
  - governance/adr/ADR-0039-layers-classify-artifacts-not-directories.md
  - governance/adr/ADR-0027-state-machine-registration-model.md
resolved-by: ADR-0041
---

# ISSUE-0057 — The dimension set is not fixed

## Statement

`ADR-0040` introduces Architectural Dimensions and lists eight as **examples**:

Semantic Layer · Artifact Taxonomy · Lifecycle · Governance Status · Ownership ·
Authority · Visibility · Compilation Phase

`ADR-0039` similarly lists Cross-Cutting Infrastructure as **examples**:
Governance · Tooling · Automation · Validation · Testing · CI/CD.

Neither set is closed, and neither says how a new member is added.

## Why it matters

The metamodel must model dimensions explicitly (`ADR-0040`), and the metamodel is
M2's first deliverable. It cannot model a set that is not fixed, and cannot
define entities whose meaning is unstated.

## Three distinct problems

### 1. Closed set, or registered?

`ADR-0027` faced this exact question for state machines and answered
**registration, not enumeration** — because the rule applied to target domains
that no inventory here could anticipate. `ADR-0031` then named the Registry
Pattern and required **every extensible concept** to be evaluated against it.

Dimensions are an extensible concept. **By `ADR-0031`'s own compliance rule they
must be evaluated for Registry + Specification modeling**, which makes this a
compliance obligation rather than an open preference.

If dimensions are registered, this would be the fifth instance of the pattern.

### 2. Four dimensions are undefined

**Governance Status**, **Ownership**, **Authority** and **Visibility** have no
definition anywhere in the repository.

`Governance Status` is the most concerning: it looks like it overlaps
`ArtifactRevisionLifecycle`, whose values are `Draft`, `Under Review`,
`Accepted`, `Active`, `Superseded`, `Archived`. If they are the same axis under
two names, that is a sixth vocabulary collision — the exact failure `ADR-0040`
was written to prevent, appearing inside `ADR-0040`.

`Ownership` and `Authority` may also be one axis: the worked example gives
`Owner: Architecture` and no `Authority` value at all.

### 3. When is a new dimension justified?

`ADR-0040` records that the pressure which produced overloaded terms can equally
produce proliferating axes, and that the remedy is undefined. Without a test, a
dimension becomes the easy answer to any classification difficulty.

## Resolution

`ADR-0041`. **Dimensions are first-class semantic entities, added by
registration.**

> A Dimension is not merely a taxonomy. It is a semantic construct that defines
> one independent axis of classification.

Each declares identifier, purpose, governed entity types, value domain,
cardinality, constraints, relationships to other dimensions, and its
authoritative specification. A **Dimension Registry Specification**
(authoritative) and a generated **Dimension Registry Projection** follow the
Registry Pattern.

> **Future dimensions are added by registration, never by modifying compiler
> logic.**

This confirms problem 1 as suspected: the answer is registration, exactly as
`ADR-0027` answered it for state machines, and it discharges the compliance
obligation `ADR-0031` had created. **Fifth instance of the Registry Pattern**,
and the first adopted because a rule required it rather than because the shape
was noticed again.

Problem 3 is answered implicitly: a dimension is justified when all eight fields
can be filled. An axis with no cardinality or no governed entity types is not a
dimension.

**Problem 2 is not answered.** The four undefined dimensions become registration
work, and the `Governance Status` / `Lifecycle` overlap is untouched — carried
into `ISSUE-0059`, together with a new tension between `ADR-0040`'s
independence claim and `ADR-0041`'s "relationships to other dimensions" field.
