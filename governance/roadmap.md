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

**The goal is no longer to finish B1** (`ADR-0082`).

Every milestone is evaluated against one question (`ADR-0080`):

> **How does this improve a developer's ability to understand, modify or evolve a
> real software system?**

## Current milestone — the first vertical slice

```text
Authoritative Repository → Compiler → Canonical Knowledge Model
        → Knowledge Explorer → Developer Question → Semantic Answer
```

**Substantially delivered** in `examples/vertical-slice/`. Six of the seven
questions `ADR-0082` names are answered from the model; the seventh is not, and
the reason is recorded.

| # | Question | State |
|---|---|---|
| 1 | What breaks if I change this Concept? | ✅ |
| 2 | Why does this relationship exist? | ✅ |
| 3 | Which ADR established this Invariant? | ✅ |
| 4 | Which Capabilities depend on this Workflow? | ✅ |
| 5 | Which Tests must change? | ✅ via `validates`; no `Test` entity |
| 6 | Which Specifications become inconsistent? | ✅ via `represents`; no `Specification` entity |
| 7 | Which AI workflow should execute? | ❌ **no trigger concept exists** |

## Next — model a real software system

**A metamodel that only models Engineering OS is unproven.**

Self-modeling is cheaper and weaker evidence: the metamodel was designed against
this repository. **An external system is what demonstrates the architecture
generalizes.**

Candidates: a full self-model of Engineering OS · GEAI · GeneXus · Kubernetes ·
PostgreSQL.

## Then — the CKM as the platform's IR

`ADR-0081` commits the Canonical Knowledge Model to becoming the semantic
intermediate representation. What that still requires:

- **queryability** — consumers scan lists today; there is no index
- **provenance at revision granularity** (`ADR-0064`)
- **a stability contract with real consumers** to break it

## Deferred metamodel work

Three entities remain, built **when the slice or a real model needs them**
(`ADR-0075`, `ADR-0082`): `Manifest`, `Vocabulary`, and whatever the trigger
concept turns out to be.

`Principle` and `KnowledgePackage` stay deferred — the compiler compiles no ADRs,
and there is one repository.

## Completed build deliverables

| | |
|---|---|
| **B1** | Engineering OS Metamodel — **23 of 27 entities**; scope unchanged, priority superseded by `ADR-0082` |
| **B2** | First OWL ontology — 0.4.0, 660 triples, generated from the metamodel by hand |
| **B3** | First Canonical Knowledge Model — delivered |
| **B4** | Knowledge Compiler specification — delivered as an executable modular compiler |
| **B5** | First compilation pipeline — delivered, with a 13-fixture regression suite |
| **B6** | First navigable Knowledge Explorer — delivered, question-oriented |

**M1–M13** from the original plan remain eventual scope. They are not the
objective; the questions above are.
