---
id: ADR-0076
title: The Canonical Knowledge Model is a Layer A entity, and a concept is a compiler concept only if it is meaningless without a compiler
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0047, ADR-0052, ADR-0053, ADR-0072, ADR-0073]
---

# ADR-0076 — The Canonical Knowledge Model is Layer A

## Context

`ADR-0072` made the Canonical Knowledge Model the primary product. The direction
now is to give it **its own Layer A specification** — identity, version,
provenance, determinism guarantees, invariants, serialization independence,
compatibility policy.

**This appears to contradict `ADR-0053`**, which states that the metamodel
contains no compiler concepts, and under which four concepts were relocated out
of the Layer A inventory: `Compiler`, `Projection`, `RegistryProjection`,
`ValidationResult`.

The Canonical Knowledge Model appears in the compilation hierarchy
(`ADR-0052`). If that makes it a compiler concept, it cannot be a Layer A
entity, and the direction and the decision are incompatible.

## The test

They are compatible, and the reason generalises:

> **A concept is a compiler concept only if it is meaningless without a
> compiler.**

Applied:

| Concept | Meaningful with no compiler? | Where it belongs |
|---|---|---|
| **Canonical Knowledge Model** | **yes** — it is the meaning the sources assert, whether or not anything materialises it | **Layer A** |
| Compiler | no | compiler architecture |
| Compiler Phase | no | compiler architecture |
| Projection | no — derivation requires a deriver | compiler architecture |
| ValidationResult | no — a result requires an execution | compiler architecture |

**The compiler does not invent the Canonical Knowledge Model. It materialises
it.** That a Skill produces an Artifact does not make Artifact a Skill concept,
and the same reasoning applies here.

`ADR-0047` had already settled this without anyone noticing: the **Semantic
Representation** is one of the three Knowledge Representations, and the
Canonical Knowledge Model *is* the Semantic Representation. It has been a Layer A
concept since `ADR-0047` and was listed nowhere.

## Decision

**`CanonicalKnowledgeModel` is a Layer A descriptive entity**, specified in
`model/metamodel/entities/`.

It declares seven things:

| Declares | States |
|---|---|
| **identity** | what makes one model the same model as another |
| **version** | the metamodel version it conforms to |
| **provenance** | which sources, at which revisions, produced it |
| **determinism guarantees** | what is identical across runs given identical input |
| **invariants** | what must hold of any valid model |
| **serialization independence** | that JSON, OWL and any future encoding are projections of it, not it |
| **compatibility policy** | what may change without breaking consumers |

**`ADR-0053` is not amended.** The relocations it caused remain correct, and this
decision supplies the test that shows *why* they were correct — which the ADR
itself did not state.

## Alternatives considered

**Keep the Canonical Knowledge Model as an implementation artifact.** Rejected:
it is the declared product (`ADR-0072`), and the product having no specification
while twenty entities that are not the product have one is indefensible.

**Amend or supersede `ADR-0053`.** Rejected, and this was the tempting move. The
boundary it draws is right; what was missing was a stated criterion for which
side a concept falls on. Superseding it would have discarded a correct decision
to fix an unstated rationale.

**Put the Canonical Knowledge Model in the compilation hierarchy only.**
Rejected. `ADR-0052` describes how artifacts flow through compilation; it is not
a home for the concept, any more than `ArtifactRevision` lives in the lifecycle
that governs it.

## Consequences

### Positive

- **The test is reusable and retroactively validates four relocations** that were
  made on judgement.
- The product gets a specification, which is where its determinism guarantees and
  compatibility policy can be stated once rather than per-tool.
- **Serialization independence becomes explicit.** The JSON on disk is not the
  model, which is the same distinction `ADR-0045` made about front matter and
  `ADR-0066` made about edges. Third instance of one pattern.

### Negative

- **The metamodel grows by one entity** in a session whose stated priority is
  compiler evolution over metamodel completion. Justified under `ADR-0075` — the
  compiler needs this entity, and it needs it more than the four already queued.
- The line will be tested again. `ValidationRule` is meaningful without a
  compiler; `ValidationResult` is not; **and they differ by one word.**

### Neutral

- Entity count 26 → 27.

## Compliance

`model/metamodel/entities/canonical-knowledge-model.md` declares the seven
fields. New candidate entities state whether they are meaningful without a
compiler.
