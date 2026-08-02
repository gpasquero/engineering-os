---
id: ADR-0082
title: The first vertical slice replaces metamodel completion as the milestone
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0062, ADR-0075, ADR-0079, ADR-0080, ADR-0081]
---

# ADR-0082 — The vertical slice replaces metamodel completion

## Context

B1 is *the Engineering OS Metamodel*, and its completion criterion is
twenty-seven entities specified. Twenty-two are.

**Finishing it is no longer the goal.**

## Decision

**The milestone is the first complete vertical slice:**

```text
Authoritative Repository
        ↓
    Compiler
        ↓
Canonical Knowledge Model
        ↓
 Knowledge Explorer
        ↓
 Developer Question
        ↓
  Semantic Answer
```

**A developer must be able to ask, and get an answer from the model:**

1. What breaks if I change this Concept?
2. Why does this relationship exist?
3. Which ADR established this Invariant?
4. Which Capabilities depend on this Workflow?
5. Which Tests must change?
6. Which Specifications become inconsistent?
7. Which AI workflow should execute?

**This is the product. Everything else exists to enable it.**

### Consequences for the remaining metamodel

`Registry`, `Manifest` and `Vocabulary` are built **when the slice needs them**,
not to complete an inventory. `ADR-0075` already required a compiler
justification; this narrows it further to a slice justification.

**Entities the slice does not need are not built during it.**

### Real-world validation follows

**A metamodel that only models Engineering OS is unproven.** After `Registry`,
the next major milestone is **modeling a real software system** — a full
self-model of Engineering OS, or an external system such as GEAI, GeneXus,
Kubernetes or PostgreSQL.

Self-modeling is the cheaper first target and the weaker evidence: the metamodel
was designed against this repository, so success proves less. **An external
system is what demonstrates that the architecture generalizes**, and it is
therefore the one that matters.

### The Explorer becomes a semantic workbench

Navigation is not enough. The Explorer is designed **around questions rather than
nodes**: eventually every screen answers one engineering question — *explain this
Concept*, *show impact*, *show provenance*, *show rationale*, *show evolution*,
*show alternatives*, *show affected artifacts*, *show implementation status*.

> **The user should feel they are interrogating the engineering knowledge itself,
> not browsing generated documentation.**

## Alternatives considered

**Finish B1, then build the slice.** Rejected — five more entities delay the
first evidence that any of this works, and `ADR-0062` has been right about
construction outpacing analysis for ten sessions.

**Build the slice against the existing tiny example.** Rejected as insufficient:
thirteen nodes cannot answer *which tests must change* or *which ADR established
this invariant*, because neither tests nor ADR-to-invariant links exist in it.
**The slice needs a model rich enough to have questions worth asking.**

**Declare B1 complete at twenty-two entities.** Rejected as bookkeeping. The
remaining entities are not cancelled; their trigger changes from an inventory to
a need.

## Consequences

### Positive

- **The project acquires a demonstrable outcome** for the first time. Every prior
  milestone produced capability; this one produces an answer to a question a
  developer actually has.
- Each of the seven questions is a **concrete requirement on the model**, and
  several are already known to fail — *which ADR established this Invariant*
  requires `establishes` edges that no example asserts.
- It orders the remaining work by evidence rather than by inventory.

### Negative

- **B1 ends incomplete and stays incomplete**, with five entities specified only
  if something reaches for them. An inventory nobody finishes is a standing
  invitation to forget why.
- **Two questions may not be answerable at all yet.** *Which tests must change*
  and *which AI workflow should execute* require concepts the metamodel has no
  entity for. The slice will expose that rather than deliver it, and that is the
  correct outcome but it will read as failure.

### Neutral

- No decision is superseded. B1's scope is unchanged; its priority is not.

## Compliance

`governance/roadmap.md` records the vertical slice as the current milestone.
Each of the seven questions is either answered by the slice or recorded, with the
reason it is not.
