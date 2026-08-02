---
id: ISSUE-0051
title: ProcessPolicy overlaps the workflow catalogue
type: inconsistency
status: resolved
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M3, M8]
evidence:
  - governance/adr/ADR-0030-normative-artifact-taxonomy.md
  - governance/roadmap.md
  - governance/design/workflow-catalog.md
resolved-by: ADR-0033
---

# ISSUE-0051 — `ProcessPolicy` overlaps the workflow catalogue

## Statement

`ADR-0030` defines `ProcessPolicy` as rules governing **execution of workflows**,
with these examples:

feature implementation workflow · bug investigation workflow · release
workflow · migration workflow

M8 delivers a workflow catalogue whose entries are: `feature`, `bug`,
`behavior-change`, `refactoring`, `integration`, `architecture-evolution`.

The names coincide. Whether a `ProcessPolicy` **governs** a workflow, **is** a
workflow's normative half, or **replaces** the workflow artifact is undefined.

## Why it matters

M3 writes policies and M8 writes workflows. If the distinction is not drawn, one
of two failures follows: the same content is written twice in two milestones, or
a workflow arrives in M8 with its rules already fixed by an M3 policy nobody
reconciled against it.

`ADR-0008` gave workflows their own directory and defined them as compositions
of skills that "contain no methodology of their own". A `ProcessPolicy`
containing execution rules sounds like methodology about a workflow, which is
plausibly the missing half — but that reading is not stated.

## Options

- **A `ProcessPolicy` governs workflow execution; a workflow sequences skills.**
  The policy says what must hold during execution — gates, write scope,
  escalation, evidence requirements; the workflow says what runs in what order.
  Clean separation, consistent with `ADR-0008`.
- **A `ProcessPolicy` is the normative specification and the workflow is its
  registry entry**, per the Registry Pattern (`ADR-0031`). Attractive, and would
  make workflows the fifth instance of the pattern — but it changes what a
  workflow artifact is.
- **They are the same thing under two names.** Then one must be eliminated, and
  M8's catalogue or M3's policy list is redundant.

The first two are both coherent and lead to different M8 deliverables.

## Resolution

`ADR-0033`. **A `ProcessPolicy` defines normative execution rules; a Workflow
defines executable orchestration.** Independent artifact types — the first
option listed above.

- A Workflow **references** one or more ProcessPolicies.
- A ProcessPolicy **never embeds** workflow execution.
- A Workflow **never embeds** normative rules.

```text
ProcessPolicy  governs  Workflow
Workflow       executes Process
```

The stated purpose is the sharp part: **this prevents implementation procedures
from becoming the source of engineering policy.** A rule that lives only inside
the steps implementing it cannot be reviewed, reused by another workflow, or
changed without editing an executable artifact.

The Registry Pattern reading was rejected — a workflow is not an index of a
policy, and forcing the pattern would misuse an abstraction that fits
identity-and-semantics, not rules-and-orchestration.

`ADR-0008`'s existing rule that workflows "contain no methodology of their own"
now has a mechanism.
