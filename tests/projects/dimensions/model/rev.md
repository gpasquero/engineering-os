---
id: ArtifactRevision.Doc.r1
type: ArtifactRevision
label: Doc r1
relationships:
  - revision-of: Artifact.Doc
---
Carries no dimension value. `revision-of` was absent until `VR-0007` caught it:
identity is the pair (artifact-id, revision-id) (`ADR-0064`), and a revision with
no artifact has half an identity.
