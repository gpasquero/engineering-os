---
id: METAMODEL-Invariant
title: Invariant
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0035, ADR-0065]
---

# Invariant

**A condition that must hold, stated independently of whatever enforces it.**

## identity

A qualified name within a BoundedContext, like `Concept` and `Capability`.

## purpose

To separate **what must be true** from **where it is checked**.

An invariant such as *an order cannot ship before payment clears* may be enforced
in a database constraint, a service, a form validator, all three, or nowhere.
Those are facts about an implementation. The invariant is a fact about the
domain, and it is true whether or not anything enforces it.

This separation is what makes an invariant useful to a reconstruction. Recording
*where a rule is checked* documents code. Recording *the rule, and then where it
is checked* exposes the gap — and **the gap is the finding**.

> **An invariant with no enforcement point is not an error in the model. It is a
> result.**

## Invariant is not ValidationRule

The distinction is the one `ADR-0060` draws between kinds of knowledge, and
getting it wrong would repeat the `Validation` collision that `SESSION-0022`
caught.

| | Invariant | ValidationRule |
|---|---|---|
| About | the domain | the repository |
| Answers | what must be true of the modelled world | what must be true of the model |
| Discovered by | Interpretive Discovery — authored | Mechanical Discovery — executed |
| Family | descriptive | to be assigned |

An Invariant is **never executable by the Knowledge Compiler**. The compiler does
not know the domain; it records what was asserted about it (`ADR-0061`).

## ownership

Owned by the BoundedContext in which it is stated.

## lifecycle owner

`ArtifactRevisionLifecycle`.

## authoritative representation

A statement in the semantic model: the condition, in natural language, plus its
scope and the entities it constrains.

**Natural language is the authoritative form.** A formal expression, where one
exists, is an additional representation and never replaces the statement — most
real invariants are not formalisable without losing the part that matters.

## derived representations

- A node in the Canonical Knowledge Model, linked to what it constrains and to
  its enforcement points.
- An unenforced-invariant report — a projection whose entire value is what it
  finds missing.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| constrains | Concept, Capability or Relationship | one or more |
| scoped-to | BoundedContext | exactly one |
| enforced-at | Artifact | **zero or more** |
| evidenced-by | Evidence | zero or more |

**`enforced-at` is zero-or-more.** The same cardinality decision as
`Capability.realised-by`, for the same reason: the unenforced case is the one
worth being able to state.

## extension points

An adopting repository states any invariants its domain has. The framework
supplies none.

## Debt

**Enforcement claims are unverifiable.** `enforced-at` says an artifact enforces
a rule. Nothing checks it, and nothing can — the claim is Interpretive
(`ADR-0060`). Whether it decays silently is the open question, and it is the
same shape as the stale-serialization problem `DimensionAssignment` recorded.

**Formal expression has no place to live.** The authoritative representation
names natural language and nothing else. Adding a formal slot is easy; deciding
which formalism is not, and B1 does not need it.
