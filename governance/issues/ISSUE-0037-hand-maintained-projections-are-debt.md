---
id: ISSUE-0037
title: Hand-maintained projections are transitional technical debt
type: risk
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M9]
evidence:
  - governance/adr/ADR-0016-governance-is-authoritative-manifests-are-projections.md
  - governance/adr/ADR-0017-reference-architecture-not-reference-implementation.md
  - governance/issues/index.md
resolved-by: null
---

# ISSUE-0037 — Hand-maintained projections are transitional debt

## Statement

`ADR-0016` establishes that projections are generated from authoritative
governance documents, and permits temporary hand-maintenance where a generator
does not yet exist — on condition that the debt is **tracked explicitly**.

`ADR-0017` defers the implementation language (`ISSUE-0036`), so no generator
can be built yet. Every projection is therefore hand-maintained today, and will
remain so for several milestones.

This issue is that explicit tracking. It is the register of the debt.

## Register

| Projection | Authoritative source | Status |
|---|---|---|
| `governance/issues/index.md` | Issue front matter | Hand-maintained |
| `governance/adr/README.md` index table | ADR front matter | Hand-maintained |
| `governance/sessions/README.md` index table | Session log front matter | Hand-maintained |
| Highest-allocated-ID counters (3 files) | Directory contents | Hand-maintained |
| `BUILD-STATE.yaml` | `roadmap.md`, `build-state.md`, issue front matter | Not yet created |

`governance/build-state.md` is **not** in this register. It is an authoritative
governance document under `ADR-0016`, not a projection.

## Why it matters

The debt is not neutral. A hand-maintained projection can silently disagree with
its source, and `governance/issues/index.md` is read at session start to
determine what is blocked. A stale index would misreport blockers, which is
worse than having no index — a session could start a milestone that an open
issue blocks.

The risk grows with every issue and ADR added, and the deferral in `ISSUE-0036`
has no fixed end date.

## Mitigation until generators exist

- Every hand-maintained projection carries a visible notice saying so.
- Indexes are updated in the same change that adds or modifies a record, never
  later.
- The session protocol's closing checklist already requires index updates.

These reduce the risk; they do not remove it. Only generation does.

## Resolution criteria

Every entry in the register is generated, and hand-editing any of them becomes a
detectable defect. Requires `ISSUE-0036` and the compiler interface.
