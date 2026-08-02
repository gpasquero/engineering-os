---
id: ACCEPT-0015
artifact: SESSION-0019 decisions and associated repository changes
artifact-revision: 4d1c8d0
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0054, ADR-0055, ADR-0056]
related-issues: [ISSUE-0067, ISSUE-0068, ISSUE-0069, ISSUE-0070]
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0015 — SESSION-0019 decisions

## Artifact

The decisions and repository changes of `SESSION-0019`, at revision
**`4d1c8d0`**.

Scope:

- `ADR-0054` — Engineering Gate is a first-class metamodel concept
- `ADR-0055` — evaluation questions belong to Gates; supersedes `ADR-0038`
- `ADR-0056` — Principle, Policy, Process
- `ISSUE-0069` — "Level" and "Process" reused for new schemes
- `ISSUE-0070` — are Principles a first-class artifact type?
- `ACCEPT-0014`, created in that session
- The repository changes associated with this session

### Scope boundary

This record covers revision `4d1c8d0` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- The architecture is now beginning to **distinguish stable engineering
  knowledge from operational engineering knowledge**.
- The introduction of Engineering Gates **completes the process architecture**
  and removes an important source of coupling between semantic concepts and
  review procedures.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Decision | Resolves |
|---|---|
| `ADR-0054` | `ISSUE-0067` — Dimension Review artifact type |
| `ADR-0055` | `ISSUE-0068` — compiler-phase question versus the separation |
| `ADR-0056` | — (establishes the three levels; resolves no issue) |

`ISSUE-0069` and `ISSUE-0070` are accepted as recorded open questions.

## Condition 3 — validation summary

**No deterministic validators exist.** None are applicable, and the condition is
satisfied by the applicability rule in `ADR-0021`.

Non-deterministic checks recorded in `SESSION-0019`: 140 records verified for
identifier-to-filename consistency, bidirectional traceability, supersession
symmetry, link resolution, referenced-path existence, dangling references across
all three record types, and duplicate headings. All passed.

## Exceptions

None.

## Notes

The rationale names the decoupling `ADR-0055` achieved without stating it in
those terms: moving evaluation questions from artifacts to Gates removed a
coupling between *what a concept is* and *how it is reviewed*. The session
recorded the consequence — that triggering conditions became the entire
enforcement surface — as a cost; the reviewer records the decoupling as the
point.
