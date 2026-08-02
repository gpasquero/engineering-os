---
id: Invariant.RejectsTheCorrectPasswordWhileTheLockoutWind
type: Invariant
label: rejects the CORRECT password while the lockout window is active
attributes:
  granularity: guarantee
  locator: it('rejects the CORRECT password while the lockout window is active')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: packages/backend/src/modules/auth/__tests__/account-lockout.spec.ts
  support: S-inferred
relationships:
- enforced-at: Artifact.AccountLockoutSpec
- specializes: Invariant.AccountLockoutBruteForceProtection
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R4-both-levels`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
