---
id: ACCEPT-0030
artifact: SESSION-0034 — the Engineering Planning Engine
artifact-revision: f49b1a1810e22f88685cd7ed91723ffe3bd0e86d
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0092, ADR-0093, ADR-0094]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0030 — The Engineering Planning Engine

## Artifact

The work of `SESSION-0034`, at revision
**`f49b1a1810e22f88685cd7ed91723ffe3bd0e86d`**.

Scope:

- Engineering Plan generation
- The deterministic planning pipeline
- Planning metrics
- The `EngineeringIntent` architectural proposal

### Scope boundary

This record covers revision `f49b1a1` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **The first artifact that starts looking like an engineering decision engine
  instead of a semantic knowledge system.**
- The separation between deterministic reasoning and probabilistic
  implementation is preserved.
- **This direction is correct.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Item | Decision |
|---|---|
| Engineering Plan generation | `ADR-0094` |
| Deterministic planning pipeline | `ADR-0092` |
| Planning metrics | `ADR-0093` |
| `EngineeringIntent` proposal | requested before implementation; **nothing was built** |

## Condition 3 — validation summary

231 records verified across the standard governance checks. 17 fixtures, 9
negative, golden outputs, deterministic rebuild. 981 query/subject pairs in
full-fidelity parity across four projects. Eight registries. The metamodel
unchanged for three milestones.

## Exceptions

None.

## Notes

**The `EngineeringIntent` proposal is accepted as recommended.** The reviewer
confirms it should **not** become a Layer A entity — it is part of an engineering
session, not of the software knowledge — and that a declarative registry is the
correct abstraction. **Do not promote it unless reality forces it.**

Recorded as `ADR-0096`.

The reviewer also fixes the architecture around the complete engineering loop
(`ADR-0095`) and names the next artifact: a deterministic **TaskGraph** derived
from the plan (`ADR-0097`).
