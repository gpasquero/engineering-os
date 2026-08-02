---
id: Artifact.TicketController
type: Artifact
label: ticket.controller.ts
attributes:
  locator: 14 routes
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T02-interpret
  routes: '14'
  rule: S2-controller-implements-module
  source: packages/backend/src/modules/ticket/ticket.controller.ts
  support: S-implemented
relationships:
- implements: Capability.Ticket
---

Proposed by `W-domain-interpreter` in task `T02-interpret` and accepted through review. Support: `S-implemented`.

Inferred by rule `S2-controller-implements-module`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
