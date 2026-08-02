---
id: ACCEPT-0040
artifact: SESSION-0044 — drift routing, the skill catalog and the product-experience test
artifact-revision: 20c75024c5d92b791b773b2fb8d570f3fd889958
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0114, ADR-0115, ADR-0116]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0040 — Drift routing, the skill catalog, and a product-oriented test

## Artifact

The work of `SESSION-0044`, at revision
**`20c75024c5d92b791b773b2fb8d570f3fd889958`**.

Scope: `ADR-0114`, `ADR-0115`, `ADR-0116`, the fifteen routed drift classes, the
eight Engineering Plans, `tools/drift-queue.py`, the not-applicable step
reporting in the planner, and the two checks committed as
`tools/check-plans.py` and `tools/check-governance.py`.

**Sequence continuous.**

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **`ADR-0116` is an important milestone.** It is **the first architectural
  decision whose admission criterion is explicitly product-oriented rather than
  architecture-oriented**, and that direction is to be kept.
- From now on, **architecture should increasingly be justified by improvements
  to real engineering work on Brownfield systems**.
- **The Discovery Skill catalog is now sufficiently established.** It is not to
  be populated exhaustively; it is an evolving engineering asset driven by
  repeated use on real systems.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

Three decisions, each carrying its own rationale and compliance section; each
implemented in the same session that recorded it.

## Condition 3 — validation summary

271 records, 17 fixtures, both query engines in agreement, generation
deterministic, and — for the first time — the governance corpus checked by a
committed tool rather than by a script retyped from memory.

## Exceptions

None.

## Notes

The reviewer set the next objective: **validate generalization**, against
repositories chosen to exercise **different engineering characteristics rather
than different programming languages**, with a **Spring Boot business
application** first.

The accompanying discipline is explicit and is recorded as `ADR-0119`:

> **Do not optimize Discovery Skills after the first repository. Use each
> repository as a benchmark. Only when the same limitation appears repeatedly
> should Engineering OS evolve.**

Also recorded: `ADR-0117` (Stack Profiles) and `ADR-0118` (the three acquisition
modes are product capabilities).
