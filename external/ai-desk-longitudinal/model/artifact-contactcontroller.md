---
id: Artifact.ContactController
type: Artifact
label: contact.controller.ts
attributes:
  locator: 6 routes
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T-continuous
  routes: '6'
  rule: C4-new-routes
  source: packages/backend/src/modules/contact/contact.controller.ts
  support: S-implemented
relationships:
- implements: Capability.Contact
---

Proposed by `W-domain-interpreter` in task `T-continuous` and accepted through review. Support: `S-implemented`.

Inferred by rule `C4-new-routes`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
