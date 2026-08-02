---
id: ADR-0035
title: The Engineering OS Metamodel is the ontology of the framework itself
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0054]
related: [ADR-0014, ADR-0036, ISSUE-0031, ISSUE-0055]
---

# ADR-0035 — The Engineering OS Metamodel

**This is the semantic backbone of Engineering OS.** Everything else should
ultimately be expressible as instances of it.

## Context

Concepts have emerged incrementally across thirty-four decisions: artifact
kinds, revision lifecycles, state machines, registries, manifests, policies,
acceptance records. Each was introduced when a specific problem demanded it, and
each was named after the fact — which produced five vocabulary collisions,
recorded most recently in `ADR-0032`.

`ISSUE-0054` recorded that `ADR-0032` named a metamodel without defining it, and
observed that a substantial body of concepts describing *the model itself* had
accumulated with no home.

The project has reached the point where the incremental approach has run out.

## Decision

Engineering OS has an explicit **Metamodel**.

**The Engineering OS Metamodel is the ontology of Engineering OS itself.**

> **Its purpose is not to describe software systems. Its purpose is to describe
> how Engineering OS describes software systems.**

This is a **meta-level ontology**. It defines the core semantic entities of the
framework and the relationships between them.

### Entities

Artifact Type · Artifact Revision · Registry Specification · Registry
Projection · Manifest · Policy · Workflow · Skill · Capability · Vocabulary ·
State Machine · Ontology · Concept · Knowledge Package · Compiler · Projection ·
Validation · Acceptance Record · ADR · Issue

### Each entity defines

- identity
- purpose
- ownership
- lifecycle owner
- authoritative representation
- derived representations
- relationships
- extension points

### The process gate

**From this point onward, every new concept must first be positioned within the
metamodel before a new artifact type is introduced.**

This inverts how the project has worked for eleven sessions. It is the direct
remedy for naming after the fact.

## Alternatives considered

**Continue incrementally, naming concepts as problems demand them.** Rejected:
it produced five overloaded terms — "skill", "authoritative", "state", "policy",
"registry" — each caught after propagation and each requiring a split. `ADR-0032`
recorded the recurrence as the finding rather than the incident.

**A glossary as the semantic backbone.** Rejected: `governance/glossary.md`
defines terms as prose for readers. A metamodel defines entities with identity,
ownership, representations and relationships, for a compiler. The glossary
remains useful and becomes a human-facing view of what the metamodel states
formally.

**Defer until more concepts exist.** Rejected: `ADR-0036` establishes that the
compiler compiles *into* the metamodel, so deferring would mean the compiler
inventing its own structure first — precisely the outcome to avoid.

## Consequences

### Positive

- **A single semantic backbone**, replacing concepts scattered across
  thirty-four ADRs and a prose glossary.
- The process gate stops vocabulary collisions at the source rather than
  catching them afterwards, which is a structural fix for a defect the project
  has now hit five times.
- It gives `ADR-0027`'s `related ontology concepts` field and `ADR-0031`'s
  "evaluate every extensible concept" rule something concrete to refer to. Both
  presupposed a vocabulary that did not exist.
- The eight required properties per entity force questions the project has been
  answering ad hoc — every entity must now declare its lifecycle owner and its
  authoritative versus derived representations.

### Negative

- **The entity list contains concepts this project has never defined.**
  Capability, Concept, Validation and Ontology appear in the metamodel while
  having no ADR, no specification and no agreed meaning here. Defining them is
  not transcription; it is new design work, and the list understates it.
- **Where the metamodel lives is undefined**, and it matters more than usual: an
  adopting repository's canonical model must conform to it, so it cannot be
  purely repository-local. `ISSUE-0055`.
- The metamodel will need its own lifecycle, acceptance and versioning, and a
  change to it potentially invalidates every conforming canonical model.
- The relationship to `ISSUE-0031`'s self-model is now urgent rather than
  academic: both describe Engineering OS, at different levels, and nothing yet
  says whether they are one artifact or two.

### Neutral

- No existing concept changes meaning. The metamodel states formally what is
  currently distributed across ADRs and the glossary.

## Compliance

No new artifact type is introduced without first being positioned in the
metamodel. Every metamodel entity declares all eight required properties. The
glossary and the metamodel do not disagree; where they do, the metamodel governs.
