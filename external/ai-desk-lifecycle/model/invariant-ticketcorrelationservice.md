---
id: Invariant.Ticketcorrelationservice
type: Invariant
label: TicketCorrelationService
attributes:
  established-by-cases: '1'
  granularity: concept
  locator: describe('TicketCorrelationService')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: packages/backend/src/modules/channel/correlation/ticket-correlation.service.spec.ts
  support: S-inferred
relationships:
- enforced-at: Artifact.TicketCorrelationServiceSpec
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R4-both-levels`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
