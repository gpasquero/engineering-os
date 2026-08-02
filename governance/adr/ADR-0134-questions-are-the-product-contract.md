---
id: ADR-0134
title: Engineering Questions are the product contract; predicates are implementation detail
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0120, ADR-0126, ADR-0128, ADR-0130, ADR-0132]
---

# ADR-0134 — Questions are the contract

## Context

`ADR-0130` set the next objective as *restore semantic parity* — four predicates
that Continuous Acquisition drops. The reviewer corrected the level:

> The next objective should not be **"restore semantic parity"**. That is the
> implementation objective. The product objective is stronger: **Continuous
> Acquisition should preserve the system's ability to answer Engineering
> Questions.**
>
> **Predicates matter only because Engineering Questions depend on them. Keep
> Engineering Questions as the product contract. Treat predicates as
> implementation details.**

## Decision

**The Engineering Question Set is the product contract. Predicates, rules,
entities and edges are implementation.**

Three consequences, and each changes how work is specified and accepted.

**1. Work is specified by the question it restores, not by the mechanism.** *"`EQ-06`
must be answered at `t9`"*, never *"`constrains` must be emitted"*.

**2. Acceptance is measured on questions.** A change that emits every predicate
and moves no question has not delivered. A change that moves a question by some
other mechanism has.

**3. Predicates may change freely; the contract may not.** The relationship
vocabulary can be refactored, renamed or replaced without a product change,
provided the questions still answer. **The reverse — a question quietly ceasing
to answer — is a breaking change even if every predicate is intact.**

## Rationale

The reframing was immediately load-bearing rather than semantic.

The parity work restored four predicates. **One of them, `scoped-to`, produces no
edge at all in the frozen suite** — the curation policy never accepts the
BoundedContext, so the relationship has nothing to point at. Judged as *semantic
parity*, the work is 3 of 4 and something is unfinished. Judged as *the product
contract*, `EQ-06` is answered at `t9` and retention is 100 %: **the work is
done, and `scoped-to` is a detail that happens not to matter here.**

Only one of those two readings tells a customer something true.

## Consequences

**Questions will eventually be organised into capability families.** The reviewer
named them — Understanding · Impact · Behavior · Evolution · Governance — and
named the reason: *customers think in these categories*.

**This is a direction and is not implemented.** With nine questions and two
answered, families would produce five headings of which three are empty, and
`ADR-0126` already establishes that a level with nothing behind it improves no
one's experience. The direction is recorded so that the day coverage justifies
families, the grouping is not invented under pressure.

**Predicates lose their status as a goal and keep it as a diagnosis.** The
2-of-6 measurement was how the cause was found, and it remains the right
instrument. It is not the specification.

## Compliance

- Work items name the Engineering Question they restore or add.
- Acceptance criteria are stated in coverage and retention, never in predicates.
- Question families are not implemented until coverage justifies them.
