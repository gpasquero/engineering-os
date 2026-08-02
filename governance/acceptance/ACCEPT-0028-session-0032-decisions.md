---
id: ACCEPT-0028
artifact: SESSION-0032 — the external Kubernetes validation
artifact-revision: 6d5da52b3cf3ade8db0208496739d1d89ec3ca0e
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0087]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0028 — The external Kubernetes validation

## Artifact

The work of `SESSION-0032`, at revision
**`6d5da52b3cf3ade8db0208496739d1d89ec3ca0e`**.

Scope:

- `ADR-0087` completion
- The external Kubernetes validation
- Provenance improvements
- Query validation against real sources

### Scope boundary

This record covers revision `6d5da52` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **The first successful external validation of Engineering OS.**
- A real software subsystem was modelled **without changing the compiler, the
  metamodel or the query language**, and the resulting Canonical Knowledge Model
  revealed engineering knowledge **not explicitly available in any individual
  source**.
- **The first evidence that Engineering OS generalizes beyond itself.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

`ADR-0087` set nine completion criteria. All nine are met and recorded in
`governance/build-state.md`. The charter fixing scope was written before any
modeling, as that decision requires.

## Condition 3 — validation summary

221 records verified across the standard governance checks.

- **16 fixtures**, 9 negative, golden outputs, deterministic rebuild, pinned
  query rows, status and paths.
- **832 query/subject pairs** across three projects agreeing on status, rows,
  paths, ordering, edges and diagnostics.
- 12 malformed query declarations rejected.
- Every external source **fetched and verified before authoring**; every
  unverified claim marked `support: incomplete` and classified `ambiguous`.

## Exceptions

None.

## Notes

**This acceptance changes what the project optimises for.** Three progressively
stronger claims have now been demonstrated — Engineering OS can model itself,
compile itself, and explain a real external system.

The next target is not proving that it works but proving that it becomes
**indispensable**. Recorded as `ADR-0089` (engineering value is the optimization
target), `ADR-0090` (the finding taxonomy, and no confidence scores) and
`ADR-0091` (Engineering Recommendation).
