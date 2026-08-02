---
id: Invariant.TicketserviceMergeAdditionalScenarios
type: Invariant
label: TicketService.merge — additional scenarios
attributes:
  granularity: concept
  locator: describe('TicketService.merge — additional scenarios')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T-continuous
  rule: C1-new-suite
  source: packages/backend/src/modules/ticket/__tests__/ticket-merge-extra.spec.ts
  support: S-inferred
relationships:
- enforced-at: Artifact.TicketMergeExtraSpec
---

Proposed by `W-constraint-interpreter` in task `T-continuous` and accepted through review. Support: `S-inferred`.

Inferred by rule `C1-new-suite`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
