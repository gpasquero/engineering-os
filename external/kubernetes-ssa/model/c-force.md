---
id: Concept.Force
type: Concept
label: Force
attributes:
  source: https://kubernetes.io/docs/reference/using-api/server-side-apply/
  support: confirmed
relationships:
  - scoped-to: BC.ApiMachinery
  - references: Concept.Conflict
  - evidenced-by: Evidence.DocsForce
---
Setting `force=true` "forces the operation to succeed, changes the value of the
field, and **removes the field from all other managers' entries in
managedFields**."
