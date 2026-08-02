---
id: ACCEPT-0032
artifact: SESSION-0036 — the Engineering Director runtime
artifact-revision: fe7a2638075b041e5d05c267d368d05c1fbd1afb
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0098, ADR-0099, ADR-0100, ADR-0101]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0032 — The Engineering Director runtime

## Artifact

The work of `SESSION-0036`, at revision
**`fe7a2638075b041e5d05c267d368d05c1fbd1afb`**.

Scope:

- The Engineering Director runtime
- The end-to-end deterministic execution loop
- Worker Registry integration
- Governance Gate execution
- Execution Observation processing

### Scope boundary

This record covers revision `fe7a263` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **The first complete execution of the Engineering Director architecture.**
- The complete deterministic loop now exists.
- The architecture remains cleanly separated between deterministic engineering
  reasoning and probabilistic execution.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Item | Decision |
|---|---|
| Director runtime, the loop, the KPI | `ADR-0098` |
| Worker Registry integration | `ADR-0099` |
| Governance Gate execution | `ADR-0100` |
| Execution Observation processing | `ADR-0101` |

## Condition 3 — validation summary

242 records verified. 17 fixtures, 9 negative, golden outputs, deterministic
rebuild. Fourteen registries, **with cross-registry references now checked** —
the check added in response to the two defects the end-to-end simulation found.

## Exceptions

None.

## Notes

**The objective becomes autonomy** (`ADR-0102`), and one invariant is now
explicitly protected: **Engineering OS may become smarter; it may not become less
deterministic** (`ADR-0103`).

The direction on structured worker confidence **conflicts with `ADR-0090`**,
which rejected confidence scores. The conflict is real and is resolved rather
than absorbed: `ADR-0104` admits confidence as an **intake signal that may only
add scrutiny**, and never as model content.

**Execution Memory is not implemented**, as directed. The proposal is
`governance/design/PROPOSAL-execution-memory.md`.
