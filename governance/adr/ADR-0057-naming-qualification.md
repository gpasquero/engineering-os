---
id: ADR-0057
title: Naming Qualification — a concept's canonical name includes its architectural dimension
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0069]
related: [ADR-0025, ADR-0030, ADR-0046, ADR-0056]
---

# ADR-0057 — Naming Qualification

**This becomes the default naming discipline for the Engineering OS metamodel.**

## Context

Seven terminology collisions in nineteen sessions: "skill", "authoritative",
"state", "policy", "registry", "layer/level", and now "level/process". Each was
solved individually — five by splitting an overloaded term, two by qualifying.

`ADR-0046` had already recorded that three ADRs applying one discipline meant
the discipline was a rule belonging somewhere other than an ADR. `ISSUE-0069`
made it eight.

## Decision

Engineering OS establishes a **Naming Qualification Policy**.

> **Whenever a concept belongs to a specific architectural dimension, its
> published name includes that dimension whenever ambiguity is possible.**

### Examples

| Qualified name | Distinguishes from |
|---|---|
| **Abstraction Level** | Semantic Layer |
| **Semantic Layer** | Abstraction Level |
| **Engineering Process** | Business Process |
| **Business Process** | Engineering Process |
| **Engineering Gate** | any other gate |
| **Workflow Execution** | Engineering Process |
| **Artifact Revision Lifecycle** | State Machine Lifecycle |
| **State Machine Lifecycle** | Artifact Revision Lifecycle |
| **Compiler Phase** | any other phase |
| **Knowledge Representation** | any other representation |

### It is not a renaming strategy

**It is a semantic qualification strategy.** The short name may still be used
informally when the context is unambiguous. **The qualified name is the
canonical architectural name.**

## What this settles in ISSUE-0069

`ADR-0056`'s Process becomes **Engineering Process**, distinguished from
**Business Process** — a domain concept an adopting repository will have. Gates
and workflows are both Engineering Processes; a **Workflow Execution** is the
act of running one.

`ADR-0056`'s level scheme takes a qualified name by applying the policy rather
than by being named here. Its fourth stage, `Artifact`, remains an output rather
than a level.

## Alternatives considered

**Continue solving collisions individually.** Rejected: eight occurrences is a
pattern, and each was found later than the last would have needed to be.

**Rename the ambiguous terms.** Rejected, as in `ADR-0046`: both words in each
pair are accurate, and renaming discards precision to solve an ambiguity that
qualification solves.

**Require qualification everywhere, always.** Rejected: the decision explicitly
permits short names where context is unambiguous. A rule that makes every
sentence longer would be ignored, and ignoring it selectively is worse than
applying it deliberately.

## Consequences

### Positive

- **The class of defect closes rather than the eighth instance.** Future
  collisions are prevented by naming rather than caught after propagation.
- It supplies names for concepts the project had not yet distinguished —
  **Business Process** in particular, which an adopting repository certainly has
  and Engineering OS had no way to name.
- The distinction between canonical and informal names means precision is
  available without being mandatory, which is what makes the rule survivable.
- Applying it generates answers rather than requiring a decision per case, which
  is the property `ADR-0049`'s five conditions have for dimensions.

### Negative

- **Existing unqualified names in the corpus are now informal usages**, not
  errors — but nothing distinguishes deliberate informality from an unqualified
  name that should have been qualified. Auditing the corpus is real M3 work.
- "Whenever ambiguity is possible" requires judgement, and ambiguity is often
  visible only in retrospect. This is exactly how seven of the eight collisions
  were found.
- **This is a policy stated in an ADR.** `ADR-0029` and `ADR-0056` say a rule
  belongs in a Policy artifact; none exists until M3. The ADR records the
  decision, and the `ModelingPolicy` will hold the rule.

### Neutral

- Nothing is renamed. Ten canonical names are fixed.

## Compliance

Every metamodel concept has a canonical qualified name. Specifications,
diagrams and ontology definitions use it. Short names appear only where context
makes them unambiguous.
