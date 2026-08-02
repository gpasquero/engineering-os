---
id: ADR-0027
title: State machines are registered, not enumerated
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0045]
related: [ADR-0013, ADR-0016, ADR-0025, ADR-0026, ISSUE-0047]
---

# ADR-0027 — State machines are registered, not enumerated

**This is a foundational architectural principle.** It makes the framework
extensible by design rather than by revision.

## Context

`ADR-0025` established that every state belongs to exactly one state machine,
and listed seven as examples. `ISSUE-0045` recorded that the list was
illustrative, that two named machines did not exist yet, that one existing
vocabulary was unlisted — and, decisively, that the rule applies to **target
domains**. A skill reconstructing a banking system will discover state machines
no inventory here could anticipate.

A closed catalogue was therefore never possible.

## Decision

**Do not maintain a fixed catalog of state machines. Engineering OS defines a
State Machine Registration Model instead.**

### Every state machine must register

- identifier
- owner
- governed entity
- purpose
- vocabulary
- transition rules
- authoritative specification
- related ontology concepts
- related workflows

### The registry is the source of truth

**The repository contains only the state machines that exist today.** Future
repositories and future domains are expected to introduce additional ones.

**The framework validates registrations rather than enumerating every possible
lifecycle.**

Documentation, visualizations, ontology navigation and validation are all
**generated from the registry** rather than from manually maintained lists —
consistent with `ADR-0016`, which makes governance authoritative and machine
views derived.

### One mechanism for everyone

The registration mechanism is general enough that **Engineering OS itself and
every adopting repository use exactly the same mechanism.** This mirrors
`ADR-0013`, where the same three manifests serve the framework and its adopters.

## Alternatives considered

**A fixed catalogue of state machines.** Rejected: it cannot anticipate target
domains, so every adopting repository would either be constrained to the
framework's lifecycles or would extend them outside the model.

**Per-repository ad-hoc definitions**, with no registration model. Rejected: no
interoperability, no validation, and no way for a Knowledge Package
(`ADR-0019`) to carry a state machine another repository can interpret.

**Enumerate the framework's machines, and allow adopters to extend.** Rejected
despite being the obvious middle path: it creates two mechanisms where one
suffices, and the framework's own machines would inevitably drift from the
extension mechanism because nothing would force them through it.

## Consequences

### Positive

- **Extensible by design.** Adding a state machine is a registration, not an
  amendment to the framework.
- Registrations are uniform, so tooling written once serves the framework, every
  adopter and every target domain.
- **`registry over catalogue` is now the second instance of a pattern** —
  `MANIFEST.yaml` is already a registry of skills, workflows and contracts. That
  the same shape recurred independently suggests it may be a general principle
  worth naming later, not a coincidence.
- The registry becomes a natural input to the knowledge compiler, and its
  projections replace lists that would otherwise be hand-maintained.

### Negative

- **Registration correctness is unenforced until validators exist.** The
  decision says the framework *validates* registrations, and no validator can be
  built while `ISSUE-0036` is deferred. Until then a malformed registration is
  caught only by review — the same debt as `ISSUE-0037`, now extended to the
  registry.
- **Three of the nine fields are substantial sub-specifications that do not
  exist.** `transition rules`, `related ontology concepts` and `authoritative
  specification` each need a defined shape before a registration can be written.
  This is real M2 work that the field list makes look smaller than it is.
- **Where the registry lives is undefined**, and it overlaps
  `KNOWLEDGE-MANIFEST.yaml`, which `ADR-0013` already says declares state
  machines. `ISSUE-0047`.

### Neutral

- The seven machines named in `ADR-0025` become the first registrations, minus
  those whose subject does not yet exist.

## Compliance

No state machine exists without a registration. No document enumerates state
machines as a hand-maintained list. Documentation, visualizations and validation
concerning state machines derive from the registry. The framework's own machines
are registered through the same mechanism offered to adopters.
