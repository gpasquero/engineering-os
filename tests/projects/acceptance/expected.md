---
id: TEST-acceptance
exercises: Acceptance — an act that confers Active status on a revision
outcome: pass
expected-nodes: 5
expected-edges: 5
expected-queries:
  Q-status:
    subject: Artifact.Spec
    rows: [ArtifactRevision.Spec.r1]
  Q-unaccepted:
    rows: []
  Q-impact:
    subject: Actor.Reviewer
    rows: [AcceptanceRecord.1]
    status: ok
    paths:
      AcceptanceRecord.1: [reviewed-by]
  Q-status:
    subject: Actor.Reviewer
    status: not-applicable
    rows: []
---
**`expected-queries` pins the answers, not just the shape.** The first attempt
declared `Q-impact(Actor.Reviewer)` as empty; it is not — changing the reviewer
affects the acceptance record that names them. The expectation was wrong and the
model was right.

The acceptance chain terminates at the record (`ADR-0024`): nothing accepts the
AcceptanceRecord. The reviewer is an Actor, and `ADR-0023` requires that it not
be the author — a rule nothing yet enforces, which this project makes visible.
