---
id: ISSUE-0030
title: MANIFEST.yaml serves both this repository and every adopting repository
type: question
status: resolved
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0009-manifest-is-the-root-composition-manifest.md
  - governance/adr/ADR-0010-repository-local-knowledge-ownership.md
resolved-by: ADR-0013
---

# ISSUE-0030 — `MANIFEST.yaml` serves two audiences

## Statement

`ADR-0009` defines `MANIFEST.yaml` as the root manifest of *an Engineering OS
project*. `ADR-0010` establishes that every repository adopting Engineering OS
owns its own knowledge model.

Together these imply that **every adopting repository has a `MANIFEST.yaml`**,
and that this repository has one too — but the two are not obviously the same
kind of document.

This repository *authors* the methodology: it has `skills/`, `workflows/`,
`shared/`, `model-spec/`, extension points and plugin registrations to declare.
A banking system *consumes* it: it declares which modules it enables, which
ontology modules it owns, and which artifacts are authoritative versus
generated.

Whether one schema covers both, and how, is undefined.

## Why it matters

`MANIFEST.yaml` and its schema are M2 deliverables. Building for one audience
and discovering the other was meant is an expensive correction, because
everything downstream is discoverable from this file.

## Options

- **One schema, all sections optional.** Simple, single source. Risks a schema
  so permissive it validates almost nothing.
- **One schema with a declared project kind** (`framework` versus `adopter`),
  with per-kind required sections. Keeps one file format while allowing real
  validation. Most likely correct.
- **Two schemas.** Clearest per-audience validation; duplicates every shared
  section and invites drift — the failure recorded in `ISSUE-0018`.
- **Core schema plus extensions**, where authoring sections are an extension of
  the adopter schema.

## Resolution

`ADR-0013` — **neither one nor two, but three.** The question had the wrong
axis: the problem is not *audience*, it is **responsibility and lifecycle**.

- `MANIFEST.yaml` — architectural. Stable, changes rarely.
- `BUILD-STATE.yaml` — implementation state. Changes continuously.
- `KNOWLEDGE-MANIFEST.yaml` — knowledge model. Changes when semantics change.

The decisive argument is rate of change: binding content that changes yearly to
content that changes hourly is how a manifest becomes a source of architectural
drift rather than a defence against it.

The audience question dissolves — an adopting repository has the same three
manifests, leaving unused sections empty.

Opened by this answer: `ISSUE-0035` (`BUILD-STATE.yaml` overlaps `governance/`).
`ISSUE-0031` is compounded, because `KNOWLEDGE-MANIFEST.yaml` lists glossary
modules while the glossary lives in `governance/`.
