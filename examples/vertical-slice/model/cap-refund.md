---
id: Capability.Refund
type: Capability
label: Refund an order
relationships:
  - scoped-to: BC.Ordering
  - references: Concept.Payment
  - realised-by: Artifact.PaymentService
---
Reverses a settled Payment. **Depends on the checkout workflow** through the
Skill it shares.
