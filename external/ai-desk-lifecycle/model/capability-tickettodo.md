---
id: Capability.TicketTodo
type: Capability
label: ticket-todo module
attributes:
  locator: module directory
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T02-interpret
  rule: S1-module-is-a-capability
  source: packages/backend/src/modules/ticket-todo
  support: S-implemented
  ts-files: '5'
relationships:
- scoped-to: BoundedContext.Backend
---

Proposed by `W-domain-interpreter` in task `T02-interpret` and accepted through review. Support: `S-implemented`.

Inferred by rule `S1-module-is-a-capability`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
