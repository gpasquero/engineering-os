---
id: Artifact.VoicessecontrollerJava
type: Artifact
label: VoiceSseController.java
attributes:
  locator: 1 routes
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T02-interpret
  routes: '1'
  rule: S2-controller-implements-module
  source: backend/src/main/java/com/wab2b/voice/VoiceSseController.java
  support: S-implemented
relationships:
- implements: Capability.Voice
---

Proposed by `W-domain-interpreter` in task `T02-interpret` and accepted through review. Support: `S-implemented`.

Inferred by rule `S2-controller-implements-module`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
