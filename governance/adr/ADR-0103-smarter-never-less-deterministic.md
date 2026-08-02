---
id: ADR-0103
title: Engineering OS may become smarter; it may not become less deterministic
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0061, ADR-0092, ADR-0098, ADR-0101, ADR-0102]
---

# ADR-0103 — Smarter, never less deterministic

## Context

Every capability added from here — experience, learning, better routing — has a
cheaper probabilistic implementation than a deterministic one. **The pressure
runs one way**, and it will be applied one feature at a time, each individually
reasonable.

## Decision

**One invariant is explicitly protected:**

> **Engineering OS is allowed to become smarter. It is not allowed to become less
> deterministic.**

### The question that becomes design culture

Before any feature is proposed:

> **Can this decision be derived mechanically from existing engineering
> knowledge?**

**Only if the answer is genuinely no** should the responsibility be delegated to
a worker.

The word *genuinely* is the load-bearing one. *It would be easier with a model*
is not a no. *The information required is not present in any knowledge the system
holds* is a no.

### What this forbids concretely

- No stage before Execution invokes a language model (`ADR-0092`), **and no
  stage after it does either** — Review and Knowledge Update are deterministic.
- No heuristic where a rule would do (`ADR-0099`).
- No score where an enumeration would do (`ADR-0090`).
- **No capability is added probabilistically first with the intention of making
  it deterministic later.** That intention is never acted on.

### The ratchet

Determinism may increase and may never decrease. **A capability that is
deterministic today may not become probabilistic tomorrow**, even if a
probabilistic version is better — it must instead be shown that the deterministic
version was wrong.

## Alternatives considered

**State it as a goal rather than an invariant.** Rejected: a goal yields to
convenience one feature at a time, which is exactly the failure mode.

**Allow probabilistic implementations behind a deterministic interface.**
Rejected, and it is the most seductive option. A deterministic interface over a
probabilistic core produces answers that cannot be explained, and explanation is
what every artifact in this system exists to preserve.

**Allow exceptions with recorded justification.** Rejected. An invariant with a
documented exception process is a guideline, and this project already has enough
of those.

## Consequences

### Positive

- **It makes the pressure visible each time it is applied**, rather than after
  five features have quietly eroded the boundary.
- The design-culture question is cheap, answerable, and adversarial to
  hand-waving.
- **It protects the property that distinguishes this system** from every
  agent framework that coordinates models with models.

### Negative

- **Some genuinely valuable capabilities will be refused**, and they will be
  visibly available to anyone willing to use a model. Semantic similarity across
  differently-worded artifacts is the obvious one, and this decision forbids it.
- **The invariant is unfalsifiable in the direction that matters**: nothing
  detects a decision that *could* have been mechanical being delegated anyway.

### Neutral

- No artifact changes. What changes is what may be proposed.

## Compliance

Every proposed feature answers *can this be derived mechanically from existing
engineering knowledge?* **A capability that is deterministic is never replaced by
a probabilistic implementation**; it may only be shown to have been wrong.
