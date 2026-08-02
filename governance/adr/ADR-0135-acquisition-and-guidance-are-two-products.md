---
id: ADR-0135
title: Engineering Acquisition and Engineering Guidance are two products sharing an implementation
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0092, ADR-0094, ADR-0098, ADR-0118, ADR-0123, ADR-0133, ADR-0136]
---

# ADR-0135 — Two products

## Context

Everything built in forty-nine sessions sits on one side or the other of a line
nobody has drawn. The reviewer drew it:

> It is now time to begin separating two products that currently happen to share
> an implementation.
>
> **Engineering Acquisition** — produces understanding.
> **Engineering Guidance** — consumes understanding.
>
> Everything built so far naturally belongs to one side or the other. That
> separation will eventually make the architecture clearer.

## Decision

**Engineering OS is two products with one boundary between them: the
Authoritative Engineering Model.**

| | Engineering Acquisition | Engineering Guidance |
|---|---|---|
| Does | **produces** understanding | **consumes** understanding |
| Owns | Mechanical Acquisition · Stack Profiles · Interpretive Discovery · Discovery Skills · the three modes · Drift · curation | Queries · Recommendations · Plans · Task graphs · Worker routing · the Director |
| Measured by | coverage · **retention** | Guidance Preservation (`ADR-0133`) — **unmeasured** |
| State | strong | **weakest verb** (`ADR-0123`) |

**The boundary is a contract, not a layer.** Guidance reads the Engineering Model
and the Engineering Question Set. **It may not read a repository, a Stack
Profile, a mechanical model, a candidate model or a drift report** — those are
Acquisition's internals, and a guidance component that read one would make the
separation decorative.

**Acquisition may not know what guidance exists.** A Discovery rule that emitted
a relationship because a plan needed it would be fitting the model to its
consumer, and the model is the product (`ADR-0072`).

## Rationale

The separation is already true and unstated, which is the cheapest kind to
formalise: the inventory above assigns every existing component without
ambiguity or duplication.

It also explains an imbalance the five verbs exposed. **Guidance was built first
and has never run against a model it did not build for itself** — every plan
demonstration used a fixture. Naming it as a product with its own metric makes
that testable rather than merely known.

**And it clarifies what is being sold.** `ADR-0123` records that guidance is what
customers buy; this decision records that acquisition is nonetheless a product in
its own right, with its own promise — *your understanding will survive* — that
holds whether or not guidance ever runs.

## Consequences

**This decision moves no file.** It is a boundary, and the first check is whether
the existing code already respects it — which is the honest first task, not a
reorganisation.

**Guidance is behind preservation in the queue** (`ADR-0136`), and this decision
says why that is a sequencing choice rather than neglect: guidance derived from
understanding that degrades silently is worse than no guidance.

**The two products will eventually have separate lifecycles**, and possibly
separate customers: a team may buy acquisition alone. Nothing depends on that
yet, and the boundary is what makes it possible later.

## Compliance

- No guidance component reads a repository or any acquisition intermediate.
- No acquisition rule cites a plan, recommendation or intent as its reason.
- Each new component declares which product it belongs to.
