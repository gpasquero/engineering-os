---
id: ACCEPT-0045
artifact: SESSION-0049 — semantic preservation and the move to the team
artifact-revision: d6d3bef
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0132, ADR-0133, ADR-0134, ADR-0135, ADR-0136]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0045 — Questions become the contract

## Artifact

The work of `SESSION-0049`, at revision **`d6d3bef`**.

Scope: `ADR-0132`–`ADR-0136`, semantic preservation in Continuous Acquisition,
the `preserves` field, `C4-new-routes`, and the frozen-suite rerun reaching
100 % Understanding Retention.

**Sequence continuous.**

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **Engineering Questions are no longer just a benchmark. They are becoming the
  contract of the product.** Everything underneath may evolve; the questions
  should remain stable.
- **`ADR-0135` is especially important.** Engineering OS is two cooperating
  products sharing one model, and **the Engineering Model is the API between
  them**.
- **`ADR-0136` is the strongest North Star the project has had** — *"we preserve
  an engineering team's ability to make correct engineering decisions as
  software evolves"* — and it will eventually become part of the public
  positioning. **Do not optimize that sentence. Build toward it.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

Five decisions, each implemented in the session that recorded it, against an
acceptance criterion written before the work began and met exactly.

## Condition 3 — validation summary

301 records, 17 fixtures, 20 registries, both query engines in agreement, and
the frozen suite rerun with its baseline preserved.

## Exceptions

None. A prediction in `ADR-0130` — that the fix would add zero knowledge — was
recorded as refuted rather than restated.

## Notes

The reviewer named the harder question the project is approaching:

> **The customer does not buy Understanding Preservation. The customer buys
> Decision Preservation.** Two systems may answer exactly the same Engineering
> Questions while recommending different engineering actions. **I would resist
> the temptation to invent another metric** — begin thinking about how it could
> eventually become experimentally measurable.

And three directions, recorded as decisions:

- the benchmark begins measuring **Guidance** (`ADR-0139`);
- **do not continue optimizing Brownfield Discovery** — the next major
  capability is the non-deterministic **Brownfield Onboarding Skill**
  (`ADR-0140`);
- **the customer lifecycle** is probably more important than the compiler
  architecture (`ADR-0141`).
