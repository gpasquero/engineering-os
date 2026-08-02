---
id: TEST-workflow-ordering
exercises: Extrinsic ordering — the same Skill at two positions in one Workflow
outcome: pass
expected-nodes: 5
expected-edges: 6
---
`Skill.Validate` is executed at position 1 and again at position 3. **This is
unrepresentable without `ADR-0068`'s reification** — it is the concrete case that
decision exists for, and the reason `WorkflowStep` identity is (Workflow,
position) rather than (Workflow, Skill).
