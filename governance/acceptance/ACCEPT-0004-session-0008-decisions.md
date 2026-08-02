---
id: ACCEPT-0004
artifact: SESSION-0008 decisions and associated repository changes
artifact-revision: 51bed77
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0026, ADR-0027]
related-issues: [ISSUE-0044, ISSUE-0045]
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0004 — SESSION-0008 decisions

## Artifact

The decisions and repository changes of `SESSION-0008`, at revision
**`51bed77`**.

Scope:

- `ADR-0026` — the lifecycle belongs to a Revision; state machines are named
  after the entity they govern
- `ADR-0027` — state machines are registered, not enumerated
- The issue updates created during that session (`ISSUE-0044` and `ISSUE-0045`
  resolved; `ISSUE-0046`, `ISSUE-0047` and `ISSUE-0048` opened)
- `ACCEPT-0003`, created in that session
- The repository changes associated with this review, including the
  `ArtifactLifecycle` → `ArtifactRevisionLifecycle` propagation and the new
  Corrections section of the ADR index

### Scope boundary

This record covers revision `51bed77` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- The architecture continues to increase conceptual precision.
- The distinction between Artifact and Artifact Revision **removes an entire
  class of invalid questions** rather than merely renaming concepts.
- The registration model is a scalable architectural mechanism that generalizes
  correctly beyond Engineering OS itself.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Decision | Resolves |
|---|---|
| `ADR-0026` | `ISSUE-0044` — artifact versus revision lifecycle naming |
| `ADR-0027` | `ISSUE-0045` — the state machine inventory is not fixed |

## Condition 3 — validation summary

**No deterministic validators exist.** None are applicable, and the condition is
satisfied by the applicability rule in `ADR-0021`.

Non-deterministic checks recorded in `SESSION-0008`: 78 records verified for
identifier-to-filename consistency, bidirectional traceability, supersession
symmetry, link resolution and referenced-path existence. All passed.

## Exceptions

None.

## Notes

The rationale identifies the criterion that distinguishes these two decisions
from a naming change: `ADR-0026` makes "what state is this artifact in?" a
malformed question rather than one with a misleading answer, and `ADR-0027`
produces a mechanism that works for domains nobody here has seen. Both are
generalizations rather than fixes, which is the standard the previous acceptance
established.
