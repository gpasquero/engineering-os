---
id: Invariant.RefreshRotation
type: Invariant
label: Refresh rotates and revokes; a replayed token fails
attributes:
  source: packages/backend/src/modules/auth/__tests__/refresh-token-rotation.spec.ts
  locator: "refresh returns a new access+refresh pair AND revokes the old token"
  support: confirmed
relationships:
  - scoped-to: BC.Auth
  - constrains: Capability.RefreshSession
  - enforced-at: Artifact.RefreshRotationTests
  - evidenced-by: Evidence.RotationTests
---
Also: expired tokens auto-revoke, and refresh is rejected for deactivated or
soft-deleted agents.
