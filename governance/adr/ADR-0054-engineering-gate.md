---
id: ADR-0054
title: Engineering Gate is a first-class metamodel concept
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0067]
related: [ADR-0035, ADR-0038, ADR-0051, ADR-0055, ADR-0056]
---

# ADR-0054 — Engineering Gate

## Context

`ISSUE-0067` asked whether a Dimension Review is a distinct artifact type or a
structured ADR, and recorded that the metamodel-first gate could not be
satisfied for it because the metamodel does not exist.

The question assumed Dimension Review was the thing to classify. It is not.

## Decision

**The project now has multiple architectural gates that evolved independently.
This indicates that "gate" is itself a first-class metamodel concept.**

Engineering OS introduces the concept of an **Engineering Gate**: a review
process applied to the introduction or modification of an architectural concept.

### Every Gate defines

- purpose
- scope
- triggering conditions
- required evidence
- evaluation criteria
- resulting decision
- produced artifacts

### Existing gates become instances

- **Metamodel Position Gate** (`ADR-0035`)
- **Dimension Review** (`ADR-0051`)
- **Artifact Definition Review** (`ADR-0038`)
- **Compiler Impact Review** *(future)*

> **The metamodel models Gate independently from the rules executed by that
> Gate.** This prevents review logic from being scattered across ADRs.

## Alternatives considered

The three options recorded in `ISSUE-0067` — a structured ADR, a distinct
artifact type, or an ADR plus a registry entry — are all **answers to the wrong
question**. Each asked how to classify one review. The answer classifies the
*category*: Dimension Review is an instance of Gate, and Gate is the concept the
metamodel needs.

**Leave gates scattered across the ADRs that introduced them.** Rejected — the
decision names why: review logic distributed across a decision corpus cannot be
found, compared or applied uniformly. Three gates had already accumulated
without anyone noticing they were the same kind of thing.

## Consequences

### Positive

- **`ISSUE-0067`'s deadlock dissolves.** Dimension Review is not a new artifact
  type needing to pass the metamodel-first gate; it is an instance of a concept
  that goes *into* the metamodel. The gate binds on `Gate`, once.
- Gates become comparable. Four instances with the same seven fields can be read
  side by side, which is impossible when each lives in the prose of a different
  ADR.
- **`ADR-0038` gets a name.** Its four questions become the Artifact Definition
  Review — a gate rather than a rule floating free.
- Separating Gate from its rules means a review procedure can change without
  changing what a gate *is*, which is the same separation `ADR-0053` drew
  between the metamodel and the compiler.

### Negative

- **A fourth gate is named before it exists.** Compiler Impact Review is marked
  *future*, the third such pre-commitment after Inference Rules (`ADR-0044`) and
  Policy Assignment (`ADR-0050`). The practice is sound; the accumulation of
  named-but-absent concepts is worth watching.
- Gates now need their own place in the semantic hierarchy — a Gate
  Specification, a Gate, and possibly an assignment. `ADR-0052`'s three stages
  should apply, and nothing says they do.
- Retrofitting three existing gates into seven fields each will expose gaps.
  `ADR-0035`'s Metamodel Position Gate, in particular, has no stated triggering
  conditions or required evidence.

### Neutral

- No gate changes what it does. What changes is that they are now one kind of
  thing.

## Compliance

Every review process is modelled as a Gate instance with all seven fields. No
review logic is defined only in the prose of an ADR. The metamodel defines
`Gate` independently of the rules any gate executes.
