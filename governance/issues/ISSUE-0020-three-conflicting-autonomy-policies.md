---
id: ISSUE-0020
title: The three prototypes state incompatible autonomy policies
type: inconsistency
status: deferred
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M3]
evidence:
  - imports/reconstruct-system-knowledge/SKILL.md
  - imports/ontology-driven-development-v2/SKILL.md
  - imports/principal-engineering-skill/SKILL.md
resolved-by: null
defers-to: [M3]
debt: architectural
---

# ISSUE-0020 — Three incompatible autonomy policies

> **Architectural debt** (`ADR-0062`). Deferred because it is not needed to
> build the next deliverable. Reopen when implementation requires it.

## Statement

Each prototype states a different rule for when to stop and ask:

1. `reconstruct-system-knowledge` — "Do not wait for confirmation unless a
   genuinely blocking decision exists." Record ambiguity and continue.
2. `ontology-driven-development` — a hard implementation gate that halts at
   `blocked`, with seven enumerated blocking conditions.
3. `principal-engineering` — "If compatibility or understanding is low, continue
   investigation instead of coding."

## Why it matters

These produce different behavior in the same situation. When a workflow composes
reconstruction into change execution — which M8 requires — the agent inherits
three contradictory stopping rules with no arbitration.

Rule 1 pushes toward continuing, rule 2 toward halting, rule 3 toward neither:
it redirects effort without stopping.

## What we know

The rules may be reconcilable by scope: rule 1 governs *knowledge
reconstruction*, where continuing is safe because nothing is being changed; rule
2 governs *implementation*, where continuing is not safe. Rule 3 is a heuristic
about effort allocation rather than a stopping rule.

If that reading is right, the resolution is a scoped policy rather than a choice
between three. It has not been confirmed.

## Resolution criteria

One autonomy and escalation policy in `shared/policies/`, stating the stopping
rule per phase and the arbitration order when phases compose. Depends on
`ISSUE-0009` for who holds authority.
