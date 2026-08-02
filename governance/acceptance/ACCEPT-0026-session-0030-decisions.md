---
id: ACCEPT-0026
artifact: SESSION-0030 decisions and the semantic query API
artifact-revision: a55f5f69b00db3e7d52c64d31862955c62c385e8
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0084, ADR-0085, ADR-0086, ADR-0087]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0026 — SESSION-0030 decisions and the semantic query API

## Artifact

The decisions and repository changes of `SESSION-0030`, at revision
**`a55f5f69b00db3e7d52c64d31862955c62c385e8`**.

Scope:

- `ADR-0084` — the prove-usefulness phase
- `ADR-0085` — question-driven development
- `ADR-0086` — the query engine is the semantic API
- `ADR-0087` — model one large external software system
- The declarative query registry
- The semantic query engine
- Explorer query execution
- Cross-engine conformance verification

### Scope boundary

This record covers revision `a55f5f6` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- This session correctly shifts Engineering OS **from entity-driven development
  to question-driven development**.
- The declarative query registry is aligned with the original objective:
  **developers and agents should interact with engineering knowledge through
  stable semantic questions rather than implementation-specific graph traversal
  code.**
- The shared query declarations and cross-engine verification are **strong
  architectural decisions**.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Item | Decision |
|---|---|
| Declarative query registry | `ADR-0086`, `ADR-0083` |
| Semantic query engine | `ADR-0086` |
| Explorer query execution | `ADR-0079`, `ADR-0086` |
| Cross-engine conformance | `ADR-0086`, which recorded the divergence risk it detects |

## Condition 3 — validation summary

216 records verified across identifier consistency, bidirectional traceability,
supersession symmetry, link resolution, dangling references, duplicate headings,
entity-family declaration, inventory count and numbering, issue-index counts and
predicate registration against the registry the compiler itself reads.

13 fixtures, 7 negative, with golden outputs, deterministic rebuild and pinned
query answers.

**Cross-engine conformance: 334 query/subject pairs, both engines agreeing.**

## Exceptions

None.

## Notes

**The query engine is now part of the product contract**, and the reviewer's
direction accompanying this acceptance requires one focused hardening iteration
before external-system findings depend on it.

Seven defects in the query semantics are named, and are addressed by `ADR-0088`:
traversal provenance reduced to a single predicate, induced-subgraph edge output,
parallel-edge ambiguity in `with`, absent query-declaration validation, absent
applicability distinction, undefined determinism and resource limits, and a
parity check that compared only identifiers.

**Every one is a case where the engine could return a plausible answer that is
wrong.** That is the correct thing to fix before a real system is modelled.
