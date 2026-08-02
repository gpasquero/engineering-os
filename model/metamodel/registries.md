---
id: METAMODEL-REGISTRIES
title: Registries
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
artifact-kind: authoritative
established-by: [ADR-0031, ADR-0032, ADR-0070, ADR-0083]
---

# Registries

**Every registry the compiler reads, declared in one place.**

Before this artifact, the compiler had **three ad-hoc readers** — a regex for
entity types, a regex for the relationship mapping table, and a YAML-block
extractor for validation rules. Each knew the shape of one file. Adding a
registry meant adding a reader.

> **A Registry Specification is authoritative; a Registry Projection is derived**
> (`ADR-0032`). This declares the specifications.

## The registries

```yaml
registries:
  - id: REG-entity-types
    registers: Layer A metamodel entity types
    source: entities/*.md
    extraction: front-matter
    key: title
    fields: [entity-family]
    membership: >
      An entity type is registered by having a specification file whose front
      matter declares a title and an entity-family.
    extension: >
      An adopting repository does not extend this registry. Layer A entity types
      are framework-owned (ADR-0037).

  - id: REG-relationship-predicates
    registers: predicates and the core type each specializes
    source: relationship-vocabulary.md
    extraction: markdown-table
    section: The mapping
    columns: [predicate, core, category]
    membership: >
      A predicate is registered by appearing in the mapping table with a core
      type and a category. A core type used directly is its own parent.
    extension: >
      An adopting repository registers domain predicates that specialize a core
      type. It does not add core types without a metamodel change (ADR-0071).

  - id: REG-core-relationship-types
    registers: the core relationship vocabulary and its categories
    source: relationship-vocabulary.md
    extraction: markdown-table
    section-pattern: "^### (Structural|Behavioral|Semantic|Traceability) — "
    section-label: category
    columns: [core, means, inverse]
    membership: >
      A core type is registered by appearing in one of the four category tables
      with a definition and an inverse. An inverse is itself a core type: the
      table declares the pair on one row, and the pair is unfolded by the reader
      because that is interpretation rather than extraction.
    extension: >
      Registered, not enumerated (ADR-0031), but adding a core type is a
      metamodel change and should be rare.

  - id: REG-queries
    registers: the engineering questions Engineering OS can answer
    source: ../queries.md
    extraction: yaml-block
    collection: queries
    membership: >
      A query is registered by appearing in the queries block with an id, a
      question, a subject mode, a rationale and a list of steps whose operators
      the engine implements.
    extension: >
      An adopting repository declares additional queries using registered
      operators. Adding an operator is an engine change (ADR-0086).

  - id: REG-finding-kinds
    registers: the taxonomy classifying discoveries by strength
    source: ../finding-kinds.md
    extraction: yaml-block
    collection: finding-kinds
    membership: >
      A finding kind is registered by appearing in the taxonomy with an id, a
      rank, a strength, what it claims and what it requires.
    extension: >
      An adopting repository may add kinds. It may not weaken the requirements of
      a framework kind (ADR-0090).

  - id: REG-recommendations
    registers: engineering recommendations, composed of semantic queries
    source: ../recommendations.md
    extraction: yaml-block
    collection: recommendations
    membership: >
      A recommendation is registered by appearing with an id, an intent, the
      subject types it applies to, a rationale and steps whose queries exist.
    extension: >
      An adopting repository declares recommendations from registered queries.
      Recommendation logic is never written in code (ADR-0091).

  - id: REG-validation-rules
    registers: the rules the compiler executes
    source: validation-rules.md
    extraction: yaml-block
    collection: rules
    membership: >
      A rule is registered by appearing in the rules block with an id, a kind
      that the compiler implements, a severity, a message and a rationale.
    extension: >
      An adopting repository declares additional rules of any registered kind,
      and may not weaken a framework rule (ADR-0077).
```

## What a Registry declaration must state

| Field | States |
|---|---|
| `id` | the registry's stable identifier |
| `registers` | what kind of thing it holds |
| `source` | the authoritative artifact |
| `extraction` | how entries are read — `front-matter`, `markdown-table`, `yaml-block` |
| `section-label` | for `markdown-table`: a field name to carry the section a row came from |
| `membership` | what makes an entry a member |
| `extension` | how an adopting repository may add to it |

**`extraction` is the only field that is about mechanism**, and it is a closed
vocabulary. Three kinds cover four registries, which is the first evidence that
the shapes are not arbitrary.

## What declaring these exposed

**All four registries are extracted from Markdown by pattern.** Declaring them
did not make that go away — it made it visible in one place, and it makes
`ISSUE-0037` measurable: **four registries, four hand-maintained sources, zero
generated.**

**`membership` and `extension` were unstated for every registry.** `ADR-0032`
required both since `SESSION-0011` and no registry had ever declared either.
Writing them raised a question no reader had: *may an adopting repository add
Layer A entity types?* The answer is no (`ADR-0037`), and it had never been
recorded where anyone would look.

## Debt

**No Registry Projection is generated.** `ADR-0032` distinguishes specification
from projection and only the specification exists.

**`extraction` binds the registry to a file format.** A registry whose source
became a database or a compiled artifact would need a new extraction kind, which
is the Registry Pattern applied to itself and bounded in the same way.

**Nothing checks that a declared source exists** until the compiler tries to read
it.
