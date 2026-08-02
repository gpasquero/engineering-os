---
id: Concept.ManagedFields
type: Concept
label: managedFields
attributes:
  source: https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go
  locator: "type ManagedFieldsEntry"
  support: confirmed
relationships:
  - scoped-to: BC.ApiMachinery
  - references: Concept.FieldManagement
  - evidenced-by: Evidence.ManagedFieldsEntryType
  - evidenced-by: Evidence.DocsManagedFieldsShape
---
An entry in `metadata.managedFields` recording `manager`, `operation`
(`Apply` or `Update`), `apiVersion`, `time`, `fieldsType` (`FieldsV1`) and
`fieldsV1`.
