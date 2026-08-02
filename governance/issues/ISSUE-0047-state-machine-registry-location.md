---
id: ISSUE-0047
title: Where the State Machine Registry lives, and how it relates to KNOWLEDGE-MANIFEST.yaml
type: question
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0027-state-machine-registration-model.md
  - governance/adr/ADR-0013-three-manifests-by-responsibility.md
resolved-by: null
---

# ISSUE-0047 — Where the State Machine Registry lives

## Statement

`ADR-0027` establishes a State Machine Registration Model and makes the registry
the source of truth. It does not say where the registry lives.

`ADR-0013` already assigns "state machines" to `KNOWLEDGE-MANIFEST.yaml`, among
ontology modules, vocabularies, bounded contexts, capabilities and invariants.

Whether these are the same thing, or whether the manifest merely points at a
separate registry, is undefined.

## Why it matters

Both are M2 deliverables. Two artifacts claiming the same content is the
duplication failure that `ADR-0016` and the artifact taxonomy exist to prevent,
and the project has already hit it twice — `ISSUE-0018` and `ISSUE-0035`.

It also interacts with `ADR-0025`'s rule that `shared/vocabularies/` is grouped
by state machine. If the registry owns the vocabulary field, then
`shared/vocabularies/` and the registry overlap too, and there would be three
candidate homes for one piece of content.

## Options

- **The registry *is* the state machines section of `KNOWLEDGE-MANIFEST.yaml`.**
  One artifact, no duplication. But the manifest is a *manifest* — a declaration
  of composition — and nine-field registrations with transition rules may be too
  heavy to sit inside it.
- **A separate registry, declared from `KNOWLEDGE-MANIFEST.yaml`.** Mirrors how
  `MANIFEST.yaml` declares the other manifests (`ADR-0013`). Keeps the manifest
  light and the registry expressive. Adds one indirection.
- **The registry lives in `shared/vocabularies/`,** since `ADR-0025` already
  groups vocabularies by state machine. Natural for the vocabulary field, wrong
  for owner, governed entity and related workflows, which are not vocabulary.

The second is the most consistent with existing structure, but it has not been
decided.

## A related sub-question

`ADR-0027` says the same mechanism serves Engineering OS and every adopting
repository. If the registry sits inside `KNOWLEDGE-MANIFEST.yaml`, an adopter
declares its domain state machines in the same file as the framework's — which
may be correct, or may need a distinction between framework-owned and
domain-owned registrations.

## Resolution criteria

An ADR naming the registry's location, its relationship to
`KNOWLEDGE-MANIFEST.yaml` and to `shared/vocabularies/`, and how framework-owned
and adopter-owned registrations are distinguished.
