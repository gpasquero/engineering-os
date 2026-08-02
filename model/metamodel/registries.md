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

  - id: REG-plans
    registers: engineering plans, derived deterministically from the model
    source: ../plans.md
    extraction: yaml-block
    collection: plans
    membership: >
      A plan is registered by appearing with an id, an objective, the subject
      types it applies to, a rationale, phases whose recommendations and actions
      exist, and an explicit list of what it defers.
    extension: >
      An adopting repository declares plans from registered recommendations and
      queries. No plan logic is written in code, and no language model
      participates in producing a plan (ADR-0092, ADR-0094).

  - id: REG-engineering-intents
    registers: why a developer entered the system
    source: ../engineering-intents.md
    extraction: yaml-block
    collection: engineering-intents
    membership: >
      An intent is registered by appearing with an id, a label, the question it
      asks, and the plans and recommendations it selects.
    extension: >
      An adopting repository declares its own intents. An intent is never a
      metamodel entity: its instances belong to a session, not to a model
      (ADR-0096).

  - id: REG-worker-capabilities
    registers: what kind of worker a task requires
    source: ../worker-capabilities.md
    extraction: yaml-block
    collection: worker-capabilities
    membership: >
      A capability is registered by appearing with an id, a label, an execution
      class of mechanical, reasoning or human, and a rationale.
    extension: >
      An adopting repository declares capabilities its workers have. A task
      declares capabilities, never workers (ADR-0097).

  - id: REG-task-kinds
    registers: how a plan action becomes a task
    source: ../task-kinds.md
    extraction: yaml-block
    collection: task-kinds
    membership: >
      A task kind is registered by appearing with an id, either a from-action or
      terminal flag, an objective template, required capabilities, a completion
      condition and the evidence it produces.
    extension: >
      An adopting repository declares kinds for its own plan actions. A TaskGraph
      is derived, never declared (ADR-0097).

  - id: REG-workers
    registers: worker types and the capabilities they provide
    source: ../workers.md
    extraction: yaml-block
    collection: workers
    membership: >
      A worker type is registered by appearing with an id, a label, the
      capabilities it provides, an execution class and a scope.
    extension: >
      An adopting repository declares its own worker types. No model or vendor is
      ever named; runtime implementations are outside the model (ADR-0099).

  - id: REG-governance-gates
    registers: gates that authorize change
    source: ../governance-gates.md
    extraction: yaml-block
    collection: governance-gates
    membership: >
      A gate is registered by appearing with an id, what it authorizes, the
      decision it enforces and the rule it states.
    extension: >
      An adopting repository declares its own gates. A gate is never a worker and
      has no capabilities (ADR-0100).

  - id: REG-observation-kinds
    registers: what a worker may report, and whether it may enter the model
    source: ../observation-kinds.md
    extraction: yaml-block
    collection: observation-kinds
    membership: >
      An observation kind is registered by appearing with an id, what it asserts,
      an intake outcome of record, govern or reject, what it produces and a
      rationale.
    extension: >
      An adopting repository declares kinds its execution can report. Workers
      never write to the model (ADR-0101).

  - id: REG-support-classification
    registers: what kind of support a proposed assertion has
    source: ../support-classification.md
    extraction: yaml-block
    collection: support-classification
    membership: >
      A classification is registered by appearing with an id, what it means, the
      workers that propose it, and how it is reviewed.
    extension: >
      An adopting repository may add classifications. These are kinds, not a
      scale: they are unordered and do not combine (ADR-0090).

  - id: REG-assertion-origins
    registers: what kind of process produced a proposed assertion
    source: ../assertion-origins.md
    extraction: yaml-block
    collection: assertion-origins
    membership: >
      An origin is registered by appearing with an id, what it means, its
      discovery stage, whether it is reproducible, and how it is reviewed.
    extension: >
      An adopting repository may add origins. Origin is reported as counts by
      kind and never combined into a score (ADR-0090, ADR-0109).

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
