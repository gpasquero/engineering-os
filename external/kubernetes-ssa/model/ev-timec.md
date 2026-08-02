---
id: Evidence.TimeFieldComment
type: Evidence
label: ManagedFieldsEntry.Time doc comment
attributes:
  source: https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go
  locator: "lines 1419-1424"
  kind: source-reference
  fetched: "2026-08-02"
  support: confirmed
relationships: []
---
'The timestamp will also be updated if a field is added, the manager changes any
of the owned fields value or removes a field. **The timestamp does not update
when a field is removed from the entry because another manager took it over.**'
