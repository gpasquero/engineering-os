---
id: Invariant.RejectsContactIdThatIsNotAUuid
type: Invariant
label: rejects contact_id that is not a UUID
attributes:
  granularity: guarantee
  locator: it('rejects contact_id that is not a UUID')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T-continuous
  rule: C1-new-suite
  source: packages/backend/src/modules/ticket/__tests__/dto-validation.spec.ts
  support: S-inferred
relationships: []
---

Proposed by `W-constraint-interpreter` in task `T-continuous` and accepted through review. Support: `S-inferred`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
