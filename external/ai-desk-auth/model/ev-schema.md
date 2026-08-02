---
id: Evidence.RefreshTokenSchema
type: Evidence
label: refresh-tokens.ts
attributes:
  source: packages/backend/src/common/database/schema/refresh-tokens.ts
  locator: "lines 11-27"
  kind: source-reference
  extracted: "2026-08-02"
  support: confirmed
relationships: []
---
pgTable with expiresAt, revokedAt, and a partial index WHERE revoked_at IS NULL.
