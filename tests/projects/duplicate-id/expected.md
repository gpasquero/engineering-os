---
id: TEST-duplicate-id
exercises: Node identity is unique within a project
outcome: fail
expected-errors:
  - "duplicate node id 'Concept.Same' declared 2 times"
---
**A negative fixture.** Two nodes with one identity make every edge to that
identity ambiguous.
