---
id: METAMODEL-RELATIONSHIP-VOCABULARY
title: Relationship Vocabulary
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
artifact-kind: authoritative
established-by: [ADR-0031, ADR-0066, ADR-0071]
---

# Relationship Vocabulary

**The registered core relationship types, and the predicate each metamodel
relationship specializes** (`ADR-0071`).

> **Registered, not enumerated** (`ADR-0031`). An adopting repository registers
> its own core types; it does not modify this list to add a domain predicate,
> because domain predicates specialize rather than extend.

## The four categories

### Structural — how things are composed

| Core type | Means | Inverse |
|---|---|---|
| `contains` | A is a container for B | `contained-by` |
| `references` | A points at B without owning it | `referenced-by` |
| `specializes` | A is a narrower kind of B | `specialized-by` |
| `implements` | A realises what B describes | `implemented-by` |

### Behavioral — how one thing acts on another

| Core type | Means | Inverse |
|---|---|---|
| `governs` | A constrains B normatively | `governed-by` |
| `validates` | A checks that B holds | `validated-by` |
| `triggers` | A causes B to occur | `triggered-by` |
| `executes` | A carries out B | `executed-by` |

### Semantic — how meaning relates

| Core type | Means | Inverse |
|---|---|---|
| `represents` | A stands for B in another representation | `represented-by` |
| `defines` | A states what B is | `defined-by` |
| `instantiates` | A is a case of B | `instantiated-by` |
| `derives-from` | A is obtained from B | `derived-into` |

### Traceability — how the record hangs together

| Core type | Means | Inverse |
|---|---|---|
| `established-by` | A exists because of decision B | `establishes` |
| `accepted-by` | A was granted status by act B | `accepts` |
| `supersedes` | A replaces B, which remains readable | `superseded-by` |
| `resolves` | A answers open question B | `resolved-by` |
| `depends-on` | A cannot proceed without B | `depended-on-by` |
| `evidenced-by` | A is supported by observable B | `supports` |

**`evidenced-by` is not in the seed proposal.** It was added because seven
existing predicates map to it and forcing them onto `depends-on` would have
conflated *support* with *blocking* — a distinction `Evidence` exists to make.

## The mapping

Every predicate currently used in `entities/*.md`, and the core type it
specializes.

| Predicate | Core type | Category |
|---|---|---|
| `contains` | `contains` | structural |
| `scoped-to` | `contained-by` | structural |
| `owns` | `contains` | structural |
| `has-step` | `contains` | structural |
| `step-of` | `contained-by` | structural |
| `holds` | `contains` | structural |
| `defined-in` | `contained-by` | structural |
| `references` | `references` | structural |
| `cites` | `references` | structural |
| `has-provenance` | `references` | structural |
| `observed-at` | `references` | structural |
| `along` | `references` | structural |
| `of-kind` | `references` | structural |
| `relates-to` | `references` | structural |
| `specialises` | `specializes` | structural |
| `realised-by` | `implemented-by` | structural |
| `provided-by` | `implemented-by` | structural |
| `produces` | `implements` | structural |
| `governs` | `governs` | behavioral |
| `governed-by` | `governed-by` | behavioral |
| `controls-lifecycle-of` | `governs` | behavioral |
| `constrains` | `governs` | behavioral |
| `constrained-by` | `governed-by` | behavioral |
| `enforced-at` | `validated-by` | behavioral |
| `enforced-by` | `validated-by` | behavioral |
| `reviews` | `validates` | behavioral |
| `passes-through` | `validated-by` | behavioral |
| `driven-by` | `triggered-by` | behavioral |
| `invoked-by` | `triggered-by` | behavioral |
| `guarded-by` | `triggered-by` | behavioral |
| `executes` | `executes` | behavioral |
| `executed-by` | `executed-by` | behavioral |
| `uses` | `executes` | behavioral |
| `requires` | `depends-on` | traceability |
| `expressed-in` | `represents` | semantic |
| `preserves` | `represents` | semantic |
| `defines` | `defines` | semantic |
| `declares-states` | `defines` | semantic |
| `declares-transitions` | `defines` | semantic |
| `has-domain` | `defines` | semantic |
| `has-range` | `defines` | semantic |
| `decides` | `defines` | semantic |
| `classifies` | `defines` | semantic |
| `classified-by` | `defined-by` | semantic |
| `assigns-via` | `defined-by` | semantic |
| `has-value` | `defines` | semantic |
| `has-position` | `defines` | semantic |
| `instantiates` | `instantiates` | semantic |
| `revises` | `derives-from` | semantic |
| `revision-of` | `derives-from` | semantic |
| `has-revision` | `derived-into` | semantic |
| `has-active-revision` | `derived-into` | semantic |
| `motivated-by` | `established-by` | traceability |
| `establishes` | `establishes` | traceability |
| `accepts` | `accepts` | traceability |
| `accepted-by` | `accepted-by` | traceability |
| `reviewed-by` | `accepted-by` | traceability |
| `decided-by` | `accepted-by` | traceability |
| `supersedes` | `supersedes` | traceability |
| `superseded-by` | `superseded-by` | traceability |
| `corrects` | `supersedes` | traceability |
| `resolves` | `resolves` | traceability |
| `resolved-by` | `resolved-by` | traceability |
| `blocks` | `depended-on-by` | traceability |
| `defers-to` | `depends-on` | traceability |
| `supports` | `supports` | traceability |
| `evidenced-by` | `evidenced-by` | traceability |

## Strained mappings

Recorded rather than smoothed over, because a mapping that is forced is a
finding.

**`produces → implements`.** A Skill producing an Artifact is closer to
*creation* than to *realisation*. If a `produces` core type is ever added, this
is the case that motivates it.

**`guarded-by → triggered-by`.** A guard prevents rather than causes. It is the
negation of a trigger, and the vocabulary has no negative behavioral type.

**`has-position → defines`.** An ordinal is data, not a definition. It is here
because `ADR-0068` made position a first-class part of `WorkflowStep`, and no
category holds plain attributes.

**`requires → depends-on`** crosses categories — a structural-looking predicate
landing in traceability. That is probably correct and it reads oddly.

## Measured effect

| | Before | After |
|---|---|---|
| Distinct predicates | 66 | 66 |
| Predicates with a registered parent | 0 | 66 |
| Core types | 0 | 18, plus 18 inverses |
| Most-used core type | — | `references`, 7 predicates |

**The predicate count does not fall, and that is the intended outcome**
(`ADR-0069`). What changes is that every predicate now has a parent, so the
ontology can be traversed, queried and validated by category rather than by
sixty-six special cases.

## Debt

**Eighteen core types is a seed, not a result.** Some will prove unused.

**No core type has a declared cardinality or constraint convention**, which is
half of what having a vocabulary is for.

**Nothing enforces that a new predicate declares a parent.** It is a rule in
`ADR-0071` and a natural early `ValidationRule`.
