---
id: METAMODEL-OWL-FINDINGS
title: What the first OWL skeleton exposed
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
artifact-kind: authoritative
established-by: [ADR-0062, ADR-0065]
---

# What the first OWL skeleton exposed

The skeleton was generated at 12 of 27 entities rather than at completion,
specifically to find problems while they are cheap. It found six, and confirmed
three decisions.

**None of these blocks B1.** They are recorded here and, where they need to
survive beyond this document, in the affected specification's `Debt` section.

## The findings

### 1. `Relationship` competes with OWL's own mechanism for edges

Every association in the skeleton is expressed as an `owl:ObjectProperty`. The
metamodel also declares an entity, `Relationship`, whose stated purpose is to
represent an association as a first-class thing.

**So the metamodel now has two ways to express an edge**, and the specification
does not say which is authoritative.

The likely resolution is that they are at different abstraction levels
(`ADR-0043`): `owl:ObjectProperty` declarations are Layer A *metamodel*
statements about what kinds of edge exist, while `Relationship` instances are
Layer B statements asserting particular edges. If so, `Relationship` is a
metamodel type whose instances never appear in this file — which is consistent,
but it is not what the specification says.

**This is the finding most likely to change an entity.** It would have been much
more expensive to discover after the operational entities were written, since
every one of them relates to something.

### 2. `Dimension` carries no data its specification does not already carry

In OWL, `eos:Dimension` is a class whose every instance stands in a one-to-one
functional relation to a `DimensionSpecification`, has no authoritative
representation of its own, and holds no property the specification lacks.

The Markdown said as much — *"a Dimension does not have an identity separate
from the specification that defines it"* — but reading it as a class definition
makes the consequence plain: **it may be a distinction without a difference.**

Against removing it: `DimensionAssignment.along` reads more naturally pointing
at an axis than at a document, and the Specification/Instance split is a
deliberate pattern used for state machines and registries too. If `Dimension`
collapses, that pattern is in question everywhere.

**Deferred.** Nothing is built on it yet — `Dimension` still has no instances.

### 3. Four entities shared an identity definition nobody had noticed

`Concept`, `Capability`, `Invariant` and `Actor` each independently define
identity as *"a qualified name within a BoundedContext"* and each declares a
`scoped-to` relationship.

Written as OWL, that is four identical restrictions — which is the standard
signal of a missing superclass. The skeleton introduces **`ContextualEntity`**,
which appears in no Markdown specification.

This is the clearest instance of the effect the checkpoint was meant to produce:
the repetition was invisible across four files and obvious in one.

### 4. `Evidence.supports` has no range, because `Assertion` does not exist

The specification says Evidence *supports* "any assertion". OWL requires a
range, and there is no `Assertion` class.

An assertion appears to be: a Concept's stated meaning, an Invariant, a claimed
Capability realisation, a Relationship. That is not a natural class — it is
"anything a human claimed rather than something the compiler derived", which is
exactly `ADR-0060`'s Interpretive/Mechanical boundary.

**If that boundary needs to be expressible in the model rather than only in
prose, `Assertion` is the entity that expresses it.** Left undeclared for now.

### 5. `Relationship.typedBy` points at nothing defined

Already recorded as debt when `Relationship` was written; OWL forced a
provisional choice rather than allowing the question to stay open. The skeleton
guesses `Concept`, marked `PROVISIONAL`.

### 6. `DimensionAssignment.hasValue` is not expressible in plain OWL

The valid range depends on which `Dimension` the assignment is along. OWL has no
way to say *"the range of this property is determined by the value of that
one"* without either a value partition per dimension or leaving it unconstrained.

The skeleton leaves it unconstrained. This is a genuine expressiveness limit,
not a modelling error, and it is the first concrete evidence for what the
Knowledge Compiler must check that an ontology cannot (`ISSUE-0063`).

## What the skeleton confirmed

**The Artifact / ArtifactRevision split expresses cleanly.** `hasActiveRevision`
as a functional sub-property of `hasRevision` with `maxCardinality 1` says
exactly what `ADR-0026` and `ADR-0064` intended, with no contortion. A model
where `Artifact` carried lifecycle state could not be written this way.

**The zero-or-more cardinalities survive contact with a reasoner.**
`Capability.realisedBy`, `Invariant.enforcedAt` and `Actor.uses` are all
unconstrained, so an unrealised capability and an unenforced invariant are both
consistent — which is the whole point of choosing those cardinalities.

**`ADR-0065`'s split gives the ontology a usable top.** Without it the file would
be a flat list of seventeen sibling classes.

## What the skeleton cannot yet express

**Nothing operational.** No Workflow, Gate, AcceptanceRecord, ADR, Issue, Policy
or Skill. The ontology can describe a domain and cannot describe a single act of
engineering performed on it.

That gap is the strongest available argument that `ADR-0065`'s two families are
real: **half the metamodel is missing and the half that is present is internally
complete.**

## Status of this artifact

**Hand-written from the Markdown specifications, not compiled from them.** It is
a Layer A authoritative artifact today. When the Knowledge Compiler exists (B4,
B5) the direction must be settled: either the ontology is generated and the
Markdown is authoritative, or the reverse, or both are projections of a third
thing.

Maintaining both by hand is precisely what `ISSUE-0037` records the cost of, and
this file is now the sixth hand-maintained projection in the repository.

## Namespace

`https://example.org/engineering-os/metamodel#` is **a placeholder**, chosen
because `example.org` is IANA-reserved and cannot be mistaken for a commitment.

A published ontology needs a stable, resolvable, owned namespace. That requires
a domain, and it is a decision for whoever publishes, not for B1.
