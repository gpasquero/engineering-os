---
id: ADR-0145
title: Human Curation is a first-class product and a user-experience problem
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0104, ADR-0135, ADR-0140, ADR-0141, ADR-0142, ADR-0143, ADR-0144]
---

# ADR-0145 — Curation is a product

## Context

Human Curation has been a governance requirement since `SESSION-0039`: nothing
enters the Authoritative Model without authorization. It has never been anything
else. In practice it has been a **filter function inside a script** — a tuple of
substrings deciding which proposals a fictional reviewer would have accepted.

The reviewer reclassified it:

> Begin treating Human Curation as a first-class product. So far it has mostly
> been treated as a governance requirement. **I think it is becoming a user
> experience problem.**
>
> The success of Engineering OS will depend **as much on making Human Curation
> efficient as on making Discovery intelligent.** That interaction between AI and
> human engineering judgment is likely to become one of the core differentiators.

## Decision

**Human Curation is a product surface with its own design, its own measurements
and its own failure modes.**

`tools/curate.py` is its first implementation: one proposal at a time, with its
evidence, its relationships, its Engineering Review (`ADR-0142`), and whether its
producer was non-deterministic. Four decisions — **authorize · reject · correct ·
defer** — and the session is resumable, because a reviewer who cannot stop will
not start.

**Three properties make it a product rather than a gate.**

**1. `correct` exists.** A gate offers accept and reject. A partner lets a
reviewer say *right idea, wrong words* and keep the proposal with their own
statement. **The correction is the most valuable thing a session produces** — it
is human engineering judgement, captured, in a form the model can hold.

**2. `defer` exists and is not failure.** A proposal a reviewer cannot decide on
is a finding about the evidence, not about the reviewer.

**3. The reviewer is asked what they thought of the evidence.** Confidence and
evidence quality are recorded per decision, so a session says not only *what was
authorized* but *how well the skill argued for it* (`ADR-0144`).

## Rationale

Curation is the only stage where a person decides anything (`ADR-0143`), and it
is where the two halves of the product meet: everything Discovery produces is
worth exactly what a reviewer can act on.

**The asymmetry is the argument.** Discovery can be made twice as intelligent and
deliver nothing if the reviewer's throughput is unchanged. Curation can be made
twice as efficient and double the model with no change to Discovery at all.

It also explains the direction `ADR-0142` took. The Engineering Review is not a
Discovery feature. **It is a curation feature that Discovery happens to
produce**, and it exists because a reviewer's scarcest resource is the time to
decide.

## Consequences

**Curation acquires user-experience failure modes the project has no experience
with**: 453 proposals in an undifferentiated list; no way to see why one matters
more than another; no sense of progress; no way to revisit a decision. All are
real and none is a correctness bug.

**The filter function is retired as a model of curation and kept as a fixture.**
The frozen longitudinal suite uses it deliberately — a benchmark needs a
*constant* curation policy (`ADR-0129`), and a human is not one.

**Ordering becomes a design question.** Proposals are currently reviewed in id
order, which is alphabetical and meaningless. What a reviewer should see first is
unknown, and it is the first thing a real session will answer.

**The measurement is empty and stays empty until a human uses it.** Nothing
simulates it (`ADR-0144`).

## Compliance

- Curation is designed and measured as a product surface, not a validation step.
- Every proposal is shown with its evidence and its review before a decision.
- Corrections are recorded as the reviewer's statement, attributed to them.
- No curation session is generated.
