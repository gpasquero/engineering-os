---
id: Invariant.SingleCurrency
type: Invariant
label: An order has exactly one currency
relationships:
  - scoped-to: BC.Ordering
  - constrains: Concept.Order
---
**No `enforced-at`.** Nothing records where this is checked, which is a finding
rather than an omission.
