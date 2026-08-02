---
id: ADR-0083
title: Registries are declared; the compiler knows extraction kinds, not registry shapes
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0031, ADR-0032, ADR-0070, ADR-0077, ADR-0081]
---

# ADR-0083 — Registries are declared

## Context

The compiler had **three ad-hoc readers**: a regex for entity types, a regex for
the relationship mapping table, a YAML-block extractor for validation rules. Each
knew the shape of one file, and adding a registry meant adding a reader.

`ADR-0032` has required every registry to declare its identity, membership rules
and extension rules since `SESSION-0011`. **No registry had ever declared any of
them.**

## Decision

**Registries are declared in `model/metamodel/registries.md`. The compiler
implements *extraction kinds*, never registry shapes.**

Same split as `ADR-0077`: **adding a registry is a data change; adding an
extraction kind is a compiler change and should be rare.** Three kinds —
`front-matter`, `markdown-table`, `yaml-block` — cover four registries.

Every declaration states `id`, `registers`, `source`, `extraction`, `membership`
and `extension`.

## Alternatives considered

**Keep the three readers.** Rejected — the reason for the decision, and it scales
linearly with registries forever.

**A single registry format all sources must adopt.** Rejected: it would force the
relationship vocabulary and the entity specifications into a shape chosen for the
reader rather than for the human author, and `ADR-0017` requires authoring to
stay readable without tooling.

**Load registries lazily, per consumer.** Rejected as a determinism risk. A
registry read twice in one compilation could differ, and `ADR-0073` requires each
feature to state a determinism guarantee.

## Consequences

### Positive

- **`membership` and `extension` exist for the first time.** Writing them raised a
  question no reader had asked — *may an adopting repository add Layer A entity
  types?* The answer is no (`ADR-0037`), and it had never been recorded anywhere
  a reader would look.
- `ISSUE-0037` becomes measurable: **four registries, four hand-maintained
  sources, zero generated.**
- The resolver now reads nothing from disk, which makes its determinism
  guarantee real rather than incidental.

### Negative

- **`extraction` binds a registry to a file format.** A source that became a
  database would need a new kind — the Registry Pattern applied to itself, and
  bounded the same way.
- **Nothing checks that a declared source exists** until the compiler reads it.

### Neutral

- No registry's content changes. Four readers become one mechanism.

## Compliance

`compiler/registry/` implements extraction kinds and reads the declaration. No
other module reads a registry source directly.
