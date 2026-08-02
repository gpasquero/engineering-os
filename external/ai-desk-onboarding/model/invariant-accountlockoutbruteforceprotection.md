---
id: Invariant.AccountLockoutBruteForceProtection
type: Invariant
label: account lockout & brute-force protection
attributes:
  asserted-by-cases: '3'
  locator: describe('account lockout & brute-force protection')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R3-describe-names-the-invariant
  source: packages/backend/src/modules/auth/__tests__/account-lockout.spec.ts
  support: S-inferred
relationships:
- constrains: Capability.Auth
- enforced-at: Artifact.AccountLockoutSpec
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R3-describe-names-the-invariant`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
