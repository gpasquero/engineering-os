---
id: Invariant.UpdatedescriptionRejectsmissingfield
type: Invariant
label: updateDescription_rejectsMissingField
attributes:
  granularity: guarantee
  grouping: none-declared
  locator: case('updateDescription_rejectsMissingField')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: backend/src/test/java/com/wab2b/tools/ToolControllerTest.java
  support: S-inferred
relationships:
- enforced-at: Artifact.Toolcontrollertest
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R4-both-levels`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
