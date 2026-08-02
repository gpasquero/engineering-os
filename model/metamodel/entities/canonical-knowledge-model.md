---
id: METAMODEL-CanonicalKnowledgeModel
title: CanonicalKnowledgeModel
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0047, ADR-0052, ADR-0072, ADR-0076]
---

# CanonicalKnowledgeModel

**The semantic content a set of authoring sources asserts.** The product
(`ADR-0072`).

## What new semantics does this introduce?

**Closure.** It is the only entity that denotes *the whole of what is known* in a
scope, rather than one thing that is known.

Every other entity names a part. Nothing else can be the subject of *this model
conforms to that metamodel*, *this model is deterministic*, or *this model is
compatible with the previous one*.

## Why this is Layer A and not compiler architecture

`ADR-0053` states the metamodel contains no compiler concepts, and `ADR-0076`
supplies the test that decides which side a concept falls on:

> **A concept is a compiler concept only if it is meaningless without a
> compiler.**

**The compiler does not invent this model. It materialises it.** The meaning
exists in the sources whether or not anything reads them. `Compiler`,
`Compiler Phase`, `Projection` and `ValidationResult` all fail the test and are
correctly relocated; this one passes.

`ADR-0047` had already settled it: the **Semantic Representation** is one of the
three Knowledge Representations, and this is that representation.

## identity

The pair of **scope and the resolved assertion set**. Two models are the same
model when they contain the same nodes and edges over the same scope — **not when
they were produced by the same run.**

## version

Two versions, and they are independent:

| Version | Of |
|---|---|
| **format version** | the serialization contract consumers depend on |
| **metamodel version** | the Layer A vocabulary the model conforms to |

A model states both. Neither is a compiler version: **the compiler is not part of
the model's identity.**

## provenance

Every node records the source that asserted it. Provenance is carried *by the
model*, not remembered outside it — which is what makes *why is this here?*
answerable without the sources.

## determinism guarantees

> **Identical input produces an identical model.**

Concretely: node order, edge order and diagnostic order are stable; no timestamp,
path outside the project, or environment value enters the model. **A model
carries nothing that cannot be recomputed from its nodes and edges.**

This is checked, not asserted — every passing regression fixture compiles twice
and compares (`ADR-0073`).

## invariants

1. **Every edge was asserted.** Nothing is inferred (`ADR-0044`, `ADR-0061`).
2. Every node's type is a declared metamodel entity.
3. Every predicate specializes a registered core type (`ADR-0071`).
4. Every edge endpoint resolves to a node in the model.
5. Every identifier is unique within the model.

Violating any of these is not a model.

## serialization independence

**JSON, OWL, Mermaid and HTML are projections of the model. None of them is the
model.**

The same distinction `ADR-0045` drew about front matter and `ADR-0066` drew about
edges. Third instance, and it is now the load-bearing one: a consumer reading the
JSON is reading a rendering, and a future encoding changes nothing semantic.

## compatibility policy

| Change | Compatible? |
|---|---|
| adding a node, edge or statistic | yes |
| adding an optional field | yes |
| removing or renaming a field | **no** — format version increments |
| changing an existing field's meaning | **no** |
| a new metamodel entity or core relationship type | yes, metamodel version increments |

## ownership

Owned by the repository whose sources produced it. **A model is never authored**
— authoring produces sources, and the model is what they mean.

## lifecycle owner

**None.** A model is not revised; a new one is produced. It is the second entity
with no lifecycle after `AcceptanceRecord`, and for a related reason: **it is a
statement about a moment, not a thing that changes.**

## authoritative representation

None of its own — the point of serialization independence. The authoritative
*sources* are Markdown; the model is their meaning; every encoding is derived.

## derived representations

JSON · OWL · Mermaid graphs · the Knowledge Explorer · registry projections ·
every future generator.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| contains | any Layer B node | zero or more |
| derives-from | Artifact | one or more, its sources |
| instantiates | the metamodel | exactly one |
| represents | Vocabulary | zero or more, the core types it carries |

## extension points

An adopting repository adds emitters. **It does not extend what a model is** —
extending that is a metamodel change and a format version increment.

## Debt

**Provenance records a path, not a revision.** `ADR-0064` defines identity as
`(artifact-id, revision-id)` and the compiler carries only the source filename.
The Explorer's provenance query states this gap rather than hiding it.

**Scope is undefined.** Identity is *scope and assertion set*, and nothing says
what determines a scope — today it is "whatever is in `model/*.md`". `Manifest`
is the entity that would answer it (`ADR-0075`).

**No model has ever been compared to another.** The compatibility policy is
written and unexercised; nothing computes a diff between two models.
