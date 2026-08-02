---
id: ISSUE-0069
title: ADR-0056 reuses "Level" and "Process", both already in use for other concepts
type: inconsistency
status: resolved
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0056-principle-policy-process-artifact.md
  - governance/adr/ADR-0046-abstraction-level-and-semantic-layer.md
  - governance/adr/ADR-0033-process-policy-governs-workflow.md
resolved-by: ADR-0057
---

# ISSUE-0069 — "Level" and "Process" are reused

## Statement

`ADR-0056` introduces "three levels of engineering knowledge" and names one of
them "Process". Both words are already in use.

### "Level"

`ADR-0046` established **Abstraction Level** as a qualified name — Metamodel,
Model, Classification — *precisely so that "level" would not be ambiguous*. It
recorded that qualification, not renaming, is the discipline, and that it was
the third application of that discipline.

`ADR-0056`'s levels are Principle, Policy, Process. **A second unqualified
scheme.**

### "Process"

`ADR-0033` recorded *Workflow executes Process* in its conceptual diagram, and
explicitly noted: *"Process appears in the conceptual diagram as the activity a
workflow executes. It is descriptive here, not a declared artifact type."*

`ADR-0056` makes Process a level containing Dimension Review, Acceptance Review
and the Metamodel Position Gate — that is, gates. Whether the activity a workflow
executes is this Process is unstated.

## Why it matters

This is the **seventh** terminology collision in nineteen sessions, and the
second to arrive in the ADR that establishes an organizing principle — `ADR-0032`
was the first.

`ADR-0056` is to become one of the central organizing concepts of the metamodel,
and the metamodel is M2's first deliverable. A scheme written into it with an
ambiguous name propagates into every schema and projection downstream.

## What the existing discipline says

`ADR-0046` already supplies the remedy: **qualify, do not rename**. Both words
are accurate for what they describe. What is missing is the qualified form.

Candidates for the levels scheme: *Engineering Knowledge Level*, *Normative
Level*, *Governance Level*. Candidates for the process concept depend on whether
it is the same as a workflow's process or not — which is the substantive part.

## Open sub-questions

- What is the qualified name for `ADR-0056`'s levels?
- Is a `Process` in the Principle/Policy/Process hierarchy the same thing as the
  Process a Workflow executes (`ADR-0033`)? If yes, workflows are processes and
  gates are processes; if no, two things share a name.
- `ADR-0056`'s diagram has four stages — Principle, Policy, Process, Artifact —
  while the text names three levels. Is Artifact a level or the output?

## Resolution

`ADR-0057`, **by closing the class rather than the eighth instance.**

> **Whenever a concept belongs to a specific architectural dimension, its
> published name includes that dimension whenever ambiguity is possible.**

A **Naming Qualification Policy**, not a renaming strategy. The short name may
still be used informally where context is unambiguous; the qualified name is
canonical.

Ten canonical names are fixed, including three that settle this issue:
**Engineering Process** (distinguished from **Business Process**),
**Workflow Execution**, and **Knowledge Representation**.

Gates and workflows are both Engineering Processes; a Workflow Execution is the
act of running one. `ADR-0056`'s level scheme takes its qualified name by
applying the policy rather than by being named here.

This is what `ADR-0046` predicted three sessions ago: three ADRs applying one
discipline meant the discipline was a rule. It is now one — recorded in an ADR,
and destined for a `ModelingPolicy` in M3.

Auditing the existing corpus for unqualified names is M3 work.
