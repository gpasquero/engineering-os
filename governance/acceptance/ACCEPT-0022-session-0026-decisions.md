---
id: ACCEPT-0022
artifact: SESSION-0026 decisions, normalization and first executable pipeline
artifact-revision: f2ba10ca3432a0b0bc78dc3529efb554e95c8bf6
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0069, ADR-0070, ADR-0071]
related-issues: [ISSUE-0074]
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0022 — SESSION-0026 decisions and the first executable pipeline

## Artifact

The decisions and repository changes of `SESSION-0026`, at revision
**`f2ba10ca3432a0b0bc78dc3529efb554e95c8bf6`**.

Scope:

- `ADR-0070` — the Specification criterion
- `ADR-0071` — the relationship vocabulary
- The **first executable compiler pipeline** — `tools/compile.py` and
  `examples/tiny/`
- The relationship taxonomy
- The registry simplification

### Scope boundary

This record covers revision `f2ba10c` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- This session marks the transition of Engineering OS **from an architectural
  framework into an executable engineering platform**.
- **The metamodel is no longer descriptive.** It has become an **executable
  contract enforced by the compiler**.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Decision | Answers |
|---|---|
| `ADR-0069` | The reviewer's reframing of `ISSUE-0074` during `ACCEPT-0021` |
| `ADR-0070` | `ISSUE-0074`, and `FINDINGS.md` #2 |
| `ADR-0071` | `views/README.md` #3 and #4 |

## Condition 3 — validation summary

192 records verified for identifier consistency, bidirectional traceability,
supersession symmetry, link resolution, dangling references, duplicate headings,
entity-family declaration, inventory count and numbering, and issue-index counts
computed from files.

**Three checks are new and are of a different kind:**

- **Every predicate used in an entity specification has a registered parent** —
  63 used, zero orphans. This check found and fixed a malformed relationship row.
- **Every object property in the ontology declares a parent** — 73 of 73.
- **Generation is deterministic** — regenerating the views and recompiling
  `examples/tiny` after the commit is a no-op.

The generated OWL merges with the metamodel ontology at 719 triples, with no
instance typed by an undeclared class and no edge using an undeclared property.

**Compiler rejection verified positively**: breaking the example three ways
produced exactly three errors and a non-zero exit.

## Exceptions

None.

## Notes

The reviewer's observation accompanying this acceptance draws a distinction that
reorganises the architecture: **a validator answers "is this repository
correct?"; a compiler answers "what knowledge exists in this repository?"**

Recorded as `ADR-0072`, with two further decisions it forces — `ADR-0073` on
compiler phases and `ADR-0074` on `RelationshipType` as a type system.
