---
id: ADR-0104
title: Worker confidence is an intake signal that may only add scrutiny, never model content
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0061, ADR-0088, ADR-0090, ADR-0101, ADR-0103]
---

# ADR-0104 — Worker confidence

## Context

The direction is that workers should emit **structured confidence** rather than
free-form observations: *Observation · Evidence · Confidence · Reasoning ·
Affected Nodes*.

**This conflicts with an accepted decision.** `ADR-0090` states:

> *Do not evolve toward confidence scores. Engineering evidence is not
> probabilistic. Instead continue expressing evidence quality through provenance
> and support classification.*

The conflict is real. Recording it rather than absorbing it is what `ADR-0002`
requires of an accepted decision.

## The distinction that resolves it

`ADR-0090` governs **Engineering OS's own conclusions** — findings it derives
from the model. Those must never carry a score, because the system derived them
deterministically and a number would imply a judgement it did not make.

**A worker's confidence is a different object.** The worker *is* probabilistic.
Reporting its own uncertainty is the most honest thing it can do, and suppressing
it discards information the system would otherwise have to guess at.

> **`ADR-0090` forbids Engineering OS from scoring its conclusions. It does not
> forbid a probabilistic executor from reporting its own uncertainty.**

## Decision

**A worker may report confidence. Engineering OS never stores it.**

### The observation envelope

| Field | Is |
|---|---|
| `kind` | a registered observation kind (`ADR-0101`) |
| `statement` | what the worker observed |
| `evidence` | what supports it — source, locator |
| `confidence` | `high` · `medium` · `low` — **an enumeration, never a number** |
| `reasoning` | why the worker concluded it |
| `affectedNodes` | model identifiers the observation concerns |

### Confidence is a ratchet: it may only add scrutiny

| Declared intake | Worker confidence | Effective outcome |
|---|---|---|
| `record` | high | `record` |
| `record` | medium or low | **`govern`** |
| `govern` | any | `govern` |
| `reject` | any | `reject` |

**High confidence never lowers scrutiny.** A governed observation stays governed
however certain the worker is, because the reason it is governed has nothing to
do with the worker's certainty.

**Low confidence raises it.** That is the only effect confidence has.

### It is discarded at the boundary

Confidence, reasoning and the free-form statement **inform the intake decision
and do not enter the Canonical Knowledge Model.** What enters is what an
authorized proposal produces: an assertion, with provenance.

**A model node never carries a confidence field**, and `ADR-0090` holds intact.

## Alternatives considered

**Reject the direction and keep free-form observations.** Rejected: the reviewer
is right that structure is better than prose, and the conflict is with *scoring
conclusions*, not with *structured self-report*.

**Accept numeric confidence.** Rejected. A number invites arithmetic — averaging,
thresholding, combining — on a judgement made by a probabilistic process, and
`ADR-0090`'s argument against that is unchanged.

**Let confidence lower scrutiny when high.** Rejected, and this is the important
rejection. It would make a worker's self-assessment able to bypass governance,
which inverts `ADR-0101`: **the reason an observation is governed is a property
of the claim, not of the claimant.**

**Supersede `ADR-0090`.** Rejected: its reasoning about the system's own
conclusions is correct and untouched. The two decisions govern different objects,
and that distinction is worth keeping visible.

## Consequences

### Positive

- **The conflict is resolved rather than absorbed**, and both decisions survive
  with their scope clarified.
- Structured observations are better inputs than prose, and the ratchet means the
  structure can only make the system more careful.
- **A low-confidence worker output can no longer enter the model mechanically**,
  which is a real safety improvement over the current design.

### Negative

- **Three levels is a scale, and a scale is a scoring system with fewer values.**
  The line between an enumeration and a score is defensible and thin, and it will
  be pushed.
- **Workers will report high confidence by default**, so the ratchet's protection
  depends on a self-report that is systematically optimistic. It adds scrutiny
  exactly when a worker is honest enough to admit doubt.

### Neutral

- `ADR-0090` is unchanged. No model node gains a field.

## Compliance

`model/observation-kinds.md` documents the envelope. `compiler/direct/` applies
the ratchet. **No confidence value is written to the Canonical Knowledge Model**,
and no code averages, thresholds or combines confidence values.
