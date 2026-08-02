---
id: ACCEPT-0037
artifact: SESSION-0041 — three acquisition stages and the first comparative benchmark
artifact-revision: 288a3516a7280e63ffc8c15d912de075e15b00a4
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0110, ADR-0111, ADR-0112]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0037 — Acquisition stages and the first benchmark

## Artifact

The work of `SESSION-0041`, at revision
**`288a3516a7280e63ffc8c15d912de075e15b00a4`**.

Scope:

- The frozen Mechanical Model benchmark
- The `R1`, `R3`, `R4` and Claude interpreter comparison
- The interpretation-failure taxonomy
- Cross-source synthesis findings
- Granularity modeling through existing metamodel constructs

### Sequence note

**Continuous.** `ACCEPT-0037` follows `ACCEPT-0036` with no gap. The two earlier
gaps — `ACCEPT-0033` and `ACCEPT-0035` — remain documented in the index.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- The session **correctly separates extraction volume, abstraction and
  cross-source synthesis as independent acquisition capabilities.**
- It demonstrates that deterministic and probabilistic interpreters are
  **complementary rather than competing** implementations of one capability.
- **The explicit acknowledgement of benchmark contamination and unsupported
  generalization is important and should remain part of the record.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Item | Decision |
|---|---|
| Three stages, failure taxonomy | `ADR-0110` |
| Granularity via `specializes` | `ADR-0111` |
| Acquisition modes and drift | `ADR-0112` |
| Frozen Mechanical Model as shared input | `ADR-0108` |

## Condition 3 — validation summary

261 records verified, 17 fixtures, 18 registries, golden outputs for six
emitters. The Mechanical Model reproducible at digest `dd47744e6bc66150`.

## Exceptions

None.

## Notes

**The benchmark question is answered and interpreter experimentation stops after
one final blind run.** Deterministic workers provide reproducible breadth and
precise local guarantees; probabilistic workers propose cross-source
abstractions and distribution-level observations.

The next bottleneck is **packaging acquisition into a reusable Brownfield
Onboarding workflow**, and `ADR-0113` records what that packaging is: **Discovery
Skills — engine-independent investigation contracts owned by Engineering OS, of
which a model is only a worker implementation.**
