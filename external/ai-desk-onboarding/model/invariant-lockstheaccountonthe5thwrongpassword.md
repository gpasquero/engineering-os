---
id: Invariant.LocksTheAccountOnThe5ThWrongPassword
type: Invariant
label: locks the account on the 5th wrong password for exactly 15 minutes
attributes:
  asserted-by: Artifact.AccountLockoutSpec
  locator: it('locks the account on the 5th wrong password for exactly 15 minutes')
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R1-test-name-states-a-rule
  source: packages/backend/src/modules/auth/__tests__/account-lockout.spec.ts
  support: S-inferred
relationships:
- constrains: Capability.Auth
- enforced-at: Artifact.AccountLockoutSpec
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R1-test-name-states-a-rule`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
