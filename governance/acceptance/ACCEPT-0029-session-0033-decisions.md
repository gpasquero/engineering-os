---
id: ACCEPT-0029
artifact: SESSION-0033 — the Engineering Recommendation Engine
artifact-revision: 0499e77499018f4f8700a389d2cf44ea42eb44bb
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0089, ADR-0090, ADR-0091]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0029 — The Engineering Recommendation Engine

## Artifact

The work of `SESSION-0033`, at revision
**`0499e77499018f4f8700a389d2cf44ea42eb44bb`**.

Scope:

- The Engineering Recommendation Engine
- `tools/advise.py`
- The recommendation taxonomy
- The `has-path` query operator
- External Kubernetes validation improvements

### Scope boundary

This record covers revision `0499e77` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **The first transition from semantic answers to engineering guidance.**
- Engineering OS is no longer limited to answering engineering questions. It
  produces **explainable engineering recommendations whose provenance is
  completely traceable through declarative semantic queries.**
- **A major product milestone.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Item | Decision |
|---|---|
| Recommendation engine, `advise.py`, taxonomy | `ADR-0091` |
| Finding classification applied to the Kubernetes model | `ADR-0090` |
| `has-path` | the second gap external validation found; recorded in `FINDINGS.md` |

## Condition 3 — validation summary

226 records verified across the standard governance checks.

- **17 fixtures**, 9 negative, golden outputs, deterministic rebuild, pinned
  query rows, status and paths.
- **981 query/subject pairs** across four projects, full-fidelity parity.
- 12 malformed query declarations rejected; recommendations validated at load.
- Seven registries; the metamodel unchanged for two milestones.

## Exceptions

None.

## Notes

**This acceptance redirects the project.** Engineering OS stops being optimized
as a semantic compiler and begins optimizing as an **Engineering Director**.

Recorded as `ADR-0092` (the Engineering Director is the product), `ADR-0093` (the
success measure), and `ADR-0094` (the Engineering Plan).

`EngineeringIntent` is **deliberately not implemented**. A short architectural
proposal is delivered instead, as directed:
`governance/design/PROPOSAL-engineering-intent.md`.
