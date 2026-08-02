---
id: ISSUE-0004
title: Where the Layer B model tree lives for a target system is undefined
type: question
status: resolved
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - imports/reconstruct-system-knowledge/SKILL.md
  - imports/reconstruct-system-knowledge/references/repository-structure.md
  - imports/ontology-driven-development-v2/README.md
resolved-by: ADR-0010
---

# ISSUE-0004 — Where the Layer B `model/` tree lives is undefined

## Statement

All three prototypes assume the knowledge model lives at `model/` inside the
target repository. None considers a system spread across multiple repositories,
or an organization that wants one knowledge model spanning several codebases.

## Why it matters

`model-spec/` is an M2 deliverable and must state where its scaffold is
installed. The answer also determines how traceability references are written:
paths relative to a target repository do not survive a move to a central store.

## What we know

- `reconstruct-system-knowledge` restricts all its writes to `model/` in the
  current working directory.
- `ontology-driven-development` writes to `model/changes/<change-id>/`, a path
  absent from the canonical tree (`ISSUE-0014`).
- `ADR-0006` separated Layer A from Layer B but deliberately did not decide
  placement.

## Options

- **In the target repository** (`model/`) — matches the prototypes; simple;
  co-versioned with the code it describes; breaks for multi-repo systems.
- **Sibling knowledge repository** — supports multi-repo; loses atomic
  co-versioning of code and model.
- **Central knowledge store** for an organization — strongest for cross-system
  questions; heaviest; raises access-control questions.
- **Configurable, with in-repo default** — flexible; every skill must then
  resolve a configured root rather than a fixed path, which interacts with
  `ISSUE-0015`.

## Resolution

`ADR-0010`. **`model/` is always repository-local.** Every repository adopting
Engineering OS owns its own knowledge model; knowledge is owned by the
repository that owns the domain. There is no shared central model directory, and
multi-repository environments federate rather than share.

The sibling-repository, central-store and configurable options were all
rejected. Federation via versioned **Knowledge Packages** handles the
cross-repository case that a central store was meant to solve.

This answer **superseded `ADR-0006`**, which had asserted that this repository
never contains a live `model/`. Engineering OS has its own `model/` describing
the framework; Layer A and Layer B coexist in every adopting repository,
including this one.

Newly opened by this answer: `ISSUE-0029` (Knowledge Package format and
federation protocol) and `ISSUE-0031` (Engineering OS self-model scope).
