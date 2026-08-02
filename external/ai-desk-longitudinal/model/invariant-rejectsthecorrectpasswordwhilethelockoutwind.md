---
id: Invariant.RejectsTheCorrectPasswordWhileTheLockoutWind
type: Invariant
label: rejects the CORRECT password while the lockout window is active
attributes:
  granularity: guarantee
  locator: it('rejects the CORRECT password while the lockout window is active')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T-continuous
  rule: C1-new-suite
  source: packages/backend/src/modules/auth/__tests__/account-lockout.spec.ts
  support: S-inferred
relationships:
- specializes: Invariant.AccountLockoutBruteForceProtection
---

Proposed by `W-constraint-interpreter` in task `T-continuous` and accepted through review. Support: `S-inferred`.

Inferred by rule `C1-new-suite`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
