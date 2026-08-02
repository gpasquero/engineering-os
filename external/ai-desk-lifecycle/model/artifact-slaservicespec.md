---
id: Artifact.SlaServiceSpec
type: Artifact
label: sla.service.spec.spec.ts
attributes:
  cases: '14'
  describes: SlaService | createPolicy | findPolicyById
  locator: 14 cases
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T02-interpret
  rule: S4-spec-validates-module
  source: packages/backend/src/modules/sla/__tests__/sla.service.spec.ts
  support: S-tested
relationships:
- validates: Capability.Sla
---

Proposed by `W-domain-interpreter` in task `T02-interpret` and accepted through review. Support: `S-tested`.

Inferred by rule `S4-spec-validates-module`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
