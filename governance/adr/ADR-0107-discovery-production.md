---
id: ADR-0107
title: Discovery production is worker output; orchestration declarations are not a substitute for it
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0060, ADR-0090, ADR-0103, ADR-0105, ADR-0106]
---

# ADR-0107 — Discovery production

## Context

`SESSION-0038` declared Discovery in the existing registries, ran it through the
unchanged Director, and reported that **no execution mechanism was built** as the
strongest evidence for `ADR-0105`.

**That framing was wrong, and the correction matters.**

> The declarations define **how Discovery is directed.** Discovery Workers
> perform the actual reverse-engineering and knowledge-reconstruction work.
>
> **Do not treat orchestration declarations as a substitute for the discovery
> work itself.**

The visualizer, ontology and conceptual model cannot be generated from an empty
bootstrap Artifact. **They require substantive discovered knowledge.**

## Decision

**Brownfield onboarding has two equally necessary halves**, and neither is the
whole:

| Half | Produces |
|---|---|
| **Discovery production** | candidate engineering knowledge from an existing repository |
| **Proposal intake and application** | reviewed, authorized knowledge as authoring sources |

**The Proposal Applier solves only the second.**

### Three kinds of discovery worker

| Kind | Produces | Classified |
|---|---|---|
| **deterministic extractor** | what a file says; re-running reproduces it | `S-confirmed-deterministic`, `S-implemented`, `S-tested`, `S-specified` |
| **bounded interpreter** | a **named rule** applied to extracted assertions | `S-inferred` |
| **gap identifier** | what is absent | `S-unknown` — proposes no knowledge |

**Every inference names the rule that produced it.** An inference whose rule is
unnamed is indistinguishable from a guess.

### No language model participates in discovery production, for now

`ADR-0105` admits probabilistic interpreters. **None is built**, so the first
candidate model is reproducible and its digest is stable.

This is not a permanent constraint — it is `ADR-0103`'s ordering: **establish
what determinism can reach before delegating anything.** What it cannot reach is
now measured rather than assumed.

### A candidate model must allow partial and uncertain knowledge

Support classification (`model/support-classification.md`) distinguishes
confirmed, tested, implemented, specified, inferred, ambiguous, conflicting and
unknown. **These are kinds, not a scale** (`ADR-0090`).

**Discovery that could only propose what it was certain of would propose almost
nothing**, and would hide the ambiguity that is the most valuable thing it finds.

## Alternatives considered

**Treat the declarations as the deliverable.** Rejected — the reason for the
decision, and the error this corrects.

**Build a probabilistic interpreter immediately.** Rejected as premature: the
candidate model would not be reproducible, and **the deterministic ceiling would
never have been measured.** It now has been, and the measurement is the argument
for building one.

**Universal language support.** Rejected (`ADR-0105`). Workers are written for
the ai-desk stack; generalisation follows evidence, not anticipation.

## Consequences

### Positive

- **The deterministic ceiling is now a measurement rather than an opinion.** 315
  entities from a real repository, and a demonstrated quality limit.
- Reproducibility: the candidate model carries a content digest, and the same
  repository yields the same model.
- **Gaps and ambiguities are first-class output.** Discovery reports what it
  could not settle, which no parser does.

### Negative

- **Deterministic interpretation produces many assertions of low abstraction.**
  94 invariants were inferred from test names, and each is a transcription rather
  than a concept. **More assertions, worse abstractions** — measured in
  `external/ai-desk-onboarding/FINDINGS.md`.
- **The most important invariant was missed.** Tenant isolation is stated in ADR
  prose, and rule `R1` reads test names. A bounded rule cannot find what is not
  where it looks.
- Workers are stack-specific and will need writing again for the next stack.

### Neutral

- `ADR-0105` and `ADR-0106` are unchanged. What changes is what counts as having
  built Discovery.

## Compliance

Discovery production is `discovery/workers/`. **Orchestration declarations are
never reported as Discovery being built.** Every proposal carries provenance, a
support classification, its originating worker and task, and — where inferred —
the rule.
