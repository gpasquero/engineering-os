---
id: ADR-0128
title: Understanding Retention is a first-class product metric alongside coverage
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0118, ADR-0120, ADR-0123, ADR-0127, ADR-0129]
---

# ADR-0128 — Understanding Retention

## Context

`ADR-0120` made Engineering Question **coverage** the product metric. The
longitudinal experiment then produced a coverage reading that was true and
misleading in the same breath:

```text
t0   1/9 answered
t9   1/9 answered
```

The tool printed **"understanding held"**. It had not.

The one question answered at `t0` — *which capabilities would be affected by this
feature?* — **degraded to `partial` at `t1` and never returned**. A different
question became answerable later. Coverage netted the two to zero and called it
stability.

The reviewer named the missing metric:

> **Understanding Retention.** For each Engineering Question that was previously
> answerable: remained answered · degraded to partial · became unanswered.
>
> **Customers care whether Engineering OS forgets things they once relied on.
> Retention is therefore a first-class product property.**

## Decision

**Understanding Retention is a product metric, reported alongside coverage and
never merged with it.**

For every question **answered at an earlier measurement**, its state at a later
one is:

| | |
|---|---|
| `retained` | still answered |
| `degraded` | now `partial` |
| `lost` | now `no-data` or `no-query` |

**Retention rate = `retained` ÷ questions previously answered.**

**Gains are not retention.** A question that becomes answerable is Understanding
Growth (`ADR-0127`). Counting a gain as retention would let a system that forgets
everything it knew and learns something else score **100 %**, which is precisely
the substitution coverage already made.

**A verdict may not be read off coverage alone.** Where retention is below 100 %,
it governs the verdict. `tools/longitudinal.py` now reports *"understanding did
not survive"* on the run it previously reported as *"understanding held"*.

## Rationale

Coverage is a **level**; retention is a **flow**. A level can be constant while
everything underneath it turns over, and for this product the turnover is the
part a customer feels.

An engineer who relied on *"which capabilities would this feature affect?"* and
finds it no longer answered does not experience a stable 1/9. **They experience
a tool that forgot.** Nothing in the metric set could express that until now.

Retention is also the sharper instrument for the promise the project is
ultimately judged on — *can understanding be preserved as software evolves?*
Coverage measures a moment. **Retention measures survival**, which is the actual
claim.

## Consequences

**The first measurement is 0 %.** Of one question answered at `t0`, zero
retained, one degraded, one gained.

**Retention needs a baseline, so it is only defined over a sequence.** A single
benchmark run has coverage and no retention — which is one more reason the
longitudinal suite is permanent (`ADR-0129`).

**A small baseline makes the rate coarse.** One question answered at `t0` means
retention can only be 0 % or 100 %. That is a property of a weak model, not of
the metric, and it will refine itself as coverage improves.

**The metric is adversarial to the obvious fix.** Anything that raises coverage
by replacing what was answerable scores 0 % retention. That is the intended
behaviour.

## Compliance

- `tools/measure.py` exposes `retention(before, after)`; the longitudinal suite
  reports it.
- Retention and coverage are always reported together and never combined.
- A gain is never counted as retention.
