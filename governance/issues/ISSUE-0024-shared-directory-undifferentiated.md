---
id: ISSUE-0024
title: The shared/ directory was undifferentiated and had no home for contracts
type: gap
status: resolved
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/design/proposed-architecture.md
  - sources/handoff/ROADMAP.md
resolved-by: ADR-0008
---

# ISSUE-0024 — `shared/` was undifferentiated

## Statement

`governance/design/proposed-architecture.md` listed `shared/` as a single undifferentiated
directory. The inherited roadmap required "shared contracts" in delivery 1 and
"shared policies" in delivery 2 — two different kinds of content with no
distinct location.

## Why it matters

Contracts, policies and vocabularies have different normativity and different
failure modes. A single directory provides no way to express that a vocabulary
is closed while a policy is prose, or that a contract is machine-checkable.

## Resolution

`ADR-0008` splits `shared/` three ways:

- `shared/contracts/` — machine-checkable interfaces
- `shared/policies/` — normative prose, referenced never inlined
- `shared/vocabularies/` — closed enumerations, single source

Placement disputes are resolved by asking how a violation would be detected:
mechanically, by review, or by comparing two definitions.
