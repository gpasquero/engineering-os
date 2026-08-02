---
id: ADR-0110
title: Brownfield acquisition has three stages, and the trust boundary is review rather than determinism
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0060, ADR-0100, ADR-0103, ADR-0105, ADR-0106, ADR-0108]
---

# ADR-0110 — Three acquisition stages

## Context

`ADR-0108` split Discovery into mechanical and interpretive stages, and the split
made a failure attributable. It left two things unstated: **where curation sits**,
and **whether an interpreter may be probabilistic.**

`SESSION-0040` found that a better deterministic rule recovered what a human
wrote, and the honest risk is that this becomes an argument for pursuing
deterministic rules indefinitely.

> **The objective of Brownfield onboarding is not to prove that every engineering
> abstraction can be derived deterministically. The objective is to construct the
> best possible Candidate Engineering Model using all appropriate workers.**

## Decision

### Three stages, kept distinct so failures stay attributable

| Stage | Consumes | Produces |
|---|---|---|
| **Mechanical Acquisition** | the repository | a reproducible **Mechanical Model** of observable facts |
| **Interpretive Acquisition** | the Mechanical Model and source evidence | proposed engineering meaning |
| **Engineering Curation** | proposals | the **Authoritative Engineering Model** |

**Mechanical**: files, modules, symbols, dependencies, endpoints, schemas, tests,
configuration, Git history, build metadata, runtime observations when available.

**Interpretive**: Concepts, Capabilities, Bounded Contexts, Invariants,
Workflows, architectural decisions, hidden assumptions, contradictions, knowledge
gaps.

**Curation**: reviews, merges, rejects, corrects and authorizes.

### The trust boundary

> **The trust boundary remains review and acceptance, not determinism.**

This is the decision's centre, and it changes what determinism is *for*.

| | Valuable because |
|---|---|
| **Deterministic discovery** | reproducible, cheap, auditable |
| **Probabilistic discovery** | can synthesize meaning across weakly structured evidence |

**Engineering OS uses both.** Neither is authoritative; both propose, and
curation decides.

### Relationship to `ADR-0103`

`ADR-0103` protects the **Engineering Director**: it reasons deterministically,
and a language model may not enter its reasoning.

**Acquisition is not the Director.** A probabilistic interpreter proposes
knowledge that a human authorizes before it becomes authoritative — so nothing
the Director reasons over was produced probabilistically without review.

**The two decisions are compatible and the boundary between them is
curation.** Recording that explicitly matters, because *we already allow a
language model in acquisition* is exactly the argument that would later be used
to allow one in planning.

### Interpretive failures are classified before they are called failures

> **Do not call something an interpretation failure until the required mechanical
> evidence is known to be available.**

| Classification | Means |
|---|---|
| `F-fact-absent` | the required fact is not in the Mechanical Model |
| `F-fact-ignored` | the fact was present and the interpreter did not use it |
| `F-rule-insufficient` | the fact was used and the rule could not reach the conclusion |
| `F-evidence-ambiguous` | the evidence supports more than one reading |
| `F-representation-insufficient` | the conclusion cannot be expressed in the metamodel |

`SESSION-0040`'s failure was `F-fact-ignored` — the `describe` block was
extracted and `R1` did not read it. **Called a limit of determinism, it was a
rule looking in the wrong place.**

### The Mechanical Model vocabulary is a versioned contract

**A missing mechanical fact makes every interpreter fail regardless of quality.**
The vocabulary carries a version, and a change to it is a change every
interpreter's results are measured against.

## Alternatives considered

**Require determinism throughout acquisition.** Rejected — it makes weakly
structured evidence permanently unreachable, and `SESSION-0040` showed how easily
that limit is mistaken for a real one in the other direction too.

**Let probabilistic proposals be authoritative when confidence is high.**
Rejected. `ADR-0104` already forbids confidence lowering scrutiny, and this would
move the trust boundary from review to self-report.

**Merge curation into interpretation.** Rejected: an interpreter that authorizes
its own output is the self-certification `ADR-0023` prohibits.

## Consequences

### Positive

- **A probabilistic interpreter becomes admissible without weakening anything**,
  because curation is unchanged and unavoidable.
- Failure classification makes *interpretation failed* a claim that must be
  substantiated.
- The three stages give the comparative benchmark a fair shape: same mechanical
  input, different interpreters, one curation standard.

### Negative

- **Curation is the bottleneck and this decision increases the load on it.**
  Admitting probabilistic proposals raises volume and lowers average precision,
  and `ADR-0106` already recorded that review does not scale.
- **The `ADR-0103` boundary now depends on a distinction a reader must hold**:
  models in acquisition, never in direction. It is defensible and it is thin.

### Neutral

- `ADR-0108`'s two stages are unchanged; curation was always implied and is now
  named.

## Compliance

`model/interpretive-failures.md` declares the failure classification. The
Mechanical Model carries a vocabulary version. **No proposal is authoritative
before curation, whatever produced it.**
