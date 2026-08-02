---
id: ADR-0138
title: Decision Preservation is what the customer buys and it is not Understanding Preservation
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0128, ADR-0132, ADR-0133, ADR-0134, ADR-0136, ADR-0139]
---

# ADR-0138 — Decision Preservation

## Context

Understanding Retention reached 100 % and the reviewer immediately named its
limit:

> **The customer does not buy Understanding Preservation. The customer buys
> Decision Preservation. Those are not necessarily the same thing.**
>
> **Two systems may answer exactly the same Engineering Questions while
> recommending different engineering actions.**

and, in the same breath, forbade the obvious response:

> **I would resist the temptation to invent another metric.** Instead, begin
> thinking about how Decision Preservation could eventually become
> experimentally measurable. **Not today.**

## Decision

**Decision Preservation is a named product property. It is not measured, and no
metric is invented for it in this decision.**

> **Decision Preservation** — as software evolves, does an engineering team
> still reach the *correct* decision?

It sits above the three properties of `ADR-0133` and is not a fourth alongside
them:

```text
Knowledge Preservation      do we still know the same facts?
Understanding Preservation  can we still explain the system?     ← measured, 100 %
Guidance Preservation       is the recommended work the same?    ← measured, 80 %
Decision Preservation       does the team still decide correctly? ← the promise
```

**What separates Guidance from Decision is correctness.** Guidance Preservation
asks whether the advice is *the same*; Decision Preservation asks whether it is
*right*. A system that gives identical wrong advice for ten commits scores 100 %
on the first and fails the second entirely.

## Why no metric today

**Correctness cannot be self-certified** (`ADR-0023`). Every measurement this
project has is internal: the model checks itself against itself. A decision's
correctness is settled **outside** the system, by what happened next.

Any metric invented now would measure agreement with our own recommendations,
and would score 100 % on a system that has been confidently wrong throughout.
**That is the failure mode `ADR-0132` was written to prevent**, and it applies
with more force here because the flattery would be invisible.

## What would make it experimentally measurable

Recorded so the direction survives without being built:

**The evidence already exists in the repositories being measured.** A commit that
follows another commit *is* a decision a real team made, and history says which
ones were reverted, hot-fixed or re-done. An experiment could ask: **at `t0`, did
Engineering OS recommend the work the team actually did next — and was that work
subsequently undone?**

That is falsifiable, it uses an external oracle rather than our own model, and
it needs nothing new to exist. **It also needs the reviewer to define what makes
a decision correct**, which `ADR-0136` records as open.

## Consequences

**Guidance Preservation is a proxy and must be described as one.** 80 % means
*the advice was stable*, never *the advice was right*.

**No aggregate may combine the four properties.** A composite would let stable
wrong advice offset lost understanding — the exact substitution coverage already
made once (`ADR-0128`).

**The North Star is unchanged and now has its measurement path named**
(`ADR-0136`).

## Compliance

- Decision Preservation is named in reports as unmeasured.
- Guidance Preservation is never presented as evidence of correctness.
- No metric for Decision Preservation is introduced without an external oracle
  and a reviewer definition of correctness.
