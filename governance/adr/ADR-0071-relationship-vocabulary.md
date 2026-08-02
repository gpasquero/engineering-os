---
id: ADR-0071
title: Relationship types are classified into a registered vocabulary
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0031, ADR-0057, ADR-0066, ADR-0067, ADR-0069]
---

# ADR-0071 — The relationship vocabulary

## Context

The generated relationship graph reported **no relation used three or more
times** across the ontology. Counting the Markdown directly gives the same
picture from the other side: **82 relationship rows using 64 distinct
predicates.**

Every relationship in the metamodel is bespoke. For an architecture whose stated
design unit is the relationship (`ADR-0067`), that is the central defect:
`RelationshipType` exists to hold a vocabulary, and no vocabulary exists.

## Decision

**Relationship types are classified into four categories, and every predicate in
the metamodel specializes exactly one registered core type.**

| Category | Core types |
|---|---|
| **Structural** — how things are composed | `contains` · `references` · `specializes` · `implements` |
| **Behavioral** — how one thing acts on another | `governs` · `validates` · `triggers` · `executes` |
| **Semantic** — how meaning relates | `represents` · `defines` · `instantiates` · `derives-from` |
| **Traceability** — how the record hangs together | `established-by` · `accepted-by` · `supersedes` · `resolves` · `depends-on` · `evidenced-by` |

### Classification, not collapse

**Specific predicates are not renamed away.** `accepts`, `reviewed-by` and
`decided-by` remain distinct; each declares that it specializes
`traceability:accepted-by`.

This is `ADR-0069` applied to relationships. Collapsing sixty-four predicates
into eighteen would reduce a count and destroy distinctions — `Policy.governs`
and `Dimension.classifies` are genuinely different relationships and must stay
different. **Regularity means every predicate has a registered parent, not that
every predicate is the same.**

### The obligation on new entities

**A new entity reuses a core type directly wherever it can, and specializes one
where it must.** Inventing a predicate with no registered parent is a modelling
error.

The intended effect: **the ontology becomes progressively more regular as it
grows**, rather than accumulating one predicate per relationship forever.

### `governs` is reserved

`governs` named three different relationships (`views/README.md` #4). The
vocabulary admits it once, in the normative sense:

| Was | Becomes | Meaning |
|---|---|---|
| `Policy.governs` | `governs` | constrains normatively |
| `StateMachineSpecification.governs` | `controls-lifecycle-of` | controls the lifecycle of |
| `Dimension.governs` | `classifies` | may classify |

**The vocabulary's first act is to resolve the collision that motivated it** —
the tenth term this project has had to split.

## Alternatives considered

**Collapse predicates onto the eighteen core types.** Rejected under `ADR-0069`:
it optimises the count and loses distinctions. The relationship graph would look
regular because the model had been flattened.

**Leave predicates ad hoc and document conventions.** Rejected — the current
state, measured at 64 predicates for 82 rows.

**Derive the vocabulary from what already exists rather than declaring
categories.** Attractive, and rejected: the existing predicates are the artefact
of twenty-five sessions of local decisions. Deriving categories from them would
formalise the accident. The four categories are declared, and existing predicates
are mapped onto them — which is what exposed the `governs` collision.

## Consequences

### Positive

- **`RelationshipType` acquires the content it was created for.** It has been
  specified for three sessions with nothing to hold.
- The improvement is measurable: the generated views report predicate reuse, so
  the effect of this decision is visible in an artifact nobody maintains by hand.
- Each core type is a place to attach cardinality and constraint conventions
  once instead of per predicate.

### Negative

- **Eighteen core types is a guess.** The set is seeded from the reviewer's
  proposal plus `evidenced-by`, which the existing predicates demanded. Some will
  prove unused and at least one category boundary will prove wrong.
- **Some mappings are strained**, and they are marked as such in the vocabulary
  rather than smoothed over. `depends-on` in particular is absorbing predicates
  that may deserve their own core type.

### Neutral

- No entity changes. Every relationship gains a declared parent.

## Compliance

`model/metamodel/relationship-vocabulary.md` holds the registry. The ontology
declares each core type and every property declares `rdfs:subPropertyOf` its
parent. New entity specifications name the core type each relationship
specializes.
