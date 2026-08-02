---
id: MODEL-TASK-KINDS
title: Task Kinds
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0094, ADR-0097]
---

# Task Kinds

**The mechanism by which a plan action becomes a task** (`ADR-0097`).

A TaskGraph is **derived**, not declared — declaring both a plan and its graph
would let them disagree. What is declared is the kind of task each plan action
produces.

```yaml
task-kinds:
  - id: T-review
    from-action: review
    objective: Read {targets} and confirm they still hold before proceeding
    capabilities: [C-read-source]
    completion: The reviewer records a decision for every item.
    evidence: A review note citing each item read.

  - id: T-investigate
    from-action: investigate
    objective: Trace {targets} to their sources and establish what they support
    capabilities: [C-read-source, C-semantic-query]
    completion: Every item is traced to a source or recorded as unsupported.
    evidence: Provenance for each item, or a recorded gap.

  - id: T-validate
    from-action: validate
    objective: Check that {targets} still hold after the intended change
    capabilities: [C-read-source]
    completion: Each item is confirmed to hold, or recorded as violated.
    evidence: An observation per item — confirmed or violated.

  - id: T-inspect
    from-action: inspect
    objective: Assess whether {targets} require changing
    capabilities: [C-read-source]
    completion: Each item is marked as requiring change or not.
    evidence: A decision per item.

  - id: T-update
    from-action: update
    objective: Update {targets} to match the change
    capabilities: [C-modify-source]
    completion: Each item is updated or explicitly deferred.
    evidence: A modification per item.

  - id: T-verify
    from-action: verify
    objective: Execute {targets} and confirm nothing regressed
    capabilities: [C-run-tests]
    completion: Every item passes, or a failure is recorded.
    evidence: A test result per item.

  # Terminal tasks, appended to every graph. Not derived from a plan action.
  - id: T-review-gate
    terminal: true
    order: 1
    objective: Approve the completed work
    capabilities: [C-approve]
    completion: A reviewer who is not the author records a decision.
    evidence: An acceptance record (ADR-0021, ADR-0023).

  - id: T-update-knowledge
    terminal: true
    order: 2
    objective: Record what execution established, and what it disproved
    capabilities: [C-record-knowledge]
    completion: Every observation is recorded in the model or explicitly discarded.
    evidence: Model assertions, added or retracted.
```

## Terminal tasks close the plan, not the loop

`T-review-gate` and `T-update-knowledge` are appended to every graph and depend
on everything before them.

**They are declared and nothing executes them.** `T-update-knowledge` is the
Knowledge Update stage of `ADR-0095`'s loop, present as a task and absent as a
capability — the loop still does not close, and now it says so in the graph.

## Debt

**A plan action with no declared kind produces no task, silently.** Six actions
exist and six kinds map to them; a seventh action would be dropped without
diagnostic.

**Objectives are templates with one substitution.** `{targets}` is the only
variable, so a task's objective cannot reflect *why* those targets were selected
— that stays in the plan.

**`T-review-gate` requires `C-approve`, which no worker may hold** (`ADR-0023`
prohibits self-certification). That is correct and it means every graph
terminates in a task nothing can execute automatically. **By design, and worth
stating.**
