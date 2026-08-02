---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: orchestration
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**Orchestration** (`ADR-0098`). The Engineering Director owns the loop; workers
execute only individual tasks.

## The KPI

> **How much engineering judgment happens before the first LLM token is
> generated?**

```text
36 engineering decisions made before the first LLM token
 5 left to workers
```

Counts of entities, registries, queries, plans and task graphs are **inventory,
not progress**.

## The loop

```sh
python3 tools/direct.py external/kubernetes-ssa I-modify-behavior Artifact.ConflictGo \
    --observations=external/kubernetes-ssa/simulated-observations.yaml
```

| Stage | State |
|---|---|
| Developer Intent | ✅ registry, 3 intents |
| Engineering Director | ✅ `tools/direct.py` |
| Engineering Plan | ✅ 2 plans |
| Task Graph | ✅ levels computed |
| **Worker Assignment** | ✅ **set containment; no heuristic, no vendor named** |
| Execution | **mocked; no runtime exists** |
| **Execution Observations** | ✅ **intake, classification, gate routing** |
| Knowledge Update | **proposal only — nothing applies it** |
| Repository Evolution | not built |

**Seven of nine stages exist. The loop does not close.**

## What exists

| Area | State |
|---|---|
| **`compiler/direct/`** | Assignment · execution contexts · observation intake · the loop · the KPI |
| **`tools/direct.py`** | One command, intent to knowledge-update proposal. `--context=`, `--observations=`, `--json` |
| **`model/workers.md`** | 7 worker types. **No model or vendor named** (`ADR-0099`) |
| **`model/governance-gates.md`** | 3 gates. **Workers perform work; governance authorizes change** (`ADR-0100`) |
| **`model/observation-kinds.md`** | 8 kinds — **2 record, 5 govern, 1 reject** |
| `model/task-kinds.md` · `worker-capabilities.md` | 8 kinds, 6 capabilities |
| `model/plans.md` · `recommendations.md` · `queries.md` | 2 · 3 · 17 |
| `external/kubernetes-ssa/` | 41 nodes, 6 classified findings, **end-to-end simulation** |
| `tests/` | 17 fixtures, 9 negative, golden outputs |
| Registries | **14** |
| `model/metamodel/` | 23 of 27 entities — **unchanged for five milestones** |

## Two defects found only by running the loop

Both in **declarations**, not the engine, and invisible to every existing check.

**Gate identifiers were written without their `O-` prefix.** `G-decision-record`
matched nothing and every governed observation fell through to the general gate.
**A registry that names things wrongly is not detectably different from one that
names nothing** — nothing checks cross-registry references.

**A gate was declared for an observation kind that is rejected.**
`architectural-concern` never enters the model, so a gate authorizing its entry
is unreachable by construction.

## What the architecture now enforces

**Workers never write to the model** (`ADR-0101`). Six observations produced
**2 record · 2 govern · 2 reject**, and both recordable kinds are additive.

**No worker provides `C-approve`** (`ADR-0100`). Every run ends at a human, by
design.

**Assignment names no vendor.** `T02-change-inspect` matches four worker types
and the system does not choose — choosing would be a heuristic (`ADR-0099`).

## What does not exist

**Nothing applies a knowledge-update proposal.** No authorization artifact, no
write path. **This is the loop's closure and it is the one thing missing.**

No runtime implements any worker type. No second external system. No confidence
scores.

## Blocking

**Nothing.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. **Fourteen registries**, fourteen hand-maintained sources, zero generated — and cross-registry references are unchecked, which is how this session's first defect survived |

## Debt discovered while building

| Question | Where |
|---|---|
| **Cross-registry references are unchecked** — a gate naming a kind that does not exist matches silently | `simulation.md` |
| Assignment cannot express *the right worker for this artifact kind*, and preferring would be a heuristic | `workers.md` |
| Worker scope is prose and unenforced | `workers.md` |
| Observation kinds are closed; execution will find things that fit none | `observation-kinds.md` |
| `produces` is prose — proposals are described, not generated | `observation-kinds.md` |
| Gates have no recorded outcome; passing one should produce an authorization artifact | `governance-gates.md` |

## Next action

**Close the loop.** A knowledge-update proposal exists and nothing applies it.

Until an authorization artifact and a write path exist, **the system produces the
same plan on Tuesday that it produced on Monday, however Monday went.**

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
