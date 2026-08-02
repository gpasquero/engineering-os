---
id: AcceptanceRecord.1
type: AcceptanceRecord
label: Acceptance of r1
relationships:
  - accepts: ArtifactRevision.Spec.r1
  - reviewed-by: Actor.Reviewer
  - cites: Evidence.Check
---
Acceptance confers Active status. Commits do not.
