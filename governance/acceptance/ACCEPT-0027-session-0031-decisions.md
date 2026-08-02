---
id: ACCEPT-0027
artifact: SESSION-0031 decisions and the query result contract
artifact-revision: c655fd766e28a4451cdda81b84e76c9900d7fdb3
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0088]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0027 — SESSION-0031 decisions and query-result hardening

## Artifact

The decisions and repository changes of `SESSION-0031`, at revision
**`c655fd766e28a4451cdda81b84e76c9900d7fdb3`**.

Scope:

- `ADR-0088` — the query result contract
- Query-result contract hardening
- Full path provenance
- Edge-output correction
- Parallel-edge handling
- Query declaration validation
- Applicability semantics
- Deterministic ordering and traversal limits
- Cross-engine semantic parity

### Scope boundary

This record covers revision `c655fd7` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- The reviewed commit addresses **the most dangerous failure mode for a semantic
  API: plausible but incorrect answers.**
- The result contract now preserves paths, distinguishes applicability from
  emptiness, rejects malformed declarations, handles parallel edges correctly and
  verifies parity beyond final identifiers.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

Every item in scope is a numbered clause of `ADR-0088`, which records the seven
defects and their corrections.

## Condition 3 — validation summary

219 records verified across the standard governance checks.

- **14 fixtures**, 8 negative, with golden outputs, deterministic rebuild, and
  pinned query rows, status and paths.
- **12 malformed query declarations, all rejected** by
  `tools/check-query-schema.py`.
- **334 query/subject pairs** agreeing across both engines on status, rows,
  paths, ordering, edges and diagnostics.

The parity check found a real divergence on its first full-fidelity run —
JavaScript's `localeCompare` does not order like Python's codepoint comparison —
which identifier-only comparison had reported as agreement.

## Exceptions

None.

## Notes

**The semantic API is hardened enough for external-system validation.** The
reviewer's direction is to stop extending the query language and use it against a
real system: **Kubernetes Server-Side Apply and managed fields.**

The charter for that validation is
`external/kubernetes-ssa/charter.md`, written before any modeling began, as
directed.
