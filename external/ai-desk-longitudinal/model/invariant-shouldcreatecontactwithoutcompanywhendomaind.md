---
id: Invariant.ShouldCreateContactWithoutCompanyWhenDomainD
type: Invariant
label: should create contact without company when domain does not match
attributes:
  granularity: guarantee
  locator: it('should create contact without company when domain does not match')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T-continuous
  rule: C1-new-suite
  source: packages/backend/src/modules/contact/__tests__/contact.service.spec.ts
  support: S-inferred
relationships:
- enforced-at: Artifact.ContactServiceSpec
- specializes: Invariant.Contactservice
---

Proposed by `W-constraint-interpreter` in task `T-continuous` and accepted through review. Support: `S-inferred`.

Inferred by rule `C1-new-suite`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
