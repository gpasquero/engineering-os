---
id: VISION
title: Vision
status: accepted
created: 2026-08-02
updated: 2026-08-02
source: [sources/, imports/, sources/handoff/BOOTSTRAP.md, sources/handoff/HANDOFF.md]
---

# Vision

## What we are building

An **Engineering Operating System** for AI software engineering: a complete,
modular, versioned engineering methodology that AI agents and human engineers
follow when evolving software systems.

## What we are not building

- Not a prompt library.
- Not a collection of prompts packaged for one vendor's agent runtime.
- Not a giant prompt.
- Not a code generator.

The distinction matters because it determines the shape of every artifact. A
prompt library optimizes for a single invocation. An operating system optimizes
for composition, versioning, review and accumulation of knowledge over years.

## The central thesis

> **Knowledge is the product. Code is one artifact among many.**

A change that ships working code but leaves the organization's understanding
unchanged has produced an asset and a liability at the same time. Every change
must improve:

- the implementation
- the domain and engineering model
- the ontology and its semantics
- the specifications
- the traceability record
- the operational and organizational knowledge

## The four commitments

**1. Knowledge-first.** Updating the knowledge model is part of the definition
of Done, not a follow-up task.

**2. Evidence-driven epistemics.** Every source is evidence, not truth. Every
material assertion carries a status and a confidence. Source disagreement is
recorded, never silently resolved. Uncertainty is never converted into
certainty. Current state and proposed state are never mixed.

**3. Semantics before implementation.** When meaning changes, the model changes
first. Ontology carries semantics, validation shapes constrain instances,
engineering specifications capture behavior.

**4. Composition over monolithic prompts.** Small units with explicit contracts,
sequenced by workflows, referencing shared policies instead of duplicating them.

## The operational core

The mechanism that makes the methodology real rather than aspirational is
**mandatory impact analysis with an explicit gate**. No implementation begins
until the impact of the change is understood across semantics, behavior,
contracts, data, security, operations and compatibility — and until the gate
reads `ready` or `ready-with-mitigations` rather than `blocked`.

## Scope

The methodology targets **existing systems**. All three inherited prototypes
describe evolving software that already exists. Whether greenfield work is in
scope is unresolved — see `ISSUE-0008`.

## What success looks like

A team or agent can apply this repository to an unfamiliar codebase and, over
successive iterations, produce a traceable knowledge model of that system;
then make changes to it that are impact-analysed, specification-driven,
verified, and that leave the knowledge model better than they found it.

## Provenance

This vision is reconstructed from `sources/handoff/BOOTSTRAP.md`, `sources/handoff/HANDOFF.md`,
`sources/requirements.md`, `sources/conversation-summary.md` and the three
prototype skills in `imports/`. Those files are frozen inputs and remain
readable in their original form.
