---
id: ISSUE-0052
title: The Knowledge Explorer is named with a requirement but has no definition
type: gap
status: resolved
severity: medium
created: 2026-08-02
updated: 2026-08-02
blocks: [M12]
evidence:
  - governance/adr/ADR-0031-registry-pattern.md
  - governance/adr/ADR-0014-three-tier-knowledge-model.md
resolved-by: ADR-0034
---

# ISSUE-0052 — The Knowledge Explorer is undefined

## Statement

`ADR-0031` states that the Registry Pattern "should also become one of the
primary concepts exposed by the future **Knowledge Explorer**, allowing users to
navigate registries independently from the specifications they reference."

This is the first appearance of the Knowledge Explorer in the repository. It now
carries a stated requirement and has no definition.

## Why it matters

`ADR-0014` enumerated the consumers of the canonical knowledge model: Knowledge
Graph, Search Index, Cross-reference Index, Impact Database, Validation Reports,
Agent Context, Documentation Website, future AI interfaces. The Knowledge
Explorer is not among them.

So it is either a new consumer, a renaming of the Documentation Website, or a
distinct navigation surface over several consumers. Each reading implies
different M12 work.

Recording it now costs nothing. Discovering in M12 that a requirement was
attached to an undefined artifact would cost more.

## Open sub-questions

- Is it a projection of the canonical knowledge model, like every other consumer
  (`ADR-0014`), or a tool that reads registries directly?
- Is it the Documentation Website under another name, or additional to it?
- Does it require the compiler toolchain to run, which `ADR-0017` says adopters
  must not need for consumption?
- Is it framework-only, or does an adopting repository get one for its own
  domain?

That last question matters most: if every adopter gets an explorer over its own
knowledge, it is a shipped capability rather than a project website.

## Resolution

`ADR-0034`. **Every Engineering OS repository owns its own Knowledge Explorer.**

All four sub-questions are answered:

- It is a **projection of that repository's Canonical Knowledge Model**, like
  every other consumer.
- It is **not** the Documentation Website. It stands alongside documentation,
  search indexes and validation reports.
- Generating one requires the compiler toolchain — consistent with `ADR-0017`,
  which carves out generation as the case where the toolchain *is* needed.
- **It is per-repository, not framework-only.** Engineering OS has one
  describing the framework; every adopting repository generates another
  describing its own domain.

The sub-question flagged as mattering most is answered in the direction that
makes it a **shipped capability rather than a project website** — arguably the
most visible benefit of adopting Engineering OS.

Federation between Explorers via Knowledge Packages is **an additional
capability, not the default architecture**.
