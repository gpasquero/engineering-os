---
id: ADR-0139
title: The longitudinal benchmark measures Guidance, over subjects nobody touched
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0128, ADR-0129, ADR-0133, ADR-0134, ADR-0135, ADR-0138]
---

# ADR-0139 — The benchmark measures Guidance

## Context

The frozen ten-commit suite has measured Acquisition since it was built. The
reviewer changed its role:

> Until now it has measured Acquisition. **Now it should begin measuring
> Guidance.** The question is no longer *"can Continuous Acquisition preserve
> understanding?"* It is becoming: **"Ten commits later, would Engineering OS
> still recommend the same engineering work?"**
>
> That feels like **the first benchmark directly connected to customer value.**

## Decision

**The suite measures Guidance Preservation alongside Understanding Retention,
and it measures it over subjects whose evidence nobody touched.**

The restriction is the whole design. **Guidance *should* change when the system
changes** — advice that ignored nine commits of real work would be preserving
staleness. So the only version that means anything is:

> **For a subject whose evidence nobody touched, is the recommended work the
> same?**

An untouched subject that receives different advice was affected by something
other than the system. **That is guidance drift.**

**Work is compared, wording is not.** A recommendation is fingerprinted as its
status plus, per action, the sorted ids of the items it names. Two
recommendations naming the same work in different prose are the same guidance —
which is `ADR-0134` applied to advice: the contract is what a team would *do*.

## The first reading

```text
Understanding Retention  100%   1 retained of 1
Guidance Preservation     80%   10 pairs over 8 untouched subjects
                                8 stable · 2 changed · 0 lost
```

**The two properties disagree on the same run**, which is exactly what
`ADR-0138` predicted and the first direct evidence for it.

## What the disagreement was

Both changes are `R-discover`, on `Artifact.AuthController` and
`Artifact.AuthServiceSpec` — two artifacts nothing touched across ten commits.

The cause: `R-discover` declares `applies-to: [Artifact]` — subject-specific
advice — and one of its steps uses `Q-unsupported`, declared **`subject: none`**.
That step returns the same list for every subject, and the list **grows as the
model grows**.

**Two untouched artifacts received different advice because the model had grown
around them.**

**Third appearance of one authoring error.** `EQ-09` scored 216/216 for the same
reason; `EQ-05` mixed the same way and was caught by a check written for it.
Each time a new consumer was built, the mistake was waiting in a new place.

`tools/check-plans.py` now reports model-wide steps inside subject-scoped advice.
**Whether the step belongs there is the author's call. Not being able to see it
was not.**

## Consequences

**The suite now measures both products** (`ADR-0135`) — Acquisition by
retention, Guidance by preservation — on one run, over frozen commits.

**Guidance Preservation is a proxy for the promise, not the promise**
(`ADR-0138`). 80 % says the advice was stable; it says nothing about whether it
was right.

**The denominator is small and that is reported.** Eight untouched subjects, from
a curation policy that accepted ten entities at an early commit. Like retention,
it is coarse, and the remedy is broader curation rather than a softer metric.

**It found a defect on its first run**, which is the same argument `ADR-0129`
made for keeping the suite: it is the only instrument here that can fail without
anything being broken.

## Compliance

- Guidance Preservation is computed over untouched subjects only.
- Fingerprints compare recommended work, never prose.
- Both properties are reported separately and never combined.
