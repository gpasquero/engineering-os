---
id: ACCEPT-0044
artifact: SESSION-0048 — Understanding Retention and the semantic diagnosis
artifact-revision: 185db71
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0127, ADR-0128, ADR-0129, ADR-0130, ADR-0131]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0044 — The product metric was hiding product failure

## Artifact

The work of `SESSION-0048`, at revision **`185db71`**.

Scope: `ADR-0127`–`ADR-0131`, the `retention` metric, the diagnosis that
Continuous Acquisition preserves two of six semantic relationships, and the
corrected longitudinal verdict.

**Sequence continuous.**

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **One of the strongest sessions of the project — not because Continuous
  Acquisition improved, but because the project discovered that its own product
  metric was hiding product failure.** Coverage remained stable; understanding
  did not.
- **`ADR-0127` through `ADR-0131` should remain exactly as they are.**
- **Understanding Retention is now the primary longitudinal KPI.** Every future
  metric is evaluated against *could this metric increase while Engineering
  Understanding deteriorates?*
- **The benchmark is not a regression suite. It is the first product benchmark
  of Engineering OS, and it now owns part of the architecture.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

Five decisions, each implemented in the session that recorded it. `ADR-0131` is
superseded by `ADR-0136` in the following session, with symmetry on both.

## Condition 3 — validation summary

294 records, 17 fixtures, 20 registries, both query engines in agreement, and a
reproducible ten-commit suite whose baseline was recorded before any fix.

## Exceptions

None. The parity fix was deliberately withheld from the session that diagnosed
it, so that the diagnosis remained verifiable.

## Notes

The reviewer reframed the next objective one level up:

> The next objective should not be *"restore semantic parity"*. **Continuous
> Acquisition should preserve the system's ability to answer Engineering
> Questions. Keep Engineering Questions as the product contract. Treat
> predicates as implementation details.**

And moved the North Star:

> **We preserve an engineering team's ability to make correct decisions as
> software evolves.**

Recorded as `ADR-0132` (the metric admission test), `ADR-0133` (three
preservation properties), `ADR-0134` (questions are the contract), `ADR-0135`
(two products) and `ADR-0136` (the North Star).
