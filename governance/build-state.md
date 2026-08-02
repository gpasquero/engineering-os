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

**The prove-usefulness phase** (`ADR-0084`). Work begins with a question, never
with an entity (`ADR-0085`).

**Semantic API hardening is complete** (`ADR-0088`). The next milestone is
Kubernetes.

## The semantic API

```sh
python3 tools/ask.py examples/vertical-slice Q-impact Concept.Order --paths
python3 tools/ask.py examples/vertical-slice Q-status Concept.Order    # not-applicable
python3 tools/check-query-schema.py
python3 tools/check-engines.py
```

**11 questions declared as data.** The CLI implements none; the Explorer
implements none. Both execute the same declarations, and **parity is a public
invariant** compared on status, rows, paths, ordering, edges and diagnostics.

```text
every malformed declaration was rejected
both engines agree on every declared query
  examples/vertical-slice — 227 pairs
  examples/tiny           — 107 pairs
```

## The result contract (`ADR-0088`)

| | |
|---|---|
| **Path provenance** | Every row carries the complete ordered path — each edge with direction and the reason it matched. `via` is the first predicate, never the explanation |
| **Edge output** | `edges` returns what the traversal walked. `induced-subgraph` is explicit and never the default |
| **Parallel edges** | `with` evaluates the edge in hand and reports `{id, predicate}` |
| **Declarations** | Validated against a schema. **An unknown field fails** |
| **Applicability** | `ok` · `empty` · `not-applicable` · `invalid`. An empty result never hides an applicability error |
| **Limits** | depth 16, results 1000, per-query override, **truncation emits a diagnostic** |

## What exists

| Area | State |
|---|---|
| `model/queries.md` | 11 declared queries; 4 declare `applies-to` |
| `compiler/query/` | 5 operators, a declaration schema, the result contract |
| **`tools/check-query-schema.py`** | **12 malformed declarations, all rejected** |
| **`tools/check-engines.py`** | Full-fidelity parity — **334 pairs** |
| `tests/` | **14 fixtures** — 6 pass, 8 must fail — golden outputs, determinism, query rows, status and paths |
| `compiler/` | 11 features, six declared phases, declarative validation, declared registries |
| `examples/vertical-slice/` | 28 nodes, 52 edges |
| `model/metamodel/` | 23 of 27 entities. **Not the objective** |
| ADRs | 88 — 80 accepted, 8 superseded |
| Issues | 74 — 1 open, 51 resolved, 22 deferred |
| Acceptance Records | 26 |
| Session journal | 31 entries |

## What does not exist

**No real system has been modelled.** 28 nodes remains the largest model, in a
domain invented to exercise the metamodel. **Every claim is still verifiable only
by reading this repository.**

**No answer to *which engineering workflow should execute?*** It stays a product
requirement until a real external model demonstrates the minimum semantics needed
(`ADR-0084`). **No `Trigger`, no AI workflow selection, no speculative concepts.**

No index — every query scans. No `Manifest`, no `Vocabulary`. `Principle` and
`KnowledgePackage` deferred. Provenance is a path, not a revision.

## Blocking

**Nothing blocks the milestone.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. Five registries, five hand-maintained sources, zero generated, plus four governance indexes, the corrections table, the ontology and the parser schemas |

## Debt discovered while building

| Question | Where |
|---|---|
| **Paths are larger than the rows carrying them** — a 5-hop result carries 5 edge records per row, and nothing prunes them | `ADR-0088` |
| `applies-to` is declared on 4 of 11 queries; omission means *any type*, which is right for `Q-impact` and lazy for `Q-tests` | `queries.md` |
| `subject: none` queries silently ignore a subject given | `queries.md` |
| Every query scans; there is no index | `queries.md` |
| Parity is verified only where `node` is installed; it skips loudly otherwise | `check-engines.py` |
| Nothing validates a registry against its own `membership` rule | `registry.md` |

## Acceptance status

`ACCEPT-0001` (trust root) through `ACCEPT-0026`, covering `SESSION-0006`
through `SESSION-0030`.

**`ADR-0088`, the hardened query engine, the declaration schema, the parallel-edge
fixture and the full-fidelity parity check are `Under Review`.**

## Next action

**Kubernetes** (`ADR-0087`, confirmed). One bounded, decision-rich subsystem
modelled deeply — multiple KEPs, source, documentation, tests, lifecycle
transitions, known behavioural changes, dependencies on other components.

Seven required questions, and **the seventh is the proof-of-value result**:

> **What information was not discoverable from any single existing document?**

**Do not optimise the Explorer visually.** The proof comes from the answers.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
