---
id: ACCEPT-0036
artifact: SESSION-0040 — two-stage Discovery and a refuted conclusion
artifact-revision: 2a13b4cdc3acd23db639bdb70c47367a285e410f
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0108, ADR-0109]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0036 — Two-stage Discovery

## Artifact

The work of `SESSION-0040`, at revision
**`2a13b4cdc3acd23db639bdb70c47367a285e410f`**.

Scope:

- Mechanical Model separation
- Deterministic interpretation experiments `R1` and `R3`
- Assertion-origin tracking
- Correction of the previously claimed deterministic ceiling

### Sequence note

**`ACCEPT-0035` is not allocated.** Requested as `ACCEPT-0036` while the highest
allocated was `ACCEPT-0034`.

**This is the second documented gap**, after `ACCEPT-0033`. The identifiers are
used as requested — the reviewer is the authority on the register — and each gap
is recorded so it is documented rather than mysterious. Validation reports an
undocumented gap and accepts a documented one.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **Brownfield Discovery must be treated as an empirical engineering process
  rather than as a fixed extractor.**
- Separating Mechanical Discovery from Interpretation made the failure
  **attributable, measurable and correctable**.
- **A current deterministic rule failing to discover a concept is not evidence
  that deterministic discovery has reached its limit.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Item | Decision |
|---|---|
| Mechanical Model separation | `ADR-0108` |
| `R1` / `R3` comparison | `ADR-0108`, which the comparison exists to enable |
| Assertion-origin tracking | `ADR-0109` |
| Ceiling correction | recorded in the ADR index corrections table against `ADR-0107` |

## Condition 3 — validation summary

256 records verified, 17 fixtures, 16 registries, golden outputs for six
emitters. **The Mechanical Model verified reproducible** — the same repository
yields digest `dd47744e6bc66150` on every run.

## Exceptions

None.

## Notes

The reviewer redirects away from optimising deterministic rules and toward a
**fair comparative benchmark**, and formalises the acquisition architecture.

Recorded as `ADR-0110` (three acquisition stages, and that the trust boundary is
review rather than determinism), `ADR-0111` (granularity is preserved at both
levels using existing constructs), and `ADR-0112` (three acquisition modes and
the Knowledge Drift Report).
