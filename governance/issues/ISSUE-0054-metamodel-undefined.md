---
id: ISSUE-0054
title: The Engineering OS metamodel is named but undefined
type: gap
status: resolved
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0032-registry-specification-versus-registry-projection.md
resolved-by: ADR-0035
---

# ISSUE-0054 — The Engineering OS metamodel is undefined

## Statement

`ADR-0032` states that the Registry Specification / Registry Projection
distinction "should become part of the **Engineering OS metamodel**".

This is the first appearance of the metamodel in the repository. It now has a
member and no definition.

## Why it matters

The project has accumulated a substantial body of concepts that describe *the
model itself* rather than any domain: artifact kinds, the revision lifecycle,
state machines and their registration, the three-tier knowledge model, the
Registry Pattern, normative artifact types, acceptance semantics.

If a metamodel exists, those are its members and it needs a home, an artifact
kind and a specification. If it does not, then "metamodel" is loose prose in an
`Active` ADR and should be corrected.

The question is not cosmetic. `ADR-0027` requires state machines to declare
`related ontology concepts`, and `ADR-0031` requires every extensible concept to
be evaluated against the Registry Pattern. Both presuppose a vocabulary of
concepts that the metamodel would define.

## Open sub-questions

- Is the metamodel an artifact, a section of `KNOWLEDGE-MANIFEST.yaml`, or the
  ontology of Engineering OS itself — which is what `ISSUE-0031`'s self-model
  was already circling?
- Does it overlap `governance/glossary.md`? The glossary already defines most of
  these terms, but as prose for readers rather than as a model for a compiler.
- Is it framework-only, or does an adopting repository extend it?
- Is a ModelingPolicy (`ADR-0030`) the normative statement of metamodel rules,
  with the metamodel itself being the structure those rules constrain?

That last reading is the most likely and would make the metamodel the schema
layer beneath both the glossary and the policies.

## Relationship to existing issues

`ISSUE-0031` asks what Engineering OS's own `model/` should contain and whether
`governance/` overlaps it. If the metamodel is the ontology of Engineering OS,
these are the same question approached from two directions and should be
resolved together.

## Resolution

`ADR-0035`. **Engineering OS has an explicit Metamodel: the ontology of
Engineering OS itself.**

> Its purpose is not to describe software systems. Its purpose is to describe
> **how Engineering OS describes software systems.**

A meta-level ontology defining the core semantic entities of the framework —
Artifact Type, Artifact Revision, Registry Specification, Registry Projection,
Manifest, Policy, Workflow, Skill, Capability, Vocabulary, State Machine,
Ontology, Concept, Knowledge Package, Compiler, Projection, Validation,
Acceptance Record, ADR, Issue — each declaring identity, purpose, ownership,
lifecycle owner, authoritative representation, derived representations,
relationships and extension points.

**The process gate is the operative part:** from this point onward, every new
concept must be positioned within the metamodel *before* a new artifact type is
introduced. This inverts eleven sessions of practice and is the structural
remedy for naming after the fact — the defect behind five vocabulary collisions.

The reading suggested above — that a `ModelingPolicy` states metamodel rules
normatively while the metamodel is the structure those rules constrain — is
consistent with `ADR-0035` but not stated by it.

**Two sub-questions are not answered.** Where the metamodel lives is
`ISSUE-0055`, now blocking M2. Its relationship to `ISSUE-0031`'s self-model
becomes urgent rather than academic, since both describe Engineering OS at
different levels.
