---
id: ADR-0142
title: Brownfield Onboarding produces two deliverables — a Candidate Model and an Engineering Review
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0104, ADR-0113, ADR-0140, ADR-0141, ADR-0144, ADR-0145]
---

# ADR-0142 — Two deliverables

## Context

`ADR-0140` specified a non-deterministic onboarding skill that proposes with
evidence. The reviewer separated what it hands over:

> I would explicitly distinguish two outputs. **Candidate Engineering Model** and
> **Engineering Review**.
>
> The Candidate Engineering Model proposes engineering facts. **The Engineering
> Review explains why those facts should or should not become authoritative.**
> Those are different deliverables. **One updates the model. The other
> accelerates Human Curation.** Both should be produced by the Onboarding Skill.

## Decision

**The Onboarding Skill produces two artifacts, and neither substitutes for the
other.**

| | Candidate Engineering Model | **Engineering Review** |
|---|---|---|
| Contains | proposed facts, with provenance | **the argument for and against each** |
| Consumed by | the curation mechanism | **a human reviewer** |
| Effect | updates the model, after authorization | **shortens the time to decide** |
| Wrong when | a fact is unsupported | **a reviewer cannot tell whether to accept** |

**An Engineering Review entry states the case both ways.** For a proposal it
records what supports admitting it, **what argues against**, its uncertainty, and
what the skill would recommend — as an argument the reviewer may reject, never a
verdict.

**A review entry that only argues *for* is not a review.** A skill that presents
only its own case is a persuader, and the reviewer's job becomes finding what it
omitted — which is slower than having no review at all.

## Rationale

The two deliverables fail differently, and conflating them hides the second
failure entirely.

A Candidate Model is judged on whether its facts are true. **A review is judged
on whether a human decides faster and better** — a property of the *curation
session*, not of the model. Nothing in this project has ever measured that,
because until now there was nothing whose only purpose was to be read by a
person.

It also gives the non-deterministic producer somewhere honest to put what it
cannot prove. A frontier model reading 135 markdown documents will form
impressions that are **useful and not admissible as facts**. As a proposal that
is fabrication; **as an argument in a review, addressed to a human who may
disagree, it is exactly what an expert partner offers.**

## Consequences

**Curation reads the review, and `tools/curate.py` shows it inline** beside the
evidence, before any decision is taken.

**The review is where uncertainty lives.** Still `high | medium | low`, never a
score (`ADR-0090`).

**A deterministic rule produces no review, and that is correct.** Its argument is
its rule id: `S1-module-is-a-capability` is the whole case, and a review would
add words to a proposal that already explains itself. **The review exists
because non-deterministic proposals cannot.**

**Reviews are not applied to anything.** Nothing downstream reads them. They are
consumed by a person and then they are history — the first artifact in this
repository whose only consumer is human.

## Compliance

- The Onboarding Skill declares `output-schema` covering both deliverables.
- `tools/check-skills.py` rejects a non-deterministic skill that does not produce
  a review.
- A review entry states both the case for and the case against.
- No component derives model content from a review.
