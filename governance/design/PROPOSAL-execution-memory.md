---
id: PROPOSAL-EXECUTION-MEMORY
title: Proposal — the Engineering Experience layer
status: proposed
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0072, ADR-0090, ADR-0096, ADR-0101, ADR-0102, ADR-0103]
decision-required-from: Project Owner
---

# Proposal — the Engineering Experience layer

**Requested before implementation.** Nothing here has been built.

## The problem

Execution Observations are **ephemeral**. Each run classifies them, proposes what
may enter the model, and forgets everything else.

> **Without it the Director remembers the software but never learns
> engineering.**

Examples of what is currently lost:

- this recommendation repeatedly discovers the same missing invariant;
- this workflow consistently requires additional review;
- this capability often generates architectural concerns;
- this task almost always produces documentation drift.

**None of these is a fact about the software.** They are facts about **how
engineering behaves on this software** — and the direction is explicit that they
must not go in the Canonical Knowledge Model.

## Why they cannot go in the CKM

Three independent reasons, and any one suffices.

| Reason | From |
|---|---|
| The CKM is **the meaning of authoring sources**. No source asserts *this task usually produces drift* | `ADR-0072` |
| Every CKM edge is **asserted, never inferred**. An experience fact is derived from repetition, which is inference | `ADR-0044` |
| The CKM must **recompile deterministically from sources**. Experience is accumulated from runs and would not survive recompilation | `ADR-0081` |

**The two are different knowledge domains.** The software model describes the
system; Execution Memory describes how engineering evolves it.

## The proposal

### A separate layer, with its own store

`experience/` — outside `model/`, outside the CKM, never compiled into it.

**The Director reads both and confuses neither.** A plan draws its actions from
the CKM and its *cautions* from experience.

### An experience record is a counted fact, not an opinion

The single most important design constraint. `ADR-0103` forbids becoming less
deterministic, and a learning layer is exactly where that erodes.

```yaml
# NOT IMPLEMENTED — illustrative shape only
experience:
  - subject: {plan: P-change-implementation, action: inspect}
    pattern: observation-kind
    value: O-documentation-drift
    observed: 7
    of: 9
    firstSeen: <run id>
    lastSeen: <run id>
    runs: [<run id>, ...]
```

**Every field is a count or an identifier.** No score, no weight, no learned
parameter, no threshold that was fitted rather than declared (`ADR-0090`,
`ADR-0103`).

**Derivable mechanically** from the run log by counting — which is the answer to
`ADR-0103`'s culture question, and the reason this is admissible at all.

### What it may and may not do

| May | May not |
|---|---|
| **report**: *7 of 9 runs of this action produced documentation drift* | assert that this run will |
| add a **caution** to a plan, citing the counts | change what a plan derives |
| raise an observation's scrutiny — the `ADR-0104` ratchet, from history rather than self-report | lower scrutiny, ever |
| surface a pattern for a human to act on | act on it |

> **Experience may add caution. It may never remove it, and it may never add
> knowledge.**

That asymmetry is what keeps `ADR-0103` intact: the worst a wrong experience
record can do is make the system more careful.

### Three plausible uses, in order of confidence

1. **Cautions on plans.** *This action produced drift in 7 of 9 runs* appears
   beside the action. Purely additive, purely counted. **Clearly safe.**
2. **Ratchet input.** A kind that has been governed and rejected repeatedly
   escalates by history as well as by self-report. Safe by the same asymmetry.
3. **Plan selection.** An intent selecting between plans by which has historically
   required fewer governed observations. **This is the dangerous one** — it makes
   experience change what the Director *does*, and it should not be built with
   the first two.

## What must be built first, and is not part of this proposal

**A run log.** Experience is counted from runs, and **no run is currently
recorded.** `tools/direct.py` prints and exits.

The run log is a prerequisite, it is small, and it is independently useful — it
is what makes any claim about the KPI over time checkable. **It should be built
and used before any aggregation is designed**, because the shape of the
aggregation should come from friction in reading real logs (`ADR-0102`).

## The recommendation

**Build the run log now. Do not build the experience layer yet.**

The reasoning is `ADR-0102`'s own: *architectural change should originate from
friction observed during real execution rather than from hypothetical
completeness*. The four example patterns are hypotheses about what will repeat.
**Nothing has run twice.**

A run log costs little, is required by every version of this proposal, and turns
the aggregation question from a design exercise into an observation.

## Risks, stated plainly

**The layer's honest failure mode is looking useful while being noise.** With few
runs, *7 of 9* is indistinguishable from coincidence, and the record format
displays it with the same authority either way. Counts do not carry sample-size
judgement, and adding one would be a threshold — a score in disguise.

**It is the most likely place for probabilistic reasoning to enter the system.**
Every future extension — *similar tasks*, *related subjects*, *predicted
outcomes* — requires matching things that are not identical, and matching that is
not identity is inference. `ADR-0103` should be re-read before each such
extension.

**Experience and the CKM will be conflated by users** however carefully they are
separated, because both look like things the system knows.

## What would change the recommendation

| If | Then |
|---|---|
| runs accumulate and a pattern is visible by reading the log | build aggregation, shaped by that pattern |
| the run log proves sufficient on its own | do not build the layer |
| a real repetition is found that counting cannot express | reconsider — and record why, before building |

## Awaiting decision

**Nothing has been implemented.** The proposal recommends building **only the run
log**, and returning to the experience layer when there is something to
aggregate.
