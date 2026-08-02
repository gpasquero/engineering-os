---
id: Concept.TableTicketForms
type: Concept
label: ticket_forms table
attributes:
  locator: pgTable('ticket_forms')
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T-continuous
  rule: C2-new-table
  source: packages/backend/src/common/database/schema/ticket-forms.ts
  support: S-implemented
relationships: []
---

Proposed by `W-domain-interpreter` in task `T-continuous` and accepted through review. Support: `S-implemented`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
