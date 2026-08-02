---
id: ADR-0143
title: Five responsibilities stay sharply separated — extract, hypothesize, authorize, preserve, consume
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0103, ADR-0108, ADR-0117, ADR-0130, ADR-0135, ADR-0140, ADR-0141]
---

# ADR-0143 — Five responsibilities

## Context

The reviewer made the boundary explicit and named it as a property to protect:

> **Mechanical Discovery extracts. Interpretive Discovery hypothesizes. Human
> Curation authorizes. Continuous Acquisition preserves. Engineering Guidance
> consumes.**
>
> Those five responsibilities should remain sharply separated. **I believe that
> separation is becoming one of the strongest properties of Engineering OS.**

Each boundary was drawn separately, for a local reason, across many sessions.
Stated together they are one architecture.

## Decision

**Five responsibilities, five verbs, and no component holds two.**

| Verb | Owner | May not |
|---|---|---|
| **extracts** | Mechanical Discovery | name anything as engineering knowledge |
| **hypothesizes** | Interpretive Discovery | read the repository, or admit anything |
| **authorizes** | Human Curation | be performed by a machine |
| **preserves** | Continuous Acquisition | invent meaning the onboarding did not establish |
| **consumes** | Engineering Guidance | read a repository or any acquisition intermediate |

**Each prohibition has already been violated once, and each violation is what
produced the rule.**

- **extract → hypothesize.** A profile substituted a test class's *name* for a
  missing declared subject: 67 invariants asserting nothing (`SESSION-0045`).
- **hypothesize → extract.** Interpretive Discovery reads the Mechanical Model
  exclusively (`ADR-0108`) — the constraint that let a Java repository be
  understood with no interpreter change.
- **preserve → hypothesize.** Continuous Acquisition dropped four of six
  semantic relationships. The fix **preserves**; it does not infer
  (`ADR-0130`).
- **consume → hypothesize.** A Discovery rule emitting a relationship because a
  plan needed it would fit the model to its consumer (`ADR-0135`).
- **authorize.** Curation has only ever run as a filter function.
  `tools/curate.py` now **refuses to run without a terminal**.

## Rationale

The separation is what made every hard question in this project answerable, and
the pattern is consistent: **each defect was found at a boundary, by comparing
what two responsibilities said about the same evidence.**

Two acquisition modes disagreeing found the `C1`/`R4` divergence and the
semantic loss. A blind worker reading only the extractor's output found the
column defect. Guidance reading a model it did not build found the model-wide
leak. **None was found by inspecting a component alone.**

It is also what makes non-determinism safe (`ADR-0140`). A frontier model may
hypothesize freely precisely because it cannot extract, cannot authorize and
cannot be consumed directly. **Determinism is preserved by the boundary, not by
the worker** — which is how `ADR-0103` survives admitting an LLM.

## Consequences

**`tools/curate.py` refuses non-interactive execution.** A scripted curation
session would hold two responsibilities at once and produce exactly the
reviewer-efficiency numbers `ADR-0144` forbids inventing.

**The five verbs are not the five of `ADR-0123`.** Those describe what the
*product* does — acquisition learns, understanding explains, guidance
recommends, memory stores, drift challenges. These describe what each
*component* is allowed to do. They are a responsibility model, not a restatement.

**A new component declares which verb it holds.** A component that needs two is
two components.

## Compliance

- Every component declares its verb.
- No component performs a verb it does not hold.
- Curation is never automated; a scripted curation is a defect, not a
  convenience.
