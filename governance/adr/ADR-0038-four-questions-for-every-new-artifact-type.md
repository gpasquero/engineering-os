---
id: ADR-0038
title: Every new artifact type must answer four questions before acceptance
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0029, ADR-0030, ADR-0035, ADR-0037, ISSUE-0056]
---

# ADR-0038 — Four questions for every new artifact type

**This becomes the first mandatory `ModelingPolicy`** once the ModelingPolicy
system is introduced in M3.

## Context

`ADR-0035` established a process gate: every new concept must be positioned in
the Metamodel before a new artifact type is introduced. That states *when* the
positioning happens but not *what counts as positioned*.

`ADR-0037` completed the four-layer architecture and requires every artifact to
belong to exactly one layer, which supplies the first half of a concrete test.

## Decision

From this point forward, **every new artifact type introduced into Engineering
OS must answer four questions before it is accepted**:

1. **Which layer owns it?**
2. **Is it authoritative or derived?**
3. **What metamodel entity does it instantiate?**
4. **Which compiler phase consumes or produces it?**

> **If any of these questions cannot be answered, the artifact is not yet
> sufficiently defined to become part of the architecture.**

This is a definition of "sufficiently defined", not a checklist to be waved
through. An unanswerable question is a rejection, not a gap to be filled later.

## Alternatives considered

**Rely on `ADR-0035`'s gate alone.** Rejected: "positioned in the metamodel" can
be satisfied by adding a name to a list. The four questions make positioning
mean something, because three of them can only be answered by understanding how
the artifact behaves.

**Review by judgement, without fixed questions.** Rejected: the project has
introduced roughly fifteen artifact types across twelve sessions, largely by
judgement, and produced six terminology problems. Fixed questions are cheap and
catch the specific failure — a type introduced before its place is understood.

**More questions.** Rejected: each of these four maps to a decision already
made — `ADR-0037` for layers, `ADR-0012` for kinds, `ADR-0035` for metamodel
entities, `ADR-0014` for compiler phases. A fifth question would need a fifth
foundation.

## Consequences

### Positive

- **`ADR-0035`'s gate becomes operational.** "Sufficiently defined" now has a
  test rather than a feeling.
- Each question forces a decision the project has previously made implicitly and
  discovered later. Question 3 in particular would have caught several of the
  vocabulary collisions, because two concepts instantiating the same metamodel
  entity is exactly what an overloaded term looks like.
- Acceptance of a new artifact type becomes reviewable against stated criteria,
  which suits `ADR-0018`'s requirement for explicit reviewer approval.

### Negative

- **The project cannot currently answer question 1 for its own existing
  artifacts.** `shared/`, `skills/`, `workflows/`, `templates/`, `schemas/` and
  `governance/` have no layer under `ADR-0037` — `ISSUE-0056`. A rule that the
  existing corpus fails is a rule with a compliance debt from the day it is
  written.
- Question 4 presupposes the compiler phases. They are named — parsing,
  normalization, validation, semantic linking — but not specified, so answers
  will be coarse until the compiler interface exists.
- It adds friction to introducing a type, which is the intent, but will feel
  disproportionate for a small or obvious addition.

### Neutral

- Nothing existing is invalidated. The questions apply to types introduced from
  here; `ISSUE-0056` handles the retrospective case.

## Compliance

No new artifact type is accepted without all four questions answered in the ADR
that introduces it. An unanswerable question blocks acceptance. The rule moves
into a `ModelingPolicy` in M3, at which point the policy governs and this ADR
records why.
