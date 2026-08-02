---
id: ACCEPT-0016
artifact: SESSION-0020 decisions and associated repository changes
artifact-revision: ba530b5
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0057, ADR-0058, ADR-0059]
related-issues: [ISSUE-0069, ISSUE-0070, ISSUE-0071]
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0016 — SESSION-0020 decisions

## Artifact

The decisions and repository changes of `SESSION-0020`, at revision
**`ba530b5`**.

Scope:

- `ADR-0057` — Naming Qualification
- `ADR-0058` — Principles are semantic entities, not artifacts
- `ADR-0059` — authored versus discovered knowledge
- `ISSUE-0071` — how discovered knowledge is produced
- `ACCEPT-0015`, created in that session
- The repository changes associated with this session

### Scope boundary

This record covers revision `ba530b5` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- The project has successfully distinguished between **authored knowledge and
  discovered knowledge**.
- This is a major architectural step because it establishes the future role of
  the Knowledge Compiler as a **deterministic reasoning engine while preserving
  human judgment where interpretation is required**.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Decision | Resolves |
|---|---|
| `ADR-0057` | `ISSUE-0069` — "Level" and "Process" reused |
| `ADR-0058` | `ISSUE-0070` — are Principles an artifact type? |
| `ADR-0059` | — (establishes the distinction; resolves no issue) |

`ISSUE-0071` is accepted as a recorded open question.

## Condition 3 — validation summary

**No deterministic validators exist.** None are applicable, and the condition is
satisfied by the applicability rule in `ADR-0021`.

Non-deterministic checks recorded in `SESSION-0020`: 145 records verified for
identifier-to-filename consistency, bidirectional traceability, supersession
symmetry, link resolution, referenced-path existence, dangling references across
all three record types, and duplicate headings. All passed.

## Exceptions

None.

## Notes

The rationale states the boundary the session recorded as an open tension.
`SESSION-0020` reported that `ADR-0059`'s ambition collided with `ADR-0020`'s
determinism requirement, and recorded a reading that would preserve both. The
reviewer confirms that reading as the intent: **the compiler is a deterministic
reasoning engine, and human judgment stays where interpretation is required.**
