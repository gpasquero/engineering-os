---
id: ACCEPT-0024
artifact: SESSION-0028 decisions, compiler modularization and declarative validation
artifact-revision: c0b0b5997b266af797959ad7de81dba5d37288eb
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0074, ADR-0076, ADR-0077, ADR-0078, ADR-0079]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0024 — SESSION-0028 decisions and compiler modularization

## Artifact

The decisions and repository changes of `SESSION-0028`, at revision
**`c0b0b5997b266af797959ad7de81dba5d37288eb`**.

Scope:

- `ADR-0076` — the Canonical Knowledge Model is a Layer A entity
- The `ValidationRule` migration
- Compiler modularization
- The Canonical Knowledge Model specification
- Explorer semantic improvements

### Scope boundary

This record covers revision `c0b0b59` and nothing after it.

**`ADR-0074`, `ADR-0077`, `ADR-0078` and `ADR-0079` are not named individually**
in the reviewer's scope list, but each is the decision underlying a named item:
the ValidationRule migration is `ADR-0077`, the Explorer improvements are
`ADR-0079`, and modularization implements `ADR-0073` under `ADR-0078`'s parsing
change. They are therefore covered.

`ADR-0074` — carried forward from `ACCEPT-0023` — is covered by this record's
listing in `related-adrs` and by the CKM specification work it governs.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **Engineering OS is no longer an architectural proposal.**
- It possesses an executable compiler architecture, declarative validation,
  deterministic regression testing and **a growing semantic runtime centered on
  the Canonical Knowledge Model**.
- **The implementation continues to validate the architecture instead of merely
  following it.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Item | Decision |
|---|---|
| CKM specification | `ADR-0076` |
| ValidationRule migration | `ADR-0077` |
| Compiler modularization | `ADR-0073`, `ADR-0078` |
| Explorer semantic improvements | `ADR-0079` |

## Condition 3 — validation summary

204 records verified across identifier consistency, bidirectional traceability,
supersession symmetry, link resolution, dangling references, duplicate headings,
entity-family declaration, inventory count and numbering, issue-index counts and
predicate registration.

**The regression suite carries most of the weight now**: 13 fixtures, 7 of which
must fail, each declaring the phase and rule identifier expected. Golden outputs
for four emitters. Deterministic rebuild verified by compiling twice and
comparing.

Three findings arose from checks rather than from review: `VR-0007` caught a
two-session-old fixture defect, the predicate check caught an incomplete
vocabulary registry, and the golden tests correctly reported a discrepancy whose
cause was a stale bytecode cache rather than the code.

## Exceptions

None.

## Notes

The reviewer's direction accompanying this acceptance **redefines the goal**.
Finishing B1 is no longer the objective; the first complete vertical slice is.

Recorded as `ADR-0080` (the product is semantic answers to engineering
questions), `ADR-0081` (the Canonical Knowledge Model is the semantic
intermediate representation) and `ADR-0082` (the vertical slice replaces
metamodel completion as the milestone).
