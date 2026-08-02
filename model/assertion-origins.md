---
id: MODEL-ASSERTION-ORIGINS
title: Assertion Origins
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0090, ADR-0108, ADR-0109]
---

# Assertion Origins

**What kind of process produced a proposed assertion** (`ADR-0109`).

> **Origin is what the process was. Support is what the evidence is.** They are
> independent — a deterministic rule may produce a well-supported assertion, and
> a human may propose an unsupported one.

```yaml
assertion-origins:
  - id: O-mechanical-extraction
    means: Read from a file by a mechanical extractor.
    stage: mechanical
    reproducible: exactly
    review: >
      Batch-reviewable. The claim is narrow: a file says this. Re-running
      reproduces it byte for byte.

  - id: O-deterministic-rule
    means: A named rule applied to the Mechanical Engineering Model.
    stage: interpretive
    reproducible: exactly
    review: >
      Individual by default. The rule may be sound and the instance wrong, and
      the rule is named so the instance can be judged against it.

  - id: O-probabilistic-interpretation
    means: A language model applied to the Mechanical Engineering Model.
    stage: interpretive
    reproducible: no
    review: >
      Always individual, regardless of claimed support (ADR-0104). A
      probabilistic proposal is never batch-accepted.

  - id: O-imported-authoritative
    means: >
      Imported from a source that was already authoritative elsewhere — a
      Knowledge Package, or a model accepted in another repository.
    stage: interpretive
    reproducible: exactly
    review: >
      Individual. Authority does not cross repositories: an import carries its
      acceptance history as provenance and does not confer status locally
      (ADR-0019).

  - id: O-human-proposal
    means: A person proposed it.
    stage: interpretive
    reproducible: no
    review: >
      Individual, and the reviewer must not be the proposer (ADR-0023).
```

## Probabilistic proposals carry more

A `O-probabilistic-interpretation` proposal is not auditable from its statement
alone. It additionally records:

| Field | Why |
|---|---|
| `model` and `version` | the same prompt to a different model is a different worker |
| `task-contract` | the prompt or contract it was given |
| `input-evidence` | **identifiers of the mechanical facts it saw** |
| `assumptions` | what it stated it assumed |
| `uncertainty` | its own `high`/`medium`/`low` (`ADR-0104`) |
| `run` | the originating run |

**`input-evidence` is the one that makes comparison possible.** Two interpreters
are comparable only if what each saw is recorded, and `ADR-0108` makes the
Mechanical Model that shared input.

## Reported as a composition, never a score

`ADR-0090`. Counts by kind — **never combined, weighted or thresholded.**

**A model that is 100% `O-mechanical-extraction` is not better than one that is
60%.** It is differently composed, and the useful reading is the trend against a
fixed corpus: *did adding an interpreter improve abstraction, or only volume?*

## Debt

**Origin is self-reported and nothing verifies it.** A probabilistic interpreter
could label its output `O-deterministic-rule`, and only re-running would reveal
the difference. **Re-running is the check, and nothing runs it.**

**Four kinds will prove insufficient.** *Deterministic rule with a probabilistic
tie-break* has no entry, and hybrids are the likely direction.

**`stage` duplicates information that `ADR-0108` already fixes**: mechanical
extraction is stage one and everything else is stage two. It is recorded here so
that a reader of a single assertion does not need the ADR.
