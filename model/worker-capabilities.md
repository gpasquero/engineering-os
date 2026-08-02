---
id: MODEL-WORKER-CAPABILITIES
title: Worker Capabilities
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0092, ADR-0095, ADR-0097]
---

# Worker Capabilities

**What kind of worker a task requires** — never which worker.

> A task bound to a worker must be rewritten when the worker changes. **Routing
> is a separate stage** (`ADR-0095`) and is not built.

Each capability declares an **execution class**, which is what later lets the
system decide which tasks need a language model, which are mechanical, and which
need human authority.

```yaml
worker-capabilities:
  - id: C-semantic-query
    label: Execute a semantic query
    execution: mechanical
    rationale: >
      Deterministic and already implemented. A task requiring only this needs no
      worker at all — Engineering OS performs it.

  - id: C-read-source
    label: Read and comprehend source or documentation
    execution: reasoning
    rationale: >
      Requires understanding prose or code written for humans. This is the
      boundary at which a language model becomes useful.

  - id: C-modify-source
    label: Modify source
    execution: reasoning
    rationale: >
      The archetypal delegated task. Engineering OS never performs it.

  - id: C-run-tests
    label: Execute a test suite
    execution: mechanical
    rationale: >
      A script runs it and the result is a fact, not an interpretation.

  - id: C-approve
    label: Approve or reject
    execution: human
    rationale: >
      Acceptance confers Active status and self-certification is prohibited
      (ADR-0023). No worker of any kind may hold this capability.

  - id: C-record-knowledge
    label: Record an assertion in the model
    execution: mechanical
    rationale: >
      Writing to the model is mechanical. Deciding WHAT to record is not, and is
      a different capability.
```

## Execution classes

| Class | Performed by | Enters the architecture at |
|---|---|---|
| `mechanical` | Engineering OS itself, or a script | any stage |
| `reasoning` | a language model or a human | **Execution only** (`ADR-0092`) |
| `human` | a person | Review |

## Debt

**Execution classes are authored judgements.** That `C-read-source` requires
reasoning rather than mechanism is an assertion no evidence supports — it is
plausible and unverified.

**No worker exists to hold any capability.** This is a vocabulary for a routing
stage that has not been built.

**`C-record-knowledge` splits recording from deciding**, and only the mechanical
half is declared. The capability that decides *what* to record has no entry,
because the loop does not yet close.
