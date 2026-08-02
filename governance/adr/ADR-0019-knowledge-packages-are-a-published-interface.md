---
id: ADR-0019
title: Knowledge Packages are a published interface with a compiler-independent specification
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0029]
related: [ADR-0010, ADR-0014, ADR-0017]
---

# ADR-0019 — Knowledge Packages are a published interface

**This is an explicit architectural principle**, because federation depends on
long-term package stability.

## Context

`ADR-0010` established that knowledge is repository-local and that
multi-repository environments federate through versioned Knowledge Packages.
Nothing defined what a package contains or how it is versioned.

`ADR-0014`'s three tiers sharpened the question to a choice between exporting
the authoritative assets, the canonical knowledge model, or a dedicated
projection. `SESSION-0004` recorded the specific hazard in the second option: a
package derived from the canonical model would have a version depending on the
**compiler version** as well as the content, which is fatal for a federation
format meant to be stable for years.

## Decision

**A Knowledge Package must never export authoritative repository assets.**

Authoritative knowledge belongs to its repository and remains editable **only
there**.

**A Knowledge Package is a published interface between repositories.** It
exports a stable projection derived from the Canonical Knowledge Model.

```text
Authoritative Repository Assets
        ↓
Knowledge Compiler
        ↓
Canonical Knowledge Model
        ↓
Knowledge Package        ← published interface
        ↓
Consumer Repository
```

A Knowledge Package is therefore another **derived artifact**. Its purpose is
**interoperability, not editing**.

### Compiler independence

To avoid coupling package versions to compiler implementations, **the package
format is a stable, versioned specification independent of the compiler
implementation.**

Compiler implementations may evolve independently, provided they produce
conforming Knowledge Packages. This is analogous to different compilers
producing binaries that conform to the same published specification.

### Three version axes

A Knowledge Package versions:

- the **package specification**
- the **exported knowledge model**
- **compatibility information**

**Packages do not expose or depend upon compiler internals.**

## Alternatives considered

**Export the authoritative assets.** Rejected. Knowledge belongs to the
repository that owns the domain (`ADR-0010`), and shipping the sources invites
consumers to edit a copy — creating a second, unowned source of truth. It would
also force every consumer to compile another repository's assets, which requires
the toolchain that `ADR-0017` says consumers must not need.

**Export the canonical knowledge model directly.** Rejected, and this is the
decisive rejection. The canonical model is the compiler's *internal
representation*. Exporting it would make the federation format an artifact of
whichever compiler produced it, couple package versions to compiler versions,
and make `ADR-0017`'s multiple-implementations promise unachievable in practice.

**No packages — reference another repository directly.** Rejected: it exposes
the internal source of truth, breaks the ownership boundary, and gives the
producing repository no stable interface to evolve behind.

## Consequences

### Positive

- **Federation stability is decoupled from compiler evolution.** A package
  written today remains readable when the compiler is rewritten, which is the
  property federation actually needs.
- `ADR-0017`'s multiple-implementations promise becomes real and testable:
  conformance is measured against the published package specification.
- Consumers never hold an editable copy of another repository's knowledge, so
  the ownership rule in `ADR-0010` holds across repository boundaries.
- Consumers need no compiler toolchain to consume a package, consistent with
  `ADR-0017`.

### Negative

- **A published specification is a long-term commitment.** Once repositories
  depend on it, breaking changes carry migration cost across every consumer.
  This is the price of stability and is accepted deliberately.
- **The exported projection must be designed for stability**, which constrains
  what can be exported. Anything whose shape is likely to change should stay out
  of the package, and judging that in advance is hard.
- **Three version axes is real complexity.** A consumer must reason about
  specification version, content version and compatibility information
  simultaneously.
- A package is a projection of a projection. Detecting that a package is stale
  relative to the authoritative assets it ultimately derives from is harder than
  a single-hop comparison.

### Neutral

- The package specification is M13 work. What M2 must respect is only the
  constraint that nothing couples the eventual package format to compiler
  internals.

## Compliance

No Knowledge Package contains authoritative repository assets. No package field
is defined in terms of a compiler internal structure. A conforming package is
readable by a consumer that has never run the producing repository's compiler,
and by any compiler implementation that satisfies the published specification.
