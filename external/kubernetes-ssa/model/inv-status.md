---
id: Invariant.StatusFieldsProtected
type: Invariant
label: Status fields are protected from ownership claims
attributes:
  source: https://github.com/kubernetes/enhancements/blob/master/keps/sig-api-machinery/555-server-side-apply/README.md
  locator: "ResetFieldsProvider"
  support: confirmed
relationships:
  - scoped-to: BC.ApiMachinery
  - constrains: Capability.ServerSideApply
  - enforced-at: Artifact.ApplyIntegrationTest
  - evidenced-by: Evidence.Kep555ResetFields
  - evidenced-by: Evidence.TestSubresources
---
Protected through a `ResetFieldsProvider` interface that resource strategies
implement.
