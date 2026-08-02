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

## Current milestone — model one large external software system

`ADR-0087`. **Not a toy example. Not another Engineering OS repository.**

The system must already have architecture, source code, documentation, evolution
history, bugs and design decisions.

**The success criterion is not "can it represent the system."** It is:

> **Does Engineering OS reveal relationships that existing documentation
> cannot?**

**Recommended: Kubernetes** — KEPs are the only candidate whose design decisions
are already an indexed, first-class corpus, which is what *which decision
established this?* most needs. The choice is the Project Owner's.

**One subsystem modelled deeply beats the whole system modelled shallowly.**

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
