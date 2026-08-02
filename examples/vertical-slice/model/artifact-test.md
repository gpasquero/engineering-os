---
id: Artifact.CheckoutTests
type: Artifact
label: Checkout test suite
relationships:
  - validates: Artifact.CheckoutService
  - references: Concept.Order
---
Tests. Modelled as an Artifact that validates another and references the
Concepts it exercises — which is what makes *which tests must change* answerable.
