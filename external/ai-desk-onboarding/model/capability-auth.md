---
id: Capability.Auth
type: Capability
label: auth module
attributes:
  locator: NestJS module directory
  module: auth
  proposed-by: W-structure-extractor
  proposed-in: T01-extract
  source: packages/backend/src/modules/auth
  support: S-implemented
relationships:
- scoped-to: BoundedContext.Backend
---

Proposed by `W-structure-extractor` in task `T01-extract` and accepted through review. Support: `S-implemented`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
