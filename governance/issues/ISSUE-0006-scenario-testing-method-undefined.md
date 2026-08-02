---
id: ISSUE-0006
title: How a prompt-based methodology is tested is undefined
type: question
status: deferred
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M10]
evidence:
  - sources/handoff/ROADMAP.md
resolved-by: null
defers-to: [M10]
debt: architectural
---

# ISSUE-0006 — How to test a prompt-based methodology is undefined

> **Architectural debt** (`ADR-0062`). Deferred because it is not needed to
> build the next deliverable. Reopen when implementation requires it.

## Statement

The inherited roadmap names "Scenario tests" as a delivery. No document defines
what a scenario test is, what it asserts, or what makes it pass.

## Why it matters

M10 cannot start. More broadly, without a testing method there is no way to know
whether a change to a skill improved or degraded it, which undermines the claim
that the system is reviewable and versioned.

## What we know

- Skill outputs are natural-language artifacts produced non-deterministically.
  Exact-match comparison is not viable.
- The methodology does produce *structural* obligations that are checkable: an
  impact analysis must contain a gate decision; an iteration must produce named
  artifacts; assertions must carry a status.

## Options

- **Artifact-presence assertions** — run a skill against a fixture repository
  and assert the required artifacts exist and are well-formed. Cheap,
  deterministic, checks form not quality.
- **Rubric grading by a judge agent** — assess output quality against criteria.
  Checks quality, is itself non-deterministic.
- **Golden outputs** — brittle; likely to be abandoned.
- **Human review checklists** — highest fidelity, does not scale, not automatable.

A combination of the first two is the most likely answer.

## Resolution criteria

An ADR defining what a scenario test is, what it asserts, what fixtures it needs,
and what constitutes a regression.
