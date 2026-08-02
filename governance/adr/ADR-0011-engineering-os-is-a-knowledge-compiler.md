---
id: ADR-0011
title: Engineering OS is a knowledge compiler
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0012, ADR-0013, ISSUE-0033, ISSUE-0034]
---

# ADR-0011 — Engineering OS is a knowledge compiler

**This is a foundational architectural principle.** It governs the design of
generators, validators, visualizers, plugins and every future extension
mechanism. Decisions that contradict it are wrong even if locally reasonable.

## Context

Engineering OS holds authoritative engineering knowledge expressed through many
artifact types: ontology, glossary, specifications, invariants, state machines,
impact analyses, decision records, traceability.

The default framing for a repository like this is a **documentation generator**:
authored Markdown in, a website out. That framing is wrong here, and adopting it
by default would be expensive to reverse. It makes the website the product, and
every other consumer — knowledge graph, search index, agent context — becomes a
special case bolted onto a documentation pipeline.

The knowledge itself is the product. A website is one way to look at it.

## Decision

Engineering OS is designed as a **knowledge compiler**, not a documentation
generator.

The compilation pipeline transforms authoritative assets into a **canonical
knowledge model**, which is the internal representation of the system. Derived
artifacts are produced *from that model*, never directly from the authoritative
assets.

```text
Authoritative Assets
        ↓
     Parsing
        ↓
  Normalization
        ↓
   Validation
        ↓
 Semantic Linking
        ↓
Canonical Knowledge Model
        ↓
  Derived Artifacts
```

**The canonical knowledge model is the primary product of compilation.**

Consumers of the model include, with no consumer privileged over another:

- Knowledge Graph
- Search Index
- Cross-reference Index
- Impact Database
- Validation Reports
- Agent Context
- Documentation Website
- Future AI interfaces

The generated website is one **projection** of the model, not the model itself.

Intermediate representations, incremental compilation, dependency tracking,
plugins and caching are **implementation decisions**, not architectural
requirements. They may be adopted when they earn their cost.

## Alternatives considered

**Documentation generator.** Rejected. It subordinates the model to one
presentation. Adding a knowledge graph or an agent-context export would each
require reaching back into the authoring layer, and the semantics of a concept
would end up defined by whatever the website needed.

**Direct generation per consumer** — each consumer parses the authoritative
assets itself. Rejected: N parsers and N normalizations, with no guarantee they
agree. A change to any artifact format would require touching every consumer,
and semantic drift between consumers would be undetectable.

**Database-first** — load everything into a store and query it. Rejected as an
implementation choice presented as an architecture. It also weakens the property
that the entire model is reproducible from repository sources, which `ADR-0012`
requires.

## Consequences

### Positive

- One internal representation, so every consumer sees the same semantics.
- New consumers become cheap: a projection, not a pipeline.
- Validation and semantic linking happen once, at a defined stage, rather than
  being re-implemented per output.
- **Agent Context becomes a first-class consumer.** For a system whose primary
  users are AI agents, this is the point: the agent reads a compiled model, not
  a pile of prose it must re-derive on every session.
- It gives `ADR-0012`'s authoritative-versus-derived distinction a precise
  meaning — derived means "produced by this pipeline".

### Negative

- **A compiler is a serious engineering commitment.** Parser, normalizer,
  validator, semantic linker and an internal representation are real software
  with real maintenance, in a project whose value is the methodology. There is a
  genuine risk that the compiler becomes the project and the methodology
  stagnates. Complexity must be added only when a consumer demands it.
- The canonical model needs a schema, and that schema needs versioning
  (`ISSUE-0007`). A change to it invalidates every derived artifact.
- Every authoritative artifact type must be parseable, which constrains
  authoring formats. Free-form prose that carries meaning no parser can reach is
  knowledge the compiler cannot see.
- The relationship between `model/` and the canonical model is **not settled by
  this ADR** and is a live ambiguity — `ISSUE-0034`.

### Neutral

- Nothing here requires the compiler to be written soon. The principle
  constrains design; the implementation arrives with M2 and later.

## Compliance

No consumer parses authoritative assets directly — every consumer reads the
canonical knowledge model. The documentation website has no privileged status in
the pipeline, and no feature is added to the model solely because the website
needs it.
