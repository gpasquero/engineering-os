---
id: Invariant.SummarizeLeavesdocintactWhensummarizerfails
type: Invariant
label: summarize_leavesDocIntact_whenSummarizerFails
attributes:
  granularity: guarantee
  grouping: none-declared
  locator: case('summarize_leavesDocIntact_whenSummarizerFails')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: backend/src/test/java/com/wab2b/kb/KbSummaryServiceTest.java
  support: S-inferred
relationships:
- enforced-at: Artifact.Kbsummaryservicetest
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R4-both-levels`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
