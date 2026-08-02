---
id: TEST-self-reference
exercises: VR-0005 — a containment or revision edge may not point at itself
outcome: fail
expected-phase: resolution
expected-rule: VR-0005
expected-errors:
  - "'scoped-to' on 'BC.Loop' points at itself"
---
**A negative fixture.** A cycle of length one is always an authoring error, and
no rule caught it until validation became declarative (`ADR-0077`).
