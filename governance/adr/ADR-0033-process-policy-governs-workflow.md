---
id: ADR-0033
title: A ProcessPolicy governs a Workflow; the two are independent artifact types
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0051]
related: [ADR-0008, ADR-0029, ADR-0030]
---

# ADR-0033 — A ProcessPolicy governs a Workflow

## Context

`ADR-0030` defined `ProcessPolicy` as rules governing execution of workflows,
with examples — feature implementation, bug investigation, release, migration —
that are the same names as the M8 workflow catalogue. `ISSUE-0051` recorded that
the relationship was undefined and that the two are written in different
milestones, risking either duplication or an M8 workflow whose rules were fixed
in M3 by nobody reconciling them.

## Decision

**A `ProcessPolicy` defines normative execution rules. A Workflow defines
executable orchestration.** They are **independent artifact types**.

- **A Workflow references one or more ProcessPolicies.**
- **A ProcessPolicy never embeds workflow execution.**
- **A Workflow never embeds normative rules.**

```text
ProcessPolicy
    governs
Workflow

Workflow
    executes
Process
```

**This separation prevents implementation procedures from becoming the source of
engineering policy.**

## Alternatives considered

**A ProcessPolicy is the workflow's normative half, and the workflow its registry
entry** — the Registry Pattern reading `ISSUE-0051` floated. Rejected: a workflow
is not an index of a policy. Both are substantive artifacts of different kinds,
and forcing them into Registry + Specification would misuse a pattern that fits
identity-and-semantics, not rules-and-orchestration.

**One artifact combining rules and orchestration.** Rejected, and this is the
rejection the decision exists for: the procedure would become the policy. A rule
that lives only inside the steps that implement it cannot be reviewed, reused by
another workflow, or changed without editing an executable artifact.

**Rules stay in the workflow; ProcessPolicy is dropped.** Rejected for the same
reason, and it would leave `ADR-0030`'s taxonomy with two kinds where three were
identified.

## Consequences

### Positive

- **`ADR-0008`'s rule gains a mechanism.** It already said workflows "contain no
  methodology of their own"; this states where the methodology lives instead and
  how the workflow reaches it.
- The same normative rule can govern several workflows without being restated —
  the reuse `ADR-0008` created `shared/policies/` for.
- It matches the separation `ADR-0029` drew between historical and operational
  knowledge, and the one `ADR-0032` drew between specification and projection.
  Three instances of *normative artifact distinct from the thing it governs*.
- A policy can be revised without touching an executable artifact, and a
  workflow can be reordered without renegotiating a rule.

### Negative

- **The boundary will blur in practice.** "Reproduce the bug with a failing test
  before fixing it" is arguably a normative rule and arguably a step. The
  inherited prototypes state such things as workflow steps, so classifying them
  is real M3 and M8 work, not bookkeeping.
- M8 now depends on M3 concretely: a workflow cannot be written before the
  policies it references exist, or it will be written with rules inlined.
- Two artifacts where the prototypes had one, for anyone reading a workflow to
  understand what it requires.

### Neutral

- "Process" appears in the conceptual diagram as the activity a workflow
  executes. It is descriptive here, not a declared artifact type.

## Compliance

No workflow contains a normative rule. No ProcessPolicy contains execution
steps. Every workflow declares the ProcessPolicies it is governed by.
