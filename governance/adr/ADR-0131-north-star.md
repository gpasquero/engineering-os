---
id: ADR-0131
title: The North Star is whether Engineering OS preserves engineering understanding as software evolves
status: superseded
date: 2026-08-02
supersedes: null
superseded-by: ADR-0136
resolves: []
related: [ADR-0116, ADR-0119, ADR-0120, ADR-0123, ADR-0127, ADR-0128, ADR-0129, ADR-0130]
---

# ADR-0131 — The North Star

> **Superseded by `ADR-0136`.** The subject moves from the model to the team:
> preserving understanding is necessary and is not the promise. The instrument,
> the severity and the ordering below all survive unchanged.

## Context

The project has restated its objective nine times. The reviewer states the tenth
and calls it the last conceptual phase:

> The question is no longer **"Can Engineering OS acquire engineering
> knowledge?"** It has already demonstrated that.
>
> The question has become: **"Can Engineering OS preserve engineering
> understanding as software evolves?"**
>
> That is the promise customers will actually evaluate. I would optimize every
> future architectural decision against that single question.

## Decision

**The North Star is: can Engineering OS preserve engineering understanding as
software evolves?**

Every architectural decision is judged against it. Where an admission test and
the North Star disagree, **the North Star governs** — the tests are instruments
and this is the objective.

**Three words carry the whole claim, and each rules something out.**

**Preserve** — not acquire. Acquisition is demonstrated: two stacks, two
repositories, 299 and 453 proposals, no metamodel change. **Nothing further is
proven by acquiring more.**

**Understanding** — not knowledge. The distinction is `ADR-0127`, and it exists
because the longitudinal run grew knowledge 9× and understanding not at all.

**As software evolves** — not at a moment. A benchmark cannot test this;
`ADR-0129`'s frozen suite is the only instrument that can, which is why it is
permanent.

## What this promotes and demotes

| Was | Now |
|---|---|
| more repositories benchmarked | **more commits survived** |
| coverage | **coverage and retention**, and retention decides the verdict |
| what Discovery proposes | **what survives ten commits of maintenance** |
| Acquisition, the strongest verb | **the four verbs that keep understanding alive** |

**Acquisition is demoted from objective to prerequisite.** It remains necessary
and it is no longer where the risk is.

## Rationale

The claim is falsifiable, and it has already been falsified once. That is the
argument for it: it is the first framing this project has had that **could
return a bad answer**, and the first time it was asked, it did.

Every earlier framing — metamodel completeness, semantic answers, engineering
value, the Director, autonomy, orchestration, brownfield acquisition,
understanding — could be satisfied by building something. This one can only be
satisfied by something **surviving**, and survival cannot be built in a session.

It also matches what a customer can check without trusting us. A customer cannot
evaluate a metamodel or a proposal count. **They can evaluate whether the thing
they relied on last quarter still works this quarter.**

## Consequences

**The immediate work is unchanged and its justification is stronger.** `ADR-0130`
— preserve the four lost semantic relationships — is the North Star's first
concrete instance: retention is 0 %, and the cause is understanding that the
maintenance path never carried forward.

**Guidance is deferred behind preservation.** `ADR-0123` names Guidance as the
verb customers buy, and it is the weakest. It stays deferred: **guidance derived
from understanding that does not survive would be advice with a shelf life
nobody was told about.**

**"How do engineering teams work differently?" is the phase after this one.** The
reviewer named it in `ACCEPT-0042` and it is not abandoned — it is sequenced.
A team cannot work differently on the strength of understanding that degrades
silently.

**A session may now be judged to have made no progress even if it built
something**, and that is the intended severity.

## Compliance

- Architectural proposals state how they help understanding survive evolution.
- Where an admission test and the North Star conflict, the North Star governs
  and the conflict is recorded.
- The frozen longitudinal suite is the instrument of record.
