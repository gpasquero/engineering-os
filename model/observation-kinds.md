---
id: MODEL-OBSERVATION-KINDS
title: Execution Observation Kinds
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0044, ADR-0061, ADR-0090, ADR-0100, ADR-0101, ADR-0104]
---

# Execution Observation Kinds

> **Workers never update the Canonical Knowledge Model. Workers emit
> observations. Engineering OS decides what enters** (`ADR-0101`).

Each kind declares its **intake outcome**:

| Outcome | Means |
|---|---|
| `record` | may enter the model mechanically |
| `govern` | requires authorization first (`ADR-0100`) |
| `reject` | cannot enter; recorded as a finding instead |

## The observation envelope (`ADR-0104`)

| Field | Is |
|---|---|
| `kind` | a registered kind, below |
| `statement` | what the worker observed |
| `evidence` | source and locator |
| `confidence` | `high` · `medium` · `low` — **an enumeration, never a number** |
| `reasoning` | why the worker concluded it |
| `affectedNodes` | model identifiers concerned |

**Confidence is a ratchet.** It may only add scrutiny:

| Declared intake | Confidence | Effective outcome |
|---|---|---|
| `record` | high | `record` |
| `record` | medium or low | **`govern`** |
| `govern` | any | `govern` |
| `reject` | any | `reject` |

**High confidence never lowers scrutiny** — the reason an observation is governed
is a property of the claim, not of the claimant.

**Confidence and reasoning are discarded at the boundary.** They inform intake
and never enter the Canonical Knowledge Model, so `ADR-0090` holds: no model node
carries a confidence field.

```yaml
observation-kinds:
  - id: O-invariant-confirmed
    asserts: A task checked an invariant and it held.
    intake: record
    produces: An Evidence node citing the execution, linked to the invariant.
    rationale: >
      Corroboration adds evidence without changing any assertion. The safest
      thing a worker can report.

  - id: O-evidence-discovered
    asserts: A task found a source supporting an existing assertion.
    intake: record
    produces: An Evidence node with the source and locator.
    rationale: >
      Adds provenance to something already claimed. Changes no meaning.

  - id: O-invariant-violated
    asserts: A task checked an invariant and it did not hold.
    intake: govern
    produces: A finding, and a proposed retraction of the enforcement claim.
    rationale: >
      Contradicts an accepted assertion. ADR-0101 forbids recording that
      mechanically, however credible the worker.

  - id: O-assumption-disproved
    asserts: A stated assumption turned out to be false.
    intake: govern
    produces: A finding, and a proposed ADR.
    rationale: >
      An assumption that fails usually means a decision was made on wrong
      grounds. That is a decision record, not a model edit.

  - id: O-unexpected-dependency
    asserts: The work touched something the model did not connect.
    intake: govern
    produces: A proposed relationship.
    rationale: >
      A new edge changes what impact analysis returns for everything
      downstream. Cheap to add, expensive to add wrongly.

  - id: O-documentation-drift
    asserts: An artifact and what it documents disagree.
    intake: govern
    produces: A finding, kind `documentation-gap`.
    rationale: >
      Which side is wrong is a judgement the observation does not contain.

  - id: O-implementation-differs-from-plan
    asserts: What was done differs from what the plan specified.
    intake: govern
    produces: A finding, and a review of the plan that produced the task.
    rationale: >
      Either the plan was wrong or the execution was. Both are governance.

  - id: O-architectural-concern
    asserts: A worker judges something structurally wrong.
    intake: reject
    produces: A finding, kind `architectural-concern`, with support `unsupported`.
    rationale: >
      A concern is an opinion, not an observation. It is worth recording and
      must never enter the model — ADR-0061: the compiler is not an
      intelligence, and neither is a worker.
```

## Only two kinds record mechanically

**Both are additive.** Confirming an invariant and discovering evidence add
support to what is already asserted; neither changes a meaning or removes a
claim.

**Everything that could change or contradict an assertion is governed**, and the
only kind that is purely a worker's judgement is **rejected outright.**

That distribution is the decision, not an accident: `ADR-0101` keeps the model
deterministic without discarding what execution learned.

## Debt

**The vocabulary is closed and execution will find things that fit none of it.**
Those become `reject` and are recorded as findings — honest and lossy.

**An observation is a worker's claim and may simply be wrong.** Intake decides
what may enter mechanically; it cannot decide what is true.

**`produces` is prose.** It says what an observation should become and nothing
constructs it — the proposals are described, not generated.
