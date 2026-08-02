---
id: Invariant.Alwayspicksoneofthenonblanktrimmedlines
type: Invariant
label: alwaysPicksOneOfTheNonBlankTrimmedLines
attributes:
  granularity: guarantee
  grouping: none-declared
  locator: case('alwaysPicksOneOfTheNonBlankTrimmedLines')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: backend/src/test/java/com/wab2b/whatsapp/ai/AiChatServicePendingMessageTest.java
  support: S-inferred
relationships:
- enforced-at: Artifact.Aichatservicependingmessagetest
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R4-both-levels`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
