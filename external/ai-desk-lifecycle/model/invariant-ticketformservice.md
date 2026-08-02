---
id: Invariant.Ticketformservice
type: Invariant
label: TicketFormService
attributes:
  established-by-cases: '1'
  granularity: concept
  locator: describe('TicketFormService')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: packages/backend/src/modules/ticket-form/__tests__/ticket-form.service.spec.ts
  support: S-inferred
relationships:
- constrains: Capability.TicketForm
- enforced-at: Artifact.TicketFormServiceSpec
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R4-both-levels`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
