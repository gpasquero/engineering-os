---
id: ISSUE-0019
title: Two minimum evidence records disagree on their defaults
type: inconsistency
status: deferred
severity: low
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - imports/reconstruct-system-knowledge/references/evidence-model.md
  - imports/reconstruct-system-knowledge/templates/evidence-record.yaml
resolved-by: null
defers-to: [M2]
debt: architectural
---

# ISSUE-0019 — Two minimum evidence records disagree

> **Architectural debt** (`ADR-0062`). Deferred because it is not needed to
> build the next deliverable. Reopen when implementation requires it.

## Statement

The same artifact is specified twice with different defaults:

- `references/evidence-model.md` presents a "minimum evidence record" with
  `status: confirmed` and `confidence: high`.
- `templates/evidence-record.yaml` presents the template with
  `status: unknown` and `confidence: low`.

## Why it matters

Minor in isolation, but the defaults encode opposite epistemic stances. A
template that defaults to `confirmed` / `high` invites an author to leave a
strong claim unexamined, which contradicts the principle that uncertainty must
never be converted into certainty.

## What we know

The `evidence-model.md` version is illustrative — it shows a filled-in example.
The `.yaml` version is an actual template. The conflict is arguably a
documentation artifact rather than a real disagreement, but it is not marked as
such in either file.

## Resolution criteria

One evidence-record contract in `shared/contracts/`, with defaults that fail
safe (`unknown` / `low`), and any illustrative example clearly labelled as an
example rather than a default.
