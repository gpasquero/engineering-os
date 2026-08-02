---
id: Artifact.SlaController
type: Artifact
label: sla.controller.ts
attributes:
  locator: 10 routes
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T-continuous
  routes: '10'
  rule: C4-new-routes
  source: packages/backend/src/modules/sla/sla.controller.ts
  support: S-implemented
relationships:
- implements: Capability.Sla
---

Proposed by `W-domain-interpreter` in task `T-continuous` and accepted through review. Support: `S-implemented`.

Inferred by rule `C4-new-routes`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
