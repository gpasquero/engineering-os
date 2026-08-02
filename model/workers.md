---
id: MODEL-WORKERS
title: Worker Types
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0097, ADR-0099, ADR-0100]
---

# Worker Types

> **Workers are not Claude. Workers are capabilities** (`ADR-0099`).

A worker type declares **what it can do**. Claude, Codex and future models are
runtime implementations of one or more types, and **no model or vendor is named
here.**

Assignment is set containment: a worker matches a task when the task's required
capabilities are a subset of the worker's provided capabilities. **No heuristic,
no scoring, no selection logic.**

```yaml
workers:
  - id: W-source-code-editor
    label: SourceCodeEditor
    provides: [C-read-source, C-modify-source]
    execution: reasoning
    scope: Source files within the allowed scope of the task.

  - id: W-architecture-reviewer
    label: ArchitectureReviewer
    provides: [C-read-source, C-semantic-query]
    execution: reasoning
    scope: Reads decisions, invariants and structure. Modifies nothing.

  - id: W-test-runner
    label: TestRunner
    provides: [C-run-tests]
    execution: mechanical
    scope: Executes a declared test target and reports the result.

  - id: W-documentation-writer
    label: DocumentationWriter
    provides: [C-read-source, C-modify-source]
    execution: reasoning
    scope: Documentation artifacts only.

  - id: W-static-analyzer
    label: StaticAnalyzer
    provides: [C-semantic-query]
    execution: mechanical
    scope: Derives facts from artifacts without interpreting them.

  - id: W-migration-planner
    label: MigrationPlanner
    provides: [C-read-source, C-semantic-query]
    execution: reasoning
    scope: Proposes ordering across artifacts. Modifies nothing.

  # Discovery worker types (ADR-0105). They read software so that no other
  # part of the architecture has to.
  - id: W-structure-extractor
    label: StructureExtractor
    provides: [C-parse-source, C-semantic-query]
    execution: mechanical
    scope: >
      ASTs, module graphs, dependency manifests, route tables, schema
      definitions. Derives structure and interprets nothing.

  - id: W-domain-interpreter
    label: DomainInterpreter
    provides: [C-parse-source, C-interpret-source, C-propose-knowledge]
    execution: reasoning
    scope: >
      Proposes Concepts, Capabilities and BoundedContexts from source and
      documentation. Every proposal carries the exact source it came from.

  - id: W-constraint-interpreter
    label: ConstraintInterpreter
    provides: [C-read-source, C-interpret-source, C-propose-knowledge]
    execution: reasoning
    scope: >
      Proposes Invariants from tests, guards, validators and assertions, and
      names the enforcement point when one is visible.

  - id: W-decision-archaeologist
    label: DecisionArchaeologist
    provides: [C-read-source, C-interpret-source, C-propose-knowledge]
    execution: reasoning
    scope: >
      Proposes ADRs and their establishes-edges from design documents, comments
      and commit history. Proposes nothing where a rationale is absent — a
      missing decision is a knowledge gap, not a gap to fill.

  - id: W-gap-identifier
    label: GapIdentifier
    provides: [C-semantic-query, C-propose-knowledge]
    execution: mechanical
    scope: >
      Reports what a candidate model does NOT contain: capabilities with no
      realisation, invariants with no enforcement, artifacts with no rationale.
      Proposes no knowledge — only its absence.

  - id: W-knowledge-recorder
    label: KnowledgeRecorder
    provides: [C-record-knowledge]
    execution: mechanical
    scope: Writes an authorized knowledge update. Never decides what to write.
```

## No worker provides `C-approve`

**Deliberate** (`ADR-0100`). Human review is a **governance gate**, not work.

A task requiring `C-approve` matches no worker, and that is the correct result:
it is **awaiting authorization**, not unassignable. Every task graph therefore
terminates in something automation cannot complete.

## `W-source-code-editor` and `W-documentation-writer` provide the same capabilities

They differ only in **scope**, which assignment does not read. Both will match
any task requiring source modification, and **the model has no way to prefer
one** — deliberately, since preferring would be a heuristic.

**Recorded as a real limitation**, not smoothed over: capability matching cannot
express *the right worker for this kind of artifact*.

## Debt

**Scope is prose and unenforced.** It describes what a worker should touch and
nothing checks it. The task's `allowed scope` (`ADR-0101`) is the enforceable
half; this is documentation.

**A worker that provides a capability badly is indistinguishable from one that
provides it well** (`ADR-0099`). The model has no notion of quality and cannot
acquire one without becoming a heuristic.

**No runtime exists.** This registry describes types nothing implements.
