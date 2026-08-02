---
id: Invariant.TicketserviceUpdateAssignmentTags
type: Invariant
label: TicketService.update — assignment + tags
attributes:
  granularity: concept
  locator: describe('TicketService.update — assignment + tags')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T-continuous
  rule: C1-new-suite
  source: packages/backend/src/modules/ticket/__tests__/update-assignment-tags.spec.ts
  support: S-inferred
relationships: []
---

Proposed by `W-constraint-interpreter` in task `T-continuous` and accepted through review. Support: `S-inferred`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
