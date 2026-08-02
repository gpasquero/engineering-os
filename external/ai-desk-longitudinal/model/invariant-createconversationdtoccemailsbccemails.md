---
id: Invariant.CreateconversationdtoCcEmailsBccEmails
type: Invariant
label: CreateConversationDto — cc_emails / bcc_emails
attributes:
  granularity: concept
  locator: describe('CreateConversationDto — cc_emails / bcc_emails')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T-continuous
  rule: C1-new-suite
  source: packages/backend/src/modules/conversation/__tests__/create-conversation-dto.spec.ts
  support: S-inferred
relationships: []
---

Proposed by `W-constraint-interpreter` in task `T-continuous` and accepted through review. Support: `S-inferred`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
