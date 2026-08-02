---
id: ROADMAP
title: Roadmap
status: accepted
created: 2026-08-02
updated: 2026-08-02
supersedes: sources/handoff/ROADMAP.md (pre-M1, ten "Deliveries")
related: [ADR-0062]
---

# Roadmap

**Restructured under `ADR-0062`: architecture through implementation.**

The criterion is now:

1. If an existing decision permits building, **build**.
2. Stop building only when a **real contradiction** prevents continuing.
3. Avoid new architectural concepts unless **strictly necessary** for the next
   step.

Every new question is tested against *"do we need this to build the next
deliverable?"* A negative answer produces architectural debt, recorded as a
`deferred` issue, and building continues.

## The build sequence

Six deliverables, in order. Each is expected to reveal architectural defects;
that is the point.

### B1 — Engineering OS Metamodel

**In progress.** `model/metamodel/`.

Entity inventory complete: 25 entities. Two specified. The remainder are written
one at a time, each declaring the eight properties `ADR-0035` requires.

Blockers: none. Every entity has an establishing decision.

### B2 — First OWL ontologies

Formalize the metamodel inventory in OWL 2 DL. The inherited decision that OWL
models semantics is binding and awaits an ADR (`ISSUE-0027`) — which does not
block using it.

### B3 — First Canonical Knowledge Model

Compile the metamodel and the governance corpus into a graph conforming to the
metamodel (`ADR-0036`). The first test of whether the architecture produces
anything.

### B4 — Knowledge Compiler specification

Language-independent (`ADR-0017`). Defines the interface a conforming
implementation satisfies, and the stages: parsing, normalization, validation,
semantic linking.

Only **Mechanical Discovery** is in scope — traceability, dependency graphs,
impact graphs, registry projections, consistency checks (`ADR-0060`).

### B5 — First compilation pipeline

The first executable code in the repository. Requires un-deferring `ISSUE-0036`
(reference implementation language).

### B6 — First navigable Knowledge Explorer

A projection of this repository's Canonical Knowledge Model (`ADR-0034`). The
first deliverable a non-engineer would see.

## Milestones, restated

The earlier M1–M13 sequence is preserved as the eventual scope. The build
sequence above cuts a vertical slice through it rather than completing each
milestone in turn.

| Milestone | Scope | Status |
|---|---|---|
| M1 | Repository architecture and documentation system | **Complete** |
| M2 | Metamodel, contracts, manifests, compiler interface | B1–B4 are its core |
| M3 | Shared policies — Modeling, Governance, Process | Deferred behind the build sequence |
| M4–M7 | Skills | Unchanged |
| M8 | Workflows | Blocked by `ISSUE-0002` (deferred) |
| M9 | Schemas, validation, reference implementation | B5 |
| M10 | Scenario tests | Blocked by `ISSUE-0006` (deferred) |
| M11 | Engineering OS self-model | Largely delivered by B1 |
| M12 | Documentation, adapters, v1 | B6 contributes |
| M13 | Knowledge Packages and federation | Unchanged |

## Architectural debt

**23 deferred issues.** Each is a real question that does not block the next
deliverable. They are reopened when implementation requires them, not on a
schedule.

Two remain open because they are not architectural:

- `ISSUE-0011` — the repository is public with no licence. A legal exposure, not
  a design question.
- `ISSUE-0037` — five hand-maintained projections. Operational debt that B5
  discharges.

The debt most likely to be met early is `ISSUE-0073`: "runtime" names both a
compiler artifact kind and target-system telemetry, and both will appear in the
metamodel.
