---
id: Invariant.PaymentBeforeShipping
type: Invariant
label: An order cannot ship before payment clears
relationships:
  - scoped-to: BC.Ordering
  - constrains: Concept.Order
  - enforced-at: Artifact.CheckoutService
  - evidenced-by: Evidence.PaymentTrace
---
Stated independently of what enforces it.
