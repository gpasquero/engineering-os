---
id: Concept.OwnershipTransfer
type: Concept
label: Ownership transfer
attributes:
  source: https://kubernetes.io/docs/reference/using-api/server-side-apply/
  support: confirmed
relationships:
  - scoped-to: BC.ApiMachinery
  - references: Concept.FieldManagement
  - evidenced-by: Evidence.DocsOwnershipTransfer
---
"Whenever a field's value does change, ownership moves from its current manager
to the manager making the change."
