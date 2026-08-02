---
id: ISSUE-0051
title: ProcessPolicy overlaps the workflow catalogue
type: inconsistency
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M3, M8]
evidence:
  - governance/adr/ADR-0030-normative-artifact-taxonomy.md
  - governance/roadmap.md
  - governance/design/workflow-catalog.md
resolved-by: null
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

## Resolution criteria

An ADR stating the relationship between `ProcessPolicy` and workflow artifacts,
and which milestone owns which content. Needed before M3 writes process policies.
