---
id: Gate.Review
type: EngineeringGate
label: Review gate
relationships:
  - reviews: Artifact.Change
  - decided-by: Actor.Maintainer
---
Holds the questions. Outcomes are a closed enumeration per gate.
