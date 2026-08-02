---
id: ADR-0129
title: The ten-commit longitudinal experiment is a permanent benchmark suite
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0119, ADR-0120, ADR-0123, ADR-0127, ADR-0128]
---

# ADR-0129 — The longitudinal suite is permanent

## Context

The ten-commit experiment was built to answer one question and was expected to
be used once. It found three things nothing else had: a semantic regression
invisible to every other check, a published figure measured at the flattest point
of a history, and a coverage reading that hid a total turnover.

The reviewer made it permanent:

> **I now consider the ten-commit experiment one of the permanent benchmark
> suites of Engineering OS. Do not discard it after fixing Continuous
> Acquisition. Every significant architectural change should eventually rerun
> exactly this benchmark. The benchmark itself is now an engineering asset.**

and, separately:

> **Keep that experiment exactly as it is. Do not optimize it away.**

## Decision

**`external/ai-desk-longitudinal/` is a permanent benchmark suite. The ten
commits are fixed.**

`4b85ca2 · d833545 · cb03440 · 9c4cdd0 · 1c52a49 · 80f4a4f · 9228f6c · 8b15fcc ·
f2af6ca · 97ca033`

**The commit list may not be changed.** Not to add a more interesting change, not
to drop a slow one, not to make a result cleaner. A benchmark whose inputs move
measures nothing across time, and this suite exists precisely to measure across
time.

**Every significant architectural change reruns it**, and reports:

```text
coverage        answered / total, at t0 and at t9
retention       of what was answered at t0                     (ADR-0128)
knowledge       curated sources                                 (ADR-0127)
maintenance     incremental cost against a full rerun, per step
drift           the Knowledge Drift Report at the reacquisition points
```

**Its current result is the baseline to beat**, and it is recorded here so it
cannot be quietly restated:

| | |
|---|---|
| coverage | **1/9 → 1/9** |
| retention | **0 %** — one degraded, one gained |
| knowledge | 10 → **94** curated sources |
| maintenance | **278 proposals, 13 %** of re-running every time |
| structure | 94 nodes, **36 edges**, 9 of 10 capabilities isolated |

## Rationale

The suite is valuable for exactly the reason it is uncomfortable: **it is the
only thing in the project that can fail without anything being broken.** Every
other check asserts a property and passes. This one produces a number, and the
number was bad.

Fixing Continuous Acquisition will improve it, and that is the moment the
suite is most likely to be quietly retired as *"the thing that found that bug"*.
It is not. It is the instrument, and the bug was a reading.

**Freezing the commits is what makes results comparable.** A suite re-cut to
suit each change would let every architectural decision look like an
improvement.

## Consequences

**The suite must stay cheap enough to run.** It creates ten detached worktrees
and takes minutes. If it ever becomes too slow, the correct response is to make
it faster — never to shorten it.

**A regression in the suite blocks nothing automatically.** It is a measurement,
not a gate. But a change that worsens retention and is adopted anyway must say so
in its session record.

**The `ai-desk` repository becomes a dependency.** The suite reads it by commit
hash from a local clone. If it were ever unavailable, the suite would have to be
reconstructed rather than replaced, and that risk is accepted and recorded.

## Compliance

- The commit list in `governance/build-state.md` and in this decision agree.
- Significant architectural changes rerun the suite and report all five figures.
- The baseline above is amended only by recording a new measurement, never by
  editing the old one.
