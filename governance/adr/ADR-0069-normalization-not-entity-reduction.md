---
id: ADR-0069
title: Optimize semantic independence, not entity count
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0062, ADR-0067, ADR-0070]
---

# ADR-0069 — Normalization, not entity reduction

## Context

`ISSUE-0074` was framed as a simplification review whose objective was to
identify entity pairs that could merge. Framed that way, its success metric is a
smaller number, and **a smaller number is not the goal.**

## Decision

**Optimize for the smallest number of independent semantic concepts, not the
smallest number of entities.**

The distinction is the whole decision:

- **If three entities disappear because they are manifestations of one
  abstraction, that is simplification.**
- **If three entities disappear because information was collapsed together, that
  is information loss.**

Both reduce the entity count identically. Only one is an improvement.

**Always optimize semantic independence rather than entity count.**

### The test a merge must pass

> **After the merge, can everything that could be said before still be said?**

If yes, the entities were one concept wearing two names. If no, the merge
destroyed a distinction, and the fact that it produced a tidier inventory is
irrelevant.

## Alternatives considered

**Keep the entity-reduction framing.** Rejected. It optimises a proxy. An
inventory can be shrunk indefinitely by conflation, and each conflation looks
like progress in the metric that was chosen.

**Add a rule forbidding merges that lose information.** Rejected as insufficient:
the failure mode is not that someone merges knowing information is lost, it is
that a count-driven review never asks. Changing the objective removes the
pressure; a prohibition would only add a check against it.

**Defer as a review-time judgement.** Rejected. This is the criterion the review
runs on, and it must exist before the review, not be improvised during it.

## Consequences

### Positive

- **`ISSUE-0074` gets a correct objective before it is executed.** It is now a
  normalization review.
- It generalises past this review. Every future merge or split is judged the
  same way, including splits — a split that increases the entity count while
  separating two concepts is *also* normalization.
- It composes with `ADR-0067`. That decision keeps redundant entities out;
  this one keeps distinct concepts from being crushed together. They guard
  opposite failure modes.

### Negative

- **"Independent semantic concept" is not mechanically countable.** Entities are.
  The better objective is the less measurable one, and the review's outcome is
  therefore a judgement rather than a computation.
- Applied strictly, it may retain entities that look redundant on every
  structural metric. That is the intended behaviour and it will read as a failure
  to simplify.

### Neutral

- No entity changes. The review's objective changes.

## Compliance

`ISSUE-0074` and every subsequent merge or split decision states what semantic
independence is preserved, not how many entities were removed.
