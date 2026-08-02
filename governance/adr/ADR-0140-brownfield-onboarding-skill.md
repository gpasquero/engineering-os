---
id: ADR-0140
title: The next capability is a non-deterministic Brownfield Onboarding Skill that proposes, never decides
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0090, ADR-0092, ADR-0103, ADR-0104, ADR-0108, ADR-0113, ADR-0121, ADR-0124, ADR-0135]
---

# ADR-0140 — The Brownfield Onboarding Skill

## Context

Deterministic Discovery has been optimized for six milestones. The reviewer
declared it finished:

> **Do not continue optimizing Brownfield Discovery itself. I think it is now
> good enough. The deterministic onboarding is no longer the bottleneck.**
>
> The next major capability should be **the non-deterministic Brownfield
> Onboarding Skill.** Its purpose is not to build the authoritative model. Its
> purpose is **to help a human engineering team produce that model faster and
> with higher quality.** Think of it as an expert engineering partner.
>
> It does not need to be deterministic. **It only needs to produce proposals
> with evidence. The authoritative model remains deterministic.**

The evidence agrees. Two repositories, 299 and 453 proposals, no metamodel
change — and `EQ-01` (*why does this system work this way?*) answers **nothing**
in either. `wa-b2b` holds 135 documents and 369 migrations that no deterministic
rule can read. **More rules will not reach them.**

## Decision

**Build a non-deterministic Brownfield Onboarding Skill. It proposes with
evidence and it decides nothing.**

| | Deterministic Discovery | **Onboarding Skill** |
|---|---|---|
| Reproducible | **required** | **not required** |
| Reads | the Mechanical Engineering Model | the Mechanical Model **and prose** |
| Produces | candidate proposals | candidate proposals |
| Enters the model | **only through curation** | **only through curation** |
| Engine | none | Claude, Codex, or any frontier model |

**The two are indistinguishable downstream, and that is the point.** Both emit
the same candidate proposals, with the same eleven-field provenance, into the
same governed curation step. **A reviewer approving a proposal need not know
which produced it — only what evidence it cites.**

**Four constraints, and each preserves something already paid for.**

**1. It never writes to the Authoritative Engineering Model.** Curation is the
only path in, unchanged (`ADR-0135`).

**2. Every proposal cites evidence a human can check.** A proposal whose support
is *the model's judgement* is rejected at intake. This is `ADR-0104`'s ratchet:
a non-deterministic worker may add scrutiny and never remove it.

**3. No confidence scores** (`ADR-0090`). Uncertainty is `high | medium | low`
per proposal, as every Discovery Skill contract already declares (`ADR-0113`).

**4. `ADR-0103` is not weakened.** *Engineering OS is allowed to become smarter.
It is not allowed to become less deterministic.* **The authoritative model stays
deterministic** — what becomes non-deterministic is a proposer, and a proposer
was never a decision.

## Rationale

**This is the separation the project has been building toward without naming
it.** `ADR-0092` said the Director reasons deterministically and LLMs execute;
`ADR-0113` made Skills engine-independent contracts; `ADR-0135` split producing
understanding from consuming it. This decision is the first place a frontier
model is deliberately admitted, and every guard it passes through already
exists.

The reviewer's framing — **an expert engineering partner** — sets the success
criterion, and it is not coverage. A partner is judged by whether a team reaches
a good model **faster and with higher quality**, which is a claim about the
*curation session*, not about the proposal count. **500 confident proposals a
team cannot review is a worse partner than 40 it can.**

It is a **level 2 technology skill** in the making (`ADR-0124`), and it begins at
**level 1** — one repository, disposable, to find out what it needs.

## Consequences

**Two things become measurable that were not.** Proposals a curator *accepted*
per unit of review, and whether the questions with no deterministic path —
`EQ-01`, `EQ-05` — begin to answer. Both are read on repositories already
benchmarked, against recorded baselines.

**Non-determinism must be visible in the model.** A proposal's origin already
records its worker; it must now also record that its producer is
non-deterministic, so a maintained model can always be asked which of its
assertions came from a machine that would not repeat itself.

**The blind benchmark protocol applies** (`SESSION-0042`): a skill evaluated on
a repository it was tuned against measures nothing.

**Deterministic Discovery is frozen, not deleted.** It remains the reproducible
observation layer and the fixed input every comparison is run against.

## Compliance

- The skill emits candidate proposals only; no path bypasses curation.
- Every proposal cites checkable evidence and declares uncertainty, never a
  score.
- Proposals record that their producer is non-deterministic.
- Evaluation is blind, and reports acceptance under review rather than volume.
