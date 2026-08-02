---
id: Concept.EnvJwtAccessSecret
type: Concept
label: $JWT_ACCESS_SECRET
attributes:
  env-var: JWT_ACCESS_SECRET
  locator: process.env.JWT_ACCESS_SECRET
  proposed-by: W-structure-extractor
  proposed-in: T01-extract
  source: packages/backend/src/modules/auth/__tests__/jwt-security.spec.ts
  support: S-confirmed-deterministic
relationships: []
---

Proposed by `W-structure-extractor` in task `T01-extract` and accepted through review. Support: `S-confirmed-deterministic`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
