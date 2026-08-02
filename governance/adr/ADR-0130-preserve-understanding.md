---
id: ADR-0130
title: Continuous Acquisition preserves understanding; inference is a mechanism, not the objective
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0112, ADR-0118, ADR-0123, ADR-0127, ADR-0128, ADR-0129]
---

# ADR-0130 — Preserve semantics first, infer second

## Context

`SESSION-0047` ended by proposing to *decide what Continuous Acquisition may
infer*. The reviewer reframed the objective:

> The objective is no longer **"What can Continuous Acquisition infer?"** It is
> **"What understanding should Continuous Acquisition preserve without requiring
> another onboarding?"**
>
> Inference is an implementation mechanism. Preserved understanding is the
> product capability.

and predicted the cause:

> The answer is probably not "infer more". It is likely: **the maintained
> semantic relationships no longer preserve the engineering meaning that the
> initial acquisition established. Preserve semantics first. Infer second.**

**The prediction is correct, and it is now measured.**

## The measurement

Initial Acquisition establishes **six** semantic relationships. Continuous
Acquisition preserves **two**.

| Predicate | Meaning it carries | Initial | Continuous |
|---|---|---|---|
| `enforced-at` | an invariant is checked here | ✓ | **✓** |
| `specializes` | a guarantee narrows a rule | ✓ | **✓** |
| `constrains` | an invariant guards **this capability** | ✓ | **✗** |
| `implements` | this artifact realises **this capability** | ✓ | **✗** |
| `validates` | this suite covers **this capability** | ✓ | **✗** |
| `scoped-to` | this capability lives in **this context** | ✓ | **✗** |

**Every one of the four lost predicates is the one that attaches something to a
Capability.**

Two models of the same repository, one built mostly by initial acquisition and
one mostly maintained:

```text
mostly initial     76 nodes   78 edges   1.03 edges/node   all 6 predicates
mostly maintained  94 nodes   36 edges   0.38 edges/node   4 predicates, 2 in use
```

**More knowledge. Less than half the connections. Two entire semantic
relationships absent.**

## Decision

**The objective of Continuous Acquisition is to preserve the engineering
understanding an onboarding established, without requiring another onboarding.**

Three rules follow.

**1. Semantic parity is the requirement.** For any fact both modes observe,
Continuous Acquisition proposes the **same relationships** Initial Acquisition
would, from the same evidence. A new module directory is the same evidence at
`t5` as at `t0`, and must produce the same meaning.

**2. Preservation is not inference.** None of the four missing predicates
requires guessing. Each is established by a rule that already exists, from
evidence the mechanical delta already carries. **They were not inferred at `t0`
either — they were read.** Adding them adds no assertion that was not already
justified.

**3. Inference is a separate, later question.** *Adaptive* Continuous
Acquisition — *what understanding is likely to have become stale because of this
change?* — is a **direction, not a decision**, and is explicitly not implemented.
It is a genuinely different behaviour and it must not be smuggled in alongside a
parity fix.

## Rationale

The reframing changes what "done" means, and the difference is testable.

Under *"what may it infer?"* the work is a list of rules and the acceptance
criterion is that they look reasonable. Under *"what understanding must it
preserve?"* the acceptance criterion is a **number**: retention on the frozen
longitudinal suite (`ADR-0128`, `ADR-0129`).

It also explains why the defect survived so long. Continuous Acquisition was
tested by asking *did it propose the changed things?* — and it always did. **It
was never asked whether what it proposed still meant anything.**

## Consequences

**The fix should add zero knowledge and move understanding.** It proposes no new
entity. Under `ADR-0127` that is the first expected instance of understanding
growing while knowledge stays flat — and under the framing this project used
until this session, it would have looked like a change that did nothing.

**Acceptance is a measurement, stated in advance:** rerun `ADR-0129`'s frozen
suite; `EQ-06` must be `answered` at `t9`, and retention must be **100 %**.

**Retraction remains untouched.** Preserving relationships says nothing about
removing them; `D-knowledge-without-implementation: 9` in the current run is
still a report and still governed.

## Compliance

- Continuous Acquisition rules are stated as *what understanding they preserve*,
  not as *what they infer*.
- A relationship proposed by Continuous Acquisition cites the initial rule whose
  meaning it preserves.
- Adaptive behaviour is not implemented under this decision.
