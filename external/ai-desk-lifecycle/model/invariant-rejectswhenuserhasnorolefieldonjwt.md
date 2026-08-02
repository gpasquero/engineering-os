---
id: Invariant.RejectsWhenUserHasNoRoleFieldOnJwt
type: Invariant
label: rejects when user has no role field on JWT
attributes:
  granularity: guarantee
  locator: it('rejects when user has no role field on JWT')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: packages/backend/src/common/guards/__tests__/roles.guard.spec.ts
  support: S-inferred
relationships: []
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
