---
id: Capability.PlaceOrder
type: Capability
label: Place an order
relationships:
  - scoped-to: BC.Ordering
  - references: Concept.Order
  - realised-by: Artifact.CheckoutService
---
The system accepts an order and acknowledges it.
