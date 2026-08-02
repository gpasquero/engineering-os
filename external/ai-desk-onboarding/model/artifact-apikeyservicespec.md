---
id: Artifact.ApiKeyServiceSpec
type: Artifact
label: api-key.service.spec.spec.ts
attributes:
  cases: '11'
  describes: ApiKeyService | create | list
  locator: 11 cases
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T02-interpret
  rule: S4-spec-validates-module
  source: packages/backend/src/modules/api-key/__tests__/api-key.service.spec.ts
  support: S-tested
relationships:
- validates: Capability.ApiKey
---

Proposed by `W-domain-interpreter` in task `T02-interpret` and accepted through review. Support: `S-tested`.

Inferred by rule `S4-spec-validates-module`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
