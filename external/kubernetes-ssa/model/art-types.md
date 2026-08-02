---
id: Artifact.MetaV1Types
type: Artifact
label: apimachinery meta/v1/types.go
attributes:
  source: https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go
  locator: "type ManagedFieldsEntry struct"
  support: confirmed
relationships:
  - represents: Concept.ManagedFields
  - evidenced-by: Evidence.ManagedFieldsEntryType
---
The API type. Its `Time` doc comment is where the takeover-timestamp rule lives.
