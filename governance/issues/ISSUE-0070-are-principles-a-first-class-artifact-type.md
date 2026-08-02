---
id: ISSUE-0070
title: Whether Principles are a first-class artifact type, and how they relate to the ADRs recording them
type: question
status: open
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2, M3]
evidence:
  - governance/adr/ADR-0056-principle-policy-process-artifact.md
  - governance/adr/ADR-0029-modeling-policy-is-a-first-class-artifact-type.md
resolved-by: null
---

# ISSUE-0070 — Are Principles a first-class artifact type?

## Statement

`ADR-0056` establishes Principles as the first level of engineering knowledge,
with three examples: the Registry Pattern, `Definition → Instance → Assignment`,
and Semantic versus Compilation Architecture.

**All three are currently `Active` ADRs** — `ADR-0031`, `ADR-0052` and
`ADR-0053`.

Whether a Principle is a distinct artifact type, or a role an ADR plays, is
unstated.

## Why it matters

`ADR-0029` established the ADR/Policy split with a clear rationale: **ADRs
explain why a rule exists; Policies define the rule that must be followed**, and
the ADR corpus must never become the operational specification.

Principles are stated as *truths*, not as decisions or rules. That is a third
character, and it does not obviously belong to either existing type.

M3 writes the policies. A policy is required to cite the principle it derives
from (`ADR-0056`), so the citation target must exist and have a form.

## Options

- **Principles are a first-class artifact type.** Consistent with `ADR-0029`'s
  reasoning — an agent reading current architecture should not reconstruct
  principles from a decision corpus with seven supersessions. Requires the
  Metamodel Position Gate and passing through `ADR-0054`'s gates. Adds a fourth
  normative type after `GovernancePolicy`, `ModelingPolicy` and `ProcessPolicy`.
- **A Principle is a role an ADR plays**, marked by a dimension assignment. No
  new type; the Registry Pattern stays `ADR-0031` and is *classified* as a
  principle. Cheapest, and it leaves principles inside the corpus `ADR-0029`
  says is history rather than specification.
- **Principles are stated in Policies**, as the derivation each policy cites. No
  separate artifact; the principle exists only as the justification of the rules
  drawn from it. Loses the ability to state a principle no policy yet
  implements — which is what the Registry Pattern was for five sessions.

## The tension underneath

`ADR-0029`'s argument applies with more force to principles than to policies. A
principle is the most stable and most reused kind of content in the project, and
it is currently the kind most deeply buried in the decision history.

But making it an artifact type means a fourth normative type, and `ADR-0049`
established that scarcity is a virtue for exactly this reason.

## Resolution criteria

An ADR stating whether Principle is an artifact type, a classification of an
ADR, or content within a Policy — and if it is a type, how it relates to the
ADRs that currently record the three named principles.
