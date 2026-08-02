---
id: Artifact.AuthController
type: Artifact
label: auth.controller.ts
attributes:
  locator: '@Controller(''auth''), 3 routes'
  prefix: auth
  proposed-by: W-structure-extractor
  proposed-in: T01-extract
  routes: '3'
  source: packages/backend/src/modules/auth/auth.controller.ts
  support: S-implemented
relationships:
- implements: Capability.Auth
---

Proposed by `W-structure-extractor` in task `T01-extract` and accepted through review. Support: `S-implemented`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
