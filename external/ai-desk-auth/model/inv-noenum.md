---
id: Invariant.NoUserEnumeration
type: Invariant
label: Wrong password and wrong email return the same error
attributes:
  source: packages/backend/src/modules/auth/__tests__/account-lockout.spec.ts
  locator: 'wrong password and wrong email return the same "Invalid credentials" error'
  support: confirmed
relationships:
  - scoped-to: BC.Auth
  - constrains: Capability.Login
  - enforced-at: Artifact.AccountLockoutTests
  - evidenced-by: Evidence.LockoutTests
---
A security guarantee stated only as a test case.
