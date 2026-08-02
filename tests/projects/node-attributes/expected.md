---
id: TEST-node-attributes
exercises: Nodes carry domain-neutral attributes verbatim into the model
outcome: pass
expected-nodes: 2
expected-edges: 1
---
An authoring node may declare an `attributes` mapping of scalar key/value facts.
**The compiler assigns them no meaning** — a Layer B model uses them for a source
URI, a locator, a support status or anything else its domain needs.

This is the smallest general correction to the gap found while modelling
Kubernetes: *every modeled assertion must preserve provenance to its exact
source*, and no authoring field could carry one.

The fixture is deliberately **not** Kubernetes-specific (`ADR-0087`).
