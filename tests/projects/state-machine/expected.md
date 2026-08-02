---
id: TEST-state-machine
exercises: StateMachineSpecification — legal transition, and the absence of StateMachine
outcome: pass
expected-nodes: 4
expected-edges: 3
---
There is **no `StateMachine` node**, and there cannot be: `ADR-0070` removed it.
The specification governs the artifact type directly, and the instance that would
have justified a middle layer is a runtime execution outside the repository.
