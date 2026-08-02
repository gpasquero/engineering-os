---
id: ADR-0146
title: The product question moves from what we know to what an engineer should do next
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0080, ADR-0084, ADR-0123, ADR-0135, ADR-0136, ADR-0138, ADR-0139, ADR-0141]
---

# ADR-0146 — Guidance becomes the center

## Context

The reviewer named a transition already underway:

> Until now Engineering OS has mostly answered **"what do we know about this
> system?"** The next phase is **"what should an engineer do next?"**
>
> **That is a different product. Engineering Guidance is becoming the center.**

The evidence supports it from both sides. Acquisition is measured, strong and
declared mature (`ADR-0140`). Guidance was measured for the first time last
session, at **80 %**, and has never run against a model it did not build for
itself.

## Decision

**Engineering Guidance is the center of the product. Acquisition serves it.**

| | Was | **Now** |
|---|---|---|
| Question | what do we know about this system? | **what should an engineer do next?** |
| Delivers | answers | **actions** |
| Judged by | is it true? | **was it the right thing to do?** |
| Measured by | coverage, retention | **Guidance Preservation → Decision Preservation** |

**Three consequences follow.**

**1. An unanswered question is only interesting if some action depends on it.**
`EQ-01` — *why does this system work this way?* — matters because a team cannot
safely change what it cannot explain, not because the model is incomplete.

**2. Acquisition work is justified by the guidance it unlocks.** *We could
extract migrations* is not a reason; *a team cannot see which schema decisions
still stand* is.

**3. Correctness replaces truth as the standard.** An accurate answer that leads
to the wrong action has failed, and this is the same escalation `ADR-0136` made
of the North Star.

## Rationale

This is the fourth restatement of the product, and the first that changes the
*grammar* rather than the scope: from a noun — knowledge, understanding — to a
verb.

It also explains an imbalance that has been visible for several sessions and
looked like an accident. Guidance was built early — the Director, plans,
recommendations, task graphs, worker routing — and then left alone for twelve
milestones while acquisition was built underneath it. **It was not neglect. It
was built before there was anything for it to consume**, and there now is.

The reviewer's phrasing is precise: *that is a different product*. `ADR-0135`
already separated the two. **This decision says which one the project is now
building.**

## Consequences

**Acquisition is not finished and is no longer the frontier.** Deterministic
Discovery is mature (`ADR-0140`); the Brownfield Onboarding Skill remains the
active research area, and it is justified by curation throughput — which is a
guidance-side property (`ADR-0144`).

**Guidance's weakness is now the project's weakness.** 80 % preservation over
eight subjects, one recommendation found giving subject-specific advice from a
model-wide query, four recommendations in total, and no reading at all on whether
any of it is correct.

**The lifecycle is unchanged and its centre of gravity moves** (`ADR-0141`).
Stages 1–5 produce; stage 6 is what the customer came for.

**This does not license building guidance on weak understanding.** `ADR-0136`
still holds: guidance derived from understanding that degrades silently is worse
than no guidance. **Guidance is the centre; preservation is still the
precondition.**

## Compliance

- Work is justified by the engineering action it enables, not by the knowledge
  it adds.
- Acquisition proposals state which guidance they unlock.
- Guidance is not scaled beyond what measured understanding supports.
