---
id: Artifact.ConflictGo
type: Artifact
label: managedfields/internal/conflict.go
attributes:
  source: https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/conflict.go
  locator: "NewConflictError, getConflictMessage, printManager"
  support: confirmed
relationships:
  - represents: Concept.Conflict
  - evidenced-by: Evidence.ConflictSymbols
---
Formats `"Apply failed with 1 conflict: conflict with %v: %v"`. `printManager`
renders manager name, apiVersion, operation, **time** and subresource.
