---
id: Artifact.OidctestcontrollerJava
type: Artifact
label: OidcTestController.java
attributes:
  locator: 2 routes
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T02-interpret
  routes: '2'
  rule: S2-controller-implements-module
  source: backend/src/main/java/com/wab2b/oidc/OidcTestController.java
  support: S-implemented
relationships:
- implements: Capability.Oidc
---

Proposed by `W-domain-interpreter` in task `T02-interpret` and accepted through review. Support: `S-implemented`.

Inferred by rule `S2-controller-implements-module`.

**Authored from a discovery proposal** (`ADR-0106`). This is an authoring source, not a model write: the compiler reads it exactly as it reads a hand-written one.
