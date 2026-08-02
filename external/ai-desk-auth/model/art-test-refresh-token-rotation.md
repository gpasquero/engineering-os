---
id: Artifact.RefreshRotationTests
type: Artifact
label: refresh-token-rotation.spec.ts
attributes:
  source: packages/backend/src/modules/auth/__tests__/refresh-token-rotation.spec.ts
  cases: "7"
  support: confirmed
relationships:
  - validates: Artifact.AuthService
  - references: Invariant.RefreshRotation
  - evidenced-by: Evidence.TestInventory
---
7 test cases. One node per suite, with its case count — the granularity the
Kubernetes findings recommended.
