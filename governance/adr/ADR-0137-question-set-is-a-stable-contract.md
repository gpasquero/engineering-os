---
id: ADR-0137
title: The Engineering Question Set is a stable contract and changes only under review
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0023, ADR-0120, ADR-0126, ADR-0132, ADR-0134]
---

# ADR-0137 — The question set is a stable contract

## Context

`ADR-0134` made the Engineering Question Set the product contract. A contract
that can be edited by the party it constrains is not one, and the reviewer
closed that gap:

> Engineering Questions are no longer just a benchmark. **They are becoming the
> contract of the product. Protect that. Everything underneath may evolve.
> Engineering Questions should remain stable.**

The risk is specific and it has a history here. Three times in four sessions an
authoring error in the metric moved a number in the flattering direction. **A
contract nobody may quietly widen is the only version that survives its own
author.**

## Decision

**The Engineering Question Set is stable. Everything underneath it may change
freely.**

| May change without review | May not change without review |
|---|---|
| predicates, rules, entities, edges | **the text of a question** |
| Stack Profiles, Discovery Skills | **the set of questions** |
| queries, recommendations, plans | **thresholds** |
| the compiler, emitters, tools | **`answered-by` mappings** |

**Four rules.**

**1. A question's text is never edited.** A question that needs different words
is a different question; the old one is retired and the new one added, so a
measurement history is never silently re-based.

**2. Adding, retiring or re-thresholding a question is a reviewer act**
(`ADR-0120`). The implementer proposes; the reviewer decides.

**3. Changing `answered-by` is a contract change.** It is the most tempting edit
available — a question can be made to pass by pointing it at a different query —
and it is therefore held to the same bar as adding one.

**4. A retired question keeps its id.** Ids are never reused, and past
measurements remain readable.

## Rationale

The contract's value is that it outlives the implementation, and everything this
project has learned came from a measurement that stayed still while something
underneath moved. `EQ-06` is the case: the question was fixed, the model changed
around it, and the fact that only the model moved is what made the reading
mean anything.

**If the question had been adjusted at any point in those ten commits, nothing
could have been concluded.**

## Consequences

**The set will look wrong before it looks right.** Nine questions, two answered,
one with no query at all. The temptation to prune `EQ-08` — permanently
`no-query` — is exactly what this decision forbids: **it is the clearest
statement in the product of what Engineering OS cannot do.**

**Stability is not permanence.** The reviewer has already named a second level
(`ADR-0126`) and capability families (`ADR-0134`). Both are additive and both
wait on evidence.

**Every measurement records the contract it was taken against**, so a future
change to the set does not invalidate the archive.

## Compliance

- Question text, membership, thresholds and `answered-by` change only by
  reviewer decision, recorded in an acceptance record.
- Retired questions keep their ids and are marked, never deleted.
- Published measurements name the questions they cover.
