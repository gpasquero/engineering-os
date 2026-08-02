---
id: ADR-0051
title: Dimensions enter the metamodel only through a Dimension Review
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0065]
related: [ADR-0018, ADR-0048, ADR-0049, ADR-0053, ISSUE-0067]
---

# ADR-0051 — Dimension Review

## Context

`ADR-0049` established five conditions a concept must satisfy to become a
Dimension, and required an ADR for each. `ISSUE-0065` recorded nine candidates,
none evaluated — five of them already in active use across the corpus.

The obvious next step was to evaluate them one at a time.

## Decision

**Do not evaluate candidate Dimensions one by one. First define the Dimension
Evaluation Process.**

Every proposed Dimension is evaluated by a **standard review procedure** — a
**Dimension Review** — producing exactly one of four outcomes:

1. **Accepted as a Dimension.**
2. **Rejected and modeled as metadata.**
3. **Rejected and modeled as a relationship.**
4. **Rejected and modeled as another metamodel entity.**

**The decision itself becomes an authoritative artifact**, so the reasoning is
preserved.

**`ADR-0049`'s five criteria become mandatory evaluation criteria rather than
informal guidance.**

> **Dimensions become part of the metamodel only through that review process.**

## Alternatives considered

**Evaluate the nine candidates directly**, one ADR each, as `ISSUE-0065`
proposed. Rejected: nine ad-hoc evaluations would establish nine precedents
rather than one procedure, and the tenth candidate would restart the argument.

**Treat the five criteria as guidance applied by judgement.** Rejected — the
decision names why: *this prevents future discussions from becoming
subjective*. Criteria that are optional are criteria that get argued around.

**Grandfather the five dimensions already in use.** Not chosen. They are in
active use *because* the project needed them, not because they passed a test
that did not exist. Reviewing them is how the corpus becomes compliant with its
own rule rather than exempt from it.

## Consequences

### Positive

- **Process before instances**, which is the same move that resolved
  `ISSUE-0062`: define the entity, then write the instances. Applied twice in
  two sessions, it is becoming the project's default response to "evaluate these
  N things".
- Four named outcomes mean a rejection is constructive. A concept that fails
  still gets modelled — as metadata, a relationship, or another entity — so the
  review never leaves a real distinction homeless.
- The reasoning is preserved as an authoritative artifact, so a later challenge
  to a dimension reopens a recorded decision rather than a memory.
- Reviewing the five in-use dimensions is uncomfortable and correct. It is the
  same choice `ISSUE-0040` faced about the self-certified corpus, and answered
  the same way.

### Negative

- **Dimension Review is a new artifact type**, and `ADR-0038` requires four
  questions answered before one is accepted — including which metamodel entity
  it instantiates. **The metamodel does not exist yet**, so that gate cannot be
  literally satisfied. `ISSUE-0067`.
- It is unclear whether a Dimension Review *is* an ADR with required structure or
  a distinct type. `ADR-0049` already requires an ADR per dimension; this
  requires a review. Two artifacts or one is unstated — also `ISSUE-0067`.
- Nine reviews before the Dimension Registry can be written, on top of defining
  the review procedure itself. M2 grows again.

### Neutral

- The nine candidates in `ISSUE-0065` become the first inputs to the process
  rather than nine separate questions.

## Compliance

No dimension enters the metamodel except through a Dimension Review. Every
review records all five `ADR-0049` criteria and one of the four outcomes. A
rejected concept is modelled as metadata, a relationship or another metamodel
entity — never left undecided.
