---
id: Invariant.ScopesTheTagLookupByTenantidTenantIsolation
type: Invariant
label: scopes the tag lookup by tenantId (tenant isolation)
attributes:
  granularity: guarantee
  locator: it('scopes the tag lookup by tenantId (tenant isolation)')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: packages/backend/src/modules/tag/__tests__/tag-by-name.spec.ts
  support: S-inferred
relationships: []
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
