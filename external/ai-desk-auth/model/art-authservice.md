---
id: Artifact.AuthService
type: Artifact
label: auth.service.ts
attributes:
  source: packages/backend/src/modules/auth/auth.service.ts
  locator: "login, issueTokens, refresh, logout"
  support: confirmed
relationships:
  - represents: Capability.Login
  - references: Concept.RefreshToken
  - evidenced-by: Evidence.LoginSignature
  - evidenced-by: Evidence.IssueTokensSignature
---
Four public methods. Every authentication path in the backend passes through it.
