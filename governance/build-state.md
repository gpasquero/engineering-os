---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: discovery
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**Engineering Discovery** (`ADR-0105`) — the first engineering workflow
Engineering OS executes on an unknown repository.

## The correction, and its test

**The Director must never operate directly on a source repository.** It operates
on an Engineering Model.

`SESSION-0037`'s `ai-desk` input was produced by `grep` — a valid technique and
**not the architecture.**

> **The only difference between Brownfield and Continuous Engineering is the
> objective. Everything else is identical.**

**Tested and it holds:**

```sh
python3 tools/direct.py external/ai-desk-onboarding I-onboard Artifact.AiDeskRepository
```

Plan, task graph, worker assignment, governance gate, knowledge-update task —
through **`tools/direct.py` unchanged.** **22 decisions before the first LLM
token; 4 left to workers.**

**No execution mechanism was built.** Discovery is declarations in the existing
registries.

## Two mechanisms became one

`ADR-0106`. A **Candidate Engineering Model** and an **Execution Observation**
are the same artifact at different scales — sets of proposed assertions with
provenance, produced by probabilistic workers, requiring authorization.

```text
discovery workers ─┐
                   ├→ proposed assertions → review → authoring sources → compiler → CKM
execution workers ─┘
```

**The loop's unclosed step and discovery intake are one mechanism to build.**
`ADR-0072` survives untouched: the compiler remains the only writer, still
writing from authoring sources.

## What exists

| Area | State |
|---|---|
| **`discovery/ARCHITECTURE.md`** | Contracts · artifacts · extension points · worker types · compiler interaction |
| **`external/ai-desk-onboarding/`** | **The seed: two files.** A repository is an `Artifact`; discovery is a plan applied to it |
| `model/workers.md` | **12 types** — 5 for discovery, 2 of them mechanical |
| `model/task-kinds.md` | 11 kinds. **The action vocabulary is declared here and nowhere else** |
| `model/plans.md` · `recommendations.md` · `engineering-intents.md` | 4 · 4 · 4 |
| `external/ai-desk-auth/` | 31 nodes — **reclassified: a hand-made Candidate Engineering Model that skipped its review** |
| `external/kubernetes-ssa/` | 41 nodes, four source classes, end-to-end simulation |
| `tests/` | 17 fixtures, 9 negative, golden outputs |
| Registries | 14 |
| `model/metamodel/` | 23 of 27 entities — **unchanged for seven milestones** |

## Friction produced the session's only code change

Declaring discovery needed three new actions — `extract`, `interpret`,
`identify-gaps` — and **the action vocabulary was hardcoded in Python.**

Task kinds already declare `from-action`, so **an action exists because a task
kind derives from it.** The vocabulary is now derived, and a hardcoded registry
pretending to be a mechanism is gone.

**One vocabulary removed, not added** (`ADR-0102`).

## What does not exist

**No applier.** Nothing writes an accepted proposal as an authoring source — the
single missing mechanism, now serving two purposes.

**No discovery worker.** Five types are declared and none is implemented.

**No proposal serialisation format.**

## Blocking

**Nothing.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. Fourteen registries, zero generated |

## Governance note

**`ACCEPT-0033` is not allocated.** `ACCEPT-0034` was requested when the highest
allocated was `ACCEPT-0032`. The identifier is used as requested and the gap is
documented in the record and the index; **a sequence-contiguity check was added
to validation** so a future gap is reported rather than discovered.

## Debt discovered while building

| Question | Where |
|---|---|
| **Review does not scale.** A candidate model may propose thousands of assertions; batch acceptance trades scrutiny for throughput — the trade `ADR-0023` exists to prevent | `discovery/ARCHITECTURE.md`, `ADR-0106` |
| Discovery is the largest worker surface contemplated; naming the activities does not make them cheap | `ADR-0105` |
| Writing authoring sources from proposals means **workers shape the repository's text**, so the parser schema is now load-bearing | `ADR-0106` |
| `ai-desk-auth` stands as a candidate model that skipped its review | `ADR-0105` |

## Next action

**The applier.** Write an accepted proposal as an authoring source.

It closes the loop and gives discovery its path **from the same code** — which is
`ADR-0106`'s point and the reason it is worth building before any discovery
worker.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
