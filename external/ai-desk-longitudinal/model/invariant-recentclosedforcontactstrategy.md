---
id: Invariant.RecentClosedForContactStrategy
type: Invariant
label: recent_closed_for_contact strategy
attributes:
  granularity: concept
  locator: describe('recent_closed_for_contact strategy')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T-continuous
  rule: C1-new-suite
  source: packages/backend/src/modules/channel/correlation/ticket-correlation.service.spec.ts
  support: S-inferred
relationships:
- enforced-at: Artifact.TicketCorrelationServiceSpec
---

Proposed by `W-constraint-interpreter` in task `T-continuous` and accepted through review. Support: `S-inferred`.

Inferred by rule `C1-new-suite`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
