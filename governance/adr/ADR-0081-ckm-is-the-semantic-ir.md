---
id: ADR-0081
title: The Canonical Knowledge Model is the platform's semantic intermediate representation
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0014, ADR-0047, ADR-0052, ADR-0072, ADR-0076, ADR-0080]
---

# ADR-0081 — The Canonical Knowledge Model is the semantic IR

## Context

`ADR-0072` made the Canonical Knowledge Model the product. `ADR-0076` made it a
Layer A entity. What neither states is **what it must become**:

> **Do not let the Canonical Knowledge Model become merely a serialized graph.**

Today it is a JSON file with nodes, edges and statistics — one compiler's output,
consumed by four emitters that all belong to the same program.

## Decision

**The Canonical Knowledge Model is the semantic intermediate representation of
the entire platform** — the equivalent of an IR in a compiler architecture.

**Every future component is designed as a producer or a consumer of the CKM.**

```text
                    Compiler
                       │
                       ▼
        ┌──────── Canonical Knowledge Model ────────┐
        │                                           │
   Knowledge Explorer      AI agents        Impact analysis
   Architecture review     Migration planning
   Specification generation    Test generation
   Documentation           Visualizations       Code generation
```

**Eventually even code generation consumes the CKM rather than source documents
directly.**

### What this forbids

**No component rebuilds semantic understanding independently.** A generator that
re-parses Markdown, a reasoner that re-derives relationships, an agent that reads
the sources — each is a second implementation of meaning, and the second one is
always wrong eventually.

This is the same failure `ISSUE-0037` records for projections, one level up: a
component with its own semantic model is a projection with no model behind it.

### What an IR must be that a serialized graph need not

| Property | Why an IR needs it |
|---|---|
| **self-describing** | a consumer needs no access to the metamodel to interpret it |
| **stable and versioned** | consumers depend on a contract, not on a producer |
| **losslessly traversable** | every relationship navigable in both directions |
| **provenance-carrying** | every assertion traceable to its source |
| **queryable** | consumers ask; they do not scan |
| **serialization-independent** | JSON is one encoding, not the representation |

The model already satisfies self-description — it carries the relationship
vocabulary its edges use. **The rest is the work this decision commits to.**

## Alternatives considered

**Leave the CKM as compiler output.** Rejected: it makes every future consumer
build its own understanding, and guarantees divergence.

**Define a query API first and let the CKM follow.** Rejected as inverted. The
API is a consumer; designing the representation around its first consumer is how
an IR becomes one tool's data structure.

**Adopt an existing IR — RDF, a property graph, a triple store.** Rejected for
now, and this is the closest call. Each brings tooling and each binds the
representation to a formalism, which `ADR-0066`, `ADR-0068` and `ADR-0077` all
rejected in the analogous case. **The CKM may compile *to* any of them.**

## Consequences

### Positive

- **It gives every future component a defined interface**, so agents, generators
  and analyses compose instead of duplicating.
- It makes the compatibility policy in `canonical-knowledge-model.md` load-
  bearing rather than aspirational — consumers now exist to break.
- **It is what makes Engineering OS a platform rather than a documentation
  framework**, which is `ADR-0080`'s objective expressed structurally.

### Negative

- **An IR is a commitment to stability that the model has not earned.** Its
  format version is `1.0.0` on thirteen example nodes, and the first real
  consumer will demand changes.
- **Queryability does not exist.** Consumers scan lists today. Nothing in the
  model supports indexed or transitive access, and the Explorer computes closures
  in the browser — which will not scale and nobody knows where it stops.

### Neutral

- No existing component changes. What changes is how the next one is designed.

## Compliance

A new component declares whether it produces or consumes the Canonical Knowledge
Model. **No component parses authoring sources except the compiler.**
