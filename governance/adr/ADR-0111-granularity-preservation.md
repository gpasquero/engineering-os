---
id: ADR-0111
title: Abstraction and specificity coexist; the relation is specializes, and no entity is added
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0067, ADR-0071, ADR-0085, ADR-0096, ADR-0108]
---

# ADR-0111 — Granularity preservation

## Context

`R1` proposed eight invariants from eight test cases. `R3` proposed one from the
`describe` block. **`R3` reaches the concept and loses the specific guarantee**:
`NoUserEnumeration` survives at case level and is absorbed at suite level.

> **Do not flatten detailed guarantees into broad abstractions. Do not keep only
> detailed assertions and lose the concept they collectively establish.**

> **The exact modeling relation should be determined by existing metamodel
> constructs before introducing a new entity.**

## The question, answered with what exists

**Is a specific guarantee a new kind of thing?**

`Invariant` is *"a condition that must hold, stated independently of whatever
enforces it"*. **"Locks the account on the 5th wrong password for exactly 15
minutes" is a condition that must hold.** So is "account lockout &
brute-force protection". They differ in **specificity, not in kind.**

A `Guarantee` entity would therefore fail `ADR-0067`: it introduces no semantic
relationship `Invariant` cannot express.

**The relation between them already exists.** `specializes` is a registered core
relationship type — structural, meaning *A is a narrower kind of B*
(`ADR-0071`).

## Decision

**Both levels are proposed as `Invariant`, related by `specializes`. No entity is
added.**

```text
Invariant.AccountLockout                          ← the concept
    ▲ specializes
Invariant.LocksOnFifthFailureFor15Minutes         ← the specific guarantee
    │ evidenced-by
Evidence — it('locks the account on the 5th …')   ← the test case
```

**The test case is `Evidence` for both**, and each invariant cites it directly:
the specific one because the case states it, the general one because the case is
among those that collectively establish it.

### The rule that produces this

`R4` proposes the `describe` block as the general invariant and each rule-stating
case as a specific one that `specializes` it. **One rule, both levels**, and
neither is lost.

### What this rejects

**Choosing.** `R1` and `R3` were framed as alternatives and neither dominates —
which was itself the finding, and the resolution is not to pick the better one.

## Alternatives considered

**A `Guarantee` entity.** Rejected under `ADR-0067`: no new relationship. It
would also add a fourth thing readers must place relative to `Invariant`,
`Policy` and `ValidationRule`, three of which already occupy nearby ground.

**The specific case as `Evidence` only.** Rejected: `Evidence` is *a reference to
an observable fact cited in support of an assertion*. A test case is both a
reference **and** an assertion — modelling it only as evidence discards the rule
it states, which is exactly the flattening this decision forbids.

**A `Dimension` classifying invariants by granularity.** Rejected under
`ADR-0049`'s scarcity conditions: it would classify one entity type, which fails
condition 1.

**Keep both as unrelated invariants.** Rejected — it preserves the assertions and
loses the fact that they are the same subject at two levels, so impact analysis
would miss one when asked about the other.

## Consequences

### Positive

- **Both readings survive**, and a query can ask for either: the concept for
  planning, the guarantee for verification.
- **No metamodel change** — the tenth consecutive milestone.
- `specializes` acquires its first real use outside `Actor`, which is evidence
  the core vocabulary was correctly sized.

### Negative

- **Invariant counts stop being comparable across strategies.** `R4` proposes
  both levels, so *number of invariants* now conflates concepts and guarantees,
  and the benchmark must count them separately.
- **A specific invariant with no general one is now anomalous**, and nothing
  detects it. A case-level assertion outside any `describe` block has no parent.

### Neutral

- `R1` and `R3` remain available as comparison baselines.

## Compliance

`discovery/interpretive.py` implements `R4`. **Both levels are proposed when both
are supported**, related by `specializes`. No `Guarantee` entity exists.
