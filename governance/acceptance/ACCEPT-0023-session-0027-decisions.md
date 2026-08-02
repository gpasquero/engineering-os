---
id: ACCEPT-0023
artifact: SESSION-0027 decisions, compiler phases and regression suite
artifact-revision: 47eebe545b4588ca568d9e21b7c04b8f4310cddd
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0072, ADR-0073, ADR-0074, ADR-0075]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0023 — SESSION-0027 decisions and the regression suite

## Artifact

The decisions and repository changes of `SESSION-0027`, at revision
**`47eebe545b4588ca568d9e21b7c04b8f4310cddd`**.

Scope:

- `ADR-0072` — the Canonical Knowledge Model is the primary product
- `ADR-0073` — compiler phases are first-class
- `ADR-0075` — entities are justified by compiler need
- Compiler pipeline improvements
- The regression suite

### Scope boundary

This record covers revision `47eebe5` and nothing after it.

`ADR-0074` was written in the same session and is **not named in this scope**.
It is carried forward as `Under Review` rather than assumed accepted — the
reviewer's scope list is taken literally (`ADR-0021`).

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- This session **establishes the compiler as the central executable component**
  of Engineering OS.
- Executable repository fixtures and deterministic regression testing confirm
  that **the architecture is now validated through implementation rather than
  documentation**.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Decision | Answers |
|---|---|
| `ADR-0072` | The reviewer's validator/compiler distinction during `ACCEPT-0022` |
| `ADR-0073` | The stages the first pipeline revealed |
| `ADR-0075` | The reviewer's direction to justify entities by compiler need |

## Condition 3 — validation summary

198 records verified for identifier consistency, bidirectional traceability,
supersession symmetry, link resolution, dangling references, duplicate headings,
entity-family declaration, inventory count and numbering, issue-index counts,
and predicate registration — 63 predicates, zero orphans.

**The regression suite is the new evidence**: ten compiler test projects, four of
which must fail, all behaving as declared. Every passing project is compiled
twice and its Canonical Knowledge Models compared, so **determinism is checked
rather than asserted**.

Ontology: 660 triples, 31 classes, 73 object properties, every property
parented.

## Exceptions

None.

## Notes

The reviewer's observations accompanying this acceptance are the largest set of
implementation directives the project has received, and they are recorded as
four decisions: `ADR-0076` (the Canonical Knowledge Model as a Layer A entity),
`ADR-0077` (declarative validation), `ADR-0078` (schema-validated parsing) and
`ADR-0079` (the Explorer as the primary interface).

`ADR-0076` required resolving a real tension with `ADR-0053`, which states that
the metamodel contains no compiler concepts.
