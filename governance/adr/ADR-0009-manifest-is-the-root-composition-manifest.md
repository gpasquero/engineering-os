---
id: ADR-0009
title: MANIFEST.yaml is the root composition manifest of an Engineering OS project
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0003]
related: [ISSUE-0005, ISSUE-0007, ISSUE-0030, ADR-0010]
---

# ADR-0009 — `MANIFEST.yaml` is the root composition manifest

## Context

The inherited roadmap named `MANIFEST.yaml` as a headline deliverable without
describing it. `ISSUE-0003` recorded four candidate readings — registry, version
lock, capability index, distribution manifest — and blocked M2, because the
artifact cannot be built from a filename.

## Decision

`MANIFEST.yaml` is the **root manifest of an Engineering OS project**. It
describes the architecture and composition of that project.

It is explicitly **not** a dependency lock file, a package-manager manifest, or
a distribution descriptor.

The analogy is `package.json` or `Cargo.toml` — but for Engineering OS
composition rather than source-code dependencies.

It defines:

- repository metadata
- Engineering OS version
- enabled modules
- authoritative artifacts
- generated artifacts
- build pipelines
- ontology modules
- documentation generators
- workflow catalog
- skill catalog
- extension points
- plugin registrations
- artifact ownership
- repository capabilities
- validation configuration

**Governing property: everything else in the repository is discoverable from
`MANIFEST.yaml`.** It is the machine entry point, as `governance/` is the entry
point for a human or agent reconstructing context.

Every repository adopting Engineering OS has one, including this repository
(`ADR-0010`).

## Alternatives considered

The four readings recorded in `ISSUE-0003`:

**Dependency lock file.** Rejected explicitly. Engineering OS composition is not
a dependency graph of third-party packages, and conflating the two would import
package-manager semantics that do not apply.

**Capability index only.** Rejected as too narrow: it covers `repository
capabilities` but none of the artifact-ownership, pipeline or validation
concerns.

**Distribution manifest.** Rejected: distribution is an adapter concern
(`ADR-0007`) and belongs in `adapters/`, not at the root.

**Registry only.** Rejected as too narrow, though closest: a registry enumerates
skills and workflows but does not express the authoritative-versus-generated
distinction or artifact ownership.

## Consequences

### Positive

- M2 is unblocked, and the first schema in `schemas/` has a clear target.
- Machine discoverability becomes a stated property rather than an accident.
- The `authoritative artifacts` versus `generated artifacts` split is expressed
  structurally, matching the epistemic rule inherited from the prototypes that
  generated artifacts are not authoritative by themselves.
- `artifact ownership` gives write-scope enforcement (`ISSUE-0021`) somewhere to
  anchor.

### Negative

- **Fifteen concerns in one file is a large surface**, and this file must stay
  in sync with the filesystem it describes. That is precisely the drift failure
  recorded in `ISSUE-0028` for the issue index, at a larger scale and with worse
  consequences: a stale manifest would misreport what the repository contains.
  Wherever a section can be derived from the filesystem it should be **generated
  or validated**, not hand-maintained. This must be settled in M2, not deferred.
- Risk of the manifest becoming a god-file that accumulates every unresolved
  concern. Sections should be added by ADR, not by convenience.
- `build pipelines` and `documentation generators` imply executable tooling,
  which bears directly on `ISSUE-0005` — that issue is now strongly informed and
  should be resolved before or during M2.

### Neutral

- Versioning of the manifest itself, and of the components it lists, depends on
  `ISSUE-0007`.
- Whether one schema serves both this repository and adopting repositories is
  newly open — `ISSUE-0030`.

## Compliance

Every artifact directory in the repository is reachable from `MANIFEST.yaml`. A
directory that exists but is not discoverable from the manifest is a defect.
Sections derivable from the filesystem are generated or validated, never
hand-maintained without a check.
