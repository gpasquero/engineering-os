---
id: Workflow.Checkout
type: Workflow
label: Checkout
relationships:
  - has-step: WorkflowStep.Checkout.1
  - has-step: WorkflowStep.Checkout.2
  - passes-through: Gate.PaymentReview
---
Orchestration only.
