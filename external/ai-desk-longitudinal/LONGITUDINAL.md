# Longitudinal validation — does engineering understanding survive time?

**Repository:** `ai-desk` · **Ten real commits** from its own history, in order
**Run:** `SESSION-0049` (baseline recorded `SESSION-0047`) · `python3 tools/longitudinal.py`

> **Result of the semantic-preservation change** (`ADR-0130`, `ADR-0134`):
>
> ```text
>                           before        after
> coverage           1/9 → 1/9      1/9 → 2/9
> retention               0 %          100 %
> EQ-06                degraded      retained
> edges/node               0.38          0.68
> predicates in use         2 of 6       5 of 6
> isolated capabilities    9 of 10       0 of 10
> maintenance               278            314
> ```
>
> The acceptance criterion — *`EQ-06` answered at `t9`, retention 100 %* — was
> written before the work started and met exactly. **Everything below is the
> baseline it was measured against**, preserved as `ADR-0129` requires.

> **This validates the central promise of Engineering OS: that engineering
> understanding survives the passage of time. No benchmark can replace that
> experiment.**

A benchmark measures a single moment. This measures a model that was acquired
**once**, at an early commit, and then had to survive nine genuine engineering
changes without being rebuilt.

Each commit is materialised as a detached `git worktree`. The working tree is
never touched. The curation policy — the subsystems a team would own — is
applied **identically at every step**, because a team whose policy drifts
measures its own inconsistency rather than the tool's.

## The result

```text
step  kind          cost  rerun       %   answered
t0    initial         39      —       —   1/9
t1    continuous      47     91   51.6%   1/9
t2    continuous      13    110   11.8%   1/9
t3    continuous     128    216   59.3%   1/9
t4    continuous      34    249   13.7%   1/9
t5    continuous      20    267    7.5%   1/9
t6    continuous      19    287    6.6%   1/9
t7    continuous      13    298    4.4%   1/9
t8    continuous       0    299    0.0%   1/9
t9    continuous       4    302    1.3%   1/9
```

**Acquired once at 39 proposals. Maintained across nine changes for 278 more —
13 % of what re-running discovery every time would have cost.**

**Engineering questions answered: 1/9 at t0. 1/9 at t9.**

## The model got 2.4× larger and answered one question *worse*

The single number hides the only thing that moved.

| Question | t0 | t9 |
|---|---|---|
| Why does this system work this way? | `no-data` | `no-data` |
| What business rules are actually enforced? | `no-data` | `no-data` |
| What could safely be changed? | partial | partial |
| What cannot safely be changed? | partial | partial |
| Which architectural decisions still matter? | `no-data` | `no-data` |
| **Which capabilities would be affected by this feature?** | **answered** | **partial** |
| Which invariants protect this behavior? | `no-data` | `no-data` |
| Who is allowed to perform this operation? | `no-query` | `no-query` |
| Which engineering assumptions are unsupported? | `no-data` | **answered** |

**`EQ-06` was answered at `t0` and has been `partial` at every step since.**

The model grew from 39 proposals to **94 curated sources**. It answered the
planning question at its smallest and stopped answering it at its largest.

## Why: Continuous Acquisition adds nodes and does not connect them

```text
94 nodes · 36 edges · 0.38 edges per node
capabilities: 10        with no edge at all: 9
```

**Nine of ten capabilities are isolated.**

Rule `C3-new-module` proposes a `Capability` for a newly appeared module
directory — and proposes **no relationship**. The equivalent initial-acquisition
rule, `S1-module-is-a-capability`, emits `scoped-to` linking the capability to
its bounded context.

**The two acquisition modes disagree about the same evidence.** This is the same
family as the `C1`/`R4` divergence recorded in `SESSION-0043`, and it is the
second time a defect has been found by comparing two modes rather than by
checking either.

`EQ-06` has a threshold of 0.5 over `Capability` subjects. At `t0` there was one
capability and it was connected. Every capability added since arrived isolated,
so the ratio fell below the threshold at `t1` and never returned.

**Not fixed in this session, deliberately.** The fix is not a typo — it is a
decision about *which relationships Continuous Acquisition is entitled to infer
from a mechanical delta*, and that decision should be stated before it is
implemented, not discovered in a diff.

## What Periodic Reacquisition found after ten commits

```text
D-implementation-without-knowledge     114
D-new-knowledge                         97
D-invariant-without-enforcement         30
D-knowledge-without-implementation       9
D-unsupported-assertion                  3
```

**`D-unsupported-assertion` grew from 1 to 3.** Three things the maintained
model asserts that a full rediscovery would not produce. The mechanism works:
after ten commits the maintained understanding has drifted, and the drift report
says so and applies nothing.

**`D-knowledge-without-implementation: 9`** appears for the first time — nine
curated assertions whose implementation the repository no longer shows. This is
the closest the project has come to exercising the retraction path, and it is
still a report rather than a retraction, which is correct (`ADR-0118`).

## A previously published number was measured at the flattest point

`SESSION-0043` reported Continuous Acquisition costing **1.3 % of a rerun**, and
that figure has appeared in the build state ever since.

It is reproduced exactly here — **at `t9`**, the last commit of the history,
where almost nothing changes.

Across the whole history the honest figure is **13 %**, and the per-step range is
**0 % to 59 %**. Early in a system's life, when a repository is growing quickly,
continuous maintenance costs *more than half* of a full rediscovery.

> **A single-step measurement of an incremental process reports the step it was
> taken at, not the process.**

Neither number is wrong. The 1.3 % was published without its position in the
history, and that omission flattered the system.

## Verdict

**Understanding held. It did not improve.**

Under `ADR-0122`'s framing — *engineering memory* — this run is a success:
nothing was lost, everything was maintained, and maintenance was cheap.

Under `ADR-0123` — *a continuously improving Engineering Understanding System* —
**it is a failure**, because understanding is the thing that was supposed to
improve, and it is flat.

That difference is the entire argument for the correction the reviewer made, and
this experiment is the first thing in the project that could tell the two apart.

**What survives time today is the model. What does not yet accumulate is the
understanding.**

## This suite is permanent

`ADR-0129`. The ten commits are **frozen** and may not be changed — not to add a
more interesting change, not to drop a slow one, not to make a result cleaner.

Every significant architectural change reruns it and reports coverage,
retention, knowledge, maintenance cost and drift.

**The baseline to beat is the table above.** The next change to Continuous
Acquisition has its acceptance criterion written before it starts: **`EQ-06`
answered at `t9`, and retention at 100 %.**
