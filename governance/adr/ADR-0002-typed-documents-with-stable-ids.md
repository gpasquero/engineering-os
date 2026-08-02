---
id: ADR-0002
title: Knowledge is recorded as typed documents with stable IDs and front matter
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0023]
related: [ADR-0001, ADR-0003]
---

# ADR-0002 — Knowledge is recorded as typed documents with stable IDs

## Context

`ADR-0001` establishes that the repository is the memory. That is insufficient
on its own: memory that is unstructured cannot be navigated, cross-referenced,
or validated.

The inherited repository demonstrated the failure. Seven root-level Markdown
files carried no type, no status, no identifiers and no cross-references.
`sources/handoff/DECISIONS.md` mixed decisions of wildly different scope in one list.
`sources/handoff/AGENTS.md` mandated a reading order that omitted the vision document
(`ISSUE-0023`). Nothing linked a stated decision to the problem it solved.

## Decision

Every document in `governance/` has a **type**, and every instance of a
record-like type has a **stable, never-reused, zero-padded ID**.

- Types, locations, mutability and front-matter schemas are defined normatively
  in `governance/documentation-system.md`.
- Record types: `ADR-`, `ISSUE-`, `SESSION-`. Specifications gain `SPEC-` in M2.
- Status vocabularies are closed sets. Adding a value requires an ADR.
- ADRs and issues are linked **bidirectionally**: an ADR lists what it
  `resolves`, and each resolved issue names it in `resolved-by`. A one-sided
  link is a defect.
- IDs are never renumbered, because they are referenced from other documents,
  from session logs, and from commit messages.
- Mutability is explicit per type: accepted ADRs are immutable and superseded
  rather than edited; session logs are immutable; the build state is
  overwritten; issues are mutable until closed.

## Alternatives considered

**Free-form Markdown, as inherited.** Rejected: it produced exactly the defects
listed in the context, within a repository of only 2,300 lines.

**A database or structured issue tracker as the primary store.** Rejected for
the same reason as in `ADR-0001` — it is not readable from the repository
alone. Structured *validation* of front matter is planned for M9, which gets
most of the benefit without moving the source of truth.

**Types without IDs.** Rejected: cross-referencing by title is fragile, because
titles get edited and links then rot silently.

**Dated filenames instead of sequential IDs.** Rejected: two decisions on the
same day collide, and dates carry no ordering meaning for supersession chains.

## Consequences

### Positive

- Documents can be referenced precisely and permanently.
- Supersession chains are explicit rather than implied by file history.
- Front matter is machine-validatable later without restructuring content.

### Negative

- ID allocation is manual until M9 and can collide if two sessions work in
  parallel on separate branches.
- Bidirectional links are maintained by hand and can desynchronize.

### Neutral

- The inherited root documents are restructured into typed governance
  documents. Their original form remains in git history and, where they were
  inputs rather than outputs, in `sources/`.

## Compliance

Every file under `governance/` has front matter with an `id` and a `status`.
Every ADR with a non-empty `resolves` has a matching `resolved-by` on each
issue named. Verified by hand until M9, by schema thereafter.
