---
id: Invariant.ThrowsNotfoundexceptionWhenTheTicketDoesNotE
type: Invariant
label: throws NotFoundException when the ticket does not exist
attributes:
  granularity: guarantee
  locator: it('throws NotFoundException when the ticket does not exist')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T-continuous
  rule: C1-new-suite
  source: packages/backend/src/modules/tag/__tests__/tag-by-name.spec.ts
  support: S-inferred
relationships: []
---

Proposed by `W-constraint-interpreter` in task `T-continuous` and accepted through review. Support: `S-inferred`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
