---
id: TEST-dimensions
exercises: Classification as a relationship, not a property
outcome: pass
expected-nodes: 4
expected-edges: 3
---
The revision carries **no dimension value**. A `DimensionAssignment` relates it
to the axis (`ADR-0042`), so reclassifying does not touch the artifact. There is
no `DimensionSpecification` node — `ADR-0070` merged it into `Dimension`.
