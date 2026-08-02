---
id: ADR-0074
title: RelationshipType is the type system of the knowledge graph
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0031, ADR-0066, ADR-0067, ADR-0071, ADR-0072]
---

# ADR-0074 — RelationshipType is a type system

## Context

`ADR-0071` registered a relationship vocabulary of eighteen core types. In use,
`RelationshipType` has stopped being one entity among twenty-six and started
being **the type system of the knowledge graph** — the thing that decides which
edges are legal, what they mean, and what may be inferred from them.

The compiler already depends on it. `resolve()` rejects a model whose predicates
have no registered parent, which is type-checking by another name.

## Decision

**`RelationshipType` is treated as a type system, and every predicate must
eventually declare seven fields.**

| Field | Required | States |
|---|---|---|
| **semantic definition** | yes | what the relationship means |
| **parent relationship** | yes | the core type it specializes |
| **domain** | yes | what may be the source |
| **range** | yes | what may be the target |
| **cardinality** | yes | how many, from each end |
| **inference rules** | optional | what may be derived from an instance |
| **validation rules** | optional | what the compiler must check |

**Optimize for semantic reuse, not for reducing predicates.** `ADR-0069`'s
principle, applied here: a vocabulary succeeds when new entities reuse it, not
when it is small.

### Inference is optional and never implicit

`ADR-0044` holds: relationships are **descriptive, never inferential** unless an
explicit rule exists. Declaring an inference rule field does not make inference a
default — it gives the exception a place to be declared, and keeps the compiler
mechanical (`ADR-0061`) by ensuring nothing is derived that was not stated as
derivable.

### The vocabulary is a reusable asset

It is intended to be **one of the strongest reusable assets of Engineering OS** —
a repository adopting the framework inherits a typed relationship vocabulary
rather than inventing predicates.

## Alternatives considered

**Leave `RelationshipType` as a specification with five fields.** Rejected — the
five it has (`domain`, `range`, `cardinality`, `constraints`, `semantics`) lack a
parent and have no place for inference or validation. The parent is what makes
the vocabulary a taxonomy rather than a list.

**Require all seven fields immediately.** Rejected as unbuildable: sixty-three
predicates exist and none declares a domain or cardinality formally. Requiring
seven fields now would either stop B1 or produce sixty-three fabricated
declarations.

**Make inference rules mandatory.** Rejected. Most relationships imply nothing,
and a mandatory field would be filled with "none" sixty times — which is how a
required field becomes noise.

## Consequences

### Positive

- **The compiler gets something to type-check against.** Domain and range
  declarations turn `resolve()` from a name-existence check into real
  type-checking.
- Cardinality declarations make a whole class of `ValidationRule` mechanical.
- **It gives `RelationshipType` a reason to exist under its own `ADR-0067`
  test** — it introduces typing, which nothing else expresses.

### Negative

- **Seven fields for sixty-three predicates is 441 declarations**, and today
  fewer than a third exist. This is a large, unfinished obligation and it is
  recorded as such rather than pretended complete.
- **A type system is a commitment.** Once the compiler checks domain and range,
  every under-specified predicate becomes a build failure rather than a gap.
  Adoption must be incremental or it will block work.

### Neutral

- No entity is added. `RelationshipType` gains two fields and an obligation.

## Compliance

`model/metamodel/entities/relationship-type.md` declares seven fields.
`model/metamodel/relationship-vocabulary.md` records, per core type, which are
declared and which are outstanding. **The gap is stated, not hidden.**
