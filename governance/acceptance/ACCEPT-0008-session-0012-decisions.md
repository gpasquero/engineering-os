---
id: ACCEPT-0008
artifact: SESSION-0012 decisions and associated repository changes
artifact-revision: 2d35b74
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0035, ADR-0036]
related-issues: [ISSUE-0054, ISSUE-0055]
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0008 — SESSION-0012 decisions

## Artifact

The decisions and repository changes of `SESSION-0012`, at revision
**`2d35b74`**.

Scope:

- `ADR-0035` — the Engineering OS Metamodel
- `ADR-0036` — the Canonical Knowledge Model conforms to the Metamodel
- `ISSUE-0055` — where the Metamodel lives
- `ACCEPT-0007`, created in that session
- The repository changes associated with this session, including the metamodel
  process gate added to the session protocol and the reordering of M2

### Scope boundary

This record covers revision `2d35b74` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- The project has reached the point where **the metamodel becomes the
  architectural center of gravity**.
- Positioning the metamodel before defining the compiler interface **preserves
  implementation independence** and makes future compiler implementations
  conform to a shared semantic contract rather than to an existing
  implementation.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Decision | Resolves |
|---|---|
| `ADR-0035` | `ISSUE-0054` — the metamodel was named but undefined |
| `ADR-0036` | — (establishes conformance; resolves no issue) |

`ISSUE-0055` is accepted as a recorded open question.

## Condition 3 — validation summary

**No deterministic validators exist.** None are applicable, and the condition is
satisfied by the applicability rule in `ADR-0021`.

Non-deterministic checks recorded in `SESSION-0012`: 98 records verified for
identifier-to-filename consistency, bidirectional traceability, supersession
symmetry, link resolution, referenced-path existence and dangling references
across all three record types. All passed.

## Notes

The rationale endorses accepting a real cost. `ADR-0036` gated M2's readiest
deliverable — the compiler interface specification — on a metamodel that did not
exist. The reviewer names why that trade is correct: a compiler interface
defined first would have made the metamodel describe one implementation's
choices, and `ADR-0017`'s promise of multiple implementations unachievable.

## Exceptions

None.
