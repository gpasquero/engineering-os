---
id: ADR-0006
title: Separate the product layer from the model artifact layer
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0004, ISSUE-0004, ISSUE-0014]
---

# ADR-0006 — Separate the product layer from the model artifact layer

## Context

The inherited design documents describe two different directory trees without
ever distinguishing them:

- `governance/design/proposed-architecture.md` describes a seven-directory tree
  (`shared/`, `skills/`, `workflows/`, `templates/`, `schemas/`, `validation/`,
  `tests/`) — the methodology itself.
- `imports/reconstruct-system-knowledge/references/repository-structure.md`
  describes a fifteen-directory `model/` tree (`ontology/`, `domain/`,
  `traceability/`, `specs/`, …) — the artifacts the methodology *produces*.

Both are called "the repository structure". This conflation is the root cause of
several downstream defects: `ontology-driven-development` writes to
`model/changes/<change-id>/`, a path absent from the canonical `model/` tree
(`ISSUE-0014`), and template paths are stated relative to the skill while output
paths are stated relative to the target repository, with no resolution rule
(`ISSUE-0015`).

## Decision

The two trees are named, separated, and never mixed.

**Layer A — the product.** This repository. The methodology: contracts,
policies, skills, workflows, schemas, tests.

**Layer B — the model.** The `model/` tree the methodology produces *inside a
target repository*.

Consequently:

1. This repository contains **`model-spec/`** — the specification and a copyable
   scaffold of the Layer B tree — and **never a live `model/` directory**.
2. Every path in every skill declares which layer it is relative to. The
   resolution rule is owed to M2 (`ISSUE-0015`).
3. Where the Layer B tree lives for a given target system — in-repo, sibling
   repository, or centralized for multi-repo systems — is a separate question,
   recorded as `ISSUE-0004` and deliberately not decided here.

## Alternatives considered

**One tree, with `model/` as a subdirectory of this repository.** Rejected: this
repository would then contain a knowledge model of itself intermixed with the
methodology, and the scaffold shipped to users would be indistinguishable from
our own working artifacts.

**Ship only prose describing the model tree, with no scaffold.** Rejected:
every application of the methodology would re-derive the structure by hand and
drift, which is precisely the failure the three prototypes already exhibit
against each other.

**Decide the Layer B location now** (in-repo `model/` in the target). Tempting,
since all three prototypes assume it. Rejected: multi-repository systems are a
plausible target and the prototypes never considered them. Assuming here would
violate the rule against assuming, so it is recorded as `ISSUE-0004` instead.

## Consequences

### Positive

- Removes the repository's central structural ambiguity.
- Makes "what does the Engineering OS produce" answerable by pointing at one
  directory.
- The scaffold becomes a versioned artifact that can be validated.

### Negative

- Requires vocabulary discipline: every document must be explicit about which
  layer a path belongs to, and reviewers must catch violations by hand until
  M9.
- This repository cannot dogfood the methodology on itself without a decision
  on `ISSUE-0004`.

### Neutral

- The fifteen-directory tree from the prototype is adopted as the starting
  point for `model-spec/`, pending reconciliation with `model/changes/`
  (`ISSUE-0014`).

## Compliance

No directory named `model/` exists at the root of this repository. Every skill
path declaration names its layer. `model-spec/` is the single definition of the
Layer B tree.
