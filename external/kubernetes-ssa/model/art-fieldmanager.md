---
id: Artifact.FieldManagerGo
type: Artifact
label: managedfields/internal/fieldmanager.go
attributes:
  source: https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/fieldmanager.go
  locator: "FieldManager.Apply(liveObj, appliedObj runtime.Object, manager string, force bool)"
  support: confirmed
relationships:
  - represents: Concept.FieldManagement
  - evidenced-by: Evidence.FieldManagerSymbols
---
`FieldManager.Apply` takes `force bool`; `Update` handles non-apply operations;
`UpdateNoErrors` preserves the live object's managedFields on error.
