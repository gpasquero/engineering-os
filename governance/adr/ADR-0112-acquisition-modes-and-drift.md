---
id: ADR-0112
title: Acquisition has three modes; reacquisition produces a Knowledge Drift Report and never overwrites
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0072, ADR-0100, ADR-0101, ADR-0105, ADR-0106, ADR-0110]
---

# ADR-0112 — Acquisition modes and drift

## Context

Acquisition has been treated as something that happens **once**. A system that
onboards well and then diverges silently is worse than one that never onboarded,
because the divergence is invisible.

> **The defining capability of Engineering OS is that it acquires engineering
> knowledge once, maintains it throughout every change, and can later verify that
> the maintained understanding still matches reality.**

## Decision

**Three modes**, sharing one architecture and differing in objective.

| Mode | Runs | Objective |
|---|---|---|
| **Initial Acquisition** | once, deep and expensive | a sufficiently complete initial Authoritative Engineering Model |
| **Continuous Acquisition** | after engineering changes | update the model incrementally from plans, execution observations, code changes, tests and accepted decisions |
| **Periodic Reacquisition** | on a schedule, full discovery again | **compare, never overwrite** |

### Reacquisition never overwrites

> **It produces a fresh Candidate Engineering Model and compares it with the
> current Authoritative Engineering Model. The result is a Knowledge Drift
> Report.**

**Reacquisition validates and challenges the maintained model. It does not
replace it automatically.**

This follows from `ADR-0106`: a candidate model is a set of **proposals**, and
proposals require curation. A reacquisition that overwrote would be a worker
writing authoritative knowledge, which `ADR-0101` forbids at any scale.

### The Knowledge Drift Report

Eleven categories, each a **proposal requiring review**:

| Category | Is |
|---|---|
| newly discovered knowledge | the repository grew |
| **authoritative assertions no longer supported by current evidence** | the model claims something the repository no longer shows |
| implementation without modeled knowledge | code nobody described |
| modeled capabilities without implementation evidence | descriptions nothing implements |
| invariants without enforcement evidence | rules nothing checks |
| new or changed dependencies | the boundary moved |
| changed architecture boundaries | the structure moved |
| conflicting interpretations | two readings of the same evidence |
| **incremental updates missed since onboarding** | continuous acquisition did not keep up |
| stale provenance | a citation whose source moved or changed |
| unexplained divergence | none of the above fits |

**The second and the ninth are the ones the report exists for.** Everything else
a careful reader might notice; those two are only visible by comparing a
maintained model against a fresh one.

### Every drift item is a proposal

**No drift item is applied automatically**, including the ones that look
mechanical. *This assertion is no longer supported* may mean the evidence moved,
the extractor changed, or the system genuinely changed — and only the third is a
reason to retract.

## Alternatives considered

**Reacquire and replace.** Rejected: it discards curated knowledge — every
correction a human made would be silently reverted by the next run.

**Reacquire and auto-merge the unambiguous parts.** Rejected, and it is the
tempting middle. *Unambiguous* is a judgement, and making it automatically is the
judgement being avoided.

**Continuous acquisition only, with no periodic full run.** Rejected: incremental
updates cannot detect what they themselves missed, which is the ninth category
and the reason a full rerun is worth its cost.

## Consequences

### Positive

- **Drift becomes detectable rather than assumed absent**, which is the
  difference between a model that is trusted and one that is trustworthy.
- Continuous acquisition gets a check: the periodic run measures whether it kept
  up.
- One architecture serves all three modes, as `ADR-0105` requires of onboarding
  and continuous engineering.

### Negative

- **Reacquisition is as expensive as onboarding, every time**, and produces a
  report someone must read. A report nobody reads is worse than no report,
  because it converts a known gap into a false sense of coverage.
- **Continuous acquisition does not exist.** Two of three modes are declared and
  unbuilt, and the drift report cannot be meaningful until at least one
  incremental update has happened.

### Neutral

- No existing artifact changes. Initial Acquisition, which exists, is one of
  three modes rather than the whole.

## Compliance

`model/drift-categories.md` declares the report's categories. **Reacquisition
never writes the Authoritative Engineering Model**; it produces a candidate and a
drift report, and every item is curated.
