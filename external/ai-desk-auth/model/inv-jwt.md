---
id: Invariant.TokenIntegrity
type: Invariant
label: Tokens with a wrong secret, tampered payload or alg=none are rejected
attributes:
  source: packages/backend/src/modules/auth/__tests__/jwt-security.spec.ts
  locator: 'rejects a token with a tampered payload (modified tid)'
  support: confirmed
relationships:
  - scoped-to: BC.Auth
  - constrains: Concept.AccessToken
  - enforced-at: Artifact.JwtSecurityTests
  - evidenced-by: Evidence.JwtTests
---
**"modified `tid`" is tenant isolation enforced at the token layer** — the test
suite protects the multi-tenancy invariant without naming it.
