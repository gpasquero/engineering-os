---
id: Artifact.RefreshTokenSchema
type: Artifact
label: refresh-tokens.ts
attributes:
  source: packages/backend/src/common/database/schema/refresh-tokens.ts
  locator: "partial index WHERE revoked_at IS NULL"
  support: confirmed
relationships:
  - represents: Concept.RefreshToken
  - evidenced-by: Evidence.RefreshTokenSchema
---
Revocation is a lookup-time exclusion, not a delete.
