---
id: ADR-0016
title: Governance documents are authoritative; machine manifests are generated projections
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0035, ISSUE-0028]
related: [ADR-0001, ADR-0012, ADR-0013, ADR-0014, ISSUE-0037]
---

# ADR-0016 — Governance is authoritative; manifests are projections

## Context

`ADR-0013` defined `BUILD-STATE.yaml` as holding milestones, progress, blockers
and references to ADRs and issues. `ISSUE-0035` recorded that every one of those
already exists in `governance/` — in `roadmap.md`, `build-state.md`,
`issues/index.md` and the `blocks` field of issue front matter.

Two artifacts claiming the same content is the duplication failure that
`ADR-0012`'s taxonomy exists to forbid, appearing at the level of the project's
own status.

`ISSUE-0028` recorded the same failure one level down: a hand-maintained issue
index duplicating issue front matter.

## Decision

**`BUILD-STATE.yaml` must not become another manually maintained governance
document.**

Governance documents remain **authoritative**: the roadmap, ADRs, issues and
milestones.

`BUILD-STATE.yaml` is a **generated projection**. Its purpose is to expose the
current implementation state in machine-readable form. It is generated from the
authoritative governance artifacts.

```text
Governance Documents  (authoritative)
        ↓
Knowledge Compiler
        ↓
BUILD-STATE.yaml  (derived)
```

This keeps a single source of truth.

The same rule applies to `governance/issues/index.md` and to every other index
that restates content held elsewhere: they are projections, not sources.

### Transitional exception

Where generation is not yet implemented, a projection may **temporarily** be
maintained by hand. This is **transitional technical debt and must be tracked
explicitly** — `ISSUE-0037`. It is not a standing permission, and a projection
maintained by hand carries a visible notice saying so.

## Alternatives considered

**`BUILD-STATE.yaml` authoritative, Markdown as the rendering.** Rejected. It
would make the memory layer depend on the compiler existing, so a session could
not reconstruct context by reading the repository until tooling was built —
contradicting `ADR-0001`. It would also stop a human from simply editing the
build state.

**Both authoritative, with different scopes.** Rejected on sight in
`ISSUE-0035`, and rejected here for the record: it is the drift failure the
taxonomy forbids, and it is attractive only because it requires no work.

**Drop `BUILD-STATE.yaml` entirely and let machines parse the Markdown.**
Rejected: it would push front-matter parsing into every consumer, which
`ADR-0014` forbids — consumers read the compiled model, not the sources.

## Consequences

### Positive

- **A single source of truth for project status**, with the machine-readable
  form derived rather than parallel.
- `ADR-0001` is preserved intact: the repository remains fully readable as
  memory, by a human or an agent, with no tooling.
- **`ISSUE-0028` is resolved by the same decision.** The hand-maintained issue
  index becomes a projection. The two problems were one problem.
- Governance front matter becomes load-bearing input to the compiler, which
  gives the front-matter schema in M9 a concrete consumer.

### Negative

- **Everything the projection needs must be expressible in governance front
  matter.** Where it is not, either the front matter grows or the projection
  cannot be fully generated. This constrains the documentation system, and some
  status information may prove awkward to express in structured fields.
- Until generators exist, the duplication remains — now sanctioned as debt
  rather than accidental, which is better, but not fixed. `ISSUE-0037`.
- A generated `BUILD-STATE.yaml` is only as accurate as the front matter it
  reads, so stale front matter becomes stale project status, silently.

### Neutral

- Whether generated projections are committed to version control is the
  per-artifact trade left open by `ADR-0012`.

## Compliance

No projection is edited to change project status; the governance document is
edited instead. Any projection currently maintained by hand carries a notice
saying so and is listed in `ISSUE-0037`. Once a generator exists for a
projection, hand-editing it is a defect.
