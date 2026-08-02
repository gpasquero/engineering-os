---
id: Concept.EnvRedisPassword
type: Concept
label: $REDIS_PASSWORD
attributes:
  env-var: REDIS_PASSWORD
  locator: process.env.REDIS_PASSWORD
  proposed-by: W-structure-extractor
  proposed-in: T01-extract
  source: packages/backend/src/modules/sla/sla-timer.service.ts
  support: S-confirmed-deterministic
relationships: []
---

Proposed by `W-structure-extractor` in task `T01-extract` and accepted through review. Support: `S-confirmed-deterministic`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
