---
id: ACCEPT-0021
artifact: SESSION-0025 decisions, ordering resolution and generated graph views
artifact-revision: e7a07b84891843e73b03d5597c5117145fbbee7f
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0068]
related-issues: [ISSUE-0074]
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0021 — SESSION-0025 decisions and generated graph views

## Artifact

The decisions and repository changes of `SESSION-0025`, at revision
**`e7a07b84891843e73b03d5597c5117145fbbee7f`**.

Scope:

- `ADR-0068` — intrinsic and extrinsic ordering
- Metamodel view generation — `tools/generate-metamodel-views.py` and
  `model/metamodel/views/`
- The `StateMachine` analysis
- The `RelationshipType` refinements

### Scope boundary

This record covers revision `e7a07b8` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- This session demonstrates that Engineering OS is **beginning to validate its
  own metamodel mechanically rather than through architectural intuition**.
- **The generated views have become a design instrument rather than a
  visualization artifact.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Decision | Answers |
|---|---|
| `ADR-0068` | `FINDINGS.md` #7 |
| `StateMachine` analysis | The test set up in `ACCEPT-0020` — whether the Specification/Instance pattern survives a second independent domain |
| View generation | The reviewer's recommendation in `ACCEPT-0020` |

## Condition 3 — validation summary

**The first session in which a deterministic validator existed and ran.**

- 187 records verified for identifier consistency, bidirectional traceability,
  supersession symmetry, link resolution, dangling references, duplicate
  headings, entity-family declaration, inventory count and numbering, and
  issue-index counts computed from files.
- Ontology parsed with `rdflib`: **496 triples, 33 classes, 52 object
  properties**, no undeclared domains or ranges.
- **View generation verified deterministic** — regeneration against the
  committed output is a no-op.

That last check is qualitatively different from the others: it verifies a
generated artifact against its generator rather than a document against a
convention.

## Exceptions

None.

## Notes

The reviewer's observation reframes `ISSUE-0074` from **entity reduction** to
**metamodel normalization**, and supplies a test — independent existence — that
is stronger than structural similarity.

Both are recorded as `ADR-0069` and `ADR-0070`. Applying the second resolves
`ISSUE-0074`, and it resolves it in **two opposite directions**, which structural
similarity alone could not have distinguished.
