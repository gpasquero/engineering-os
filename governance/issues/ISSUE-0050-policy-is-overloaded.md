---
id: ISSUE-0050
title: "policy" names at least three different artifact kinds
type: inconsistency
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M3]
evidence:
  - governance/adr/ADR-0029-modeling-policy-is-a-first-class-artifact-type.md
  - governance/adr/ADR-0023-governance-is-self-hosting-never-self-certifying.md
  - governance/adr/ADR-0008-shared-layer-three-way-split.md
  - governance/roadmap.md
resolved-by: null
---

# ISSUE-0050 — "policy" names at least three different things

## Statement

The word now carries three distinct meanings:

**Governance policy** (`ADR-0023`) — governs *acceptance*. Cannot modify itself;
the currently `Active` one governs the acceptance of its successor.

**Modeling Policy** (`ADR-0029`) — governs *how domains are modeled*. Normative,
evolving, consumed primarily by agents.

**Process policies** — the M3 list includes write-scope, autonomy and
escalation, secrets and privacy, verification and knowledge-update. These govern
*how work is done*. They are neither governance nor modeling.

All three live in `shared/policies/` under `ADR-0008`.

## Why it matters

This is the fourth instance of the pattern the project has now caught three
times: "skill" (`ISSUE-0012`), "authoritative" (`ISSUE-0038`), and the state
vocabularies (`ISSUE-0043`). Each was expensive to find late.

`ADR-0025` established the remedy for state names — namespacing by owning
machine. Nothing equivalent yet governs artifact type names, and `shared/policies/`
is written in M3.

The practical risk is specific: `ADR-0023`'s invariant says a governance policy
cannot modify itself and that the `Active` one governs its successor's
acceptance. If "policy" is read broadly, that invariant appears to constrain
Modeling Policies too — which would make every modeling rule change require two
acceptance cycles. If read narrowly, nothing says so.

## Open sub-questions

- Are these three types, or one type with three subjects?
- Does `ADR-0023`'s self-modification invariant apply to all policies, or only
  to governance policies?
- Do Modeling Policies and process policies share the ADR-references-and-evolves
  contract that `ADR-0029` defines, or is that specific to modeling?
- Should artifact type names be namespaced the way state names are?

That last question is the general one. Three collisions in one vocabulary
dimension were solved by `ADR-0025`; this is the same problem in another
dimension.

## Resolution criteria

An ADR fixing the policy taxonomy — which types exist, what each governs, which
invariants apply to which — before `shared/policies/` is written in M3.
