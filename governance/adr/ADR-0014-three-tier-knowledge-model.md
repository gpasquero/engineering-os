---
id: ADR-0014
title: Engineering OS is a knowledge compiler over a three-tier knowledge model
status: accepted
date: 2026-08-02
supersedes: ADR-0011
superseded-by: null
resolves: [ISSUE-0034]
related: [ADR-0012, ADR-0015, ADR-0016, ISSUE-0029]
---

# ADR-0014 — Knowledge compiler over a three-tier knowledge model

**This is the foundational architectural principle.** It governs the design of
generators, validators, visualizers, plugins and every future extension
mechanism. It supersedes `ADR-0011`, which stated the compiler principle without
distinguishing the tiers, leaving `model/` ambiguous between source and output.

## Context

`ADR-0011` established Engineering OS as a knowledge compiler producing a
canonical knowledge model. `ADR-0010` established `model/` as the repository's
knowledge model.

`ISSUE-0034` recorded that these admit two incompatible readings: either
`model/` is authoritative input and the canonical model is a build output, or
`model/` *is* the compiled output. `model-spec/` could not be designed until the
question was settled, because a source tree and a compiler output tree have
different structures, different version-control policies and opposite editing
rules.

## Decision

**Repository assets are the authoritative source of knowledge. The canonical
knowledge model is a derived artifact produced by the Knowledge Compiler.**

```text
Repository Assets  (authoritative)
        ↓
Knowledge Compiler  (deterministic)
        ↓
Canonical Knowledge Model  (derived, internal representation)
        ↓
Derived Artifacts  (projections)
```

Three tiers, explicitly distinguished:

### 1. Authoritative Knowledge Model — the repository assets

Human-authored knowledge describing the domain. `model/` belongs here. It
contains ontology source, glossary, invariants, workflows, capabilities,
specifications, ADR references and traceability metadata.

Artifact kind: **`authoritative`**. Never generated. Always human-readable.

### 2. Canonical Knowledge Model — the compiler's internal representation

**Never edited by humans.** It is a compilation product.

It may be persisted, to support incremental compilation, validation, search or
visualization, but it is **always reproducible** from the authoritative assets.

It lives under generated artifacts and **never inside `model/`**. The exact
serialization is an implementation decision.

Artifact kind: **`derived`**.

### 3. Derived Artifacts — the projections

Website, indexes, knowledge graph projections, reports, caches, agent context.
Produced *from the canonical model*, never directly from the authoritative
assets.

## What survives from ADR-0011

Everything except the ambiguity. The compiler framing, the pipeline stages
(parsing, normalization, validation, semantic linking), the rule that no
consumer parses authoritative assets directly, the list of consumers, the
absence of any privileged consumer, and the deferral of intermediate
representations, incremental compilation and caching to implementation — all
carry forward unchanged.

What is added is the tier distinction that makes `model/`'s status
unambiguous.

## Alternatives considered

**Reading B — `model/` is the compiled output.** Rejected. It would leave no
name for the human-authored source, and `ADR-0010`'s ownership language
("knowledge is owned by the repository that owns the domain") describes a source
tree, not a build product. It would also make `model/` unreadable without
running a compiler, which `ADR-0017` forbids.

**Two tiers — authoritative assets and derived artifacts, with no named
canonical model.** Rejected: it is what `ADR-0011` effectively had, and it is
what produced `ISSUE-0034`. Without a named internal representation, every
consumer would either re-parse the assets or depend on some other consumer's
output.

**Canonical model persisted inside `model/`.** Rejected explicitly. It would put
a generated artifact inside the authoritative tree, where a human would
eventually edit it — the precise failure `ADR-0012`'s taxonomy exists to
prevent.

## Consequences

### Positive

- **`model-spec/` is now designable.** It specifies an authoritative source
  tree: human-authored, human-readable, hand-edited by design. M2 is unblocked
  on this axis.
- `model/` is unambiguously `authoritative`; the canonical model is
  unambiguously `derived`. The artifact taxonomy applies cleanly to both.
- Deleting the canonical model is always safe, by construction.
- The three tiers give precise language for a question that was previously
  argued in circles.

### Negative

- A third named tier is a real conceptual cost. Readers must now keep
  `model/` (authoritative), the canonical model (internal, derived) and the
  projections (derived) distinct — and two of the three are derived.
- The canonical model needs a schema and a version (`ISSUE-0007`); changing it
  invalidates every projection.
- Persisting the canonical model for performance blurs it toward `cached`. It
  is `derived` by decision; if it is ever persisted *purely* to avoid
  recomputation, the taxonomy would call that `cached`. This distinction has no
  practical consequence yet and is flagged rather than settled.

### Neutral

- Whether a Knowledge Package (`ISSUE-0029`) exports the authoritative assets or
  a projection of the canonical model is now a sharper question, and is still
  open.

## Compliance

No generated artifact is ever written inside `model/`. The canonical knowledge
model is never hand-edited, and deleting it never loses information. No consumer
parses authoritative assets directly. Every artifact in the repository is
classifiable into exactly one tier.
