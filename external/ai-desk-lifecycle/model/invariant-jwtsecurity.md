---
id: Invariant.JwtSecurity
type: Invariant
label: JWT security
attributes:
  established-by-cases: '7'
  granularity: concept
  locator: describe('JWT security')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: packages/backend/src/modules/auth/__tests__/jwt-security.spec.ts
  support: S-inferred
relationships:
- constrains: Capability.Auth
- enforced-at: Artifact.JwtSecuritySpec
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R4-both-levels`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
