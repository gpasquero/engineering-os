---
id: Invariant.RollbackClearsManagedFields
type: Invariant
label: Disabling the feature clears managedFields without affecting workloads
attributes:
  source: https://github.com/kubernetes/enhancements/blob/master/keps/sig-api-machinery/555-server-side-apply/README.md
  support: confirmed
relationships:
  - scoped-to: BC.ApiMachinery
  - constrains: Concept.ManagedFields
  - enforced-at: Artifact.ApplyIntegrationTest
  - evidenced-by: Evidence.Kep555Readme
  - evidenced-by: Evidence.TestClearManagedFields
---
Rollback safety. Four integration tests clear `managedFields` by four different
request paths.
