---
id: Actor.Customer
type: Actor
label: Customer
relationships:
  - scoped-to: BoundedContext.Sales
  - uses: Capability.PlaceOrder
---
The role that submits orders. A role, not a person.
