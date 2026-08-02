---
id: Capability.ConflictDetection
type: Capability
label: Detect and report field conflicts
attributes:
  source: https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/conflict.go
  locator: "NewConflictError, getConflictMessage"
  support: confirmed
relationships:
  - scoped-to: BC.ApiMachinery
  - references: Concept.Conflict
  - realised-by: Artifact.ConflictGo
---
Reject an apply that changes a field owned by another manager, naming the
manager and the field path.
