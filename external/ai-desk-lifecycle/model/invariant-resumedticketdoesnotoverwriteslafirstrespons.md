---
id: Invariant.ResumedTicketDoesNotOverwriteSlafirstrespons
type: Invariant
label: resumed ticket does not overwrite slaFirstResponseDueAt if first response already
  met
attributes:
  granularity: guarantee
  locator: it('resumed ticket does not overwrite slaFirstResponseDueAt if first respo')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: packages/backend/src/modules/sla/__tests__/sla-timer.service.spec.ts
  support: S-inferred
relationships:
- enforced-at: Artifact.SlaTimerServiceSpec
- specializes: Invariant.SlatimerservicePauseResumeEdgeCases
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R4-both-levels`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
