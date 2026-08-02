---
id: TEST-unregistered-predicate
exercises: ADR-0071 — every predicate must declare a registered parent
outcome: fail
expected-errors:
  - "predicate 'invented-link' has no registered parent"
---
**A negative fixture.** If this project ever compiles, the relationship
vocabulary has stopped being enforced and `ADR-0071` is decoration.
