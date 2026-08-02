---
id: ISSUE-0018
title: The assertion status vocabulary is defined in two places
type: inconsistency
status: open
severity: medium
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - imports/reconstruct-system-knowledge/SKILL.md
  - imports/reconstruct-system-knowledge/references/evidence-model.md
  - sources/handoff/DECISIONS.md
resolved-by: null
---

# ISSUE-0018 — The assertion status vocabulary is duplicated

## Statement

The twelve assertion statuses are defined twice within the same prototype:

- `imports/reconstruct-system-knowledge/SKILL.md` — the twelve values **with**
  definitions.
- `imports/reconstruct-system-knowledge/references/evidence-model.md` — the same
  twelve values as a bare list, **without** definitions.

## Why it matters

This is the exact duplication that `sources/handoff/DECISIONS.md` promised to eliminate with
"shared policies instead of duplicated prompt text" — occurring inside the
artifact that established the principle. It is the canonical example of the
failure `ADR-0008` was written to prevent.

Two copies drift. A future edit to one will not reach the other, and the version
without definitions is the one a reader is more likely to treat as the reference
list.

## What we know

The two lists currently agree on values and order. The defect is structural, not
yet substantive.

## Resolution criteria

One definition in `shared/vocabularies/assertion-statuses.yaml`, with every
other document referencing it by path rather than restating it. Per `ADR-0005`
the frozen prototypes are **not** edited; the vocabulary is extracted, and the
duplication remains visible in the frozen inputs as provenance.
