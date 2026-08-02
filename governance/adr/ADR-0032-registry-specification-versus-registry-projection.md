---
id: ADR-0032
title: A Registry Specification is authoritative; a Registry Projection is derived
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0053]
related: [ADR-0012, ADR-0016, ADR-0031, ISSUE-0037, ISSUE-0048, ISSUE-0054]
---

# ADR-0032 — Registry Specification versus Registry Projection

**This distinction is part of the Engineering OS metamodel.**

## Context

`ISSUE-0053` recorded a contradiction across three `Active` ADRs. `ADR-0031`
called a Registry an *authoritative index*. `ADR-0016` made indexes *generated
projections*. `ADR-0012` said manifests should be *validated or partially
generated*. All three manifests are M2 deliverables, and the artifact kind
determines how each is built.

The issue sketched a reconciliation based on whether a registry *restates*
content held elsewhere. That was the wrong axis.

## Decision

**The apparent contradiction comes from using the word "Registry" for two
different concepts.** Engineering OS distinguishes them.

### Registry Specification — authoritative

Defines:

- registry identity
- semantic purpose
- ownership
- membership rules
- required metadata
- constraints
- relationships
- extension rules

### Registry Projection — derived

The **generated index of the entities currently registered**.

```text
State Machine Registry Specification   (authoritative)
                 ↓
         Knowledge Compiler
                 ↓
State Machine Registry Projection      (derived)
```

**The projection is what humans browse. The specification is what governs the
registry.**

### Why this preserves everything

- **`ADR-0016` remains true**: generated indexes are still derived.
- **`ADR-0031` remains true**: registries are still first-class concepts.

The ambiguity disappears because **the authoritative artifact is the Registry
Specification, not the generated registry contents**.

## Correction to ADR-0031

`ADR-0031`'s pattern stands entirely. Its opening definition — "A Registry is an
authoritative index of semantic entities" — is imprecise under this decision and
should be read as: *a Registry Specification is authoritative; a Registry
Projection is the derived index*.

This is a correction, not a supersession. It is the **second** correction the
project has needed, after `ADR-0026` corrected `ADR-0025` — which strengthens
the case in `ISSUE-0048` for a machine-readable correction mechanism.

## Alternatives considered

**The restating test sketched in `ISSUE-0053`** — a registry is authoritative
when it holds facts no specification holds. Rejected: it makes the artifact kind
depend on a content comparison that shifts as specifications evolve, so the same
artifact could change kind without being edited.

**Declare registries authoritative and narrow `ADR-0016`.** Rejected: it would
make generated indexes authoritative, reintroducing hand-maintenance as
legitimate and undoing the single-source-of-truth property.

**Declare registries derived and narrow `ADR-0031`.** Rejected: membership rules
and extension rules are authored engineering decisions. Nothing could generate
them.

## Consequences

### Positive

- **Three `Active` ADRs are reconciled without superseding any of them**, which
  is a stronger outcome than choosing between them.
- Each artifact gets exactly one kind, so `ADR-0012`'s taxonomy holds without the
  part-authoritative-part-generated exception `ISSUE-0053` feared.
- It explains what the existing hand-maintained indexes are:
  `governance/issues/index.md` and `governance/adr/README.md` are **Registry
  Projections maintained by hand because no compiler exists**. Their Registry
  Specifications do not exist either. `ISSUE-0037`'s register now has a name for
  what it is tracking.
- `ADR-0012`'s "validated or partially generated" resolves cleanly: the
  specification is validated, the projection is generated.

### Negative

- **Two artifacts per registry**, on top of the two per registered entity from
  `ADR-0031`. A state machine now involves a Registry Specification, a Registry
  Projection, and its own specification. That is three files to understand one
  concept, and the cost falls on newcomers.
- **No Registry Specification can be honoured until a compiler exists.** Writing
  membership rules that nothing enforces, for projections that must be
  hand-maintained, is real work with deferred payoff.
- This is the fifth vocabulary collision resolved by splitting an overloaded
  term — after "skill", "authoritative", "state" and "policy". The recurrence
  suggests the discipline should be applied *before* naming, not after.

### Neutral

- The metamodel is named here for the first time and is not defined —
  `ISSUE-0054`.

## Compliance

No document calls a generated index authoritative. Every registry has a Registry
Specification that is authored and accepted, and a Registry Projection that is
generated and never hand-edited — or, until a compiler exists, is recorded as
transitional debt in `ISSUE-0037`.
