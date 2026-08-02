---
id: ISSUE-0074
title: Metamodel simplification review at approximately 75% completion
type: gap
status: deferred
severity: medium
created: 2026-08-02
updated: 2026-08-02
blocks: []
evidence:
  - model/metamodel/ontology/FINDINGS.md
  - model/metamodel/entity-inventory.md
  - model/metamodel/views/README.md
  - governance/adr/ADR-0067-the-relationship-is-the-design-unit.md
resolved-by: null
defers-to: [B1]
debt: architectural
---

# ISSUE-0074 — Metamodel simplification review

> **Scheduled work, deferred by decision** (`ADR-0062`). Not blocking. The
> trigger is a completion threshold, not a contradiction.
>
> **The trigger has been met** — 22 of 28 entities, and the three graph views the
> review is to be performed against exist (`model/metamodel/views/`). The review
> itself has not been performed.

## Statement

**When approximately 75% of the metamodel exists, perform a metamodel
simplification review.**

One explicit objective: **identify entity pairs that can be merged without
losing expressive power.**

## Why it matters

The metamodel is being built incrementally, and incremental construction
accumulates accidental complexity — distinctions that exist because the
architecture evolved that way, not because they carry meaning.

`ADR-0067` gives the review its instrument: *what new semantic relationship does
this entity introduce that cannot already be expressed?* Applied retroactively,
that question is what makes merging tractable.

**Doing this at 75% rather than at 100% is deliberate.** At completion, every
merge is a change to a finished thing. Before it, a merge changes what remains
to be built.

## What we know

**Two candidates are now confirmed**, and the second is stronger than the first.

| Candidate | Evidence |
|---|---|
| `StateMachine` / `StateMachineSpecification` | Introduces no relationship its specification declares (`ADR-0067` test, applied in `entities/state-machine.md`). **Pendant in every generated view.** Nothing points at it |
| `Dimension` / `DimensionSpecification` | Same 1:1 shape (`FINDINGS.md` #2). **A pass-through chain node in two independent views.** Defensible only on the grounds that `DimensionAssignment.along` reads better pointing at an axis |

The reviewer's instruction is explicit: **do not force them to remain separate
merely because the architecture originally evolved that way.**

**The Specification/Instance pattern was tested against a second independent
domain and did not survive.** State machines have the same empty middle layer.
The conclusion may therefore be larger than two merges: if
`RegistrySpecification` has the same shape, `Specification` is a suffix the
metamodel applies where no distinction exists.

**Genuine instantiation exists in both domains, but not where the pattern put
it** — for dimensions it is `DimensionAssignment`, which already exists; for
state machines it is an execution over time, which is Operational Knowledge and
deliberately outside the model (`ISSUE-0073`).

**A third structural candidate came from the graphs, not from the test.**
`governs` names three different relationships — constrains normatively, controls
the lifecycle of, may classify — and the ontology already had to rename one to
avoid a clash. That is a candidate tenth terminology split (`ADR-0057`), and it
belongs to this review.

**Neither premature optimisation nor preserved accidental complexity is
acceptable.** The threshold exists to hold that line.

## Options

Not a choice between answers. The review is the work, and its outcome is a set
of merge or retain decisions, each recorded.

## Resolution criteria

Resolved when the review has been performed **against the generated graph views
rather than the Markdown specifications**, and its outcome recorded as ADRs — one
per merge or explicit retention.

At minimum: `StateMachine`, `Dimension`, the `Specification` suffix as a general
question, and the `governs` collision.

**Trigger: approximately 75% of Layer A entities specified. Met** — 22 of 28.
