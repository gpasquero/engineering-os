---
id: Artifact.SsaDocs
type: Artifact
label: kubernetes.io Server-Side Apply reference
attributes:
  source: https://kubernetes.io/docs/reference/using-api/server-side-apply/
  support: confirmed
relationships:
  - represents: Concept.FieldManagement
  - references: Concept.Conflict
  - references: Concept.Force
  - references: Concept.LastAppliedAnnotation
  - evidenced-by: Evidence.DocsFieldManagement
---
User-facing reference. Describes conflict resolution's three paths and the
field-removal rule.
