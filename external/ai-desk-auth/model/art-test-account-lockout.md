---
id: Artifact.AccountLockoutTests
type: Artifact
label: account-lockout.spec.ts
attributes:
  source: packages/backend/src/modules/auth/__tests__/account-lockout.spec.ts
  cases: "8"
  support: confirmed
relationships:
  - validates: Artifact.AuthService
  - references: Invariant.AccountLockout
  - evidenced-by: Evidence.TestInventory
---
8 test cases. One node per suite, with its case count — the granularity the
Kubernetes findings recommended.
