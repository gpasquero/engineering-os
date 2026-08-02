---
id: Concept.TableBusinessHours
type: Concept
label: business_hours table
attributes:
  locator: pgTable('business_hours')
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T02-interpret
  rule: S1-pgtable-is-a-concept
  source: packages/backend/src/common/database/schema/business-hours.ts
  support: S-implemented
  tenant-scoped: 'true'
relationships: []
---

Proposed by `W-domain-interpreter` in task `T02-interpret` and accepted through review. Support: `S-implemented`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
