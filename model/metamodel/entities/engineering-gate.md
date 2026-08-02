---
id: METAMODEL-EngineeringGate
title: EngineeringGate
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: operational
artifact-kind: authoritative
established-by: [ADR-0054, ADR-0055, ADR-0051, ADR-0065]
---

# EngineeringGate

**An Engineering Process that reviews the introduction or modification of a
concept, and produces a decision.**

## What new semantics does this introduce?

**Conditionality on a judgement.** A Gate is the only entity that can say *this
does not proceed until someone decides.*

It also owns something nothing else can hold: **the questions.** `ADR-0055`
established that questions belong to Gates, not to artifacts — a question asked
of an artifact is asked once and forgotten; a question held by a Gate is asked
every time the Gate is passed.

That relocation is why the entity exists. Without Gates, review criteria live in
prose and are applied from memory.

## identity

A qualified name within the repository.

## purpose

To make review **repeatable rather than remembered**.

A Gate declares in advance what will be asked and what outcomes are possible. It
therefore turns a review from an event into a specification — and makes it
possible to ask whether a Gate was actually passed.

## ownership

Framework gates are owned by Engineering OS. Adopting repositories declare their
own and may not remove a framework gate from a framework workflow.

## lifecycle owner

`ArtifactRevisionLifecycle`.

## authoritative representation

A declaration naming: what the Gate reviews, the questions it holds, the possible
outcomes, and who may decide.

**Outcomes are a closed enumeration per Gate.** The Dimension Review
(`ADR-0051`) has exactly four, and one of them is *accept as a Dimension* while
three are forms of rejection that say what to do instead. **A Gate whose only
outcomes are accept and reject is usually under-specified** — the useful ones
name the alternative.

## derived representations

- Nodes in the Canonical Knowledge Model, linked to what they review.
- The question set, rendered as a review checklist.
- An ungated-change report: concepts introduced without passing an applicable
  Gate.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| reviews | entity type or Artifact | one or more |
| holds | question | one or more |
| produces | outcome | two or more |
| decided-by | Actor | one or more |
| governed-by | GovernancePolicy | zero or more |

## extension points

An adopting repository declares its own gates and adds questions to framework
gates. **Removing a question from a framework gate is not an extension**, and
nothing currently prevents it.

## Debt

**`question` and `outcome` are not entities.** Two relationships in the table
above point at things that exist nowhere in the inventory. This is the same shape
as `Evidence.supports` having no range (`FINDINGS.md` #4), and the same class of
gap.

Under `ADR-0067` the test applies to them too: a Question probably introduces no
relationship a `Concept` cannot express, and may not need to be an entity at all.
**Recorded for the simplification review** (`ISSUE-0074`), not resolved here.

**No Gate has ever been executed.** The Dimension Review is specified and has
never run — nine candidate dimensions exist and five are in active use, none
having passed it (`dimension.md`). This entity therefore describes a mechanism
with no instances, which is now the third such case.

**Nothing records that a Gate was passed.** The Gate specifies the review; no
entity captures the event. `AcceptanceRecord` does this for acceptance only. Gate
outcomes are, so far, unrecorded — and an unrecorded gate is indistinguishable
from an unpassed one.
