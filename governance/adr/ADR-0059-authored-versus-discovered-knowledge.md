---
id: ADR-0059
title: Distinguish authored knowledge from discovered knowledge, and maximize the discovered
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0014, ADR-0020, ADR-0034, ADR-0058, ISSUE-0071]
---

# ADR-0059 — Authored knowledge versus discovered knowledge

**This is a central design goal of the Knowledge Compiler and a defining
capability of the Knowledge Explorer.**

## Context

`ADR-0058` established that Principles are extracted by the compiler rather than
authored. That is an instance of something larger: some knowledge in this
repository is written down, and some exists only across many artifacts at once.

Until now the compiler's purpose was stated as transformation — authoritative
assets into a canonical model into projections. That describes what it does, not
why it is worth building.

## Decision

The repository increasingly distinguishes **authored knowledge** from
**discovered knowledge**.

**Authored** — explicitly written:

- ADRs
- Policies
- Specifications

**Discovered** — found by the compiler:

- Principles
- Traceability
- Dependency graphs
- Architectural patterns
- Impact graphs
- Semantic clusters

> **Engineering OS maximizes discovered knowledge.**

**The value of the compiler is not only transforming documents into graphs. Its
higher purpose is revealing architectural knowledge that exists implicitly
across many authoritative artifacts but was never written as a single
document.**

## Alternatives considered

**Author everything explicitly.** Rejected: it is what the project has been
doing, and it does not scale. The Registry Pattern took six independent arrivals
across nine sessions before anyone wrote it down, and it was only noticed
because a human held the whole corpus in mind.

**Treat discovery as a reporting feature.** Rejected: framing it as a nice-to-have
would make it the first thing cut, and it is the capability that distinguishes a
knowledge compiler from a documentation generator (`ADR-0011`, `ADR-0014`).

**Discover without distinguishing.** Rejected: authored and discovered knowledge
have different artifact kinds, different trust chains and different correction
paths. Blurring them would make a derived assertion indistinguishable from an
accepted one.

## Consequences

### Positive

- **It states why the compiler is worth building.** Transformation is
  infrastructure; discovery is the product. This gives M9's tooling a purpose
  beyond generating indexes.
- This project is its own evidence. The Registry Pattern, the reframing pattern
  in `SESSION-0015`, the recurrence of `Definition → Instance → Assignment` —
  each existed implicitly across many artifacts long before anyone wrote it, and
  each was found by a human doing what a compiler could do systematically.
- Discovered knowledge is `derived`, so it costs nothing to regenerate and is
  always current. An authored summary of the same thing would drift.
- Traceability and impact graphs stop being artifacts someone must maintain.

### Negative

- **Determinism is the open question, and it is now larger.** Architectural
  patterns and semantic clusters sound like inference. `ADR-0020` requires the
  compiler to be deterministic and forbids a generator invoking an agent. Either
  discovery is algorithmic, or the determinism rule needs qualifying.
  `ISSUE-0071`.
- **"Maximize" has no stated limit.** Over-discovery — asserting a pattern that
  is coincidence — would put confident falsehoods into the canonical model with
  the authority of derivation. Nothing yet says how a discovered assertion is
  validated or how confidence is represented.
- Discovered knowledge is never accepted (`ADR-0020` applies to authoritative
  artifacts), so it inherits trust from its sources without a review step of its
  own.
- Knowledge Packages (`ADR-0019`) would export discovered content across
  repository boundaries, carrying inference into systems that cannot check it.

### Neutral

- No existing artifact changes. What changes is what the compiler is for.

## Compliance

Every piece of knowledge in the Canonical Knowledge Model is identifiable as
authored or discovered. No discovered assertion is presented as authored. The
compiler's design is judged by what it reveals, not only by what it transforms.
