---
id: ISSUE-0067
title: Whether a Dimension Review is a distinct artifact type or a structured ADR
type: question
status: resolved
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0051-dimension-review-process.md
  - governance/adr/ADR-0049-dimensions-are-a-scarce-architectural-resource.md
  - governance/adr/ADR-0038-four-questions-for-every-new-artifact-type.md
  - governance/adr/ADR-0035-engineering-os-metamodel.md
resolved-by: ADR-0054
---

# ISSUE-0067 — Is a Dimension Review an artifact type or an ADR?

## Statement

`ADR-0049` requires that **creating a new Dimension requires an ADR**.

`ADR-0051` requires that dimensions enter the metamodel **only through a
Dimension Review**, whose decision **"must itself become an authoritative
artifact so the reasoning is preserved"**.

An ADR is an authoritative artifact that preserves reasoning. So a Dimension
Review might be an ADR with a required structure — or a distinct artifact type
that happens to resemble one.

**Nothing says which**, and the two produce different repositories: one ADR per
dimension, or one ADR plus one Review per dimension.

## Why it matters

Nine reviews are the first work of the Dimension Registry. Producing eighteen
artifacts where nine were intended, or nine where eighteen were, is not a
detail — and the answer sets the pattern for every later review process.

## Two gates cannot currently be satisfied

If a Dimension Review **is** a new artifact type, two existing rules apply and
neither can be met:

- **`ADR-0035`** requires every new concept to be positioned in the Metamodel
  before a new artifact type is introduced. **The Metamodel does not exist.**
- **`ADR-0038`** requires four questions answered before acceptance, including
  *what metamodel entity does it instantiate* — unanswerable for the same
  reason.

This is the first time the metamodel-first gate has bound on a concept the
project actually needs. It cannot be worked around by ignoring it without
setting a precedent that the gate is advisory.

## Options

- **A structured ADR.** No new artifact type, so neither gate binds. The four
  outcomes and five criteria become a required ADR section. Simplest, and it
  keeps the decision corpus as the single record of reasoning.
- **A distinct artifact type.** Justified if reviews need lifecycle, querying or
  projection behaviour that ADRs lack — plausible, since reviews are inputs to a
  registry. Requires resolving the gate problem first.
- **A Review is an ADR *plus* a registry entry.** The reasoning stays in an ADR;
  the outcome becomes a registered fact. Consistent with `ADR-0052`'s separation,
  and it may be what "becomes an authoritative artifact" already means.

## Resolution

`ADR-0054`. **All three options above answer the wrong question.**

Each asked how to classify one review. The answer classifies the *category*:

> **The project now has multiple architectural gates that evolved
> independently. This indicates that "gate" is itself a first-class metamodel
> concept.**

An **Engineering Gate** is a review process applied to the introduction or
modification of an architectural concept, defining purpose, scope, triggering
conditions, required evidence, evaluation criteria, resulting decision and
produced artifacts.

**Dimension Review is an instance of Gate.** So are the Metamodel Position Gate,
the Artifact Definition Review, and a future Compiler Impact Review.

**The deadlock dissolves.** Dimension Review is not a new artifact type that must
pass the metamodel-first gate; it is an instance of a concept that goes *into*
the metamodel. The gate binds on `Gate`, once.

`ADR-0054` also requires the metamodel to model **Gate independently from the
rules executed by that Gate**, so review logic stops being scattered across
ADRs.
