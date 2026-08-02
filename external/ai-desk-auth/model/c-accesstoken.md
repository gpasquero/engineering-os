---
id: Concept.AccessToken
type: Concept
label: Access token
attributes:
  source: packages/backend/src/modules/auth/auth.service.ts
  locator: "issueTokens(agentId, tenantId, role, name, ticketScope)"
  support: confirmed
relationships:
  - scoped-to: BC.Auth
  - references: Concept.Tenant
  - evidenced-by: Evidence.IssueTokensSignature
---
A JWT carrying agent, tenant, role, name and ticket scope.
