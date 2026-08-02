---
id: Artifact.PasswordSecuritySpec
type: Artifact
label: password-security.spec.ts
attributes:
  cases: '10'
  locator: 10 it() cases
  proposed-by: W-structure-extractor
  proposed-in: T01-extract
  source: packages/backend/src/modules/auth/__tests__/password-security.spec.ts
  support: S-tested
relationships:
- validates: Capability.Auth
---

Proposed by `W-structure-extractor` in task `T01-extract` and accepted through review. Support: `S-tested`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
