---
id: ISSUE-0015
title: Skill-relative and target-relative paths are not distinguished
type: inconsistency
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - imports/ontology-driven-development-v2/SKILL.md
resolved-by: null
---

# ISSUE-0015 — Skill-relative and target-relative paths are not distinguished

## Statement

`ontology-driven-development` reads its template from
`templates/impact-analysis.md` and writes its output to
`model/changes/<change-id>/impact-analysis.md`.

The first path is relative to the skill directory. The second is relative to the
target repository. Nothing in the document marks the difference, and no rule
defines how either is resolved.

## Why it matters

Under composition both roots move. A skill invoked by a workflow, packaged by an
adapter, and applied to a target repository has at least three candidate roots:
the skill directory, this repository, and the target. An unqualified relative
path is ambiguous in all of them.

`ADR-0006` established that every path must declare its layer. The mechanism for
doing so does not yet exist.

## What we know

- `ADR-0006` names the two layers, which gives the vocabulary for a resolution
  rule but not the rule itself.
- `ISSUE-0004` may make the Layer B root configurable, which would require path
  resolution rather than fixed paths.

## Resolution criteria

A path-resolution convention in `shared/contracts/`, defining named roots and
how a skill references each, applied consistently across every skill from M4.
