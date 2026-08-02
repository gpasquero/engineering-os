---
id: ACCEPT-0039
artifact: SESSION-0043 — the complete Brownfield Acquisition lifecycle
artifact-revision: 2924fd550c87581f6bcbcb4c87ec36bfa66bef77
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0110, ADR-0112, ADR-0113]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0039 — The complete acquisition lifecycle

## Artifact

The work of `SESSION-0043`, at revision
**`2924fd550c87581f6bcbcb4c87ec36bfa66bef77`**.

Scope: Continuous Acquisition, Periodic Reacquisition, the Knowledge Drift
Report, and the lifecycle run against a real `ai-desk` commit.

**Sequence continuous.**

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **For the first time Engineering OS demonstrates the complete lifecycle** —
  Initial Acquisition → Engineering Change → Continuous Acquisition → Periodic
  Reacquisition → Knowledge Drift Report.
- **This is no longer an architecture demonstration. It is a product
  capability.**
- The implementation confirms an important hypothesis: **the value of Periodic
  Reacquisition is not rebuilding the model but challenging the maintained
  understanding**, and that distinction must remain explicit throughout the
  architecture.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

`ADR-0112` specified the three modes and the drift report; this session built
them. **No new decision was required**, which is the correct outcome when the
architecture is ahead of the implementation.

## Condition 3 — validation summary

266 records, 17 fixtures, 19 registries, six emitters with golden outputs, both
query engines in agreement, generation deterministic. The lifecycle run against
a real commit, with the "before" state from a detached `git worktree`.

## Exceptions

None.

## Notes

**The project enters a new phase**: from proving architecture to proving product
value.

Recorded as `ADR-0114` (drift classes drive Engineering Plans), `ADR-0115`
(Discovery Skills are a composable catalog, general and domain) and `ADR-0116`
(the product-experience admission test).
