---
id: ADR-0012
title: Engineering OS is an executable framework with a typed artifact taxonomy
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0005]
related: [ADR-0011, ADR-0013, ISSUE-0028, ISSUE-0032, ISSUE-0033]
---

# ADR-0012 — Executable framework with a typed artifact taxonomy

## Context

`ISSUE-0005` recorded that nothing stated whether this repository ships
executable code, only specifications. `ADR-0009` had already made the question
urgent by requiring build pipelines, documentation generators, validation
configuration, and manifest sections generated rather than hand-maintained —
none of which is achievable by specification alone.

## Decision

**Engineering OS is not a documentation project. It is an executable
engineering framework.**

Build pipelines, validators, generators, analyzers and visualizers are
**first-class code artifacts**, not tooling incidental to the real work.

### Generated artifacts are never sources of truth

The authoritative artifacts are always the repository assets themselves. A
derived artifact may be deleted and rebuilt at any time without loss.

### Determinism

Every executable pipeline must be **deterministic**: given the same
authoritative inputs, it must always produce the same outputs.

This constrains the compilation pipeline of `ADR-0011`. It does **not** describe
agent-executed engineering work, which is not deterministic. Where that boundary
falls is unresolved — `ISSUE-0033`.

### Artifact taxonomy

The repository explicitly distinguishes four kinds of artifact:

| Kind | Authored by | In version control | Deletable |
|---|---|---|---|
| **Authoritative** | Humans (and agents, under review) | Yes | No — it is the source |
| **Derived** | Deterministically generated | Decided per artifact | Yes, rebuildable |
| **Runtime** | Produced during execution | No | Yes, temporary |
| **Cached** | Produced to avoid recomputation | No | Yes, rebuildable |

This becomes a closed vocabulary in `shared/vocabularies/` (M2).

### Every generated artifact declares

- its authoritative inputs
- the generator that produced it
- whether it is reproducible
- whether it is safe to delete and regenerate

### Continuous verification

The build pipeline is responsible for **continuously verifying that derived
artifacts remain synchronized with their authoritative sources**.

Wherever possible, manifests are validated or partially generated from
repository inspection rather than relying exclusively on manual maintenance.

## Alternatives considered

**Pure specification, no code.** Rejected. Synchronization between derived and
authoritative artifacts cannot be verified by prose, determinism cannot be
guaranteed by prose, and `ADR-0009` already requires generated manifest
sections. It would also make `ADR-0011`'s compiler impossible.

**Schemas plus thin convenience scripts.** Rejected as insufficient: a compiler
with parsing, normalization, validation and semantic linking is not a thin
script, and pretending otherwise would produce an under-designed pipeline that
grows without an architecture.

**Executable, but with generated artifacts treated as authoritative** — for
example, editing a generated index directly when it is faster. Rejected
explicitly: it destroys reproducibility and makes the authoritative source a
lie. This is the failure the taxonomy exists to prevent.

## Consequences

### Positive

- **Drift becomes mechanically detectable** rather than a matter of vigilance.
  This is the general solution to `ISSUE-0028`: the issue index, and any other
  hand-maintained index, becomes a derived artifact.
- The authoritative-versus-derived split matches the `generated` assertion
  status inherited from the prototypes, which already held that generated
  artifacts are not authoritative by themselves. The methodology and its own
  implementation now agree.
- Deletability and reproducibility become declared properties, so a contributor
  never has to guess whether a file may be regenerated.

### Negative

- **This repository now needs a language, a toolchain, dependency management and
  CI — none of which exist, and none of which are chosen.** `ISSUE-0032`. Until
  that is decided, "executable" is a commitment without an implementation.
- **Determinism is a strong claim for a framework built around AI agents.** The
  compilation pipeline can be deterministic; agent-produced artifacts cannot.
  If that boundary is drawn wrongly the requirement becomes either unenforceable
  or a straitjacket — `ISSUE-0033`.
- Maintenance burden: every generator is code that can rot, and every derived
  artifact is a sync obligation.
- Deciding which derived artifacts belong in version control is a real trade
  (reviewability versus churn) and is not settled here.

### Neutral

- `runtime` and `cached` artifacts are excluded from version control by
  definition, which will require `.gitignore` entries once paths exist.

## Compliance

Every derived artifact declares its inputs, generator, reproducibility and
deletability. No derived artifact is ever edited by hand. The build pipeline
fails when a derived artifact is out of sync with its authoritative sources.
