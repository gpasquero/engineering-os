---
id: Evidence.FieldManagerSymbols
type: Evidence
label: fieldmanager.go exported symbols
attributes:
  source: https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/fieldmanager.go
  locator: "FieldManager, Apply, Update, UpdateNoErrors"
  kind: source-reference
  fetched: "2026-08-02"
  support: confirmed
relationships: []
---
HTTP 200. Apply carries force bool. UpdateNoErrors preserves live managedFields
on error 'to prevent clients who don't understand managedFields from deleting it
accidentally.'
