---
id: Concept.LastAppliedAnnotation
type: Concept
label: last-applied-configuration annotation
attributes:
  source: https://kubernetes.io/docs/reference/using-api/server-side-apply/
  support: confirmed
relationships:
  - scoped-to: BC.ApiMachinery
  - evidenced-by: Evidence.DocsLastApplied
---
The legacy client-side mechanism SSA replaces. Tracks a user's last applied
state rather than their field management.
