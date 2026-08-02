---
id: ISSUE-0022
title: The repository was described both as a bootstrap package and as the product
type: inconsistency
status: resolved
severity: medium
created: 2026-08-02
updated: 2026-08-02
blocks: [M1]
evidence:
  - sources/handoff/README.md
  - sources/handoff/ROADMAP.md
resolved-by: ADR-0001
---

# ISSUE-0022 — Bootstrap package versus product

## Statement

The pre-M1 `sources/handoff/README.md` described this repository as a "Bootstrap repository …
a handoff intended to initialize the repository before implementation begins",
implying the real work happens elsewhere.

`sources/handoff/ROADMAP.md` treated the same repository as the product itself, through ten
deliveries to a v1 release.

## Why it matters

Determined whether to build here or to treat this as scaffolding for a future
repository — and therefore whether any of the governance layer was worth
creating.

## Resolution

`ADR-0001` establishes that this repository **is** the product and **is** the
persistent memory. It is at bootstrap stage, which is a phase, not an identity.

The alternative — building the real product elsewhere — was rejected because it
would immediately reproduce the same memory problem in the new location, and
nothing in the inherited documents justified the split.

`README.md` has been rewritten accordingly.
