---
id: Artifact.AuthServiceSpec
type: Artifact
label: auth.service.spec.spec.ts
attributes:
  cases: '12'
  describes: AuthService | login | refresh
  locator: 12 cases
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T02-interpret
  rule: S4-spec-validates-module
  source: packages/backend/src/modules/auth/__tests__/auth.service.spec.ts
  support: S-tested
relationships:
- validates: Capability.Auth
---

Proposed by `W-domain-interpreter` in task `T02-interpret` and accepted through review. Support: `S-tested`.

Inferred by rule `S4-spec-validates-module`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
