---
id: ISSUE-0029
title: Knowledge Package format and federation protocol are undefined
type: question
status: resolved
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M13]
evidence:
  - governance/adr/ADR-0010-repository-local-knowledge-ownership.md
resolved-by: ADR-0019
---

# ISSUE-0029 — Knowledge Package format and federation protocol are undefined

## Statement

`ADR-0010` establishes that knowledge is repository-local and that
multi-repository environments federate rather than share a model. Federation is
to work through versioned **Knowledge Packages** containing a repository's
ontology, graph, glossary, specifications and metadata.

Nothing about the package format or the exchange protocol is defined.

## Why it matters

`ADR-0010` requires that `model-spec/` and `MANIFEST.yaml` — both M2 artifacts —
**must not preclude** federation. That is a design constraint on M2 without a
specification to check it against, which is a real risk: M2 could bake in an
assumption that federation later cannot work around.

It also blocks M13 entirely.

## What we know

- The package is **versioned**, so it has an identity and a compatibility story
  (`ISSUE-0007`).
- It carries ontology, graph, glossary, specifications and metadata.
- Its purpose is to let one repository reference another **without sharing its
  internal source of truth** — so a package is an export, not a mirror, and the
  boundary between what is exported and what stays private is part of the
  design.
- Nothing yet defines resolution (how a repository finds a package), trust (how
  it evaluates one), or staleness (how it knows the package no longer matches
  its source).

## Open sub-questions

- What is exported versus kept private?
- How are cross-package references expressed so they survive versioning?
- How does a consumer detect that a package is stale relative to its source?
- What assertion status does an imported assertion carry? The inherited
  vocabulary has `externally-defined`, but a federated peer is not an external
  standard.
- Does importing a package create a traceability obligation on the consumer?

## Sharpened by ADR-0014

The three tiers give this question a precise form it lacked. A Knowledge Package
is an export of exactly one of:

- **The authoritative assets** — a copy of the source. Simple, but it exports
  unvalidated, unlinked material and forces every consumer to compile it.
- **The canonical knowledge model** — the validated, semantically linked
  representation. Far more useful to a consumer, and consistent with `ADR-0014`'s
  rule that consumers read the compiled model rather than the sources. But the
  canonical model is `derived`, so a package would be a projection of a
  projection, and its version would depend on the compiler version as well as
  the content.
- **A dedicated projection** built for federation specifically, with its own
  stability guarantees.

The second or third is far more likely than the first. Nothing has been decided.

## Resolution

`ADR-0019`. **A Knowledge Package is a published interface between
repositories** — the third option listed above, a dedicated projection.

It **never exports authoritative repository assets**: authoritative knowledge
belongs to its repository and remains editable only there. It exports a stable
projection derived from the Canonical Knowledge Model, and is itself a derived
artifact. Its purpose is interoperability, not editing.

The coupling hazard identified above is answered directly: **the package format
is a stable, versioned specification independent of the compiler
implementation.** Compilers may evolve provided they emit conforming packages,
analogous to different compilers producing binaries that conform to one
published specification. Packages version the specification, the exported
knowledge model and compatibility information — and never expose compiler
internals.

## Original resolution criteria

A Knowledge Package specification and a federation protocol, recorded by ADR.
Until then, M2 decisions that could constrain federation must say so explicitly.
