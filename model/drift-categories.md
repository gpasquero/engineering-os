---
id: MODEL-DRIFT-CATEGORIES
title: Knowledge Drift Categories
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0101, ADR-0106, ADR-0112]
---

# Knowledge Drift Categories

The output of **Periodic Reacquisition** (`ADR-0112`): a fresh Candidate
Engineering Model compared against the current Authoritative Engineering Model.

> **Reacquisition validates and challenges the maintained model. It does not
> replace it.** Every item below is a **proposal requiring review.**

```yaml
drift-categories:
  - id: D-new-knowledge
    means: The candidate model contains assertions the authoritative model does not.
    detects: The repository grew, or extraction improved.
    intake: govern

  - id: D-unsupported-assertion
    means: >
      An authoritative assertion is no longer supported by current evidence.
    detects: The model claims something the repository no longer shows.
    intake: govern
    note: >
      One of the two categories the report exists for. May mean the evidence
      moved, the extractor changed, or the system changed — and only the third
      is a reason to retract.

  - id: D-implementation-without-knowledge
    means: Implementation exists that no modeled knowledge describes.
    detects: Code nobody described.
    intake: govern

  - id: D-knowledge-without-implementation
    means: A modeled capability has no implementation evidence.
    detects: A description nothing implements.
    intake: govern

  - id: D-invariant-without-enforcement
    means: A modeled invariant has no enforcement evidence.
    detects: A rule nothing checks.
    intake: govern

  - id: D-dependency-change
    means: Dependencies were added, removed or changed.
    detects: The boundary moved.
    intake: record

  - id: D-boundary-change
    means: Architectural boundaries changed.
    detects: Modules, packages or contexts were restructured.
    intake: govern

  - id: D-conflicting-interpretation
    means: The candidate and authoritative models read the same evidence differently.
    detects: Two readings of one fact.
    intake: govern

  - id: D-missed-incremental-update
    means: >
      The candidate contains a change that continuous acquisition should have
      recorded and did not.
    detects: Continuous acquisition did not keep up.
    intake: govern
    note: >
      The second category the report exists for, and the only measurement of
      whether incremental maintenance is working.

  - id: D-stale-provenance
    means: A citation's source moved, changed or disappeared.
    detects: Provenance that no longer resolves.
    intake: govern

  - id: D-unexplained-divergence
    means: A difference that fits no other category.
    detects: Everything the taxonomy did not anticipate.
    intake: govern
```

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
