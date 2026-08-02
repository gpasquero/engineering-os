---
id: TEST-missing-required-relationship
exercises: VR-0006 — a WorkflowStep must declare `executes`
outcome: fail
expected-phase: resolution
expected-rule: VR-0006
expected-errors:
  - "a WorkflowStep must declare 'executes'"
---
**A negative fixture.** `WorkflowStep` exists only to carry the position of a
Skill within a Workflow (`ADR-0068`). A step that executes nothing is not a step.
