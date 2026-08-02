---
id: ACCEPT-0005
artifact: SESSION-0009 decisions and associated repository changes
artifact-revision: 7af8f44
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0028, ADR-0029]
related-issues: [ISSUE-0046, ISSUE-0047, ISSUE-0049, ISSUE-0050]
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0005 — SESSION-0009 decisions

## Artifact

The decisions and repository changes of `SESSION-0009`, at revision
**`7af8f44`**.

Scope:

- `ADR-0028` — the State Machine Registry is a section of
  `KNOWLEDGE-MANIFEST.yaml`
- `ADR-0029` — Modeling Policy is a first-class artifact type
- `ISSUE-0049` — where state machine specifications live
- `ISSUE-0050` — "policy" names at least three artifact kinds
- `ACCEPT-0004`, created in that session
- The repository changes associated with this session — propagation to
  `documentation-system.md`, `glossary.md`, `repository-architecture.md`,
  `roadmap.md`, `build-state.md` and all four indexes, including the ADR index
  banner stating that the corpus is history rather than specification

### Scope boundary

This record covers revision `7af8f44` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- The repository continues to converge toward a cleaner separation between
  **historical knowledge and operational knowledge**.
- The distinction between ADRs and Policies significantly improves the long-term
  maintainability of the framework.
- The architectural direction remains coherent.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Decision | Resolves |
|---|---|
| `ADR-0028` | `ISSUE-0047` — State Machine Registry location |
| `ADR-0029` | `ISSUE-0046` — modeling guidelines have no home |

## Condition 3 — validation summary

**No deterministic validators exist.** None are applicable, and the condition is
satisfied by the applicability rule in `ADR-0021`.

Non-deterministic checks recorded in `SESSION-0009`: 83 records verified for
identifier-to-filename consistency, bidirectional traceability, supersession
symmetry, link resolution and referenced-path existence. All passed.

## Exceptions

None.

## Notes

`ISSUE-0049` and `ISSUE-0050` are accepted as *recorded open questions*, not as
resolved. Accepting an issue means the record of the unknown is correct, not
that the unknown has been answered.
