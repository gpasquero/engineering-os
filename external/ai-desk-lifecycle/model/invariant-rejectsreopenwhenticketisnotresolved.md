---
id: Invariant.RejectsReopenWhenTicketIsNotResolved
type: Invariant
label: rejects reopen when ticket is not resolved
attributes:
  granularity: guarantee
  locator: it('rejects reopen when ticket is not resolved')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: packages/backend/src/modules/ticket/__tests__/ticket.service.spec.ts
  support: S-inferred
relationships:
- enforced-at: Artifact.TicketServiceSpec
- specializes: Invariant.Ticketservice
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R4-both-levels`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
