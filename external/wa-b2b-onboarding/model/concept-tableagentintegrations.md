---
id: Concept.TableAgentIntegrations
type: Concept
label: agent_integrations table
attributes:
  locator: pgTable('agent_integrations')
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T02-interpret
  rule: S1-pgtable-is-a-concept
  source: backend/src/main/java/com/wab2b/agent/AgentIntegrationLink.java
  support: S-implemented
  tenant-scoped: 'false'
relationships: []
---

Proposed by `W-domain-interpreter` in task `T02-interpret` and accepted through review. Support: `S-implemented`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
