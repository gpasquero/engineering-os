---
id: Invariant.TimestampNotUpdatedOnTakeover
type: Invariant
label: An entry's timestamp does not update when another manager takes a field over
attributes:
  source: https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go
  locator: "ManagedFieldsEntry.Time doc comment"
  support: confirmed
relationships:
  - scoped-to: BC.ApiMachinery
  - constrains: Concept.ManagedFields
  - references: Concept.Force
  - references: Concept.OwnershipTransfer
  - evidenced-by: Evidence.TimeFieldComment
  - evidenced-by: Evidence.DocsForce
---
"The timestamp does not update when a field is removed from the entry because
another manager took it over."

**This invariant is the cross-source finding.** See `../ground-truth.md` Q7.
