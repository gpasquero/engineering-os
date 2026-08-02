---
id: ACCEPT-0009
artifact: SESSION-0013 decisions and associated repository changes
artifact-revision: dd3d26e
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0037, ADR-0038]
related-issues: [ISSUE-0031, ISSUE-0055, ISSUE-0056]
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0009 — SESSION-0013 decisions

## Artifact

The decisions and repository changes of `SESSION-0013`, at revision
**`dd3d26e`**.

Scope:

- `ADR-0037` — the four-layer semantic architecture
- `ADR-0038` — four questions for every new artifact type
- `ISSUE-0031` — Engineering OS self-model scope
- `ISSUE-0055` — where the Metamodel lives
- `ISSUE-0056` — the methodology artifacts have no layer
- `ACCEPT-0008`, created in that session
- The repository changes associated with this session, including the
  supersession of `ADR-0014` and the correction of `ADR-0010`'s layer
  terminology

### Scope boundary

This record covers revision `dd3d26e` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- The architectural layering is now **explicit and internally consistent**.
- Separating the Engineering OS Metamodel (Layer A) from repository knowledge
  (Layer B) establishes a **clean semantic foundation for every future
  repository adopting Engineering OS**.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Decision | Resolves |
|---|---|
| `ADR-0037` | `ISSUE-0031` and `ISSUE-0055`, resolved together as recommended |
| `ADR-0038` | — (establishes an acceptance criterion; resolves no issue) |

`ISSUE-0056` is accepted as a recorded open question.

## Condition 3 — validation summary

**No deterministic validators exist.** None are applicable, and the condition is
satisfied by the applicability rule in `ADR-0021`.

Non-deterministic checks recorded in `SESSION-0013`: 102 records verified for
identifier-to-filename consistency, bidirectional traceability, supersession
symmetry, link resolution, referenced-path existence and dangling references
across all three record types. All passed.

## Exceptions

None.

## Notes

`SESSION-0013` recorded that `ADR-0038` was failed by the existing corpus on the
day it was written, and raised `ISSUE-0056` rather than quietly exempting the
methodology directories. Accepting the session accepts that compliance debt as
correctly recorded — not as tolerable.
