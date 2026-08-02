---
id: Artifact.PasswordSecurityTests
type: Artifact
label: password-security.spec.ts
attributes:
  source: packages/backend/src/modules/auth/__tests__/password-security.spec.ts
  cases: "11"
  support: confirmed
relationships:
  - validates: Artifact.AuthService
  - evidenced-by: Evidence.TestInventory
---
11 cases. Same gap: no invariant is traced to it.
