---
id: Invariant.PaymentBeforeShipping
type: Invariant
label: An order cannot ship before payment clears
relationships:
  - scoped-to: BoundedContext.Sales
  - constrains: Concept.Order
---
Stated independently of whatever enforces it. Note that `enforced-at` is absent:
this invariant has no recorded enforcement point, which is a finding rather than
an omission.
