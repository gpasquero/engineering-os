---
id: ADR-0086
title: The query engine is the semantic API; every question is an executable query
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0077, ADR-0079, ADR-0081, ADR-0083, ADR-0084]
---

# ADR-0086 — The query engine is the semantic API

## Context

`tools/ask.py` implements nine questions as **nine Python functions**. The
Explorer implements eight overlapping questions as **eight JavaScript
functions**. Neither can execute the other's, and a question added to one is
absent from the other.

That is a second implementation of meaning, which `ADR-0081` forbids for semantic
understanding and which had crept in as *presentation*.

## Decision

**Every question is an executable semantic query, declared as data.**

```text
Canonical Knowledge Model
          ↑
     Query engine  ←── declared queries
     ↑    ↑    ↑
Explorer  CLI  agents / automation
```

**The query engine — not individual commands — is the semantic API of
Engineering OS.**

### Queries are data, in a registry

Same split as `ADR-0077` for rules and `ADR-0083` for registries:

| | Is | Lives |
|---|---|---|
| **operator** | a mechanism — *traverse incoming edges transitively* | in the engine |
| **query** | a question — *what breaks if I change this?* | in the model |

Adding a question is a data change. Adding an operator is an engine change and
should be rare.

### One set of queries, more than one executor

The Explorer runs in a browser and cannot execute Python. **The declared queries
are shared; the engine has two implementations** — the same relationship a
compiler has to its backends.

This is a real cost and is recorded as such: **two engines can diverge, and
nothing yet detects it.** The alternative — precomputing every query for every
node at emit time — trades a correctness risk for a combinatorial one.

### Why this is admitted under `ADR-0084`

A query engine answers no question by itself, and `ADR-0084` scores that badly.
It is admitted under the *enables better questions* clause, and the case is
specific: **every future question executes through it, and today each new
question costs two hand-written implementations.**

## Alternatives considered

**Keep hand-written questions in both places.** Rejected — the reason for the
decision. Nine plus eight functions already disagree about what `impact` means.

**Adopt SPARQL, Cypher or Datalog.** Rejected for now, and this is the closest
call. Each is mature and each binds the semantic API to a formalism, which
`ADR-0066`, `ADR-0068`, `ADR-0077` and `ADR-0081` all rejected in the analogous
case. **A declared query may compile *to* any of them**, and should when the
graph outgrows in-memory traversal.

**Expose a general graph API and let consumers compose.** Rejected: it moves
question semantics into consumers, so *what impact means* would be defined by
whoever called it last.

## Consequences

### Positive

- **A question written once runs everywhere** — CLI, Explorer, agent, fixture.
- Questions become reviewable and acceptable artifacts, with a rationale, like
  ValidationRules.
- **It is the precondition for `ADR-0085`.** Question-driven development is
  expensive if each question costs two implementations.

### Negative

- **A small language is a language.** Operators will accumulate, and every one is
  a commitment. The bound is that operators are mechanisms, not questions.
- **Two engines, no equivalence check.** Recorded as debt; the honest mitigation
  is a fixture that runs every query through both.
- Expressiveness will be short of what a real question needs before long.

### Neutral

- The nine existing questions are re-expressed, not redesigned.

## Compliance

`model/queries.md` declares the queries and is registered. `compiler/query/`
implements operators. `tools/ask.py` executes declared queries and implements
none. The Explorer executes the same declarations.
