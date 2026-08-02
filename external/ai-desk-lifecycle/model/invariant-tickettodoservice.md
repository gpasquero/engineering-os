---
id: Invariant.Tickettodoservice
type: Invariant
label: TicketTodoService
attributes:
  established-by-cases: '5'
  granularity: concept
  locator: describe('TicketTodoService')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: packages/backend/src/modules/ticket-todo/__tests__/ticket-todo.service.spec.ts
  support: S-inferred
relationships:
- constrains: Capability.TicketTodo
- enforced-at: Artifact.TicketTodoServiceSpec
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R4-both-levels`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
