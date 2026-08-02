---
id: ISSUE-0073
title: Operational Knowledge sits outside the model while the inherited evidence hierarchy ranks it highest
type: inconsistency
status: deferred
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M3]
evidence:
  - governance/adr/ADR-0061-four-categories-of-knowledge.md
  - governance/adr/ADR-0012-executable-framework-and-artifact-taxonomy.md
  - imports/reconstruct-system-knowledge/SKILL.md
resolved-by: null
defers-to: [M3]
debt: architectural
---

# ISSUE-0073 — Operational Knowledge versus the evidence hierarchy

> **Architectural debt** (`ADR-0062`). Deferred because it is not needed to
> build the next deliverable. Reopen when implementation requires it.

## Statement

Two problems, both introduced by `ADR-0061`'s fourth category.

### 1. The strongest evidence is outside the model by default

`ADR-0061` places **Operational Knowledge** — runtime observations, metrics,
telemetry, execution history — **outside the Engineering Knowledge Model unless
explicitly imported as authored knowledge**.

The inherited `reconstruct-system-knowledge` prototype ranks evidence in twelve
tiers, and the **first** is:

> *Observable runtime behavior and executable acceptance tests.*

Its assertion vocabulary includes `observed` — *"identified from runtime
artifacts, fixtures, examples, or deployment"* — precisely for this.

So the methodology's highest-authority evidence is the category that requires
the most work to admit. The two are reconcilable — import makes it authored, and
`observed` describes its provenance — but nothing states the relationship, and
the evidence policy is M3 work.

### 2. "Runtime" names two different things

| Term | Means | Source |
|---|---|---|
| `runtime` artifact kind | temporary compiler output, not committed | `ADR-0012` |
| Operational Knowledge | telemetry from a running target system | `ADR-0061` |

`ADR-0057`'s Naming Qualification discipline is one session old and applies
directly: a concept's canonical name includes its architectural dimension
whenever ambiguity is possible.

This is the ninth occurrence of the class, and the first caught within one
session of the qualification rule existing.

## Why it matters

M3 writes the evidence policy, which must adopt or reject the inherited twelve
tier hierarchy. If observable runtime behaviour stays the top tier while
Operational Knowledge is excluded by default, a skill reconstructing a target
system is told to prioritise evidence the architecture keeps outside the model.

The naming collision matters sooner: both terms will appear in the metamodel.

## Open sub-questions

- What does "explicitly imported as authored knowledge" involve? An observation
  is a fact, not a decision — does importing it require acceptance, and by whom?
- Does an imported observation carry the `observed` assertion status from the
  inherited vocabulary?
- Is the evidence hierarchy adopted at all? It has never been decided; only
  `ISSUE-0018` on the assertion statuses touches that corpus.
- What are the qualified names? Candidates: **Compiler Runtime Artifact** and
  **System Operational Knowledge**, or a rename of one.

## Resolution criteria

An ADR reconciling Operational Knowledge with the evidence hierarchy — or
recording that the hierarchy is not adopted — and qualified names for both uses
of "runtime".
