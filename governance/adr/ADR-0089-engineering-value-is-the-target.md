---
id: ADR-0089
title: Engineering value is the optimization target; architecture serves the product
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0062, ADR-0080, ADR-0084, ADR-0085, ADR-0087]
---

# ADR-0089 — Engineering value is the target

## Context

Engineering OS has demonstrated three progressively stronger claims:

1. **It can model itself.**
2. **It can compile itself.**
3. **It can explain a real external software system.**

Those are three different proofs, and the third was completed by
`ACCEPT-0028`.

> **The next stage is no longer proving that Engineering OS works. It is proving
> that Engineering OS becomes indispensable.**

## Decision

**Optimize for engineering value, not for architecture.**

Every milestone answers:

> **What valuable engineering capability became possible after this work?**

**Not:** *what architectural capability became possible?*

**Architecture now serves the product.**

### The fourth admission test

The project's tests now form a ladder, each narrower than the last:

| Test | Governs | From |
|---|---|---|
| What new semantic relationship does this introduce? | entities | `ADR-0067` |
| What would the compiler do differently? | metamodel entities | `ADR-0075` |
| Does this let us answer better questions about real systems? | capabilities | `ADR-0084` |
| **What valuable engineering capability became possible?** | **milestones** | this decision |

The difference from `ADR-0084` is the word **valuable**. A better question is not
automatically a useful one. *Which Concepts does nothing reference?* is a better
question than the project could previously ask and no engineer has ever needed
it.

### The long-term question

The project stops asking *can Engineering OS represent software?* and starts
asking:

> **Can Engineering OS become the semantic operating system that developers and
> AI agents use to understand, change and evolve software?**

Every milestone moves closer to answering that.

## Alternatives considered

**Keep `ADR-0084` as the sole criterion.** Rejected: it optimises question
quality, and question quality is a proxy. The Kubernetes validation produced
eleven answerable questions and only one an engineer would have asked unprompted.

**Set a usage or adoption metric.** Rejected as unmeasurable at one repository
and one user, and as an invitation to optimise for a number rather than for the
work.

**Declare the architecture finished.** Rejected — it will need to change, and
forbidding that would make the product worse. What changes is that architectural
work must now be justified by the capability it unlocks rather than by its own
coherence.

## Consequences

### Positive

- **It makes "interesting" insufficient.** Several existing capabilities are
  architecturally satisfying and answer nothing an engineer asks.
- It gives the next milestone a clear shape: *exploit* the Kubernetes model
  rather than build another one.
- It converts the metamodel from a thing being completed into a thing being used.

### Negative

- **"Valuable" is judged by one reviewer at one repository.** The criterion is
  the least externally checkable of the four, which is the cost of moving from
  correctness to usefulness.
- Foundational work scores worse than it deserves, and the saving clause —
  *enables valuable capability* — is doing heavy lifting.

### Neutral

- No artifact changes. What changes is how milestones are chosen and judged.

## Compliance

Every milestone states the valuable engineering capability it makes possible.
Architectural work states the capability it serves.
