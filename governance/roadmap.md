---
id: ROADMAP
title: Roadmap
status: accepted
created: 2026-08-02
updated: 2026-08-02
supersedes: sources/handoff/ROADMAP.md (pre-M1, ten "Deliveries")
related: [ADR-0062]
---

# Roadmap

**The project has left the "prove the architecture" phase and entered the
"prove usefulness" phase** (`ADR-0084`).

> **Success is measured by the quality of the engineering questions Engineering
> OS can answer** — not by the sophistication of the metamodel.

Every proposal is evaluated by one criterion:

> **Does this allow Engineering OS to answer better engineering questions about
> real software systems?** If not, it should probably wait.

## How work begins

`ADR-0085`. **Never with "we need another entity."**

```text
Engineering Question → Required semantic capability
  → Metamodel extension (only if necessary) → Compiler → Explorer → Regression test
```

## Completed — semantic API hardening

`ADR-0088`. The query engine is part of the product contract, so its semantics
were made precise **before** real-system findings depend on it.

| Defect | Fixed |
|---|---|
| Path provenance reduced to one predicate | Rows carry the complete ordered path, every edge with direction and match reason |
| Edge output returned an induced subgraph | `output: edges` returns what the traversal walked; `induced-subgraph` is explicit and never the default |
| `with` could evaluate the wrong parallel edge | It evaluates the edge in hand; a fixture has two predicates between one pair of nodes |
| Query declarations unvalidated | A schema; **12 malformed declarations, all rejected** |
| Emptiness hid applicability errors | Four statuses: `ok`, `empty`, `not-applicable`, `invalid` |
| Determinism and limits undefined | Cycles, ties, ordering, depth 16, results 1000, truncation diagnostics |
| Parity compared only identifiers | Status, rows, paths, ordering, edges and diagnostics — **334 pairs** |

## Current milestone — model one large external software system

`ADR-0087`. **Not a toy example. Not another Engineering OS repository.**

The system must already have architecture, source code, documentation, evolution
history, bugs and design decisions.

**The success criterion is not "can it represent the system."** It is:

> **Does Engineering OS reveal relationships that existing documentation
> cannot?**

**Kubernetes**, confirmed by the Project Owner.

**One bounded, decision-rich subsystem, modelled deeply.** Not all of Kubernetes
superficially. The subsystem must have multiple KEPs, source implementation,
public documentation, tests, lifecycle or state transitions, known behavioural
changes, and dependencies on other components.

### Required questions for the external validation

1. Which design decision introduced this behaviour?
2. Which source components implement it?
3. Which tests protect it?
4. What changes if the behaviour changes?
5. Which invariants or compatibility promises constrain it?
6. Which later decisions superseded or refined the original decision?
7. **What information was not discoverable from any single existing document?**

> **The seventh is the primary proof-of-value result.** The first success
> criterion is not repository size — it is whether Engineering OS can answer
> questions that require connecting information currently scattered across KEPs,
> documentation, source and tests.

**Do not optimise the Explorer visually during this milestone.** The next product
proof comes from the quality of the answers, not from interface polish.

## Delivered

| | |
|---|---|
| **The vertical slice** | Repository → Compiler → CKM → Explorer → question → answer. 6 of 7 questions from `ADR-0082` |
| **The semantic API** | 11 declared queries, executed by two engines, **verified to agree on 334 query/subject pairs** |
| **The compiler** | 11 features, six declared phases, declarative validation, declared registries |
| **The regression suite** | 13 fixtures, 7 negative, golden outputs, deterministic rebuild, query assertions, engine equivalence |
| **The metamodel** | 23 of 27 entities. **No longer the objective** |

## Known unanswered

| Question | Why |
|---|---|
| **Which AI workflow should execute?** | Nothing connects a *kind of change* to a workflow. `triggers` is a registered core relationship type **no entity uses**. `ADR-0084` frames this as semantic workflow orchestration, not a missing `Trigger` entity |

## Deferred

`Manifest`, `Vocabulary` — built when a question needs them (`ADR-0085`).
`Principle`, `KnowledgePackage` — the compiler compiles no ADRs, and there is one
repository.

**M1–M13** from the original plan remain eventual scope. They are not the
objective; the questions are.
