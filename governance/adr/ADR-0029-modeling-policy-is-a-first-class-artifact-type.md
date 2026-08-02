---
id: ADR-0029
title: Modeling Policy is a first-class artifact type; ADRs explain why, policies define the rule
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0046]
related: [ADR-0002, ADR-0008, ADR-0025, ADR-0026, ADR-0027, ISSUE-0050]
---

# ADR-0029 — Modeling Policy is a first-class artifact type

**This is part of the core architecture.** It prevents the accumulated ADR
history from becoming the operational specification.

## Context

`ISSUE-0046` recorded that general modeling rules were accumulating across
scattered ADRs with no home. `ADR-0025` declared "a fundamental modeling rule for
the entire Engineering OS"; `ADR-0026` declared "a core modeling guideline";
`ADR-0012` defined the artifact taxonomy; `ADR-0027` defined registration rules.

The corpus is now 29 ADRs, 5 of them superseded, with one partially corrected. An
agent trying to derive the *currently applicable* modeling rules from that
history would be doing archaeology — reading superseded decisions, reconstructing
supersession chains three deep, and inferring which parts of a corrected ADR
still hold.

That is not a specification. It is a record of how a specification came to be.

## Decision

Engineering OS gains a new first-class artifact type: the **Modeling Policy**.

A Modeling Policy captures **stable engineering rules that govern how domains are
modeled**.

### How it differs from an ADR

| | ADR | Modeling Policy |
|---|---|---|
| Scope | one architectural decision | a body of rules |
| Change | immutable; superseded | **expected to evolve** |
| Character | **historical** | **normative** |
| Audience | humans seeking rationale | **directly consumed by AI agents** |

### The governing separation

> **ADRs explain *why* a policy exists. Policies define the rule that must be
> followed.**

**Policies explicitly reference the ADRs from which they originated.**

**Engineering OS agents primarily consume Policies. Humans read ADRs when they
need to understand the rationale.**

### Subject matter

Naming conventions · lifecycle ownership rules · ontology modeling rules · state
machine registration rules · traceability requirements · artifact taxonomy ·
acceptance semantics.

### Location

`shared/policies/`, per `ADR-0008` — normative prose referenced by path and
never inlined.

## Alternatives considered

**Collect the rules in a single governance document.** Rejected: it would sit
outside `shared/`, so skills could not reference it as a policy, and it would
mix the framework's own memory with the methodology it ships to adopters.

**Generate policies from ADRs.** Attractive — `ISSUE-0046` raised it as the
first legitimately derived artifact — but rejected. A policy is expected to
evolve independently of the decision that created it, and generation would pin
it to a historical record it is meant to outgrow. Policies *reference* ADRs;
they are not derived from them.

**Leave the rules in ADRs and require agents to read the corpus.** Rejected, and
this is the decisive rejection: the corpus is already 29 decisions with five
supersessions and one partial correction. It is a poor specification today and
gets worse monotonically.

## Consequences

### Positive

- **The operational specification stops growing with the decision history.** An
  agent reads current rules; the archaeology is optional and reserved for humans
  asking why.
- Rules become revisable without rewriting history. A modeling rule can improve
  while the ADR that introduced it stays an accurate record of what was decided
  and when.
- It gives `shared/policies/` its first defined type, and the M3 policy list a
  shape rather than a list of filenames.
- The ADR/policy split mirrors the distinction the methodology already imposes
  on target systems: evidence and its provenance are separate from the assertions
  drawn from them.

### Negative

- **Rule text will exist in two places** — the ADR's decision and the policy —
  which is the duplication the artifact taxonomy exists to prevent. Here the
  divergence is *intended*: the ADR records what was decided then, the policy
  states what applies now. But intended divergence and accidental drift look
  identical in a diff, and nothing distinguishes them mechanically.
- A reader arriving at an old ADR sees a rule the policy may have since changed,
  with no signal. This is `ISSUE-0048`'s problem at larger scale — supersession
  and correction both fail to express "still true as history, no longer the
  operative rule".
- **The word "policy" is now overloaded**: governance policies govern acceptance
  (`ADR-0023`), Modeling Policies govern modeling, and the M3 list contains
  process policies that are neither. Given this project's record with "skill",
  "authoritative" and "state", this is flagged immediately rather than
  discovered later — `ISSUE-0050`.

### Neutral

- No existing rule changes. The rules already decided become the content of the
  first Modeling Policies in M3.

## Compliance

Every general modeling rule is stated in a Modeling Policy, not only in an ADR.
Every Modeling Policy references the ADRs it originated from. No skill inlines
policy text. An agent seeking the applicable rules reads `shared/policies/`, not
`governance/adr/`.
