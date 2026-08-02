---
id: Invariant.RecommendProductsRejectsEmptyItems
type: Invariant
label: recommend_products_rejects_empty_items
attributes:
  granularity: guarantee
  grouping: none-declared
  locator: case('recommend_products_rejects_empty_items')
  origin: O-deterministic-rule
  proposed-by: W-constraint-interpreter
  proposed-in: T02-interpret
  rule: R4-both-levels
  source: backend/src/test/java/com/wab2b/whatsapp/ai/SystemToolExecutorBulkSearchTest.java
  support: S-inferred
relationships:
- enforced-at: Artifact.Systemtoolexecutorbulksearchtest
---

Proposed by `W-constraint-interpreter` in task `T02-interpret` and accepted through review. Support: `S-inferred`.

Inferred by rule `R4-both-levels`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
