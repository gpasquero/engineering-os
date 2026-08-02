---
id: ADR-0075
title: Remaining metamodel entities are justified by compiler need, not architectural completeness
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0062, ADR-0067, ADR-0069, ADR-0072, ADR-0073]
---

# ADR-0075 — Entities are justified by compiler need

## Context

Six entities remain unspecified: `Vocabulary`, `Principle`, `KnowledgePackage`,
`Registry`, `Manifest`, `ValidationRule`.

They are on the list because `ADR-0035` named them twenty-six sessions ago,
before anything was built. **The implementation has become the primary source of
architectural feedback**, and it now has an opinion about which of them are real.

## Decision

**A remaining metamodel entity is justified by a compiler requirement, not by
architectural completeness.**

> **If the compiler never needs an entity, question whether the metamodel needs
> it either.**

This is `ADR-0067`'s test — *what new semantic relationship does this introduce?*
— with a second, harsher question beside it: **what would the compiler do
differently if this existed?**

### It is a question, not a deletion rule

"Question whether" is deliberate. An entity may be real and not yet needed:
`KnowledgePackage` describes federation between repositories, and there is one
repository. The correct outcome there is **deferral with a stated trigger**, not
removal.

What is prohibited is specifying an entity **because the inventory lists it**.

### Prioritisation

**Compiler evolution takes precedence over metamodel expansion.** Where the two
compete, the pipeline wins, and the entity is specified when the pipeline reaches
for it.

## Applying it now

| Entity | What the compiler would do differently | Status |
|---|---|---|
| **ValidationRule** | Own the checks currently hard-coded in `resolve()` — *every predicate declares a registered parent* is a rule the model should hold, not a Python conditional | **needed now** |
| **Registry** | Hold the relationship vocabulary and the dimension registry, which the compiler reads today from Markdown by regex | **needed now** |
| **Vocabulary** | Type the closed enumerations already scattered as bare strings — evidence kinds, issue states, acceptance decisions | **needed soon** |
| **Manifest** | Declare what a project is, replacing the assumption that sources live in `model/*.md` | **needed soon** |
| **Principle** | Nothing yet. Principles are extracted from accepted ADRs, and the compiler compiles no ADRs | **deferred** |
| **KnowledgePackage** | Nothing yet. There is one repository | **deferred** |

**Four of six are needed, and the two that are not are deferred rather than
deleted.** That the split is four-two rather than six-zero is itself the evidence
this decision was worth making.

## Alternatives considered

**Finish the inventory.** Rejected — it optimises completeness, which `ADR-0069`
already rejected as a proxy in the analogous case.

**Delete entities the compiler does not need.** Rejected as too strong.
`KnowledgePackage` is not wrong, it is early, and deleting it would lose a
decision (`ADR-0019`) rather than defer it.

**Wait until the compiler demands each entity before specifying any.** Rejected
as too weak: `ValidationRule` and `Registry` are already demanded by hard-coded
behaviour, and waiting would mean writing more Python that the model should own.

## Consequences

### Positive

- **Two entities move to deferred and stop being counted as unfinished work.**
  B1's remaining scope is four entities, not six.
- Each specification will be written against a concrete requirement, which
  `ADR-0062` predicts is sharper than writing against prose — and `ISSUE-0007`
  demonstrated when nineteen sessions of analysis were resolved by one blank
  field.
- **It gives the test suite a role in metamodel design.** The uncovered features
  in `tests/README.md` are exactly the entities in question.

### Negative

- **The compiler's current shape becomes an argument about the metamodel**, and
  the compiler is four features old. An entity could be dismissed because a crude
  pipeline has not reached it.
- Deferral has no automatic trigger. `ISSUE-0074` needed a threshold and got one;
  these have prose conditions and nothing watching them — the gap `issue.md`
  already records.

### Neutral

- No entity is removed. Two are reclassified.

## Compliance

The inventory marks `Principle` and `KnowledgePackage` deferred, with the trigger
that would reopen them. Each newly specified entity states the compiler
requirement that justified it.
