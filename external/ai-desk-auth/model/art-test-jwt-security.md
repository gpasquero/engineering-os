---
id: Artifact.JwtSecurityTests
type: Artifact
label: jwt-security.spec.ts
attributes:
  source: packages/backend/src/modules/auth/__tests__/jwt-security.spec.ts
  cases: "12"
  support: confirmed
relationships:
  - validates: Artifact.AuthService
  - references: Invariant.TokenIntegrity
  - evidenced-by: Evidence.TestInventory
---
12 test cases. One node per suite, with its case count — the granularity the
Kubernetes findings recommended.
