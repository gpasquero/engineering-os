---
id: MODEL-FINDING-KINDS
title: Finding Kinds
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
artifact-kind: authoritative
established-by: [ADR-0031, ADR-0090]
---

# Finding Kinds

**Not every finding deserves the same weight** (`ADR-0090`). A system that
presents a documentation gap and a contradiction identically is misleading.

> **Evidence quality is expressed through provenance and support classification,
> never through a confidence score.** Engineering evidence is not probabilistic.
> A number answers *how much* and destroys *why*.

## The taxonomy

Ordered by the strength of the claim the kind licenses.

```yaml
finding-kinds:
  - id: confirmed-contradiction
    rank: 1
    strength: strongest
    claims: Two sources state incompatible things.
    requires: Both sources quoted, both fetched, incompatibility stated explicitly.

  - id: behavioral-inconsistency
    rank: 2
    strength: strong
    claims: The implementation and the stated behaviour disagree.
    requires: The stated behaviour and the implementing artifact, both cited.

  - id: architectural-inconsistency
    rank: 3
    strength: strong
    claims: The structure violates a stated decision.
    requires: The decision and the structure violating it, both cited.

  - id: traceability-gap
    rank: 4
    strength: moderate
    claims: Something exists with no path to its rationale.
    requires: The thing, and the demonstrated absence of a path.

  - id: documentation-gap
    rank: 5
    strength: moderate
    claims: Something is true and no document states it.
    requires: The sources that each state part of it, and none that states it whole.

  - id: observability-gap
    rank: 6
    strength: moderate
    claims: Something is true and is not visible where it matters.
    requires: The fact, and where a reader would look and not find it.

  - id: ambiguous-evidence
    rank: 7
    strength: weak
    claims: The sources permit more than one reading.
    requires: The readings, and why the sources do not decide between them.

  - id: missing-evidence
    rank: 8
    strength: weakest
    claims: The model cannot support the claim at all.
    requires: Naming the claim, and what would be needed to support it.
```

## How kind and support compose

They answer different questions and are both required.

| | Answers |
|---|---|
| **kind** | *what was found* |
| **support** | *how well it is evidenced* — `confirmed`, `incomplete`, `ambiguous`, `unsupported` (`ADR-0088`) |

A `confirmed-contradiction` with `support: ambiguous` is not a contradiction; it
is `ambiguous-evidence`. **A finding may not claim a kind stronger than its
support permits.**

## Debt

**Classification is a judgement made by the author of the finding**, and nothing
checks it. The incentive runs the wrong way: labelling a documentation gap as a
contradiction makes a result look better.

**`documentation-gap` and `traceability-gap` overlap.** The first is about a
document not saying something; the second about no path existing to a rationale.
A finding can be both, and the Kubernetes result nearly is.

**Eight kinds is a guess from one validation.** Ranks 1–3 have never been used.
