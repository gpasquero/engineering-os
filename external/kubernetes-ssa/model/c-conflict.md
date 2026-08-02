---
id: Concept.Conflict
type: Concept
label: Conflict
attributes:
  source: https://kubernetes.io/docs/reference/using-api/server-side-apply/
  support: confirmed
relationships:
  - scoped-to: BC.ApiMachinery
  - references: Concept.FieldManagement
  - evidenced-by: Evidence.DocsConflict
---
"A conflict occurs when an Apply operation tries to change a field that another
manager also claims to manage."
