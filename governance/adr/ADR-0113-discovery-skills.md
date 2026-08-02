---
id: ADR-0113
title: Discovery Skills are engine-independent investigation contracts owned by Engineering OS
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0033, ADR-0081, ADR-0099, ADR-0104, ADR-0108, ADR-0109, ADR-0110]
---

# ADR-0113 — Discovery Skills

## Context

The probabilistic worker in `SESSION-0041` was given an ad-hoc instruction. It
produced useful proposals and **nothing about the run was reusable**: no contract,
no output schema, no stopping condition, and no way to run the same
investigation with a different model.

> **A Discovery Skill is not merely a prompt. The Skill belongs to Engineering
> OS. The model is only a worker implementation.**

## Decision

**A Discovery Skill is an engine-independent investigation contract**, declaring
eleven things:

| Field | States |
|---|---|
| objective | what the investigation is for |
| required inputs | what must be provided |
| evidence to inspect | which parts of the Mechanical Model |
| questions to answer | what the skill is asking |
| permitted tools | what the worker may use |
| expected proposal types | what it may propose |
| required provenance | what every proposal must cite |
| uncertainty reporting | how it states what it is unsure of |
| stopping conditions | when it is done |
| output schema | the shape it must return |
| review expectations | how curation should treat the result |

### The Skill is the asset; the model is interchangeable

This is `ADR-0099` applied to acquisition. **A worker declares capabilities; a
Skill declares an investigation.** Claude, Codex or another model executes it,
and **no model is named in any Skill.**

Two consequences follow, and both are the point:

- **The same Skill is runnable by a different model**, which is what makes a
  comparison meaningful rather than a comparison of prompts.
- **A Skill is versioned and reviewable** like any other authoritative artifact.
  A bad investigation is a bad contract, fixable as data.

### Nine skills, independently testable

Repository Survey · Architecture Discovery · Domain Concept Discovery ·
Capability Discovery · Invariant and Business Rule Discovery · Decision and
Rationale Discovery · Workflow Discovery · Gap, Ambiguity and Contradiction
Discovery · Candidate Model Synthesis.

> **Do not turn these into one giant onboarding prompt.**

**Independently testable and replaceable** is a constraint on the design, not a
description of it: a skill that cannot be run alone has failed the requirement.

### A Skill produces proposals and never authoritative knowledge

Origin `O-probabilistic-interpretation` when a model executes it (`ADR-0109`),
with the full provenance that origin requires. **Curation is unchanged**
(`ADR-0110`).

### Skills read the Mechanical Model

`ADR-0108`. A Skill's `evidence to inspect` names parts of the Mechanical Model,
**not files.** A Skill permitted to read source would break the comparability the
two-stage split exists to provide.

**One exception is admitted and bounded**: a Skill may declare source reading as
a permitted tool **when the Mechanical Model provably lacks the fact** —
`F-fact-absent` (`ADR-0110`). The remedy is then to extend mechanical extraction,
and the exception is a diagnostic rather than a licence.

## Alternatives considered

**Keep prompts inside the worker implementation.** Rejected — the reason for the
decision. It makes the investigation unreviewable and the comparison meaningless.

**One onboarding skill.** Rejected explicitly. It cannot be tested in parts, and
a failure in it is unattributable — the same defect `ADR-0108` was written to fix
one layer up.

**Model Skills as Layer A `Skill` entities.** Rejected under `ADR-0096`'s
criterion: a Skill's instances belong to a session, not to a model. The Layer A
`Skill` describes a methodology **a modelled system has**; a Discovery Skill is
one **Engineering OS runs**. Same word, two layers, as with `EngineeringGate`.

## Consequences

### Positive

- **The investigation becomes an asset that outlives any model.**
- Nine independently testable contracts, each replaceable without touching the
  others.
- **A blind comparison becomes possible and repeatable**, because what the worker
  was asked is written down rather than improvised.

### Negative

- **Eleven fields per skill is heavy**, and the ceremony will tempt shortcuts on
  the tenth skill in a way it does not on the first.
- **Nothing verifies that a worker honoured its contract.** A skill can declare a
  stopping condition and a model can ignore it; only the output shape is
  checkable, and that is the weakest part of the contract.
- Engine independence is asserted and untested until a second engine runs one.

### Neutral

- No metamodel change. Skills are a registry.

## Compliance

`discovery/skills/` declares the skills. **No model or vendor is named in any
Skill.** A Skill's evidence names parts of the Mechanical Model, and source
reading is permitted only with a declared `F-fact-absent` justification.
