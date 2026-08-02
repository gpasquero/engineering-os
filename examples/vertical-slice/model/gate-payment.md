---
id: Gate.PaymentReview
type: EngineeringGate
label: Payment review gate
relationships:
  - reviews: Artifact.PaymentService
  - decided-by: Actor.Reviewer
---
Holds the questions asked of every payment change.
