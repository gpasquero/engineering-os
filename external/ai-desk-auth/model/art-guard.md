---
id: Artifact.JwtGuard
type: Artifact
label: jwt-auth.guard.ts
attributes:
  source: packages/backend/src/common/guards/jwt-auth.guard.ts
  locator: "export class JwtAuthGuard extends AuthGuard('jwt')"
  support: confirmed
relationships:
  - represents: Concept.AccessToken
  - evidenced-by: Evidence.GuardSymbols
---
A one-line subclass. **All verification behaviour is inherited**, so nothing
local expresses what it enforces.
