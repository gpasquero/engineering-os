---
id: MODEL-GOVERNANCE-GATES
title: Governance Gates
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0021, ADR-0023, ADR-0100, ADR-0101]
---

# Governance Gates

> **Workers perform work. Governance authorizes change. Those responsibilities
> never merge** (`ADR-0100`).

A gate declares **what change it authorizes** and **the rule it enforces**. It is
not a worker, has no capabilities, and cannot be satisfied by any model however
capable — **authority is the question, not ability.**

```yaml
governance-gates:
  - id: G-work-acceptance
    authorizes: Completion of a task graph
    enforces: ADR-0023
    rule: >
      A reviewer who is not the author records a decision. Self-certification is
      prohibited.
    required-for-task-kinds: [T-review-gate]

  - id: G-knowledge-update
    authorizes: An observation entering the Canonical Knowledge Model
    enforces: ADR-0101
    rule: >
      An observation whose kind is classified `govern` requires authorization
      before it may be recorded. An observation contradicting an accepted
      decision is never recorded mechanically.
    required-for-observation-outcomes: [govern]
    note: >
      The general gate. A kind-specific gate takes precedence over this one.

  - id: G-decision-record
    authorizes: A change that supersedes or contradicts an accepted decision
    enforces: ADR-0002
    rule: >
      An accepted ADR is never edited. A contradicting change requires a new
      decision record, and the original is superseded rather than amended.
    required-for-observation-kinds: [O-assumption-disproved]
```

## Two things are called gates

**Deliberately, and they are different** (`ADR-0100`):

| | Is | Layer |
|---|---|---|
| `EngineeringGate` | a gate **a described system has** | Layer A entity |
| Governance Gate | a gate **the Director enforces at runtime** | this registry |

Neither derives from the other. Conflating them would put runtime concerns in the
metamodel, which `ADR-0053` forbids.

## Found by the end-to-end simulation

**Two defects, both in these declarations rather than in the engine.**

**Gate identifiers were written without their `O-` prefix**, so
`G-decision-record` matched no observation and every governed observation fell
through to the general gate. A registry that names things wrongly is not
detectably different from one that names nothing.

**`G-decision-record` claimed to be required for `architectural-concern`**, which
is classified `reject` — an observation that never enters the model cannot
require authorization to enter it. **A gate on a rejected kind is unreachable by
construction**, and nothing checked it.

Both were invisible until something ran the loop end to end.

## Debt

**No gate has ever been passed.** Three are declared and nothing executes them,
because nothing executes.

**`G-decision-record` fires on two observation kinds and cannot check the
condition it states.** Whether a change *actually* contradicts an accepted
decision is a judgement; the gate can only require that someone make it.

**Gates have no recorded outcome.** Passing one should produce an authorization
artifact, and no such artifact exists.
