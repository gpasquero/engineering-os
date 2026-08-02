---
id: Invariant.TenantIdOnEveryConnection
type: Invariant
label: tenant_id must be set on every connection
attributes:
  source: docs/adr/ADR-0001-multi-tenancy-strategy.md
  locator: "Requires discipline: SET app.current_tenant_id"
  support: confirmed
relationships:
  - scoped-to: BC.Auth
  - constrains: Concept.Tenant
  - evidenced-by: Evidence.Adr0001
---
**No `enforced-at`.** The ADR calls it "discipline"; no artifact in the modelled
scope is recorded as enforcing it. **The gap is the finding.**
