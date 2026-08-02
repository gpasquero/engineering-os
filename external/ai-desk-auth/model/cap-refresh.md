---
id: Capability.RefreshSession
type: Capability
label: Exchange a refresh token for a new pair
attributes:
  source: packages/backend/src/modules/auth/auth.service.ts
  locator: "async refresh"
  support: confirmed
relationships:
  - scoped-to: BC.Auth
  - references: Concept.RefreshToken
  - realised-by: Artifact.AuthService
---
Rotates: issues a new pair and revokes the presented token.
