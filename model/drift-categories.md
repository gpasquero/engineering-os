---
id: MODEL-DRIFT-CATEGORIES
title: Knowledge Drift Categories
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0101, ADR-0106, ADR-0112, ADR-0114]
---

# Knowledge Drift Categories

The output of **Periodic Reacquisition** (`ADR-0112`): a fresh Candidate
Engineering Model compared against the current Authoritative Engineering Model.

> **Reacquisition validates and challenges the maintained model. It does not
> replace it.** Every item below is a **proposal requiring review.**

```yaml
drift-categories:
  - id: D-new-knowledge
    routes-to: ~
    routing-rationale: additive; curation alone suffices
    means: The candidate model contains assertions the authoritative model does not.
    detects: The repository grew, or extraction improved.
    intake: govern

  - id: D-unsupported-assertion
    routes-to: P-review-unsupported
    routing-rationale: retract or re-evidence
    means: >
      An authoritative assertion is no longer supported by current evidence.
    detects: The model claims something the repository no longer shows.
    intake: govern
    note: >
      One of the two categories the report exists for. May mean the evidence
      moved, the extractor changed, or the system changed — and only the third
      is a reason to retract.

  - id: D-implementation-without-knowledge
    routes-to: P-discover
    routing-rationale: extend the model over what exists
    means: Implementation exists that no modeled knowledge describes.
    detects: Code nobody described.
    intake: govern

  - id: D-knowledge-without-implementation
    routes-to: P-verify-capability
    routing-rationale: confirm it exists or retract the claim
    means: A modeled capability has no implementation evidence.
    detects: A description nothing implements.
    intake: govern

  - id: D-invariant-without-enforcement
    routes-to: P-establish-enforcement
    routing-rationale: find the enforcement point or record that none exists
    means: A modeled invariant has no enforcement evidence.
    detects: A rule nothing checks.
    intake: govern

  - id: D-dependency-change
    routes-to: ~
    routing-rationale: additive; a changed fact needs no engineering work
    means: Dependencies were added, removed or changed.
    detects: The boundary moved.
    intake: record

  - id: D-boundary-change
    routes-to: P-change-capability
    routing-rationale: the structure moved
    means: Architectural boundaries changed.
    detects: Modules, packages or contexts were restructured.
    intake: govern

  - id: D-conflicting-interpretation
    routes-to: P-resolve-conflict
    routing-rationale: a human decides; no rule can
    means: The candidate and authoritative models read the same evidence differently.
    detects: Two readings of one fact.
    intake: govern

  - id: D-missed-incremental-update
    routes-to: P-review-unsupported
    routing-rationale: the maintained model is now suspect
    means: >
      The candidate contains a change that continuous acquisition should have
      recorded and did not.
    detects: Continuous acquisition did not keep up.
    intake: govern
    note: >
      The second category the report exists for, and the only measurement of
      whether incremental maintenance is working.

  - id: D-stale-provenance
    routes-to: P-discover
    routing-rationale: the citation failed, not the claim
    means: A citation's source moved, changed or disappeared.
    detects: Provenance that no longer resolves.
    intake: govern

  - id: D-obsolete-rationale
    routes-to: P-change-concept
    routing-rationale: the decision behind the knowledge no longer stands
    means: A maintained assertion rests on a decision that has been superseded.
    detects: Knowledge whose reason expired while the knowledge remained.
    intake: govern

  - id: D-missing-evidence
    routes-to: P-discover
    routing-rationale: the claim may be sound; its citation is absent
    means: A maintained assertion carries no evidence at all.
    detects: Claims that entered the model without provenance.
    intake: govern

  - id: D-architectural-drift
    routes-to: P-change-capability
    routing-rationale: the structure moved away from what the model describes
    means: >
      The relationship between components differs from what the maintained model
      records — not a boundary appearing or disappearing, but the shape between
      them changing.
    detects: Erosion, which no single added or removed fact reveals.
    intake: govern

  - id: D-business-rule-drift
    routes-to: P-change-concept
    routing-rationale: the domain moved
    means: A maintained invariant's evidence now asserts something different.
    detects: A rule that changed rather than disappeared.
    intake: govern

  - id: D-unexplained-divergence
    routes-to: ~
    routing-rationale: unroutable by definition; escalates by having nowhere to go
    means: A difference that fits no other category.
    detects: Everything the taxonomy did not anticipate.
    intake: govern
```

## Each class routes to an Engineering Plan

`ADR-0114`. **A drift report is a work queue, not a document.**

Three classes route nowhere and each says why: two are additive, and
`D-unexplained-divergence` is **unroutable by definition** — a route for it
would be a guess, so it escalates by having nowhere to go.

**Routing says what kind of work this is, not what to do.** A routed item
produces a *plan*, and a plan defers what it cannot decide (`ADR-0094`).

## Only one category records mechanically

**`D-dependency-change`** — a dependency list is a fact, and a changed one is a
changed fact.

**Everything else is governed**, because every other category is a difference
whose *cause* is a judgement: the model may be stale, the repository may have
regressed, or the extractor may have changed.

## Debt

**Nothing computes drift.** The categories are declared and no comparison runs —
**Continuous Acquisition and Periodic Reacquisition are both unbuilt** and the
report cannot be meaningful until at least one incremental update has happened.

**`D-unexplained-divergence` will absorb more than it should.** Any comparison
taxonomy written before the first comparison is a guess, and the residual
category is where that guess will show.
