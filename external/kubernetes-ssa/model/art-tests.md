---
id: Artifact.ApplyIntegrationTest
type: Artifact
label: test/integration/apiserver/apply/apply_test.go
attributes:
  source: https://github.com/kubernetes/kubernetes/blob/master/test/integration/apiserver/apply/apply_test.go
  locator: "30 Test functions"
  support: confirmed
relationships:
  - validates: Artifact.FieldManagerGo
  - validates: Artifact.ConflictGo
  - references: Concept.ManagedFields
  - references: Concept.Force
  - evidenced-by: Evidence.TestFunctionList
---
Integration tests including `TestApplyUpdateApplyConflictForced`,
`TestApplyManagedFields`, `TestApplyRequiresFieldManager`,
`TestClearManagedFieldsWith{Update,MergePatch,StrategicMergePatch,JSONPatch}`,
`TestApplyDoesNotChangeManagedFieldsViaSubresources`.
