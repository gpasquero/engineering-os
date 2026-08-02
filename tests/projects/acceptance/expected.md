---
id: TEST-acceptance
exercises: Acceptance — an act that confers Active status on a revision
outcome: pass
expected-nodes: 5
expected-edges: 5
---
The acceptance chain terminates at the record (`ADR-0024`): nothing accepts the
AcceptanceRecord. The reviewer is an Actor, and `ADR-0023` requires that it not
be the author — a rule nothing yet enforces, which this project makes visible.
