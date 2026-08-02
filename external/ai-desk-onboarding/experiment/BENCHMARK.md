---
id: EXPERIMENT-INTERPRETIVE-BENCHMARK
title: Comparative Interpretive Acquisition — deterministic rules against a probabilistic worker
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0108, ADR-0109, ADR-0110, ADR-0111]
---

# Comparative Interpretive Acquisition

**One frozen Mechanical Model. Four interpreters. Same input, measured.**

```text
Mechanical Engineering Model   digest dd47744e6bc66150
    ├── R1  case-level        deterministic rule
    ├── R3  suite-level       deterministic rule
    ├── R4  both-levels       deterministic rule
    └── Claude Sonnet 4.5     probabilistic worker
```

## Contamination disclosure

> **This is not a blind comparison.** The probabilistic worker had already seen
> `R1`, `R3` and `R4` output in prior sessions.

**Mitigation, not a fix**: no probabilistic proposal is drawn from test-case or
`describe`-block text. All four rest on route, table, dependency or document
facts, which no deterministic rule interprets beyond mechanical restatement.

**A genuinely blind comparison requires a worker that has not seen this
repository.** Recorded as a limitation rather than worked around.

## The measurement

| | R1 | R3 | **R4** | Claude |
|---|---|---|---|---|
| assertions proposed | 271 | 203 | **302** | 4 |
| invariant concepts | 0 | 31 | **31** | 3 |
| invariant guarantees | 99 | 0 | **99** | 0 |
| `specializes` edges | 0 | 0 | **99** | 0 |
| workflows | 0 | 0 | 0 | **1** |
| **cross-source syntheses** | 0 | 0 | 0 | **4** |
| reproducible | **exactly** | **exactly** | **exactly** | no |
| cost | negligible | negligible | negligible | a session |
| execution time | < 1s | < 1s | < 1s | minutes |

**Volume and abstraction are not the same axis.** `R4` proposes 302 assertions
and zero syntheses; Claude proposes 4 assertions and 4 syntheses.

## What each class did that the other could not

### Deterministic rules

**Everything countable.** 28 modules, 161 routes, 34 tables, 70 suites — with
complete coverage, exact reproducibility and negligible cost. **`R4` recovers all
four invariants a human authored, at both levels, related by `specializes`.**

No probabilistic worker should ever be asked to do this. It is slower, more
expensive and less reliable at exactly the task rules are best at.

### The probabilistic worker

Four proposals, each requiring **synthesis across weakly structured evidence**:

**`Invariant.WebhookTenantResolutionIsAsymmetric`** — *exactly one route of 161
carries the tenant in its URL path.* Reaching this requires comparing a route
against the distribution of all other routes. Every fact was extracted; **no
declared rule compares a fact to its own population.**

The consequence matters: the tenant isolation invariant has **two enforcement
paths**, and nothing in the repository records that one of them is different.

**`Workflow.PhasedDelivery`** — six phases with terminating verification gates,
synthesized from **fifty document headings** that are individually meaningless.
Workflows are a declared gap for every deterministic rule.

**`Invariant.SoftDeleteIsPervasive`** and **`Concept.ApiKeyAuthentication`** —
both cross-source, both weaker.

## Failure attribution (`ADR-0110`)

Classified before being called a failure:

| Finding | Why no rule found it |
|---|---|
| webhook asymmetry | **`F-rule-insufficient`** — facts present, no rule compares a fact to its population |
| phased delivery workflow | **`F-fact-absent`** for workflows generally; headings are extracted, so a rule *could* be written |
| soft delete | `F-rule-insufficient` |
| api-key authentication | `F-rule-insufficient` |

**Three of four are `F-rule-insufficient`** — the only classification that is
evidence for probabilistic interpretation. `SESSION-0040`'s failure was
`F-fact-ignored`, which is not.

**That distinction is the taxonomy earning its place**: the same evidence that
looked like an argument for a language model in one session was a rule looking
in the wrong place, and here it is not.

## The worker corrected itself, and that is provenance

`Concept.ApiKeyAuthentication` began as a stronger claim: *a second
authentication path exists and is untested.* Checking the mechanical model showed
**two test suites exist**. The assumption was false and the finding is weaker
than first stated.

**The discarded hypothesis is recorded in the proposal.** A probabilistic
worker's wrong turns are part of its provenance, and a worker that reported only
its surviving conclusions would be less auditable, not more.

## Which acquisition tasks belong to which worker class

**The goal is not to choose a winner** — it is assignment.

| Task | Worker class | Because |
|---|---|---|
| enumerate modules, routes, tables, suites, dependencies | **mechanical extractor** | complete, exact, free |
| name a structural fact as a Concept or Capability | **deterministic rule** | the mapping is one-to-one |
| abstract a test suite into an invariant, at both levels | **deterministic rule (`R4`)** | the abstraction is in the `describe` block |
| compare a fact against its own population | **probabilistic** | no rule does; a rule could be written for each case, and not for the general case |
| synthesize a process from many weak documents | **probabilistic** | fifty headings, no structure |
| decide what is true | **neither** | curation (`ADR-0110`) |

**The honest boundary**: rules win wherever the structure carries the meaning.
The probabilistic worker wins where meaning is distributed across evidence that
individually says nothing.

## Not measured

**Assertions accepted and rejected under curation**, which is the metric that
matters most and requires review this session did not perform.

**Duplicates and contradictions between classes** — the four probabilistic
proposals do not overlap `R4`'s domain, by construction, so no measurement is
possible.

**Cost in comparable units.** *A session* against *< 1s* is a real difference and
not a measured one.
