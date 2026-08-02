---
id: Invariant.OnopenCloseswithservererrorWhenbridgecreatio
type: Invariant
label: onOpen_closesWithServerError_whenBridgeCreationFails
attributes:
  granularity: guarantee
  grouping: none-declared
  locator: case('onOpen_closesWithServerError_whenBridgeCreationFails')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: backend/src/test/java/com/wab2b/voice/VoiceWebSocketHandlerTest.java
  support: S-inferred
relationships:
- enforced-at: Artifact.Voicewebsockethandlertest
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R4-both-levels`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
