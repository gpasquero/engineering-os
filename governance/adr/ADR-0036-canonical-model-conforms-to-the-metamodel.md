---
id: ADR-0036
title: The Canonical Knowledge Model is a graph conforming to the Metamodel; the Metamodel precedes the compiler interface
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0014, ADR-0017, ADR-0035, ISSUE-0055]
---

# ADR-0036 — The Canonical Knowledge Model conforms to the Metamodel

**This is a fundamental distinction.** It fixes what the compiler compiles into,
and it changes the order of M2.

## Context

`ADR-0014` defined the Canonical Knowledge Model as the compiler's internal
representation, leaving its serialization an implementation decision. `ADR-0017`
required the compiler to expose a stable interface permitting multiple
implementations, and M2 was scheduled to produce that interface specification.

`ADR-0035` establishes the Metamodel as the ontology of the framework itself.

If the compiler interface were finalized first, the compiler would define its own
internal structure and the metamodel would arrive afterwards, describing whatever
the implementation happened to build.

## Decision

**Before implementing the Knowledge Compiler interface, create the Engineering
OS Metamodel.**

The compiler consumes authoritative artifacts and **progressively instantiates
the metamodel**.

> **The Canonical Knowledge Model is not an arbitrary graph. It is a graph
> conforming to the Engineering OS Metamodel.**

```text
Engineering OS Metamodel
        ↓
Canonical Knowledge Model
        ↓
Knowledge Explorer · Documentation · Indexes · Knowledge Packages ·
Future AI interfaces
```

**The metamodel is the contract between authoring and compilation.**

It must be established before the compiler interface is finalized, so that the
compiler **compiles into the metamodel rather than inventing its own internal
structure**.

> The consumers above are read as **parallel projections** of the Canonical
> Knowledge Model, consistent with `ADR-0014`'s rule that no consumer is
> privileged — not as a pipeline in which documentation derives from the
> Explorer. If a pipeline was intended, this reading needs correcting.

## Relationship to ADR-0014 and ADR-0017

Neither is superseded; both are strengthened.

`ADR-0014` said the canonical model's *serialization* is an implementation
decision. That remains true. What this ADR fixes is its **structure**, which
`ADR-0014` left open. Serialization stays free; conformance does not.

`ADR-0017` promised a stable compiler interface permitting multiple
implementations. The metamodel is what makes that promise checkable: conforming
implementations produce conforming canonical models, exactly as `ADR-0019` made
package conformance the test for federation.

## Alternatives considered

**Finalize the compiler interface first, derive the metamodel from it.**
Rejected — the decision exists to prevent this. The metamodel would then describe
one implementation's choices, and `ADR-0017`'s multiple-implementations promise
would be unachievable, since a second implementation would have to reproduce the
first's internals.

**Let the canonical model be an arbitrary graph, with the metamodel as
documentation.** Rejected: a non-binding metamodel is a glossary with more
structure. Nothing would prevent projections from depending on shapes the
metamodel never sanctioned.

**Develop both concurrently.** Rejected as unstable in practice: whichever moves
faster would constrain the other, and the compiler moves faster because it has
concrete work to do.

## Consequences

### Positive

- **The compiler has a target rather than a design problem.** Its job becomes
  instantiating a defined metamodel, not deciding what knowledge looks like.
- Conformance becomes testable, which is what `ADR-0017`'s multiple
  implementations require.
- Every projection — Explorer, documentation, indexes, Knowledge Packages —
  depends on a stable structure rather than on compiler internals. This is the
  same decoupling `ADR-0019` made for Knowledge Packages, now applied upstream.
- Authoring and compilation get an explicit contract, so a change to authoring
  formats is checkable against something.

### Negative

- **M2 is reordered, and its largest deliverable moves behind a new one.** The
  compiler interface specification was unblocked and ready; it is now gated on a
  metamodel that does not exist and whose location is undecided (`ISSUE-0055`).
- Metamodel changes become expensive. Every conforming canonical model, and
  every projection derived from one, is affected — so the metamodel needs
  versioning and a compatibility story before it has any users.
- There is a real risk of designing the metamodel without the feedback that
  building a compiler would provide. `ADR-0017` already recorded the analogous
  risk for interface design without an implementation to learn from; this
  compounds it.

### Neutral

- Nothing changes for authoritative artifacts, which remain human-readable and
  editable without the compiler (`ADR-0017`).

## Compliance

The compiler defines no internal structure the metamodel does not sanction. No
projection depends on a shape absent from the metamodel. The compiler interface
specification is not finalized before the metamodel exists.
