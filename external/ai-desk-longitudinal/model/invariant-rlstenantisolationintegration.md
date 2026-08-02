---
id: Invariant.RlsTenantIsolationIntegration
type: Invariant
label: RLS tenant isolation (integration)
attributes:
  granularity: concept
  locator: describe('RLS tenant isolation (integration)')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T-continuous
  rule: C1-new-suite
  source: packages/backend/src/common/database/__tests__/tenant-isolation.integration.spec.ts
  support: S-inferred
relationships:
- enforced-at: Artifact.TenantIsolationIntegrationSpec
---

Proposed by `W-constraint-interpreter` in task `T-continuous` and accepted through review. Support: `S-inferred`.

Inferred by rule `C1-new-suite`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
