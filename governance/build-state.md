---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: generalization
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**Generalization.** The lifecycle runs on more than the repository it was built
against — measured, not assumed (`ADR-0119`).

## Two repositories, one interpreter

| | `ai-desk` | `wa-b2b` |
|---|---|---|
| Stack | Node · NestJS · Drizzle | **Java 21 · Spring Boot · JPA** |
| Files | 780 | **1 913** |
| Routes · tables · suites | 161 · 34 · 69 | **143 · 45 · 193** |
| Proposals | 299 | **453** |
| Metamodel entities exercised | 6 of 23 | **5 of 23** |
| Metamodel changes required | — | **none** |

**Extraction is declared** (`ADR-0117`). `discovery/mechanical.py` holds eight
extraction kinds and no path, framework or file extension; `stacks.yaml` holds
the profiles. The Node profile reproduces the previous hard-coded extractor
**identically across all eight vocabulary keys**.

**The interpreter was not changed to read Java.** That was the claim under test.

## The second repository found a defect the first had hidden

`R4` names a general Invariant after a test suite's declared subject. No
`wa-b2b` suite declares one, so it fell back to the **file name** and proposed 67
invariants called things like `AgentServiceTest` — **13 % of the set, asserting
nothing, carrying full provenance.**

All 69 `ai-desk` suites declare a `describe` block, so the branch had never run
in fourteen milestones. **One repository validated a rule and hid a defect in the
same act.**

Fixed. **`ai-desk` still produces exactly 299 proposals** — which is how a
correctness fix is distinguished from an optimization (`ADR-0119`).

## The honest result

**Nine of seventeen declared queries answer nothing** on `wa-b2b`.

| | |
|---|---|
| `Q-rationale` — *which decision established this?* | **0 of 216** — 135 documents, none recognised as a decision |
| Authorization | **143 routes, not one carries who may call it** |
| `Q-constraints` | 0 — the fabricated invariants were the **only** source of `constrains` edges |

**453 proposals, and the two questions a new engineer asks first are both
unanswerable.** The count is not the result; that gap is.

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

## The drift report is a work queue

`ADR-0114`. All **15** drift classes declare `routes-to`; the three that route
nowhere declare why.

```sh
python3 tools/drift-queue.py external/ai-desk-lifecycle
```

```text
P-discover               123 item(s)   from D-implementation-without-knowledge
P-establish-enforcement   10 item(s)   from D-invariant-without-enforcement
P-review-unsupported       1 item(s)   from D-unsupported-assertion
NOT ROUTED — D-new-knowledge (104): additive; curation alone suffices
```

**Routes with no plan: none.** Eight plans exist, four written this session.

## Running a plan found a defect that validating it could not

`P-review-unsupported` was run against the one unsupported assertion. **Two of
its three phases produced nothing, silently.**

A plan phase borrows a recommendation's **steps**, not its **applicability**.
`Q-assumptions` accepts `Artifact`; the subject was an `Invariant`. The step was
skipped, and an empty phase means *nothing to do* — the opposite of *this could
not be attempted*.

The planner now says which, and `tools/check-plans.py` finds the condition at
authoring time, **per subject type**. One hollow phase across eight plans.

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
| **`discovery/drift.py`** | **15** drift categories, **each routed to a plan** |
| **`tools/lifecycle.py`** | The five stages, end to end |
| `discovery/mechanical.py` · `stacks.yaml` | Vocabulary **`2.0.0`** — eight extraction kinds, **two Stack Profiles** |
| `discovery/skills/skills.yaml` | **10** contracts — 9 `general`, **1 `domain`** — no vendor named |
| `discovery/interpretive.py` | 6 named rules, 3 strategies |
| `model/plans.md` · `tools/drift-queue.py` | **8 plans**; drift becomes work |
| `compiler/apply/` · `tools/review.py` | Authorization and application |
| `external/ai-desk-lifecycle/` | 72 authored sources · CKM 76 nodes · drift report · 6 products |
| `external/wa-b2b-onboarding/` | **The first benchmark of an unseen system** — 453 sources, `BENCHMARK.md` |
| `external/…/experiment/blind/` | The blind benchmark |
| `tools/check-governance.py` | The corpus check, **committed at last** — 271 records |
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

**Any knowledge of authorization.** The highest-value gap found, and deliberately
not built: one repository is not evidence (`ADR-0119`).

**A second stack for a polyglot repository.** `wa-b2b` hosts Java, TypeScript and
Python; detection returns one profile.

**Domain Discovery Skills beyond one.** `DS-multitenant-saas` is a shape, not a
catalogue. Six more were deferred by the test written in the same session.

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
| **Consumption is a stronger test than validation** — three defects now found by running output, none by checking it | `SESSION-0044` |
| **The same five metamodel entities in two unrelated repositories** — repeated evidence, and it points at the interpreter | `BENCHMARK.md` |
| **369 migrations and 135 documents unread** — the system's decision history is in the repository and not in the model | `BENCHMARK.md` |
| **`apply()` never asks whose model is already in the directory** — pointed at another project's model it merged the two and reported success | `SESSION-0045` |
| **A check retyped each session is not a check** — three records had unparseable front matter for many sessions | `tools/check-governance.py` |
| Synchronized is not the same as useful; only running the Director against both states would show it | `LIFECYCLE.md` |
| Nothing verifies a worker honoured its Skill contract | `ADR-0113` |
| Exhaustive stopping conditions conflict with bounded proposal counts | `BENCHMARK-BLIND.md` |
| The frontend and widget contribute nothing to the Mechanical Model | blind gap report |

## Next action

**The second repository: an event-driven service.**

Three findings are one observation short of being actionable, and this is the
cheapest way to buy the second: **authorization across a message boundary**,
decisions recorded outside an `adr/` directory, and whether five entities is a
property of interpreters or of these two repositories.

Still untested, and still where getting it wrong destroys curated knowledge:
**a change that removes evidence.**

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
