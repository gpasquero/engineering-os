---
id: TEST-dimensions
exercises: Classification as a relationship, not a property
outcome: pass
expected-nodes: 4
expected-edges: 4
---
The revision carries **no dimension value**. A `DimensionAssignment` relates it
to the axis (`ADR-0042`), so reclassifying does not touch the artifact. There is
no `DimensionSpecification` node — `ADR-0070` merged it into `Dimension`.

**This fixture was defective and passed for two sessions.** Its
`ArtifactRevision` declared no `revision-of`. `VR-0007` caught it the moment
validation became declarative — the rule was written by generalising `VR-0006`,
not by inspecting this project.
