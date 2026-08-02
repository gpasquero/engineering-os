---
id: Invariant.JwtstrategySurfacesMissingFieldsAsUndefinedD
type: Invariant
label: JwtStrategy surfaces missing fields as undefined (downstream guards must reject)
attributes:
  granularity: guarantee
  locator: it('JwtStrategy surfaces missing fields as undefined (downstream guards
    mu')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T-continuous
  rule: C1-new-suite
  source: packages/backend/src/modules/auth/__tests__/jwt-security.spec.ts
  support: S-inferred
relationships:
- specializes: Invariant.JwtSecurity
---

Proposed by `W-constraint-interpreter` in task `T-continuous` and accepted through review. Support: `S-inferred`.

Inferred by rule `C1-new-suite`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
