---
id: Invariant.PasswordPolicyRegisterdto
type: Invariant
label: Password policy — RegisterDto
attributes:
  asserted-by-cases: '5'
  locator: describe('Password policy — RegisterDto')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R3-describe-names-the-invariant
  source: packages/backend/src/modules/auth/__tests__/password-security.spec.ts
  support: S-inferred
relationships:
- constrains: Capability.Auth
- enforced-at: Artifact.PasswordSecuritySpec
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R3-describe-names-the-invariant`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
