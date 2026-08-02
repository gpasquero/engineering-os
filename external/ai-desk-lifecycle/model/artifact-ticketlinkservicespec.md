---
id: Artifact.TicketLinkServiceSpec
type: Artifact
label: ticket-link.service.spec.spec.ts
attributes:
  cases: '6'
  describes: TicketLinkService | create | remove
  locator: 6 cases
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T02-interpret
  rule: S4-spec-validates-module
  source: packages/backend/src/modules/ticket-link/__tests__/ticket-link.service.spec.ts
  support: S-tested
relationships:
- validates: Capability.TicketLink
---

Proposed by `W-domain-interpreter` in task `T02-interpret` and accepted through review. Support: `S-tested`.

Inferred by rule `S4-spec-validates-module`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
