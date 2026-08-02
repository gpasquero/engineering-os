---
id: MODEL-INTERPRETIVE-FAILURES
title: Interpretive Failure Classification
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0108, ADR-0110]
---

# Interpretive Failure Classification

> **Do not call something an interpretation failure until the required mechanical
> evidence is known to be available** (`ADR-0110`).

```yaml
interpretive-failures:
  - id: F-fact-absent
    means: The required fact is not in the Mechanical Model.
    owner: mechanical acquisition
    remedy: Extend the Mechanical Model vocabulary and re-extract.
    note: >
      Not an interpretation failure. Every interpreter fails identically,
      however good, so attributing it to interpretation is a category error.

  - id: F-fact-ignored
    means: The fact was present in the Mechanical Model and the interpreter did not use it.
    owner: interpretation
    remedy: A better rule, or a different interpreter.
    note: >
      SESSION-0040's failure. The describe block was extracted and R1 read only
      it() names. Reported as a limit of determinism; it was a rule looking in
      the wrong place.

  - id: F-rule-insufficient
    means: The fact was used and the rule could not reach the conclusion.
    owner: interpretation
    remedy: A stronger rule, or a probabilistic interpreter.
    note: >
      The only classification that is evidence for probabilistic interpretation.
      Distinguishing it from F-fact-ignored is the whole point of the taxonomy.

  - id: F-evidence-ambiguous
    means: The evidence supports more than one reading.
    owner: neither
    remedy: Record both readings. Curation decides, or declines.
    note: Not a failure. Recorded so it is not miscounted as one.

  - id: F-representation-insufficient
    means: The conclusion cannot be expressed in the metamodel.
    owner: the metamodel
    remedy: A question first, then possibly an entity (ADR-0085).
    note: >
      The rarest, and the only one that should ever change Layer A. The metamodel
      has been unchanged for ten milestones.
```

## Why this exists

**`F-fact-absent` and `F-rule-insufficient` look identical from the outside** —
an interpreter did not produce a conclusion — and they have opposite remedies.

Extending the Mechanical Model when the rule was at fault produces a larger model
that fails the same way. Writing a better rule when the fact was absent produces
a better rule that fails the same way.

## Debt

**Classification is manual.** Nothing computes which failure kind applies; it
requires checking whether the fact is in the Mechanical Model, which a tool could
do and none does.

**`F-fact-ignored` is only detectable in hindsight.** It is recognised when a
later rule uses the fact — as `R3` did — and there is no way to detect it while
the better rule does not yet exist.
