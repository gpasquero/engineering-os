---
id: Invariant.RejectsMissingPassword
type: Invariant
label: rejects missing password
attributes:
  granularity: guarantee
  locator: it('rejects missing password')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: packages/backend/src/modules/auth/__tests__/password-security.spec.ts
  support: S-inferred
relationships:
- enforced-at: Artifact.PasswordSecuritySpec
- specializes: Invariant.PasswordPolicyRegisterdto
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R4-both-levels`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
