---
id: Capability.ServerSideApply
type: Capability
label: Apply an object server-side
attributes:
  source: https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/fieldmanager.go
  locator: "func (f *FieldManager) Apply"
  support: confirmed
relationships:
  - scoped-to: BC.ApiMachinery
  - references: Concept.FieldManagement
  - realised-by: Artifact.FieldManagerGo
---
Merge an applied configuration into the live object and update managed fields.
