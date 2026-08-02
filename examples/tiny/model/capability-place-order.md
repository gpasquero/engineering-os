---
id: Capability.PlaceOrder
type: Capability
label: Place an order
relationships:
  - scoped-to: BoundedContext.Sales
  - realised-by: Artifact.CheckoutService
---
The system accepts an order from a Customer and acknowledges it.
