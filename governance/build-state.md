---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: acquisition-lifecycle
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**Brownfield Knowledge Acquisition.** Discovery is no longer the research
target; the benchmark is concluded.

## The complete lifecycle runs, against a real commit

```sh
python3 tools/lifecycle.py /tmp/ai-desk-before /Users/willy/Localsources/ai-desk \
    external/ai-desk-lifecycle
```

**`97ca033 feat: Etapa 3 — SLA business-hours`**, from `ai-desk`'s own history.
The "before" state is a detached `git worktree`; the working tree was never
touched.

| Stage | Result |
|---|---|
| **Initial Acquisition** | 299 proposals → **72 authorized** → 72 authoring sources |
| **Engineering change** | `suites +1`, detected mechanically |
| **Continuous Acquisition** | **4 incremental proposals** — **1.3% of a rerun** |
| **Periodic Reacquisition** | 302 proposals, **not applied** |
| **Knowledge Drift Report** | 76 maintained nodes against 302 fresh proposals |

## The drift report found a defect on its first real run

**`D-missed-incremental-update: 0`** — incremental maintenance kept up.

**`D-unsupported-assertion: 1`** — and it is not the kind of drift the report was
designed to look for.

> `Invariant.Addbusinessminutes` is maintained and a full reacquisition does not
> support it.

The suite declares **two** `describe` blocks. `Continuous` iterates all of them;
`R4` reads only the first.

**Two acquisition modes disagreed about the same evidence**, and the maintained
model carried an assertion a full rerun would never produce.

**Recorded, not silently fixed.** Correcting `R4` would remove the finding and
the evidence that the mechanism works. Whichever rule is wrong, the correction is
a proposal like any other.

## What exists

| Area | State |
|---|---|
| **`discovery/continuous.py`** | Consumes a mechanical delta, not the repository. **Retractions are governed, never applied** |
| **`discovery/drift.py`** | 11 drift categories; **every item a proposal** |
| **`tools/lifecycle.py`** | The five stages, end to end |
| `discovery/mechanical.py` | Vocabulary `1.1.0`, reproducible |
| `discovery/skills/skills.yaml` | 9 engine-independent contracts, no vendor named |
| `discovery/interpretive.py` | 6 named rules, 3 strategies |
| `compiler/apply/` · `tools/review.py` | Authorization and application |
| `external/ai-desk-lifecycle/` | 72 authored sources · CKM 76 nodes · drift report · 6 products |
| `external/…/experiment/blind/` | The blind benchmark |
| Registries | 19 |
| `model/metamodel/` | 23 of 27 entities — **unchanged for twelve milestones** |

## What the maintained model does not contain

| | |
|---|---|
| `D-implementation-without-knowledge` | **123** |
| `D-new-knowledge` | **104** |
| `D-invariant-without-enforcement` | 10 |

**72 of 299 proposals were authorized.** 227 things the repository contains are
absent by choice, and **the drift report states the size of that choice** — which
nothing previously did.

## What does not exist

**A change that removes evidence.** The retraction path exists and **has never
fired**; `Etapa 3` only added.

**A change to a curated assertion.** Nothing a human corrected was later
contradicted by the repository — the hardest case.

**Probabilistic Discovery Skills inside Initial Acquisition.** The directive
accepts hours of onboarding; **the current run takes seconds and that budget is
unspent.**

**Runtime evidence.** No mode consumes it.

**The navigable product from a broad model.** 72 of 299 is not broad.

## Blocking

**Nothing.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. Nineteen registries, zero generated |

## Debt discovered while building

| Question | Where |
|---|---|
| **`C1` and `R4` disagree about multi-`describe` suites** — found by the drift report, deliberately unfixed | `LIFECYCLE.md` |
| Synchronized is not the same as useful; only running the Director against both states would show it | `LIFECYCLE.md` |
| Nothing verifies a worker honoured its Skill contract | `ADR-0113` |
| Exhaustive stopping conditions conflict with bounded proposal counts | `BENCHMARK-BLIND.md` |
| The frontend and widget contribute nothing to the Mechanical Model | blind gap report |

## Next action

**A change that removes evidence**, to exercise the retraction path — the one
branch of Continuous Acquisition that has never run, and the one where getting it
wrong destroys curated knowledge.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
