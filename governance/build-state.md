---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: vertical-slice
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**The first vertical slice** (`ADR-0082`). Finishing B1 is no longer the goal.

Every capability is evaluated against one question (`ADR-0080`): *how does this
improve a developer's ability to understand, modify or evolve a real software
system?*

## The slice runs

```sh
python3 tools/compile.py examples/vertical-slice
python3 tools/ask.py examples/vertical-slice impact Concept.Order
python3 tools/ask.py examples/vertical-slice rationale Invariant.PaymentBeforeShipping --json
open examples/vertical-slice/build/explorer.html
```

**Six of the seven questions `ADR-0082` names are answered from the model.**

| # | Question | State |
|---|---|---|
| 1 | What breaks if I change this Concept? | ✅ |
| 2 | Why does this relationship exist? | ✅ |
| 3 | Which ADR established this Invariant? | ✅ — and whether it still stands |
| 4 | Which Capabilities depend on this Workflow? | ✅ |
| 5 | Which Tests must change? | ✅ via `validates`; **no `Test` entity needed** |
| 6 | Which Specifications become inconsistent? | ✅ via `represents` |
| 7 | Which AI workflow should execute? | ❌ **no trigger concept exists** |

## What exists

| Area | State |
|---|---|
| **`examples/vertical-slice/`** | **28 nodes, 52 edges.** The product demonstration |
| **`tools/ask.py`** | **9 questions**, every one with `--json`. A CKM consumer that parses no source |
| **`compiler/emitters/explorer/`** | **8 question-oriented screens** |
| **`compiler/registry/`** | **4 declared registries, 3 extraction kinds.** Three ad-hoc readers removed |
| `compiler/` | 10 features, each declaring input, output, invariants, determinism |
| `compiler/validator/` | 6 rule kinds executing 7 declared rules |
| `tests/` | 13 fixtures — 6 pass, 7 must fail — with golden outputs for four emitters |
| **`model/metamodel/`** | **23 of 27 entities specified** |
| `model/metamodel/ontology/` | OWL 0.4.0 — 660 triples |
| ADRs | 83 — 75 accepted, 8 superseded |
| Issues | 74 — 1 open, 51 resolved, 22 deferred |
| Acceptance Records | 24 |
| Session journal | 29 entries |

## What does not exist

**No trigger concept**, so question 7 is unanswerable. `triggers` is a registered
core relationship type and **no entity uses it**.

No `Manifest` — a project is still *whatever is in `model/*.md`*. No
`Vocabulary`. `Principle` and `KnowledgePackage` deferred.

**No queryability.** Consumers scan lists; there is no index, and the Explorer
computes transitive closures in the browser. Nobody knows where that stops.

**Provenance is a path, not a revision** (`ADR-0064` wants
`(artifact-id, revision-id)`).

**No real system has been modelled.** 28 nodes is the largest model that exists.

## Blocking

**Nothing blocks the slice.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections — an architectural violation under `ADR-0072`. Now measurable: **4 registries, 4 hand-maintained sources, 0 generated.** Plus four governance indexes, the corrections table, the ontology and the parser schemas |

## Architectural debt

**22 deferred issues.** Nearest: `ISSUE-0073` (Operational Knowledge),
`ISSUE-0048` (`ADR.corrects` has no mechanism), `ISSUE-0063`.

## Debt discovered while building

| Question | Where |
|---|---|
| **Question 7 has no answer** — nothing connects a kind of change to a workflow | `examples/vertical-slice/README.md` |
| Nothing validates a registry against its own `membership` rule; rule and mechanism can disagree silently | `registry.md` |
| No Registry Projection is generated; the specification/projection split is half-built | `registry.md` |
| The CKM's compatibility policy is written and unexercised; nothing diffs two models | `canonical-knowledge-model.md` |
| `VR-0007` has no fixture of its own | `tests/README.md` |
| Severity is declared and unused | `validation-rules.md` |
| 441 field declarations required by `ADR-0074`; fewer than a third exist | `relationship-vocabulary.md` |

## Acceptance status

`ACCEPT-0001` (trust root) through `ACCEPT-0024`, covering `SESSION-0006`
through `SESSION-0028`.

**`ADR-0080`–`ADR-0083`, the vertical slice, `tools/ask.py`, declared registries,
the question-oriented Explorer and the `Registry` specification are
`Under Review`.**

## Next action

**Model a real software system** (`ADR-0082`).

A metamodel that only models Engineering OS is unproven. Self-modeling is the
cheaper first target and the weaker evidence — the metamodel was designed against
this repository. **An external system is what demonstrates the architecture
generalizes**, and is therefore the one that matters.

Candidates: a full self-model of Engineering OS · GEAI · GeneXus · Kubernetes ·
PostgreSQL.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
