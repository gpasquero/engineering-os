---
id: ISSUE-0029
title: Knowledge Package format and federation protocol are undefined
type: question
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M13]
evidence:
  - governance/adr/ADR-0010-repository-local-knowledge-ownership.md
resolved-by: null
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

## Resolution criteria

A Knowledge Package specification and a federation protocol, recorded by ADR.
Until then, M2 decisions that could constrain federation must say so explicitly.
