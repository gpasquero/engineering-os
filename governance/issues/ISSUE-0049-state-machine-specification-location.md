---
id: ISSUE-0049
title: Where state machine specifications live, and their boundary with shared/vocabularies/
type: question
status: deferred
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0028-state-machine-registry-lives-in-knowledge-manifest.md
  - governance/adr/ADR-0027-state-machine-registration-model.md
  - governance/adr/ADR-0025-every-state-belongs-to-exactly-one-state-machine.md
resolved-by: null
defers-to: [M2]
debt: architectural
---

# ISSUE-0049 — Where state machine specifications live

> **Architectural debt** (`ADR-0062`). Deferred because it is not needed to
> build the next deliverable. Reopen when implementation requires it.

## Statement

`ADR-0028` places the State Machine Registry in `KNOWLEDGE-MANIFEST.yaml`, which
**indexes and relates** machines. It states that individual state machine
specifications remain **separate artifacts**, without saying where they are.

`ADR-0025` had already assigned `shared/vocabularies/` the job of holding
vocabularies **grouped by state machine**. `ADR-0027` makes `vocabulary` one of
the nine registration fields.

So the vocabulary of a state machine has two candidate homes, and the boundary
between a *specification* and a *vocabulary file* is undefined.

## Why it matters

Both are M2 deliverables. Two artifacts owning one piece of content is the
duplication failure recorded in `ISSUE-0018` and `ISSUE-0035`, and the project
has now hit it three times.

## The sharper question underneath

**Not every vocabulary is a state machine vocabulary.**

- Assertion statuses, artifact kinds and the revision lifecycle plausibly belong
  to state machines.
- Confidence (`high`/`medium`/`low`) and risk levels are **ordinal scales**, not
  states. Nothing transitions between them.
- Gate decisions (`ready`/`ready-with-mitigations`/`blocked`) are outcomes of an
  evaluation, which may or may not be a state machine.

If `shared/vocabularies/` becomes "state machine vocabularies", the non-state
vocabularies need a home. If it stays "all closed enumerations", it overlaps
every state machine specification.

## Options

- **Specifications in `shared/vocabularies/<machine>/`**, each containing the
  full nine-field registration. `shared/vocabularies/` then means "state machine
  specifications", and non-state enumerations move elsewhere.
- **Specifications alongside the domain they describe** — framework machines in
  `shared/`, domain machines in `model/`. Consistent with `ADR-0028`'s reasoning
  that a state machine is domain semantics, but it splits the framework's own
  machines across two layers.
- **`shared/vocabularies/` holds only the vocabulary field**, with the other
  eight fields in the manifest index. Contradicts `ADR-0028`, which says the
  manifest only indexes.

## Shape clarified by ADR-0031

The Registry Pattern fixes the *division of content* without fixing the
location. A registry holds identity, location, relationships, ownership, status
and version; a specification holds complete semantics, constraints, examples,
rationale and evolution.

So the nine registration fields split across both: the registry entry carries
identifier, owner and governed entity; the specification carries vocabulary,
transition rules and the rest. That narrows this issue to one question — where
the specification file lives — and removes the third option below, which
contradicts the pattern.

## Vocabulary sharpened by ADR-0032

Three artifacts are now distinguishable where this issue saw two: the **Registry
Specification** (governing the registry itself), the **Registry Projection**
(the generated index), and each **entity specification** — one per state
machine.

This issue concerns only the third. The first two have homes: the specification
is authored, the projection is generated from it.

## Narrowed again by ADR-0039

Layers classify artifacts, not directories, and repository layout is an
implementation concern. So this issue is no longer an architectural question —
choosing a directory does not choose a layer, and a state machine specification
is Layer A or B by what it is, not by where it sits.

What remains is a placement convention, which is a smaller decision than the
issue was originally recorded as.

## Resolution criteria

An ADR naming where state machine specifications live, what
`shared/vocabularies/` contains, and where enumerations that are not state
vocabularies belong.
