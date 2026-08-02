---
id: METAMODEL-VALIDATION-RULES
title: Validation Rules
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
artifact-kind: authoritative
established-by: [ADR-0048, ADR-0071, ADR-0077]
---

# Validation Rules

**The rules the compiler executes.** It does not contain them (`ADR-0077`).

```text
Metamodel  →  ValidationRule  →  Compiler  →  ValidationResult
```

> **If changing *what* is checked requires editing Python, the rule is in the
> wrong place. If changing *how* a class of check is evaluated requires editing
> Python, that is correct.**

The compiler implements **rule kinds** — mechanisms. This file declares **rules**
— instances of a kind bound to specific model elements.

## Rule kinds

Registered, not enumerated (`ADR-0031`). Adding a kind is a compiler change and
should be rare.

| Kind | Checks |
|---|---|
| `declared-entity-type` | every node's `type` names a declared metamodel entity |
| `registered-predicate` | every predicate specializes a registered core type |
| `resolvable-target` | every relationship target resolves to a node in the project |
| `unique-identity` | no identifier is declared twice |
| `required-relationship` | nodes of a given type declare a given predicate |
| `forbidden-self-reference` | a predicate may not point at its own subject |

## Rules

```yaml
rules:
  - id: VR-0001
    kind: declared-entity-type
    severity: error
    message: "'{value}' is not a metamodel entity"
    rationale: >
      The metamodel is an executable contract, not a suggestion (ADR-0072).

  - id: VR-0002
    kind: registered-predicate
    severity: error
    message: "predicate '{value}' has no registered parent (ADR-0071)"
    rationale: >
      A predicate with no parent is outside the relationship vocabulary, and
      the vocabulary is the type system of the knowledge graph (ADR-0074).

  - id: VR-0003
    kind: resolvable-target
    severity: error
    message: "'{predicate}' points at unknown node '{value}'"
    rationale: >
      An edge to nothing is not knowledge.

  - id: VR-0004
    kind: unique-identity
    severity: error
    message: "duplicate node id '{value}' declared {count} times"
    rationale: >
      Two nodes with one identity make every edge to that identity ambiguous.

  - id: VR-0005
    kind: forbidden-self-reference
    severity: error
    applies-to-predicates: [scoped-to, revision-of, step-of, specialises, supersedes]
    message: "'{predicate}' on '{subject}' points at itself"
    rationale: >
      A containment, revision or supersession edge to itself is a cycle of
      length one. It is always an authoring error and no existing rule catches it.

  - id: VR-0006
    kind: required-relationship
    severity: error
    applies-to-type: WorkflowStep
    requires-predicate: executes
    message: "a WorkflowStep must declare 'executes'"
    rationale: >
      A step that executes nothing is not a step. WorkflowStep exists only to
      carry the position of a Skill within a Workflow (ADR-0068).

  - id: VR-0007
    kind: required-relationship
    severity: error
    applies-to-type: ArtifactRevision
    requires-predicate: revision-of
    message: "an ArtifactRevision must declare 'revision-of'"
    rationale: >
      Identity is the pair (artifact-id, revision-id) (ADR-0064). A revision
      with no artifact has half an identity.
```

## What was learned by declaring these

**Five rules existed as Python; seven exist now.** `VR-0005` and `VR-0006` were
written because the format made their absence obvious — declaring rules in a
table invites the question *what else belongs here?* in a way that adding
conditionals to a function does not.

**`VR-0007` was found by the rule it generalises.** Writing `VR-0006` for
`WorkflowStep.executes` immediately raised `ArtifactRevision.revision-of`, which
is the same shape and had never been checked.

## Debt

**Severity is declared and unused.** Every rule is `error`; nothing consumes the
field, and a `warning` severity has no defined behaviour.

**Rules are not versioned individually.** They live in one artifact whose
revision covers all of them, so a rule cannot be superseded on its own.

**Nothing checks that a rule kind exists.** A rule naming an unimplemented kind
is silently skipped — which is the failure mode this file was created to
eliminate, reproduced one level up.
