---
id: ACCEPT-0007
artifact: SESSION-0011 decisions and associated repository changes
artifact-revision: ef8e067
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0032, ADR-0033, ADR-0034]
related-issues: [ISSUE-0051, ISSUE-0052, ISSUE-0053, ISSUE-0054]
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0007 — SESSION-0011 decisions

## Artifact

The decisions and repository changes of `SESSION-0011`, at revision
**`ef8e067`**.

Scope:

- `ADR-0032` — Registry Specification versus Registry Projection
- `ADR-0033` — a `ProcessPolicy` governs a Workflow
- `ADR-0034` — the Knowledge Explorer is a per-repository projection
- `ISSUE-0054` — the Engineering OS metamodel is named but undefined
- `ACCEPT-0006`, created in that session
- The repository changes associated with this session

### Scope boundary

This record covers revision `ef8e067` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- The project has successfully **transitioned from building governance
  mechanisms to defining the first elements of the Engineering OS metamodel**.
- The distinction between normative artifacts and their governed artifacts
  continues to generalize consistently across the architecture.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Decision | Resolves |
|---|---|
| `ADR-0032` | `ISSUE-0053` — Registry authoritative or derived |
| `ADR-0033` | `ISSUE-0051` — `ProcessPolicy` versus Workflow |
| `ADR-0034` | `ISSUE-0052` — Knowledge Explorer undefined |

`ISSUE-0054` is accepted as a recorded open question.

## Condition 3 — validation summary

**No deterministic validators exist.** None are applicable, and the condition is
satisfied by the applicability rule in `ADR-0021`.

Non-deterministic checks recorded in `SESSION-0011`: 94 records verified for
identifier-to-filename consistency, bidirectional traceability, supersession
symmetry, link resolution, referenced-path existence and — newly — dangling ADR
references. All passed.

## Exceptions

None.

## Notes

The rationale marks a phase change. Eleven sessions built the mechanisms by which
this project remembers, decides and accepts. The reviewer's framing — a
transition from governance mechanisms to the first elements of the metamodel —
is the point at which the project stops describing how it will work and starts
describing what it is about.
