---
id: Capability.Login
type: Capability
label: Authenticate an agent into a workspace
attributes:
  source: packages/backend/src/modules/auth/auth.service.ts
  locator: "async login"
  support: confirmed
relationships:
  - scoped-to: BC.Auth
  - references: Concept.Agent
  - realised-by: Artifact.AuthService
---
Resolve the tenant by slug, verify the password, issue tokens.
