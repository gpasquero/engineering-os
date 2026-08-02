---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: autonomy
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**Autonomy** (`ADR-0102`). Reduce the engineering judgment delegated to workers.

> **Engineering OS is allowed to become smarter. It is not allowed to become less
> deterministic** (`ADR-0103`).

## The KPI

| Measure | Value |
|---|---|
| decisions **before the first LLM token** — *ai-desk, "add OAuth"* | **54** |
| decisions **left to workers** | **7** |
| decisions that **never require an LLM** | *not yet separately counted* |

The third is the target the KPI evolves toward. **Reporting only the first would
reward deferral dressed as ordering.**

## First run on a real repository

```sh
python3 tools/compile.py external/ai-desk-auth
python3 tools/direct.py external/ai-desk-auth I-modify-behavior Capability.Login
```

`external/ai-desk-auth/` — 469-file TypeScript SaaS backend, authentication
subsystem, **31 nodes modelled from the working tree by `grep`**. Six tasks: three
requiring a worker, two mechanical, one gated.

**Six findings, ranks 4–6.** The one worth acting on: ADR-0001's
`tenant_id`-on-every-connection requirement, which the ADR calls *"discipline"*,
**has no enforcement point.**

## Friction produced the session's only new artifact

`I-modify-behavior` on `Capability.Login` — the obvious reading of *"add OAuth"* —
returned **not-applicable**. No plan applied to a capability.

`P-change-capability` was added **because a real run could not express the
workflow it was given** (`ADR-0102`). It is **data, not a construct**: no entity,
operator, registry or engine.

## What exists

| Area | State |
|---|---|
| `compiler/direct/` | Assignment · contexts · intake · loop · KPI. **Confidence ratchet** (`ADR-0104`) |
| `tools/direct.py` · `plan.py` · `taskgraph.py` · `advise.py` · `ask.py` | The Director and its stages |
| `model/plans.md` | **3 plans** — Artifact, Concept, **Capability** |
| `model/workers.md` · `governance-gates.md` · `observation-kinds.md` | 7 · 3 · 8 |
| `external/ai-desk-auth/` | **31 nodes, real repository, 6 classified findings** |
| `external/kubernetes-ssa/` | 41 nodes, four source classes, end-to-end simulation |
| `tests/` | 17 fixtures, 9 negative, golden outputs |
| Registries | 14, **cross-references checked** |
| `model/metamodel/` | 23 of 27 entities — **unchanged for six milestones** |

## The confidence tension, resolved not absorbed

The direction on structured worker confidence **conflicted with `ADR-0090`**,
which rejected confidence scores.

`ADR-0104` resolves it: `ADR-0090` governs **Engineering OS's own conclusions**;
a worker's confidence is a **probabilistic executor's self-report**. It is
admitted as an **intake signal that may only add scrutiny** — `record` with
medium or low confidence escalates to `govern`; **high confidence never lowers
scrutiny**, because the reason an observation is governed is a property of the
claim, not of the claimant.

**Confidence and reasoning are stripped at the boundary on every path**, verified
by assertion including the reject paths — where the first implementation leaked
them.

## Awaiting decision

**Execution Memory** — `governance/design/PROPOSAL-execution-memory.md`. **Not
implemented**, as directed.

It recommends building **only the run log**: experience is counted from runs and
**nothing currently records a run**. The four example patterns are hypotheses,
and **nothing has run twice.**

## What does not exist

**Nothing applies a knowledge-update proposal.** The loop still does not close.

**No run log.** The KPI cannot be compared across sessions.

No runtime implements any worker type. No confidence value anywhere in any model.

## Blocking

**Nothing.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. Fourteen registries, zero generated |

## Debt discovered while building

| Question | Where |
|---|---|
| **`Q-tests` names suites, not cases** — better than files, still not the case that protects a behaviour | `ai-desk-auth/FINDINGS.md` |
| Two ai-desk test suites have no invariant traced to them; **may be a modelling gap rather than a repository one** | `ai-desk-auth/FINDINGS.md` |
| Workers will report high confidence by default, so the ratchet protects only when a worker is honest enough to doubt | `ADR-0104` |
| Three confidence levels is a scale, and a scale is a score with fewer values | `ADR-0104` |
| **Nothing detects a decision that *could* have been mechanical being delegated anyway** | `ADR-0103` |

## Next action

**The Project Owner's decision on Execution Memory.**

The proposal recommends the run log alone. It is small, is required by every
version of the experience layer, and is what would make the KPI comparable across
runs — which is the number this milestone just started reporting and cannot yet
compare.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
