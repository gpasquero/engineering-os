---
id: ISSUE-0032
title: The implementation language and toolchain of the framework are undefined
type: question
status: open
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0012-executable-framework-and-artifact-taxonomy.md
  - governance/adr/ADR-0011-engineering-os-is-a-knowledge-compiler.md
resolved-by: null
---

# ISSUE-0032 — Implementation language and toolchain are undefined

## Statement

`ADR-0012` establishes that Engineering OS is an executable framework, and
`ADR-0011` that it is a knowledge compiler with parsing, normalization,
validation and semantic linking stages.

No language, runtime, dependency manager, test framework or CI configuration has
been chosen. The repository currently contains no executable code of any kind.

## Why it matters

"Executable" is a commitment without an implementation until this is decided.
Every M2 deliverable that involves generation or validation — manifest
validation, the issue-index generator, schema checking — needs a runtime to run
in. Choosing late means writing specifications that no chosen toolchain can
implement cleanly.

It is marked `blocking` rather than `high` because M2 now contains generated and
validated artifacts, and those cannot be built at all without an answer.

## What we know

- The inherited `reconstruct-system-knowledge` prototype deliberately defers
  tooling choice to the *target* repository's ecosystem, listing ROBOT, Apache
  Jena, OWLAPI, RDFLib and pySHACL as candidates, and warns against introducing
  a heavy platform prematurely. That guidance concerns the target, not this
  repository.
- The semantic-web tooling that the ontology work depends on is strongest in
  Java (Jena, OWLAPI, ROBOT) and Python (RDFLib, pySHACL).
- Agent runtimes and adapters (`ISSUE-0001`) may pull in a different ecosystem,
  most likely TypeScript. A split between the compiler's language and the
  adapters' language is possible but doubles the toolchain surface.

## Open sub-questions

- One language or several?
- What may the compiler depend on? `ADR-0012` requires determinism, which
  constrains dependency choice more than usual.
- Does an adopting repository need this toolchain installed to use Engineering
  OS, or only to rebuild derived artifacts?

That last question is the important one: if adopters must install a compiler
toolchain, the adoption cost of the methodology rises sharply.

## Resolution criteria

An ADR naming the language, runtime, dependency manager and test framework, and
stating what an adopting repository is required to install.
