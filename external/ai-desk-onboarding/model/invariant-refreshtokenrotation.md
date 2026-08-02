---
id: Invariant.RefreshTokenRotation
type: Invariant
label: Refresh token rotation
attributes:
  asserted-by-cases: '3'
  locator: describe('Refresh token rotation')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R3-describe-names-the-invariant
  source: packages/backend/src/modules/auth/__tests__/refresh-token-rotation.spec.ts
  support: S-inferred
relationships:
- constrains: Capability.Auth
- enforced-at: Artifact.RefreshTokenRotationSpec
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R3-describe-names-the-invariant`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
