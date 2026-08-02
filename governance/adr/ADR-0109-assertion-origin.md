---
id: ADR-0109
title: Every proposed assertion records its origin kind
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0090, ADR-0102, ADR-0104, ADR-0106, ADR-0107, ADR-0108]
---

# ADR-0109 — Assertion origin

## Context

A proposed assertion currently records **which worker** produced it. It does not
record **what kind of process** did.

> Recording the origin of every proposed assertion will become **one of the
> strongest quality metrics of Engineering OS over time.**

## Decision

**Every proposed assertion records an origin kind**, from a closed vocabulary:

| Origin | Means | Reproducible |
|---|---|---|
| `mechanical-extraction` | read from a file | **yes, exactly** |
| `deterministic-rule` | a named rule over the Mechanical Model | **yes, exactly** |
| `probabilistic-interpretation` | a language model over the Mechanical Model | no |
| `human-proposal` | a person proposed it | no |

**Origin is what the process was. Support is what the evidence is**
(`support-classification.md`). They are independent: a deterministic rule may
produce a well-supported assertion, and a human may propose an unsupported one.

### What it makes measurable

**The composition of a model over time**, which no other field reports:

- what fraction of knowledge is reproducible, and whether that fraction falls as
  the system grows;
- whether a probabilistic interpreter's proposals survive review at a different
  rate than a deterministic rule's;
- **whether adding an LLM improved abstraction or only volume** — the question
  `SESSION-0039` could not answer.

### It is a composition, never a score

`ADR-0090`. Origin is reported as **counts by kind**, never combined into a
number, never weighted, never thresholded.

**A model that is 100% `mechanical-extraction` is not better than one that is
60%.** It is differently composed, and the useful reading is the trend against a
fixed corpus.

## Alternatives considered

**Infer origin from the worker.** Rejected: a worker may use more than one
process, and a probabilistic interpreter with a deterministic fallback would be
indistinguishable in its output.

**Record only reproducible versus not.** Rejected as too coarse — it would merge
`probabilistic-interpretation` with `human-proposal`, and those differ in exactly
the way that matters for review.

**Add a quality score derived from origin.** Rejected under `ADR-0090`, and it is
the obvious next step someone will propose.

## Consequences

### Positive

- **The composition of a model becomes a measurement**, and it is the measurement
  that makes `ADR-0108`'s comparison meaningful.
- Review can be routed by origin as well as by support: a probabilistic proposal
  is individually reviewed regardless of how well supported it claims to be.
- **A model can state what fraction of itself is reproducible** — which is the
  honest answer to *how much of this do you actually know?*

### Negative

- **Origin is self-reported by the worker**, and nothing verifies it. A
  probabilistic interpreter could label its output `deterministic-rule`, and only
  re-running it would reveal the difference.
- Four kinds will prove insufficient. *Deterministic rule with a probabilistic
  tie-break* has no entry, and hybrid processes are the likely direction.

### Neutral

- No existing assertion changes meaning. Each gains a field.

## Compliance

`model/assertion-origins.md` declares the vocabulary and is registered. Every
proposed assertion carries an origin. **Origin is reported as counts by kind and
never as a score.**
