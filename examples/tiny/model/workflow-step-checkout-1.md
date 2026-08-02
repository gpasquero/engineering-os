---
id: WorkflowStep.Checkout.1
type: WorkflowStep
label: Checkout step 1
position: 1
relationships:
  - step-of: Workflow.Checkout
  - executes: Skill.ValidateOrder
---
The reified association. The position lives here, not on the Skill.
