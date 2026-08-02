---
id: ADR-0102
title: Autonomy is the target; the KPI becomes decisions that never require an LLM
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0089, ADR-0093, ADR-0098, ADR-0103]
---

# ADR-0102 — Autonomy is the target

## Context

`ADR-0098` measured **decisions made before the first LLM token**. That measure
rewards moving work upstream, and it is satisfied by a system that still hands
every hard decision to a worker — just later.

> **For the first time Engineering OS behaves as an operating system for
> engineering rather than a semantic compiler.**

## Decision

**The objective is autonomy: progressively reduce the engineering judgment
delegated to workers.**

The KPI evolves:

| From | To |
|---|---|
| decisions **before the first LLM token** | **decisions that never require an LLM** |

The first counts sequence. **The second counts elimination**, and only the second
improves when a decision moves from a worker into the system permanently.

### Both are reported, and the difference is the signal

A decision that is *made upstream* and a decision that *never needs a worker* are
different achievements. Reporting only the second would hide progress; reporting
only the first would reward deferral dressed as ordering.

**The gap between them is the work remaining.**

### Infrastructure stops being built for its own sake

> **Stop building internal infrastructure unless it directly improves the
> Engineering Director.**

The architecture is sufficiently rich. A new registry, entity, operator or engine
is admitted only if it removes a decision from a worker or makes the Director
useful on real work.

### Architectural change now originates from friction

> **Every future architectural change should originate from friction observed
> during real execution rather than from hypothetical completeness.**

This is the strongest form of `ADR-0062`'s *architecture through implementation*,
and it retires the mode the project has operated in for thirty-six sessions:
identifying a gap by inspection and filling it.

## Alternatives considered

**Keep the `ADR-0098` KPI.** Rejected: it is satisfied by decomposition alone. A
system that splits one hard decision into five and hands all five to a worker
scores better, not worse.

**Measure the fraction of tasks that are mechanical.** Rejected — it improves by
adding trivial mechanical tasks, which is the same defect one level down.

**Set an autonomy target percentage.** Rejected under `ADR-0090`: a ratio is a
score, and the enumerated lists carry information a ratio destroys.

## Consequences

### Positive

- **The measure now rewards the thing that matters**, and cannot be satisfied by
  rearrangement.
- It gives infrastructure a hard admission test at the milestone level.
- **Friction-driven change is falsifiable**: either a real run produced the
  friction or it did not.

### Negative

- **The number will move very slowly, and may not move at all for several
  milestones.** Genuinely eliminating a judgement is far harder than sequencing
  it, and a flat KPI will look like no progress when it may be honest.
- **Some decisions must never be eliminated.** A system that eventually delegates
  nothing has started guessing, and this decision states no limit — the same
  unresolved tension `ADR-0093` recorded.

### Neutral

- No artifact changes. What changes is what counts as progress.

## Compliance

Every milestone reports both numbers. **Infrastructure is admitted only when it
removes a decision from a worker or makes the Director useful on real work**, and
architectural change cites the real execution whose friction motivated it.
