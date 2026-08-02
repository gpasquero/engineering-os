---
id: ACCEPT-0013
artifact: SESSION-0017 decisions and associated repository changes
artifact-revision: 1345bfc
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0048, ADR-0049, ADR-0050]
related-issues: [ISSUE-0062, ISSUE-0064, ISSUE-0065, ISSUE-0066]
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0013 — SESSION-0017 decisions

## Artifact

The decisions and repository changes of `SESSION-0017`, at revision
**`1345bfc`**.

Scope:

- `ADR-0048` — `DimensionSpecification` is a metamodel entity
- `ADR-0049` — dimensions are a scarce architectural resource
- `ADR-0050` — the `Definition → Instance → Assignment → Projection` hierarchy
- `ISSUE-0065` — nine dimension candidates, none evaluated
- `ISSUE-0066` — where the Registry Specification sits in the hierarchy
- `ACCEPT-0012`, created in that session
- The repository changes associated with this session

### Scope boundary

This record covers revision `1345bfc` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- The project continues to **replace isolated architectural decisions with
  reusable metamodel patterns**.
- The `Definition → Instance → Assignment → Projection` hierarchy significantly
  improves conceptual consistency and **provides a common modeling vocabulary
  for future extensible concepts**.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Decision | Resolves |
|---|---|
| `ADR-0048` | `ISSUE-0062` — four dimensions undefined |
| `ADR-0049` | `ISSUE-0064` — Representation versus Semantic Layer |
| `ADR-0050` | — (establishes the hierarchy; resolves no issue) |

`ISSUE-0065` and `ISSUE-0066` are accepted as recorded open questions.

## Condition 3 — validation summary

**No deterministic validators exist.** None are applicable, and the condition is
satisfied by the applicability rule in `ADR-0021`.

Non-deterministic checks recorded in `SESSION-0017`: 128 records verified for
identifier-to-filename consistency, bidirectional traceability, supersession
symmetry, link resolution, referenced-path existence, dangling references across
all three record types, and duplicate headings. All passed.

## Exceptions

None.

## Notes

The hierarchy accepted here is corrected in the following session:
`SESSION-0017` recorded that naming it immediately exposed what it did not cover
(`ISSUE-0066`), and the fourth stage turns out to belong to a different
architecture. The acceptance stands — the hierarchy was correct about what it
described, and incomplete about its own boundary.
