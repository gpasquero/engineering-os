---
id: ADR-0077
title: The compiler executes ValidationRules; it does not contain them
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0048, ADR-0061, ADR-0071, ADR-0073, ADR-0075]
---

# ADR-0077 — Declarative validation

## Context

`resolve()` hard-codes four checks: node types must be declared entities,
predicates must have a registered parent, targets must resolve, identities must
be unique.

**Those are rules the model should own, expressed as Python.** `ADR-0075` already
identified this: `ValidationRule` exists today as implementation because the
model has no term for it.

## Decision

**Validation is declarative. The compiler is an execution engine for rules, not
the place where rules are authored.**

```text
Metamodel  →  ValidationRule  →  Compiler  →  ValidationResult
```

- A **ValidationRule** is authored, versioned and accepted like any other
  authoritative artifact. It is Layer A: it is meaningful without a compiler
  (`ADR-0076`).
- A **ValidationResult** is produced by execution and is compiler architecture.
- **The compiler contains rule *kinds*, not rules.** A kind is a mechanism —
  *this predicate must be registered*; a rule is an instance of a kind bound to
  specific model elements.

### What stays in code

A rule kind is code, and must be, because something has to evaluate it. The line:

> **If changing what is checked requires editing Python, the rule is in the wrong
> place. If changing *how* a class of check is evaluated requires editing Python,
> that is correct.**

Adding a new rule of an existing kind is a data change. Adding a new *kind* is a
compiler change and should be rare.

## Alternatives considered

**Keep checks in `resolve()`.** Rejected — the reason for the decision. Every
rule added this way makes the metamodel less able to describe its own
enforcement.

**A general expression language for rules.** Rejected as premature and as a
determinism risk. An arbitrary expression evaluator makes it hard to guarantee
that validation terminates or that it is deterministic (`ADR-0073`), and there
are four rules. Rule kinds are a smaller commitment that can grow.

**Express rules in SHACL or OWL restrictions.** Attractive, and rejected for now:
it binds validation to one formalism, which `ADR-0066` and `ADR-0068` both
rejected in the analogous case. A rule kind may *compile to* SHACL later, which
is the correct direction.

## Consequences

### Positive

- **The metamodel owns its own enforcement.** A rule can be read, reviewed and
  accepted without reading the compiler.
- Rules become testable individually, and a test project can name the rule it is
  expected to violate.
- `ValidationRule` gains the concrete justification `ADR-0075` requires.

### Negative

- **Indirection for four rules.** A rules file plus a kind registry is more
  machinery than four `if` statements, and it pays off only as rules accumulate.
- **A rule kind is still a hard-coded vocabulary**, so the extensibility is
  bounded by what kinds exist. The Registry Pattern applies (`ADR-0031`) and the
  bound is real.

### Neutral

- The four existing checks keep their behaviour and change their location.

## Compliance

`compiler/validator/` implements rule kinds and executes rules.
`model/metamodel/validation-rules.md` declares the rules. No check is authored in
Python.
