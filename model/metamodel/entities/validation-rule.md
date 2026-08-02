---
id: METAMODEL-ValidationRule
title: ValidationRule
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: operational
artifact-kind: authoritative
established-by: [ADR-0048, ADR-0075, ADR-0076, ADR-0077]
---

# ValidationRule

**A constraint a knowledge model must satisfy, stated so that a compiler can
execute it.**

## What new semantics does this introduce?

**Executable normativity.**

`Invariant` states what must be true of the modelled world. `Policy` states what
must be true of the engineering performed on it. **Neither is executable, and
neither is about the model.** A ValidationRule is the only entity that constrains
the model itself in a form a machine can check.

## Why this is Layer A and `ValidationResult` is not

`ADR-0076`'s test, applied to two things that differ by one word:

| | Meaningful with no compiler? | Where |
|---|---|---|
| **ValidationRule** | **yes** — *every predicate must declare a registered parent* is true whether or not anything checks it | **Layer A** |
| `ValidationResult` | no — a result requires an execution | compiler architecture |

## identity

A stable identifier — `VR-0001` — unique within its registry.

## purpose

**The compiler executes rules. It does not contain them** (`ADR-0077`).

```text
Metamodel  →  ValidationRule  →  Compiler  →  ValidationResult
```

> **If changing *what* is checked requires editing code, the rule is in the wrong
> place. If changing *how* a class of check is evaluated requires editing code,
> that is correct.**

## Rule and rule kind

A ValidationRule is an **instance of a kind bound to specific model elements**.

| | Is | Lives |
|---|---|---|
| **rule kind** | a mechanism — *this type must declare this predicate* | in the compiler |
| **rule** | a binding — *`WorkflowStep` must declare `executes`* | in the model |

Kinds are **registered, not enumerated** (`ADR-0031`). Adding a rule is a data
change; adding a kind is a compiler change and should be rare.

## ownership

Framework rules are owned by Engineering OS. An adopting repository declares its
own and **may not weaken a framework rule** — only add.

## lifecycle owner

`ArtifactRevisionLifecycle`.

## authoritative representation

A declaration naming: identifier, kind, severity, the elements it binds, the
message, and **the rationale**.

**Rationale is not optional.** A rule whose reason is unstated cannot be
evaluated when circumstances change — the same argument `Policy` makes about
`motivated-by`.

## derived representations

- Diagnostics carrying the rule identifier that produced them.
- A rule registry projection.
- Coverage: which rules are exercised by which regression fixtures.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| of-kind | rule kind | exactly one |
| constrains | entity type or RelationshipType | one or more |
| motivated-by | ADR | one or more |
| validates | CanonicalKnowledgeModel | exactly one, at execution |

## extension points

An adopting repository declares additional rules of any registered kind, and may
register new kinds by implementing them.

## Debt

**Declaring rules produced two that did not exist.** Five checks were Python;
seven are declared. `VR-0005` and `VR-0006` were written because a table invites
*what else belongs here?* in a way a function does not — and **`VR-0007`, written
by generalising `VR-0006`, immediately caught a defect in a regression fixture
that had passed for two sessions.**

**Severity is declared and unused.** Every rule is `error`; `warning` has no
defined behaviour.

**Rules are not individually versioned.** They share one artifact's revision, so
a rule cannot be superseded alone.

**A rule naming an unimplemented kind aborts compilation.** That is deliberate
and it is the strictest possible choice; whether it should instead be a
diagnostic is unaddressed.
