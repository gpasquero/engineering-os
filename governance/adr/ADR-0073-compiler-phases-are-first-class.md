---
id: ADR-0073
title: Compiler phases are first-class and every feature declares its contract
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0014, ADR-0053, ADR-0061, ADR-0072]
---

# ADR-0073 — Compiler phases are first-class

## Context

The first pipeline **revealed its own stages** rather than having them designed:

```text
Authoring → Discovery → Parsing → Resolution → Canonical Knowledge Model → Projection
```

They exist today as four function names in one file. Left implicit, every future
feature couples to whatever the implementation happens to do.

## Decision

**The six stages are first-class compiler phases.**

| Phase | Consumes | Produces |
|---|---|---|
| **Authoring** | human intent | authoring sources |
| **Discovery** | authoring sources | a source set |
| **Parsing** | a source set | assertions |
| **Resolution** | assertions | a resolved assertion set |
| **Canonical Knowledge Model** | resolved assertions | the semantic model |
| **Projection** | the semantic model | derived artifacts |

**Authoring is a phase and the compiler does not execute it.** Naming it matters:
it is where Interpretive Discovery happens (`ADR-0060`), and the boundary between
it and Discovery is the boundary between judgement and mechanism.

### Every compiler feature declares its contract

Four fields, mandatory:

| Field | States |
|---|---|
| **input phase** | which phase's output it consumes |
| **output phase** | which phase's output it contributes to |
| **invariants** | what must hold for the feature to be correct |
| **determinism guarantees** | what is guaranteed identical across runs given identical input |

**A feature that cannot state its determinism guarantee does not have one.**

### Phases are compiler architecture, not metamodel

`ADR-0053` holds: the semantic architecture is separate from the compiler
architecture, and **the metamodel contains no compiler concepts.** These phases
are declared in the compiler, not in `model/metamodel/`. `Compiler Phase` was
already relocated out of the Layer A inventory for exactly this reason, and was
already expected to fail a Dimension Review on the same grounds.

## Alternatives considered

**Leave the phases as implementation structure.** Rejected — the reason for the
decision. Implicit stages become implicit coupling.

**Model the phases as Layer A entities.** Rejected under `ADR-0053`. They would
put compiler concepts in the semantic model, which is the boundary that decision
exists to hold.

**Declare only the four executed phases**, omitting Authoring and treating the
Canonical Knowledge Model as an output rather than a phase. Rejected: omitting
Authoring hides the judgement/mechanism boundary, and collapsing the model into
Projection would make the product a step in producing projections — the exact
inversion `ADR-0072` rejects.

**Add invariants and determinism later.** Rejected. They are cheap to state while
the compiler has four features and expensive to reconstruct once it has forty.

## Consequences

### Positive

- **Extensibility without coupling.** A new feature names the phase it plugs
  into, and phases are the only interface it depends on.
- Determinism becomes a declared property rather than an accident. The current
  pipeline is deterministic and nothing said so until now.
- **It gives the test projects something to test against.** A phase with declared
  invariants is checkable; a function is not.
- The phase boundary is where future concurrency, caching and incremental
  compilation become possible.

### Negative

- **Ceremony on a compiler with four features.** Four fields per feature is
  overhead that pays off later and costs now.
- Some features will straddle phases. Validation in particular is arguably both
  Resolution and Projection, and forcing a single answer may distort it.

### Neutral

- The current pipeline already implements four of the six phases and gains a
  declaration rather than a restructuring.

## Compliance

`tools/compile.py` declares the phases as data, and each feature declares its
four fields. The declaration is printable (`--phases`) so it can be inspected
without reading the implementation.
