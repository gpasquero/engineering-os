---
id: Invariant.BackwardCompatible
type: Invariant
label: Changes must be strictly backward compatible
attributes:
  source: https://github.com/kubernetes/enhancements/blob/master/keps/sig-api-machinery/555-server-side-apply/README.md
  support: confirmed
relationships:
  - scoped-to: BC.ApiMachinery
  - constrains: Capability.ServerSideApply
  - evidenced-by: Evidence.Kep555Readme
---
"All the changes should be strictly backward compatible, and shouldn't break
existing automation or users."
