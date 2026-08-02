---
id: Invariant.Attachmentservice
type: Invariant
label: AttachmentService
attributes:
  granularity: concept
  locator: describe('AttachmentService')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T-continuous
  rule: C1-new-suite
  source: packages/backend/src/modules/attachment/__tests__/attachment.service.spec.ts
  support: S-inferred
relationships:
- constrains: Capability.Attachment
- enforced-at: Artifact.AttachmentServiceSpec
---

Proposed by `W-constraint-interpreter` in task `T-continuous` and accepted through review. Support: `S-inferred`.

Inferred by rule `C1-new-suite`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
