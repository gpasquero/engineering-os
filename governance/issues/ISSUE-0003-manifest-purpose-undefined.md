---
id: ISSUE-0003
title: The purpose and schema of MANIFEST.yaml are undefined
type: question
status: resolved
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - sources/handoff/ROADMAP.md
  - governance/design/proposed-architecture.md
resolved-by: ADR-0009
---

# ISSUE-0003 — The purpose of `MANIFEST.yaml` is undefined

## Statement

The inherited `sources/handoff/ROADMAP.md` names `MANIFEST.yaml` as a headline artifact of its
first delivery. No document states what it contains, what problem it solves, or
what reads it.

## Why it matters

It is a named M2 deliverable. It cannot be built from a filename. It also
determines the first schema in `schemas/` and interacts with versioning
(`ISSUE-0007`).

## What we know

- `governance/design/proposed-architecture.md` does not list it among the seven
  directories, so it is presumably a root-level file.
- `sources/handoff/BOOTSTRAP.md` requires that "everything must be versioned", which suggests a
  registry role.

## Options

- **Registry** — enumerates skills, workflows and contracts with versions and
  paths. Most consistent with the stated intent.
- **Version lock** — pins compatible versions of components against each other.
- **Capability index** — declares what the OS can do, for discovery by an agent.
- **Distribution manifest** — describes what an adapter packages and installs.

These are not mutually exclusive; the risk is building one and discovering
another was meant.

## Resolution

`ADR-0009`. `MANIFEST.yaml` is the **root composition manifest** of an
Engineering OS project — the equivalent of `package.json` or `Cargo.toml`, but
for Engineering OS composition rather than source-code dependencies. It is
explicitly not a dependency lock file, package-manager manifest or distribution
descriptor.

Governing property: everything else in the repository is discoverable from it.

All four candidate readings above were rejected as too narrow or as the wrong
category. See `ADR-0009` for the fifteen concerns it defines.

Newly opened by this answer: `ISSUE-0030` (does one schema serve both this
repository and adopting repositories?). `ISSUE-0005` is now strongly informed,
because build pipelines and documentation generators imply executable tooling.
