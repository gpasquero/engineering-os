---
id: Invariant.Publishwithoutsampleimagenorstoredfails
type: Invariant
label: publishWithoutSampleImageNorStoredFails
attributes:
  granularity: guarantee
  grouping: none-declared
  locator: case('publishWithoutSampleImageNorStoredFails')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: backend/src/test/java/com/wab2b/config/appsettings/ChannelTemplateServiceTest.java
  support: S-inferred
relationships:
- enforced-at: Artifact.Channeltemplateservicetest
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R4-both-levels`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
