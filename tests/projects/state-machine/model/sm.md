---
id: SMS.RevisionLifecycle
type: StateMachineSpecification
label: Artifact revision lifecycle
relationships:
  - controls-lifecycle-of: ArtifactRevision.Doc.r1
  - driven-by: Workflow.Review
---
Draft, Under Review, Accepted, Active, Superseded, Archived. Every state belongs
to exactly one machine.
