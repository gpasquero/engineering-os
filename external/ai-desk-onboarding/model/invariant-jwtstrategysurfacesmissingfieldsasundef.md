---
id: Invariant.JwtstrategySurfacesMissingFieldsAsUndef
type: Invariant
label: JwtStrategy surfaces missing fields as undefined (downstream guards must reject)
attributes:
  asserted-by: Artifact.JwtSecuritySpec
  locator: it('JwtStrategy surfaces missing fields as undefined (downstream guards
    mu')
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R1-test-name-states-a-rule
  source: packages/backend/src/modules/auth/__tests__/jwt-security.spec.ts
  support: S-inferred
relationships:
- constrains: Capability.Auth
- enforced-at: Artifact.JwtSecuritySpec
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R1-test-name-states-a-rule`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
