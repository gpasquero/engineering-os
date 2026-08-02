---
id: ACCEPT-0020
artifact: SESSION-0024 decisions, operational family and second OWL checkpoint
artifact-revision: 1fdc3378150b2b82feb143519bfc2f5b407315e6
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0066, ADR-0067]
related-issues: [ISSUE-0074]
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0020 — SESSION-0024 decisions and operational family

## Artifact

The decisions and repository changes of `SESSION-0024`, at revision
**`1fdc3378150b2b82feb143519bfc2f5b407315e6`**.

Scope:

- `ADR-0066` — `RelationshipType`, not `Relationship`
- `ADR-0067` — the relationship is the design unit
- `ISSUE-0074` — the scheduled metamodel simplification review
- The seven operational metamodel entities
- The second OWL checkpoint

### Scope boundary

This record covers revision `1fdc337` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- This session validates that the metamodel is **being shaped primarily through
  implementation feedback rather than architectural speculation**.
- The emergence of distinct operational semantics confirms that the
  descriptive/operational split represents **a genuine structural property of the
  model rather than an imposed categorization**.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Decision | Answers |
|---|---|
| `ADR-0066` | `FINDINGS.md` #1, and #5 as a consequence |
| `ADR-0067` | The reviewer's observation during `ACCEPT-0019` |
| `ISSUE-0074` | `FINDINGS.md` #2, deferred rather than resolved |

The seven operational specifications each answer the `ADR-0067` question, which
is the traceability that decision requires of them.

## Condition 3 — validation summary

**No deterministic validators exist**, and the condition is satisfied by the
applicability rule in `ADR-0021`.

Checks recorded in `SESSION-0024`: 184 records verified for identifier
consistency, bidirectional traceability, supersession symmetry, link resolution,
dangling references, duplicate headings, family declaration on every entity
specification, inventory count accuracy, and **issue-index counts computed from
the files rather than asserted**.

Ontology verified mechanically: **433 triples, 30 classes, 45 object properties,
5 datatype properties**, parsed with `rdflib`, no undeclared domains or ranges.

## Exceptions

None.

## Notes

The reviewer's observation accompanying this acceptance marks a change in what
the checkpoints are finding: **the design is no longer revealing missing
entities, it is revealing missing semantic constructs.** That distinction is
recorded in `ADR-0068`, which answers the first such construct — ordering — and
finds that it required no new construct at all.
