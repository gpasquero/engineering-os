---
id: ADR-0062
title: Architecture through implementation — build first, refine when implementation demands it
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0003, ADR-0035, ADR-0049, ADR-0054]
---

# ADR-0062 — Architecture through implementation

**This changes how the project advances.** It does not change any architectural
decision.

## Context

Twenty sessions produced sixty-one architectural decisions, seventy-three
recorded issues, sixteen acceptance records — and **no artifact outside
`governance/`**. Every session followed the same shape: answer the previous
session's questions, and open new ones.

The architecture that emerged is coherent. It has also never been tested against
anything.

## Decision

**The fundamental architecture of Engineering OS has reached sufficient
stability.** The order of priority changes.

### The criterion

1. **If an existing decision permits building, build.**
2. **Stop building only when a real contradiction prevents continuing.**
3. **Avoid opening new architectural concepts unless strictly necessary to
   implement the next step.**

### The question asked of every new decision

> **"Do we need to resolve this in order to build the next deliverable?"**

If the answer is **no**, it is recorded as **architectural debt** and building
continues.

### The focus

- Engineering OS Metamodel
- first OWL ontologies
- first Canonical Knowledge Model
- Knowledge Compiler specification
- first compilation pipeline
- first navigable Knowledge Explorer

**The architecture continues to evolve — guided by implementation, not by
analysis alone.**

**The goal is no longer a perfect architecture. It is the first executable
system that demonstrates the architecture works.**

## Alternatives considered

**Continue architecture-first until every open issue is resolved.** Rejected:
twenty-four issues are open and each session's answers have opened roughly two
more. The corpus is not converging on zero by this route, and nothing tests
whether the decisions are right.

**Freeze the architecture entirely and implement against it.** Rejected — the
decision explicitly preserves evolution. Implementation reveals defects that
analysis cannot, and refusing to act on them would waste the main benefit of
building.

**Reduce rigour on the artifacts already produced.** Not considered. Acceptance,
traceability and the record of decisions stay exactly as they are; what changes
is the *order* of work, not its discipline.

## Consequences

### Positive

- **The architecture becomes testable.** Sixty-one decisions have been reviewed
  by one reader; none has met an implementation.
- **Over-engineering risk drops sharply.** Concepts introduced to answer
  hypothetical questions will now be introduced only when a deliverable needs
  them.
- Architectural debt becomes visible as debt rather than as blockers, so the
  distinction between *cannot proceed* and *would prefer to know* is explicit.
- It restores the project's own principle: `ADR-0011` and `ADR-0014` describe a
  knowledge compiler, and a compiler is judged by what it compiles.

### Negative

- **Debt deferred under this rule will be discovered later, in code**, where it
  is more expensive to correct than in an ADR. That is the trade being made
  deliberately.
- Some deferred issues are genuine inconsistencies, not merely unanswered
  questions — `ISSUE-0073`'s "runtime" collision will propagate into the
  metamodel if the metamodel is written before it is settled.
- Building under an architecture with twenty-plus open questions means some
  early artifacts will be rebuilt. Accepting that is the point, but the cost is
  real.

### Neutral

- No architectural decision is superseded, corrected or weakened. The
  governance, acceptance and traceability discipline is unchanged.

## Compliance

Every new question is tested against *"do we need this to build the next
deliverable?"* before an issue is opened as a blocker. A negative answer
produces `deferred` architectural debt. Building stops only for a contradiction
that prevents continuing.
