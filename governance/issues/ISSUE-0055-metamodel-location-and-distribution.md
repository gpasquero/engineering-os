---
id: ISSUE-0055
title: Where the Metamodel lives, and how adopting repositories obtain it
type: question
status: open
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0035-engineering-os-metamodel.md
  - governance/adr/ADR-0036-canonical-model-conforms-to-the-metamodel.md
  - governance/adr/ADR-0010-repository-local-knowledge-ownership.md
resolved-by: null
---

# ISSUE-0055 — Where the Metamodel lives

## Statement

`ADR-0035` establishes the Engineering OS Metamodel as the ontology of the
framework itself. `ADR-0036` makes it the contract between authoring and
compilation, and requires it before the compiler interface.

Neither says where it lives, nor how an adopting repository obtains it.

## Why it matters

It is now the **first M2 deliverable**, and it cannot be written without a
location. It is marked `blocking` for that reason.

The question is not filing. **Every adopting repository's Canonical Knowledge
Model must conform to the metamodel**, so the metamodel cannot be purely
repository-local — which is what `ADR-0010` makes everything in `model/`.

## Options

- **Layer A, shipped with the methodology** (`shared/metamodel/` or a top-level
  `metamodel/`). Adopters receive it as part of Engineering OS, exactly as they
  receive contracts and policies. Simplest, and consistent with `ADR-0036`
  treating it as a contract.
- **Engineering OS's own `model/`, published as a Knowledge Package.** Elegant:
  `ADR-0035` calls it "the ontology of Engineering OS itself", and an ontology
  belongs in a knowledge model. Adopters would import it via `ADR-0019`'s
  federation — which would make the metamodel the first real use of Knowledge
  Packages. But federation is M13, and M2 cannot wait for it.
- **Both** — authored in `model/`, exported to Layer A by the compiler. Requires
  a compiler that does not exist, and would make the metamodel derived, which
  contradicts its role as a contract.

The first is the only option that works within M2. The second is the more
coherent long-term answer and would be blocked for eleven milestones.

## The question underneath

**Is the metamodel Layer A or Layer B?**

`ADR-0035` describes it as an ontology of Engineering OS, which sounds like Layer
B. `ADR-0036` describes it as a contract every implementation must satisfy,
which is Layer A. `ADR-0014` keeps the layers strictly separate.

This is the same tension as `ISSUE-0031`, which asks what Engineering OS's own
`model/` contains. The two should be resolved together.

## Resolution criteria

An ADR naming the metamodel's location and artifact kind, stating whether it is
Layer A or Layer B, and defining how an adopting repository obtains the version
its canonical model must conform to.
