---
id: ADR-0119
title: A repository is a benchmark, not a backlog; evolve only on repeated evidence
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0085, ADR-0087, ADR-0113, ADR-0115, ADR-0116, ADR-0117]
---

# ADR-0119 — A repository is a benchmark, not a backlog

## Context

Engineering OS has been designed, tested, tuned and validated against **one**
repository. Every Discovery rule, every extraction path and every quality
judgement traces back to `ai-desk`.

The reviewer named the risk precisely:

> **Do not optimize Discovery Skills after the first repository. Use each
> repository as a benchmark. Only when the same limitation appears repeatedly
> should Engineering OS evolve. This prevents overfitting.**

and:

> **A Discovery Skill should only become more general after multiple
> repositories expose the same need.**

The temptation is real and immediate. Running against a second repository
produces a list of things that did not work, and every item on it looks like a
task.

## Decision

**A repository run is a measurement. Its output is a benchmark report, not a
change list.**

Three rules:

**1. One repository never justifies generalizing a Discovery Skill.** A skill
becomes more general when **two or more** repositories expose the same need. Until
then the need is recorded in the benchmark report and nothing is built.

**2. One repository never justifies a metamodel change.** This is `ADR-0085`
applied to Discovery. When a repository seems to demand a new entity, the
question is not *which entity* but *which of the twenty-three was it?* — and, if
genuinely none, whether the gap is caused by the repository or by a missing
concept in Engineering OS. **The two have different remedies and the benchmark
report must say which.**

**3. Correctness is exempt.** A defect is fixed on first sight. The two are
distinguished by a single test:

> **Does the change make Engineering OS better at this repository, or does it
> stop Engineering OS from being wrong?**

Fabricating evidence, crashing, and misreporting provenance are wrongness.
Recognising one more framework's idiom is fitting.

## Rationale

Overfitting to a single repository is not a hypothetical failure mode here — it
is the state the project was already in. `ADR-0117` found the Mechanical layer
hard-coded to one repository's directory layout, and nothing had detected it in
fourteen milestones, because nothing else had ever been tried.

Repeated evidence is the only signal that separates *a property of software* from
*a property of the repository in front of us*, and a project with one data point
cannot tell the two apart at all.

**The rule also has a cost, and it is accepted deliberately.** Real gaps will sit
unaddressed in benchmark reports for several sessions. That is the price of
knowing which of them were real.

## Consequences

**Every repository run produces a benchmark report answering eight questions,
verbatim as the reviewer posed them:**

1. Which metamodel entities were actually exercised?
2. Which Discovery Skills produced valuable engineering knowledge?
3. Which produced mostly noise?
4. Which engineering questions could not be answered?
5. Which gaps appeared?
6. Did the metamodel require changes?
7. If yes, were those changes caused by the repository or by missing concepts in
   Engineering OS?
8. Which new reusable Discovery Skill would now be justified?

**Question 8 is answered with a candidate and its outstanding evidence**, not
with an implementation. A Discovery Skill named after one repository would be a
parser plugin wearing a skill's clothes, which `ADR-0115` already forbids.

**Repositories are chosen for engineering characteristics, not languages.**
Layered business application · event-driven service · domain-heavy ERP · large
multi-module. A second Node repository would measure almost nothing.

## Compliance

- Each repository run publishes `BENCHMARK.md` under `external/<repo>-onboarding/`
  answering all eight questions.
- A skill generalization cites **two or more** benchmark reports naming the same
  need.
- A change made during a benchmark run states which side of the correctness test
  it falls on.
