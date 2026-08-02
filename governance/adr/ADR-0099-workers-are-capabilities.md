---
id: ADR-0099
title: Workers are capabilities, not vendors; assignment is deterministic matching
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0017, ADR-0081, ADR-0092, ADR-0097, ADR-0098]
---

# ADR-0099 — Workers are capabilities

## Context

`ADR-0097` made tasks declare **required capabilities, never workers**. Nothing
yet declares what a worker *is*.

## Decision

### Workers are types, not vendors

> **Workers are not Claude. Workers are capabilities.**

A Worker is a **type** — `SourceCodeEditor`, `ArchitectureReviewer`,
`TestRunner`, `DocumentationWriter`, `StaticAnalyzer`, `MigrationPlanner` —
declaring the capabilities it provides.

**Claude, Codex and future models are runtime implementations of one or more
worker types.** They are named nowhere in the model.

This is `ADR-0081`'s rule about the CKM applied to execution: **a component bound
to a vendor must be rewritten when the vendor changes**, and models change faster
than anything else in this architecture.

### Assignment is deterministic matching

```text
Task declares required capabilities
Worker declares provided capabilities
Assignment = { worker : required ⊆ provided }
```

> **No heuristic. No model selection logic. No prompt engineering.**

Where several worker types satisfy a task, **all are reported**; the Director
does not choose between them. Choosing an implementation is a **runtime**
concern, and the runtime is not part of Engineering OS.

> **The Engineering Director decides the work. The runtime decides which
> implementation satisfies each capability.**

### An unsatisfiable task is a first-class result

A task whose capabilities no worker type provides is **reported, not dropped**.
That is not a failure of routing — it is the system stating that the work it
planned cannot currently be performed.

## Alternatives considered

**Route to named models.** Rejected — it dates the architecture to a model
generation and makes capability declarations decorative.

**Score workers and pick the best.** Rejected twice over: it is a heuristic where
the decision states there is none, and scoring is the confidence-number failure
`ADR-0090` already rejected.

**Let the runtime infer capabilities from a model's description.** Rejected: an
inferred capability is a guess, and the whole assignment stage would inherit its
uncertainty.

## Consequences

### Positive

- **Vendor independence is structural**, not a promise. No model name appears in
  any declaration.
- Assignment is a set-containment test — trivially deterministic, trivially
  testable, and impossible to make clever by accident.
- **Unsatisfiable tasks become visible**, which is how missing worker types are
  discovered rather than assumed.

### Negative

- **A worker type that provides a capability badly is indistinguishable from one
  that provides it well.** The model has no notion of quality, and by design
  cannot acquire one without becoming a heuristic.
- **Reporting all matching workers pushes a real decision to the runtime**, which
  is correct by this decision and means the KPI stops improving at that boundary.

### Neutral

- No entity is added. Workers are a registry.

## Compliance

`model/workers.md` declares worker types and their capabilities. **No model or
vendor is named.** `compiler/assign/` performs set containment and nothing else.
