---
id: Artifact.TicketTodoController
type: Artifact
label: ticket-todo.controller.ts
attributes:
  locator: 5 routes
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T02-interpret
  routes: '5'
  rule: S2-controller-implements-module
  source: packages/backend/src/modules/ticket-todo/ticket-todo.controller.ts
  support: S-implemented
relationships:
- implements: Capability.TicketTodo
---

Proposed by `W-domain-interpreter` in task `T02-interpret` and accepted through review. Support: `S-implemented`.

Inferred by rule `S2-controller-implements-module`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
