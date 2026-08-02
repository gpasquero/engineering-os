---
id: Artifact.AuthServiceTests
type: Artifact
label: auth.service.spec.ts
attributes:
  source: packages/backend/src/modules/auth/__tests__/auth.service.spec.ts
  cases: "12"
  support: confirmed
relationships:
  - validates: Artifact.AuthService
  - evidenced-by: Evidence.TestInventory
---
12 cases. **No invariant in this model is traced to it** — the suite exists and
nothing records what it guarantees.
