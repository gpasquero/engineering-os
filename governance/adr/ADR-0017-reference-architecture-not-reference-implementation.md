---
id: ADR-0017
title: Engineering OS defines a reference architecture, not a reference implementation
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0032]
related: [ADR-0007, ADR-0012, ADR-0014, ISSUE-0036, ISSUE-0037]
---

# ADR-0017 — Reference architecture, not reference implementation

## Context

`ADR-0012` committed Engineering OS to being an executable framework, and
`ADR-0014` to being a knowledge compiler. `ISSUE-0032` recorded that no
language, runtime, dependency manager or test framework had been chosen, and
that "executable" was therefore a commitment without an implementation.

It also raised the question that matters most for adoption: must a repository
install a compiler toolchain merely to *use* Engineering OS?

## Decision

**The architecture must not depend on any specific implementation language.**

Engineering OS defines a **reference architecture**, not a reference
implementation.

- The compiler exposes a **stable interface** that permits multiple
  implementations.
- There will initially be one reference implementation. Future implementations
  in other languages must remain possible.
- **An adopting repository does not need the complete compiler toolchain to
  consume Engineering OS.** The toolchain is required only when *generating or
  validating* derived artifacts.
- **Authoritative artifacts must remain human-readable and usable without
  executing the compiler.**

The reference implementation language is **intentionally deferred** until
architectural stabilization — `ISSUE-0036`.

### Relationship to ADR-0012

There is no contradiction. `ADR-0012` says the framework *is* executable and
that pipelines are first-class code. This ADR says the *architecture* does not
depend on which language that code is written in, and that consuming the
methodology does not require running it.

## Alternatives considered

**Choose a language now.** Rejected. It would couple the architecture to one
ecosystem before the architecture is stable, and `ISSUE-0001` may pull adapters
toward a different ecosystem entirely. The cost of deferring is low; the cost of
an early wrong choice is a rewrite.

**Require the toolchain for adoption.** Rejected: it raises the adoption cost of
the methodology sharply, for a benefit adopters do not need. Most adopters
consume authoritative artifacts and never regenerate anything.

**No interface — just an implementation.** Rejected: a second implementation
would then be impossible except by imitation, and the architecture would be
whatever the first implementation happened to do.

## Consequences

### Positive

- **Adoption cost stays low.** A team can read the methodology, author
  authoritative artifacts and follow the workflows with no tooling installed.
- **`ADR-0001` is reinforced.** The session protocol — reconstruct context by
  reading the repository — works with no compiler, permanently, by architectural
  requirement rather than by accident.
- Consistent with `ADR-0007`'s runtime-neutral core: the methodology survives a
  change of both agent runtime and implementation language.
- Portability is designed in rather than retrofitted.

### Negative

- **A stable compiler interface is itself a design artifact that must be
  specified before any implementation exists.** This is genuinely hard: interface
  design without an implementation to learn from tends to produce interfaces
  that no implementation can satisfy cleanly. There is real risk of specifying
  the wrong seams.
- **M2 can no longer ship executable tooling.** With the language deferred,
  manifest validation and index generation cannot be built, so generated
  projections stay hand-maintained for longer — extending the debt in
  `ISSUE-0037`.
- "Human-readable without the compiler" constrains authoring formats
  permanently. Any format that needs tooling to be legible is excluded, however
  convenient it might be for the compiler.

### Neutral

- Deferring the language does not defer the architecture. The compiler interface
  specification becomes an M2 deliverable in place of the tooling.

## Compliance

No architectural document names an implementation language. Every authoritative
artifact is legible and editable with a text editor alone. No adopting
repository is required to install a toolchain in order to read, author or follow
the methodology.
