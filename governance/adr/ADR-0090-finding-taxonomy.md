---
id: ADR-0090
title: Findings are classified by kind and strength; evidence quality is never a score
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0031, ADR-0060, ADR-0061, ADR-0087, ADR-0088, ADR-0089]
---

# ADR-0090 — The finding taxonomy

## Context

The Kubernetes validation produced **a documentation-and-observability insight,
not a correctness bug**, and said so. That distinction turned out to matter more
than the finding itself.

**Not every finding deserves the same weight**, and a system that presents them
identically is misleading in exactly the way `ADR-0088` was written to prevent.

## Decision

### 1. Findings are classified by kind

A registered vocabulary (`ADR-0031`), ordered by the strength of the claim it
licenses:

| Kind | Claims | Strength |
|---|---|---|
| **confirmed-contradiction** | two sources state incompatible things | strongest |
| **behavioral-inconsistency** | implementation and stated behaviour disagree | strong |
| **architectural-inconsistency** | the structure violates a stated decision | strong |
| **traceability-gap** | something exists with no path to its rationale | moderate |
| **documentation-gap** | true and stated in no document | moderate |
| **observability-gap** | true and not visible where it matters | moderate |
| **ambiguous-evidence** | sources permit more than one reading | weak |
| **missing-evidence** | the model cannot support the claim at all | weakest |

**The Kubernetes result is a documentation gap plus an observability gap**, and
naming that is more honest than calling it a finding.

### 2. Evidence quality is expressed through provenance and support, never a score

> **Engineering evidence is not probabilistic.**

The four support states — `confirmed`, `incomplete`, `ambiguous`, `unsupported`
— stay. **No confidence numbers, no percentages, no weights.**

A developer must always be able to see **why** a conclusion is strong or weak, by
following its provenance to a source. A score answers *how much* and destroys
*why*.

This is `ADR-0061` applied to reporting: the compiler is not an intelligence, and
a number would imply a judgement it did not make.

### 3. No `Finding` entity

`ADR-0085` admits an entity only when a question requires it. **No question does
here.** A finding is a *report about* the model, not a node in it, and the
taxonomy is a registry the reporting layer consumes.

If a future question needs findings to be queryable — *which findings does this
concept participate in?* — that question justifies the entity. It has not been
asked.

## Alternatives considered

**Confidence scores.** Explicitly rejected. They are the obvious next step and
they are wrong: a 0.7 cannot be traced to a source, cannot be argued with, and
invites arithmetic on judgements that are not numbers.

**A flat list of findings with no classification.** Rejected — the current state,
and it presents a documentation gap and a contradiction identically.

**Model findings as `Issue` nodes.** Rejected: an `Issue` is *a recorded
unknown*, and a documentation gap is a recorded **known** that a document fails
to state. Reusing the entity would corrupt it.

## Consequences

### Positive

- **The system can now say a finding is weak.** That is a capability, not a
  limitation, and it is what makes a strong finding believable.
- The ordering gives the next external validation a target: **aim for a confirmed
  contradiction**, which the Kubernetes model did not produce.
- It composes with `ADR-0088`'s support states: kind describes *what was found*,
  support describes *how well it is evidenced*.

### Negative

- **Classification is a judgement made by the author of the finding.** Nothing
  checks that a documentation gap has not been labelled a contradiction, and the
  incentive runs the wrong way.
- Eight kinds is a guess from one validation. Some will prove unused and at least
  one boundary — documentation gap versus traceability gap — is already thin.

### Neutral

- No existing finding changes. The Kubernetes result gains two labels.

## Compliance

`model/finding-kinds.md` declares the taxonomy and is registered. Every reported
finding states its kind and the support state of its evidence. **No artifact
emits a confidence score.**
