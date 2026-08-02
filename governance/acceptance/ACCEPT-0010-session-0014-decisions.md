---
id: ACCEPT-0010
artifact: SESSION-0014 decisions and associated repository changes
artifact-revision: c8e50a2
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0039, ADR-0040]
related-issues: [ISSUE-0056, ISSUE-0057, ISSUE-0058]
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0010 — SESSION-0014 decisions

## Artifact

The decisions and repository changes of `SESSION-0014`, at revision
**`c8e50a2`**.

Scope:

- `ADR-0039` — layers classify artifacts, not directories
- `ADR-0040` — Architectural Dimensions
- `ISSUE-0057` — the dimension set is examples, and four are undefined
- `ISSUE-0058` — how an artifact declares its classification
- `ACCEPT-0009`, created in that session
- The repository changes associated with this session, including the correction
  of `ADR-0037` and the demotion of the directory contracts to implementation
  guidance

### Scope boundary

This record covers revision `c8e50a2` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- The architecture has evolved **from a single classification model into a
  multidimensional semantic model**.
- This significantly improves extensibility and **removes the need to overload
  concepts with multiple unrelated meanings**.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Decision | Resolves |
|---|---|
| `ADR-0039` | `ISSUE-0056` — the methodology artifacts had no layer |
| `ADR-0040` | — (establishes a modeling rule; resolves no issue) |

`ISSUE-0057` and `ISSUE-0058` are accepted as recorded open questions.

## Condition 3 — validation summary

**No deterministic validators exist.** None are applicable, and the condition is
satisfied by the applicability rule in `ADR-0021`.

Non-deterministic checks recorded in `SESSION-0014`: 107 records verified for
identifier-to-filename consistency, bidirectional traceability, supersession
symmetry, link resolution, referenced-path existence, dangling references across
all three record types, and — newly — duplicate headings within acceptance
records, after one was found and corrected. All passed.

## Exceptions

None.

## Notes

The rationale names the transition precisely. Five vocabulary collisions were
resolved by splitting overloaded terms, each a local remedy. `ADR-0040` replaced
the single classification model with a multidimensional one, which is why the
overloading pressure disappears rather than being relieved case by case.
