---
id: Invariant.ApplyRequiresFieldManager
type: Invariant
label: An apply request must name a field manager
attributes:
  source: https://github.com/kubernetes/kubernetes/blob/master/test/integration/apiserver/apply/apply_test.go
  locator: TestApplyRequiresFieldManager
  support: confirmed
relationships:
  - scoped-to: BC.ApiMachinery
  - constrains: Capability.ServerSideApply
  - enforced-at: Artifact.ApplyIntegrationTest
  - evidenced-by: Evidence.TestRequiresFieldManager
---
**Asserted by a test, stated by no fetched document.** The docs describe what a
manager is; the requirement that a request carry one is visible in the test
name.
