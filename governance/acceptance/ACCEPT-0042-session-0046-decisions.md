---
id: ACCEPT-0042
artifact: SESSION-0046 — the product metric, skill kinds and the memory framing
artifact-revision: d82ec43
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0120, ADR-0121, ADR-0122]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0042 — Engineering understanding becomes the product metric

## Artifact

The work of `SESSION-0046`, at revision **`d82ec43`**.

Scope: `ADR-0120`, `ADR-0121`, `ADR-0122`, the Engineering Question Set,
`tools/measure.py`, `tools/check-questions.py`, and the three-kind skill
taxonomy.

**Sequence continuous.**

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **`ADR-0120` is one of the most important architectural decisions made so
  far.** Engineering Understanding is now explicitly the product metric.
- **Engineering Questions should become the primary measure of product value.
  Everything else becomes implementation telemetry.**
- `ADR-0122` is also important, **and the long-term vision is rephrased**:
  Engineering OS is not simply an Engineering Memory. It is a continuously
  improving **Engineering Understanding System**. *Memory stores. Understanding
  explains. Guidance recommends. Acquisition learns. Drift challenges.*
- Discovery Skills are becoming a primary asset of the product, and now carry
  **three maturity levels**; only levels 2 and 3 are long-lived catalog assets.
- **On the next benchmark, agreement with the session's own conclusion:** do not
  force a weak event-driven benchmark. The more valuable experiment is
  longitudinal understanding.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

Three decisions, each implemented in the session that recorded it. `ADR-0122` is
superseded by `ADR-0123` in the following session, with symmetry recorded on
both records.

## Condition 3 — validation summary

281 records, 17 fixtures, 20 registries, both query engines in agreement, and
the product metric itself checked by `tools/check-questions.py` — which found a
scoring defect two rounds of manual review had missed.

## Exceptions

None. The Organization Question level was named by the reviewer and explicitly
**not** to be built; recorded as `ADR-0126`.

## Notes

The reviewer set the next experiment and it is the one this project could not
otherwise have justified:

> Take one real repository. Run Initial Acquisition. Wait through multiple
> genuine engineering changes. Maintain the model incrementally. Run Periodic
> Reacquisition. Produce Knowledge Drift. Repeat. **This validates the central
> promise of Engineering OS: that engineering understanding survives the passage
> of time.**

And the transition the project is approaching, recorded in `ADR-0123`:

> **The product is no longer acquisition. Acquisition enables engineering
> guidance. That guidance is what customers ultimately buy.**
