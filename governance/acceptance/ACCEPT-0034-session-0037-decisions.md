---
id: ACCEPT-0034
artifact: SESSION-0037 — autonomy and the first real-repository run
artifact-revision: 1003d575851edbff1491cff713cf5198f8ac6590
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0102, ADR-0103, ADR-0104]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0034 — Autonomy and the first real-repository run

## Artifact

The work of `SESSION-0037`, at revision
**`1003d575851edbff1491cff713cf5198f8ac6590`**.

Scope:

- Engineering Director execution against `ai-desk`
- Capability planning improvements
- Worker confidence refinement

### Scope boundary

This record covers revision `1003d57` and nothing after it.

### Sequence note

**`ACCEPT-0033` is not allocated.** The reviewer requested this record as
`ACCEPT-0034` while the highest allocated identifier was `ACCEPT-0032`.

The identifier is used as requested — the reviewer is the authority on the
register — and the gap is recorded here so it is documented rather than
mysterious. **No `ACCEPT-0033` exists and none will be allocated**, since
`ADR-0002` prohibits reuse. A sequence-contiguity check was added to validation
so that any future gap is reported rather than discovered.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- This session **validated the Engineering Director against a real engineering
  problem** and the architecture **evolved because of observed execution
  friction.**
- **That is exactly the evolution process we want.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Item | Decision |
|---|---|
| Director execution against `ai-desk` | `ADR-0102` — friction-driven change |
| Capability planning | `P-change-capability`, added because a real run could not express its workflow |
| Worker confidence | `ADR-0104`, resolving the conflict with `ADR-0090` |

## Condition 3 — validation summary

247 records verified. 17 fixtures, 9 negative, golden outputs, deterministic
rebuild. Fourteen registries with cross-references checked. Confidence
verified stripped on every intake path, including the reject paths where the
first implementation leaked it.

## Exceptions

None.

## Notes

**The reviewer identifies a skipped architectural stage**, and it is a
correction rather than an addition: the Director must operate on an **Engineering
Model**, never directly on a repository.

`ADR-0105` establishes Engineering Discovery as **the first engineering workflow
executed by Engineering OS itself**, using the same architecture as continuous
engineering.

`ADR-0106` records what that correction exposed: **a Candidate Engineering Model
and an Execution Observation are the same artifact at different scales**, so the
loop's unclosed step and the discovery intake are one problem.
