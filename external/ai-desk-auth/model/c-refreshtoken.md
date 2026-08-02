---
id: Concept.RefreshToken
type: Concept
label: Refresh token
attributes:
  source: packages/backend/src/common/database/schema/refresh-tokens.ts
  locator: "pgTable refreshTokens: expiresAt, revokedAt"
  support: confirmed
relationships:
  - scoped-to: BC.Auth
  - references: Concept.AccessToken
  - evidenced-by: Evidence.RefreshTokenSchema
---
A persisted, revocable credential. The partial index filters on
`revoked_at IS NULL`, so revocation is a lookup-time exclusion.
