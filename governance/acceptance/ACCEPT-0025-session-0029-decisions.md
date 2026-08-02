---
id: ACCEPT-0025
artifact: SESSION-0029 decisions, the first vertical slice
artifact-revision: 17ab3fd9b0a50119041d25072549b1a90b56009b
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0080, ADR-0081, ADR-0082, ADR-0083]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0025 — SESSION-0029 decisions and the first vertical slice

## Artifact

The decisions and repository changes of `SESSION-0029`, at revision
**`17ab3fd9b0a50119041d25072549b1a90b56009b`**.

Scope:

- `ADR-0082` — the vertical slice replaces metamodel completion as the milestone
- The Vertical Slice
- `tools/ask.py`
- The Registry refactoring

### Scope boundary

This record covers revision `17ab3fd` and nothing after it.

`ADR-0080`, `ADR-0081` and `ADR-0083` are not named individually but each is the
decision underlying a named item: `ask.py` implements `ADR-0081`'s
producer/consumer rule, the Registry refactoring is `ADR-0083`, and the slice
exists because of `ADR-0080`. They are covered.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- This session demonstrates, **for the first time, the complete Engineering OS
  value proposition**.
- A developer question was successfully transformed into a semantic answer
  through the complete pipeline.
- **This is no longer a compiler demonstration. It is the first working
  Engineering OS application.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Item | Decision |
|---|---|
| Vertical Slice | `ADR-0082` |
| `tools/ask.py` | `ADR-0080`, `ADR-0081` |
| Registry refactoring | `ADR-0032`, `ADR-0083` |

## Condition 3 — validation summary

210 records verified across identifier consistency, bidirectional traceability,
supersession symmetry, link resolution, dangling references, duplicate headings,
entity-family declaration, inventory count and numbering, issue-index counts and
predicate registration.

**Predicate registration is now checked against the registry the compiler itself
reads**, not a parallel regex — a consequence of `ADR-0083` that removed one
opportunity for the validator and the compiler to disagree.

13 fixtures, 7 of which must fail, with golden outputs for four emitters.
Determinism verified by compiling twice and by regenerating every projection
after commit.

## Exceptions

None.

## Notes

**This acceptance closes the "prove the architecture" phase.** The reviewer's
direction accompanying it changes the optimization target, and is recorded as
`ADR-0084` (the phase transition and the product metric), `ADR-0085`
(question-driven development) and `ADR-0086` (the query engine is the semantic
API).
