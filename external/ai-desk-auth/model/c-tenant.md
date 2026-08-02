---
id: Concept.Tenant
type: Concept
label: Tenant
attributes:
  source: docs/adr/ADR-0001-multi-tenancy-strategy.md
  support: confirmed
relationships:
  - scoped-to: BC.Auth
  - evidenced-by: Evidence.Adr0001
---
A workspace. Resolved by slug at login and carried in every token as `tid`.
