---
id: Invariant.AccountLockout
type: Invariant
label: Five wrong passwords lock the account for exactly 15 minutes
attributes:
  source: packages/backend/src/modules/auth/__tests__/account-lockout.spec.ts
  locator: "locks the account on the 5th wrong password for exactly 15 minutes"
  support: confirmed
relationships:
  - scoped-to: BC.Auth
  - constrains: Capability.Login
  - enforced-at: Artifact.AccountLockoutTests
  - evidenced-by: Evidence.LockoutTests
---
**Asserted by a test and by no fetched document.** The correct password is
rejected while the window is active, and lockout is per-agent.
