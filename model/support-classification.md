---
id: MODEL-SUPPORT-CLASSIFICATION
title: Support Classification
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0088, ADR-0090, ADR-0105, ADR-0106, ADR-0107]
---

# Support Classification

**What kind of support a proposed assertion has**, in a Candidate Engineering
Model.

> A candidate model must allow **partial and uncertain knowledge** (`ADR-0107`).
> Discovery that could only propose what it was certain of would propose almost
> nothing, and would hide the ambiguity that is the most valuable thing it finds.

**These are kinds, not a scale.** They are not ordered and they do not combine
(`ADR-0090`). An assertion may carry several.

```yaml
support-classification:
  - id: S-confirmed-deterministic
    means: Derived mechanically from a file. Re-running the extractor reproduces it.
    proposed-by: deterministic extractors
    review: May be accepted in batch — the claim is that a file says so.

  - id: S-tested
    means: A test asserts it. The test name or body is the evidence.
    proposed-by: deterministic extractors
    review: Batch-acceptable per suite; the mapping test→invariant is interpretive.

  - id: S-implemented
    means: Code implements it. A symbol, signature or route is the evidence.
    proposed-by: deterministic extractors
    review: Batch-acceptable.

  - id: S-specified
    means: A document states it. An ADR, README or design doc is the evidence.
    proposed-by: deterministic extractors
    review: Individual — a document stating something is not the system doing it.

  - id: S-inferred
    means: >
      Derived by a bounded rule from other assertions, not read from a source.
      The rule that produced it is named.
    proposed-by: bounded interpreters
    review: Individual. The rule may be sound and the instance wrong.

  - id: S-ambiguous
    means: Sources permit more than one reading, and the readings are recorded.
    proposed-by: any worker
    review: Individual, and the outcome may be to accept neither.

  - id: S-conflicting
    means: Two sources state incompatible things. Both are recorded.
    proposed-by: any worker
    review: >
      Individual and never batch. A conflict is the strongest finding kind
      (ADR-0090) and accepting one side silently discards the other.

  - id: S-unknown
    means: >
      A gap. Something the model would need and discovery did not find.
      Proposes no knowledge — only its absence.
    proposed-by: gap identifiers
    review: Not accepted into the model; recorded as a knowledge gap.
```

## Why `S-unknown` is a classification and not an absence

A gap that is not recorded is indistinguishable from a gap nobody looked for.
**`S-unknown` is how discovery reports what it could not find**, and it is the
only classification that proposes no assertion at all.

## Batch review, and where it stops

`ADR-0106` records that review does not scale, and that batch acceptance trades
scrutiny for throughput.

**This classification is where that trade is made explicit.** Deterministic
classifications may be accepted in batch because the claim is narrow — *this file
says this*. **`S-inferred`, `S-ambiguous` and `S-conflicting` are individual**,
because each involves a judgement no extractor made.

## Debt

**`S-implemented` and `S-tested` overlap.** A test is code; whether a test
asserting behaviour makes that behaviour *implemented* or *tested* is a judgement
the extractor makes by file path.

**Nothing enforces that a classification matches its evidence.** A worker may
label an inference `S-confirmed-deterministic`, and only review would catch it.
