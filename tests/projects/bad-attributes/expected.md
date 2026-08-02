---
id: TEST-bad-attributes
exercises: Attribute values must be scalar; a nested structure fails at Parsing
outcome: fail
expected-phase: parsing
expected-errors:
  - "attributes must be scalar"
---
**A negative fixture.** Attributes are a deliberately flat, uninterpreted
key/value space. Allowing nested structures would make them a second modelling
language beside the graph, which is what the metamodel exists to be.
