---
id: ISSUE-0005
title: Whether the Engineering OS ships executable code is undecided
type: question
status: resolved
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2, M9]
evidence:
  - sources/handoff/ROADMAP.md
  - governance/design/proposed-architecture.md
  - imports/reconstruct-system-knowledge/SKILL.md
  - governance/adr/ADR-0009-manifest-is-the-root-composition-manifest.md
resolved-by: ADR-0012
---

# ISSUE-0005 — Whether this repository ships executable code is undecided

## Statement

The architecture includes `validation/` and `tests/`, and the roadmap includes
"Schemas" and "Scenario tests". These imply a runtime. Nothing states whether
this repository contains runnable code, or only specifications that a target
project implements.

## Why it matters

Determines whether M9 produces scripts or specifications, whether the repository
needs a language toolchain, dependency management and CI, and whether
`ISSUE-0002` may resolve to an executable runner.

## What we know

- `reconstruct-system-knowledge` deliberately defers tooling choice to the
  target ecosystem, listing ROBOT, Jena, OWLAPI, RDFLib and pySHACL as
  possibilities, and warns: "Do not introduce a heavy platform before a simpler
  tool proves insufficient."
- That guidance is about the *target* repository, not this one. The distinction
  was never drawn.

## Options

- **Pure specification** — no code; validation is described and implemented
  per-project. Maximum portability, no enforcement.
- **Reference implementation** — this repository ships validators and a runner
  in one language. Enforceable, adds a dependency and a maintenance burden.
- **Schemas plus thin scripts** — JSON Schema as the contract, small scripts for
  convenience. Middle path.

## New evidence (ADR-0009)

`ADR-0009` defines `MANIFEST.yaml` as declaring **build pipelines**,
**documentation generators** and **validation configuration**. All three are
executable tooling. `ADR-0009` further requires that manifest sections derivable
from the filesystem be **generated or validated rather than hand-maintained**,
which cannot be satisfied by specification alone.

This effectively answers the question in the affirmative, but the answer has not
been recorded as a decision, and the language and dependency policy remain open.
The severity is therefore raised: it must now be settled in **M2**, not M9.

## Resolution

`ADR-0012`. **Engineering OS is not a documentation project; it is an executable
engineering framework.** Build pipelines, validators, generators, analyzers and
visualizers are first-class code artifacts.

Generated artifacts are never sources of truth. Every executable pipeline must
be deterministic. The repository distinguishes four artifact kinds —
`authoritative`, `derived`, `runtime`, `cached` — and every generated artifact
declares its inputs, its generator, whether it is reproducible and whether it is
safe to delete.

`ADR-0011` goes further: the framework is a **knowledge compiler**, not a
documentation generator.

The "pure specification" option is rejected outright.

**The second half of the original resolution criteria — which language, and what
may depend on it — is not answered.** It is carried into `ISSUE-0032`, which
blocks M2. `ISSUE-0033` records the unresolved determinism boundary.
