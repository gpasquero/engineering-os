---
id: EXAMPLE-TINY
title: Tiny end-to-end example
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: B
artifact-kind: authoritative
established-by: [ADR-0062]
---

# Tiny end-to-end example

**The first running Engineering OS pipeline.** Thirteen nodes, compiled from
Markdown into a Canonical Knowledge Model and four projections.

> Built deliberately before B1 was complete. The objective is to validate the
> whole pipeline as early as possible, **even crudely** — every remaining design
> decision is easier once something runs end to end.

## Run it

```sh
python3 tools/compile.py examples/tiny
```

```text
[metamodel] 20 entity types, 67 registered predicates
[discover]  13 authoring sources
[parse]     13 nodes
[resolve]   OK — 16 edges, all types and predicates valid
[emit]      canonical-knowledge-model.json, model.ttl, graph.md, explorer.html
```

## What it contains

`model/` is a **Layer B model expressed in the Layer A metamodel** — a trivial
sales domain plus the governance records around it.

| Node | Metamodel type | Family |
|---|---|---|
| Sales | BoundedContext | descriptive |
| Order | Concept | descriptive |
| Customer | Actor | descriptive |
| Place an order | Capability | descriptive |
| Payment before shipping | Invariant | descriptive |
| Checkout service | Artifact | descriptive |
| Checkout service r2 | ArtifactRevision | descriptive |
| Validate an order | Skill | operational |
| Checkout | Workflow | operational |
| Checkout step 1 | WorkflowStep | operational |
| Should payment be synchronous? | Issue | operational |
| Verify payment synchronously | ADR | operational |
| Acceptance of r2 | AcceptanceRecord | operational |

## What it produces

| Output | What it is |
|---|---|
| `build/canonical-knowledge-model.json` | The Canonical Knowledge Model — nodes, typed edges, statistics |
| `build/model.ttl` | OWL, importing the metamodel ontology |
| `build/graph.md` | A Mermaid graph, coloured by family |
| `build/explorer.html` | A navigable Knowledge Explorer, self-contained |

**All four are derived** (`ADR-0012`). Do not edit them; edit `model/` and
recompile.

## Why this is a compiler and not a converter

Phase 3 reads `model/metamodel/` to learn which entity types exist and which
predicates are registered, then **rejects a model that violates them.**

Breaking the example three ways produces:

```text
[resolve]   FAILED — 3 error(s):
    adr-0001.md: 'resolves' points at unknown node 'Issue.9999'
    concept-order.md: 'Blorp' is not a metamodel entity
    concept-order.md: predicate 'invented-predicate' has no registered parent (ADR-0071)
```

**The metamodel is now load-bearing.** For twenty-five sessions it was
a description of a language nothing spoke. It is now the rulebook a
program executes.

## What the example demonstrates on purpose

**`Invariant.PaymentBeforeShipping` has no `enforced-at`.** The invariant is
stated and nothing records where it is enforced. That is the zero-cardinality
case `invariant.md` argued for: **the gap is the finding**, and the compiler
carries it rather than rejecting it.

**`WorkflowStep.Checkout.1` holds the position, not the Skill.** `ADR-0068` in
one node: the ordering lives on the reified association, and both surrounding
relationships are ordinary.

**`Artifact.CheckoutService` has an active revision; the Artifact has no state.**
`ADR-0026` and `ADR-0064` are visible in the graph rather than only asserted.

**Every edge carries its core relationship type and category.** The explorer
groups relationships as structural, behavioral, semantic and traceability
(`ADR-0071`) — which is what having a vocabulary buys.

## What is missing

No acceptance is enforced, no lifecycle state is checked, no dimension is
assigned, no `Principle` is extracted, and nothing is validated beyond type and
predicate resolution. The compiler has four phases where `ADR-0014` describes
more.

**Crude, and running.**
