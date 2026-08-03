---
id: ADR-0147
title: Research Freeze — the objective is a third party completing the MVP, not a better architecture
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0116, ADR-0119, ADR-0136, ADR-0141, ADR-0144, ADR-0145, ADR-0146]
---

# ADR-0147 — Research Freeze and MVP closure

## Context

Fifty-one sessions produced 146 decision records, 23 metamodel entities, 20
registries, six emitters, three acquisition modes, two stack profiles, four
measured properties and two benchmarked repositories.

**None of it has ever been installed by anyone.**

The reviewer closed the research phase:

> Engineering OS has reached sufficient architectural maturity for an MVP. From
> this point forward, **enter Research Freeze.**
>
> **The goal is no longer to improve the architecture. The goal is to make
> Engineering OS installable, understandable and usable by someone who did not
> build it.**

## Decision

**Research Freeze is in effect.** The following may not be introduced unless
they **directly block** third-party installation or the documented MVP journey:

```text
new metamodel entities · new architectural directions · new benchmark families
new product metrics · new Discovery Skill categories · new registries
new compiler capabilities
```

**The MVP is the sixteen-step journey** in `README.md`: clone · install · verify
· point at a repository · Initial Acquisition · Mechanical Discovery ·
Onboarding Skill with Claude or Codex · Candidate Model · curate · apply ·
compile · generate products · ask questions · request guidance · Continuous
Acquisition · Periodic Reacquisition and Drift.

**Everything else is deferred.**

**No further ADR is written** unless a documented workflow cannot be completed,
a third-party user hits a blocker, or correctness or trust would otherwise be
compromised.

## Rationale

The freeze is not a pause in ambition; it is a change in what counts as
evidence. Every measurement this project has is internal — the model checking
itself, the benchmark checking the model, the checks checking the benchmark.
**A third-party engineer completing the journey is the first external oracle
this project will ever have**, and it is worth more than any further internal
result.

It also fits what the last five sessions found. The weakest stage of the
lifecycle is **Human Curation**, which no human has performed (`ADR-0145`); the
onboarding skill's success criterion is **reviewer efficiency**, which no
reviewer has produced (`ADR-0144`); and the North Star is about a **team**
(`ADR-0136`). All three are blocked on the same missing thing: a person outside
this repository.

**More architecture cannot unblock them.**

## What the freeze bought immediately

Applying it produced findings no architectural session had:

- **`tools/check.py` and `tools/smoke.py` did not exist.** The journey had no
  verification and no end-to-end test.
- **`discovery/run.py` crashed on any project directory outside this
  checkout** — which is every third-party use.
- **`tools/direct.py` crashed on `I-investigate`**, a documented workflow, on an
  intent the registry deliberately declares as having no plan.
- **No repository was bundled to onboard**, so the documented path could not be
  followed without a system on one of two supported stacks.
- **`README.md` described milestone M1 of 11 and claimed no skills existed.**

Four of these are defects. **Every one was found by writing down what a stranger
would type.**

## Consequences

**`README.md` is the primary deliverable**, and `docs/` supports it.

**The MVP is complete only when a third-party engineer completes the flow
without private guidance** — `docs/mvp-checklist.md`, item 14 of 14. Thirteen
items are verifiable from inside and are done. **The fourteenth is not, and it
governs.**

**Honesty in the README is load-bearing.** Its status section separates
implemented · experimental · unvalidated · planned, and its limitations section
states that the onboarding skill has never run end to end, that guidance
correctness is unmeasured, and that curation has never been performed. **A
README that oversold this would fail the only test that now matters**, because
the first stranger to try it would find out in ten minutes.

**The freeze ends when the reviewer says so**, on the evidence of a real
third-party run.

## Compliance

- No new entity, registry, metric, skill category, benchmark family or compiler
  capability without a documented blocker.
- No new ADR except under the three stated conditions.
- Every command in `README.md` is verified by execution before it is published.
- `docs/mvp-checklist.md` records only externally observable requirements.
