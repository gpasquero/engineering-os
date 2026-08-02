---
id: ADR-0034
title: Every repository owns a Knowledge Explorer, generated from its Canonical Knowledge Model
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0052]
related: [ADR-0010, ADR-0014, ADR-0017, ADR-0019, ADR-0031]
---

# ADR-0034 — The Knowledge Explorer is a per-repository projection

## Context

`ADR-0031` named the Knowledge Explorer as a future surface exposing registries
for navigation, and attached a requirement to it. `ISSUE-0052` recorded that it
had no definition, did not appear in `ADR-0014`'s consumer list, and could be
read as a new consumer, a renaming of the Documentation Website, or a navigation
layer over several consumers.

## Decision

**Every Engineering OS repository owns its own Knowledge Explorer.**

**It is not documentation.** It is a **projection of that repository's Canonical
Knowledge Model**.

- Engineering OS itself has a Knowledge Explorer describing the framework.
- Every adopting repository generates another describing **its own domain**.

**It is a first-class generated product of the Knowledge Compiler**, alongside
search indexes, validation reports and documentation.

### Federation is additional, not default

Future federation may allow multiple Knowledge Explorers to interoperate through
Knowledge Packages (`ADR-0019`), but **federation is an additional capability
rather than the default architecture**. A repository's Explorer is complete and
useful over its own knowledge alone.

## Alternatives considered

**The Documentation Website under another name.** Rejected: the decision places
the Explorer *alongside* documentation, not in place of it. Documentation is
authored narrative shaped for reading; the Explorer is generated navigation over
a model. Conflating them would make the model's structure subordinate to
editorial choices — the failure `ADR-0011` rejected when it refused the
documentation-generator framing.

**A framework-only surface**, one Explorer over Engineering OS. Rejected: it
would make the framework's own knowledge navigable while leaving every adopter's
domain knowledge inert, which inverts the point. The methodology exists to make
*target systems* understandable.

**A federated Explorer as the default**, spanning repositories. Rejected as
premature: it would make a single-repository adopter depend on machinery for a
case they do not have, and the Knowledge Package specification does not exist
(M13).

## Consequences

### Positive

- **It becomes a shipped capability, not a project website.** An adopting
  repository gets a navigable view of its own domain — arguably the most visible
  benefit of adopting Engineering OS, and the first deliverable that a
  non-engineer stakeholder would see.
- Consistent with `ADR-0010`: knowledge is repository-local, and so is the
  surface that navigates it. No central explorer, no shared model.
- Consistent with `ADR-0014`: it is a projection of the canonical model, so it
  reads the compiled model rather than parsing authoritative assets. It is
  another consumer, with no privilege over the others.
- The Registry Pattern gets its primary navigation surface: registries browsable
  independently of the specifications they reference (`ADR-0031`).

### Negative

- **Generating an Explorer requires the compiler toolchain.** `ADR-0017`
  guarantees an adopter needs no toolchain to *consume* Engineering OS — reading
  and authoring work with a text editor — but an adopter who wants an Explorer
  must install it. That is consistent, since generation is exactly the case
  `ADR-0017` carves out, but it means the most visible benefit is behind the
  toolchain.
- M12 scope grows from documentation and adapters to a generated interactive
  product, and nothing yet says what its interface is.
- Every adopting repository now has a build output to host or serve somewhere,
  which is an operational concern the project has not touched.

### Neutral

- Federation between Explorers is deferred with the rest of M13, and depends on
  the Knowledge Package specification.

## Compliance

No Knowledge Explorer reads authoritative assets directly; it is generated from
the Canonical Knowledge Model. No repository's Explorer contains another
repository's knowledge except through a Knowledge Package. The Explorer is never
hand-edited.
