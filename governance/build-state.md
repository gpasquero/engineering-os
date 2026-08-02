---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: prove-usefulness
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**The prove-usefulness phase** (`ADR-0084`). The prove-the-architecture phase
closed with `ACCEPT-0025`.

> Success is measured by **the quality of the engineering questions Engineering
> OS can answer**, about **real software systems**.

Work begins with a question, never with an entity (`ADR-0085`).

## The semantic API

```sh
python3 tools/ask.py examples/vertical-slice questions
python3 tools/ask.py examples/vertical-slice Q-rationale Invariant.SingleCurrency --json
python3 tools/check-engines.py
open examples/vertical-slice/build/explorer.html
```

**11 questions, declared as data** in `model/queries.md`. The CLI implements
none of them; the Explorer implements none of them. Both execute the same
declarations (`ADR-0086`).

```text
both engines agree on every declared query
  examples/vertical-slice — 227 query/subject pairs agree
  examples/tiny           — 107 query/subject pairs agree
```

## What exists

| Area | State |
|---|---|
| **`model/queries.md`** | **11 declared queries**, each with a rationale. Adding a question is a data change |
| **`compiler/query/`** | 5 operators — `select`, `traverse`, `keep`, `reject`, `with` |
| **`tools/check-engines.py`** | Runs every query through both engines for every node. **334 pairs, all agree** |
| **`compiler/emitters/explorer/`** | Question-driven. Home page asks *what are you trying to accomplish?* |
| `tools/ask.py` | A thin executor. Implements no question |
| `examples/vertical-slice/` | 28 nodes, 52 edges |
| `compiler/` | 11 features, six declared phases, declarative validation, declared registries |
| `tests/` | 13 fixtures — 6 pass, 7 must fail — golden outputs, determinism, **query assertions, engine equivalence** |
| `model/metamodel/` | 23 of 27 entities. **No longer the objective** |
| ADRs | 87 — 79 accepted, 8 superseded |
| Issues | 74 — 1 open, 51 resolved, 22 deferred |
| Acceptance Records | 25 |
| Session journal | 30 entries |

## What does not exist

**No real system has been modelled.** 28 nodes is the largest model, in a domain
invented to exercise the metamodel. **This is the gap `ADR-0087` exists to
close**, and until it does, every claim is verifiable only by reading this
repository.

**No answer to *which AI workflow should execute?*** `triggers` is a registered
core relationship type that **no entity uses**.

No index — **every query scans**. `Q-orphan-concepts` walks every edge for every
Concept. At 28 nodes that is invisible.

No `Manifest`, no `Vocabulary`. `Principle` and `KnowledgePackage` deferred.
Provenance is a path, not a revision (`ADR-0064`).

## Blocking

**Nothing blocks the milestone.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections — an architectural violation under `ADR-0072`. **Five registries, five hand-maintained sources, zero generated**, plus four governance indexes, the corrections table, the ontology and the parser schemas |

## Architectural debt

**22 deferred issues.** Nearest: `ISSUE-0073` (Operational Knowledge),
`ISSUE-0048`, `ISSUE-0063`.

## Debt discovered while building

| Question | Where |
|---|---|
| **Two engines execute the query language.** Divergence is now *detected*, not prevented — and only where `node` is installed | `ADR-0086`, `check-engines.py` |
| No query is parameterised beyond `subject` — *impact limited to two hops* is inexpressible | `queries.md` |
| `subject: none` queries silently ignore a subject | `queries.md` |
| Every query scans; there is no index | `queries.md` |
| Nothing validates a registry against its own `membership` rule | `registry.md` |
| The CKM compatibility policy is unexercised; nothing diffs two models | `canonical-knowledge-model.md` |
| 441 field declarations required by `ADR-0074`; fewer than a third exist | `relationship-vocabulary.md` |

## Acceptance status

`ACCEPT-0001` (trust root) through `ACCEPT-0025`, covering `SESSION-0006`
through `SESSION-0029`.

**`ADR-0084`–`ADR-0087`, `model/queries.md`, the query engine, the rewritten
`ask.py`, the question-driven Explorer and `tools/check-engines.py` are
`Under Review`.**

## Next action

**Model one large external software system** (`ADR-0087`).

The success criterion is **not** *can it represent the system*. It is:

> **Does Engineering OS reveal relationships that existing documentation
> cannot?**

Recommended: **Kubernetes** — KEPs are the only candidate whose design decisions
are already an indexed corpus, which is what *which decision established this?*
most needs. **The choice is the Project Owner's.**

One subsystem modelled deeply beats the whole system modelled shallowly.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
