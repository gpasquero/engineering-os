---
id: Invariant.RejectsCcEmailsContainingAnInvalidEmailAddre
type: Invariant
label: rejects cc_emails containing an invalid email address
attributes:
  granularity: guarantee
  locator: it('rejects cc_emails containing an invalid email address')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T-continuous
  rule: C1-new-suite
  source: packages/backend/src/modules/conversation/__tests__/create-conversation-dto.spec.ts
  support: S-inferred
relationships:
- specializes: Invariant.CreateconversationdtoCcEmailsBccEmails
---

Proposed by `W-constraint-interpreter` in task `T-continuous` and accepted through review. Support: `S-inferred`.

Inferred by rule `C1-new-suite`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
