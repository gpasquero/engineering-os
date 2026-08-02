---
id: ADR-0118
title: The three acquisition modes are product capabilities, not implementation details
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0108, ADR-0110, ADR-0112, ADR-0114, ADR-0116]
---

# ADR-0118 — Initial, Continuous and Periodic are product capabilities

## Context

`ADR-0112` introduced three acquisition modes and described them as stages of a
lifecycle. They were built, run end to end, and treated as **phases of a
pipeline**.

The reviewer named them differently:

> **These are now product capabilities, not implementation details.**

The distinction matters because a phase is something a pipeline passes through,
while a capability is something a customer buys, schedules, budgets and judges.
Phases may be reordered, merged or optimized away. **Capabilities may not**,
without changing what the product is.

## Decision

**Initial Acquisition, Continuous Acquisition and Periodic Reacquisition are
three distinct product capabilities**, each with its own objective, cost profile
and success criterion. No design may collapse them.

| Capability | Objective | Cost | Succeeds when |
|---|---|---|---|
| **Initial Acquisition** | **Engineering understanding** of an unfamiliar system | Slow, expensive, **possibly highly probabilistic** | Future development is measurably easier |
| **Continuous Acquisition** | Keep the Authoritative Engineering Model **synchronized** after accepted changes | Incremental, proportional to the change | The model reflects the accepted change and nothing else |
| **Periodic Reacquisition** | **Challenge** the maintained understanding | Onboarding-quality, therefore expensive | It produces a Knowledge Drift Report |

**Three consequences follow directly, and each forbids something.**

**Initial Acquisition is allowed to be slow and probabilistic.** Its budget is
onboarding: hours, not seconds. Optimizing it toward the speed of Continuous
Acquisition would be optimizing the wrong capability.

**Continuous Acquisition is not a small Initial Acquisition.** It consumes a
mechanical delta, proposes only what changed, and **never applies a retraction
without governance**.

**Periodic Reacquisition does not rebuild the model.** Its output is a Knowledge
Drift Report, and its result is *challenge*, never *replacement*. A reacquisition
that overwrote the maintained model would destroy exactly the curation that makes
the model authoritative.

## Rationale

Naming them as capabilities makes a class of design error visible in advance.

The most likely such error is efficiency-shaped: *Initial Acquisition and
Periodic Reacquisition run the same code, so let us share the fast path.* They do
run the same code. **They do not have the same objective**, and the shared
implementation is a fact about today, not a licence to merge the capabilities.

The second is scheduling-shaped: *Continuous keeps the model current, so
Periodic is redundant.* Continuous can only see what a change touched. **A model
maintained perfectly by Continuous Acquisition can still be wrong about
everything nothing touched** — which is precisely what Periodic Reacquisition
exists to detect, and what it detected on its first real run.

## Consequences

**Each capability is measured separately.** *Coverage* belongs to Initial;
*proportionality* to Continuous; *challenge* to Periodic. A single "accuracy"
figure over the three would hide all three.

**The current cost profile of Initial Acquisition is a gap, not an achievement.**
It runs in seconds because it is entirely deterministic. The budget the reviewer
granted is unspent, and the capability is under-delivered rather than efficient.

## Compliance

- The three modes remain separately invocable and separately reported.
- No shared implementation may cause Periodic Reacquisition to write to the
  Authoritative Engineering Model.
- Documentation and the roadmap name the three capabilities, not "the pipeline".
