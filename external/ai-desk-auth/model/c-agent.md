---
id: Concept.Agent
type: Concept
label: Agent
attributes:
  source: packages/backend/src/modules/auth/auth.service.ts
  locator: "login(email, password, workspaceSlug)"
  support: confirmed
relationships:
  - scoped-to: BC.Auth
  - evidenced-by: Evidence.LoginSignature
---
A human user authenticating into a workspace. Identified by email within a
tenant, never globally.
