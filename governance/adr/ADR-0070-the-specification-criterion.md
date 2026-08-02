---
id: ADR-0070
title: A Specification is justified by independent existence
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0074]
related: [ADR-0025, ADR-0027, ADR-0041, ADR-0057, ADR-0067, ADR-0069]
---

# ADR-0070 — The Specification criterion

## Context

`SESSION-0025` found that `StateMachine` introduces no relationship its
specification does not declare, and that `Dimension` has the same shape. The
tempting conclusion was that **`Specification` is a suffix the metamodel applies
where no distinction exists.**

That conclusion was wrong, and it was reached by structural similarity — which
can detect that two entities are 1:1 but **cannot say which of the two should
survive.**

## The hypothesis

> **Does a Specification define something whose instances may exist
> independently of Engineering OS?**

This is stronger than structural similarity because it asks *why* the pair
exists rather than *what shape* it has.

## The test, applied

| Entity | Instances exist independently? | Where they exist |
|---|---|---|
| `StateMachineSpecification` | **yes** | runtime executions, outside the repository |
| `Workflow` | **yes** | executions, outside the repository |
| `Policy` | **yes** | decisions made under it, outside the repository |
| `EngineeringGate` | **yes** | gate passages, outside the repository |
| `Skill` | **yes** | applications of the method, outside the repository |
| `DimensionSpecification` | **no** | a dimension has no runtime existence |
| `RegistrySpecification` | **no** | a registry is a list; it does not run |

## Decision

**A `Specification` entity is justified only when it defines something that can
have independent existence beyond the repository.**

The criterion resolves `ISSUE-0074` **in two opposite directions**, which is
precisely what structural similarity could not do.

### 1. `StateMachine` is removed; `StateMachineSpecification` is kept

Instances exist — as executions, outside the repository. So the specification is
real and correctly named.

**What was redundant was never the Specification. It was the phantom middle
layer** that claimed to be the instance while the actual instance was elsewhere.

### 2. `DimensionSpecification` is merged into `Dimension`

No independent existence, so nothing is being specified *for* anything. One
entity, named `Dimension`, holding the ten fields `ADR-0048` requires.

### 3. `RegistrySpecification` becomes `Registry`

Same reasoning, applied before the entity is written rather than after.

### The suffix rule

`Specification` is used when **both** hold:

1. instances exist independently of the repository, **and**
2. the unqualified name would be ambiguous (`ADR-0057`).

`Workflow`, `Policy`, `Skill` and `EngineeringGate` satisfy the first and not the
second — their execution counterparts already have distinct canonical names, so
`Workflow` unqualified means the specification and `Workflow Execution` means the
other thing.

`StateMachine` satisfied both, which is why it is the one entity carrying the
suffix.

## Semantic independence preserved

Required by `ADR-0069`: **after the merge, can everything that could be said
before still be said?**

| Change | Check |
|---|---|
| `StateMachine` removed | Its only relationship was `specified-by`, pointing at the entity that replaces it. Nothing was expressible through it alone |
| `Dimension` merged | The ten fields move intact; `DimensionAssignment.along` now points at `Dimension` directly, which is what it always meant |
| `Registry` renamed | Nothing specified yet |

**Two entities disappear because they were manifestations of one abstraction.**
No information is collapsed.

## Alternatives considered

**Remove `Specification` from the metamodel entirely.** Rejected — the
conclusion the previous session was heading toward. It would have deleted
`StateMachineSpecification`, the one specification the criterion shows is real,
and kept `StateMachine`, which is the empty half.

**Keep both halves everywhere pending more data.** Rejected. The criterion is
decisive on the cases in hand and the third data point it was waiting for —
`RegistrySpecification` — is answered by the criterion without needing to be
written first.

**Apply the criterion but retain the suffix uniformly for consistency.**
Rejected: it would rename `Workflow` to `WorkflowSpecification` and three others
besides, adding qualification where `ADR-0057` says none is needed.

## Consequences

### Positive

- **The metamodel drops from 28 confirmed entities to 26 without losing a single
  expressible statement.** Normalization, in `ADR-0069`'s sense.
- The criterion is predictive rather than retrospective: it answers
  `RegistrySpecification` before that entity is written.
- It gives a principled reason for an inconsistency that looked like sloppiness —
  why one entity carries the suffix and four others do not.
- **It draws the model's boundary.** A Specification whose instances live outside
  the repository is exactly where Engineering OS stops and the world begins,
  which is `ISSUE-0073`'s territory approached from a direction that does not
  require resolving it.

### Negative

- **"Independent existence" is a judgement**, and the easy cases were the ones
  tested. A future entity whose instances are partly inside and partly outside
  will not classify cleanly.
- Two accepted entity specifications are withdrawn.

### Neutral

- `Dimension` keeps a `Debt` note that it has no instances. That remains true.

## Compliance

`model/metamodel/entities/state-machine.md` and `dimension-specification.md` are
removed; `dimension.md` absorbs the ten fields. The inventory lists 26 confirmed
entities, with `Registry` in place of `RegistrySpecification`. Any future
`Specification` entity states which independently existing instances justify it.
