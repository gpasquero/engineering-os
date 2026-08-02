---
id: Invariant.TenantIsolation
type: Invariant
label: No tenant can read or modify another tenant's data
attributes:
  source: docs/adr/ADR-0001-multi-tenancy-strategy.md
  support: confirmed
relationships:
  - scoped-to: BC.Auth
  - constrains: Capability.Login
  - enforced-at: Artifact.AuthService
  - evidenced-by: Evidence.Adr0001
---
"RLS policies are enforced by PostgreSQL itself, making cross-tenant data leakage
impossible even if application code has bugs."
