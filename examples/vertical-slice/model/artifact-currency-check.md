---
id: Artifact.CurrencyCheck
type: Artifact
label: Legacy currency checker
relationships:
  - represents: Invariant.SingleCurrency
  - validates: Artifact.CheckoutService
---
**Implements a rationale that no longer stands.** `Invariant.SingleCurrency` was
established by `ADR.004`, which `ADR.011` superseded. The code is still here and
nothing in the repository connects it to the decision that replaced its reason.

This is what `Q-stale-implementation` finds.
