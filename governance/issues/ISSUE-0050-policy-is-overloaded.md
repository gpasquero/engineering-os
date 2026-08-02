---
id: ISSUE-0050
title: "policy" names at least three different artifact kinds
type: inconsistency
status: resolved
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M3]
evidence:
  - governance/adr/ADR-0029-modeling-policy-is-a-first-class-artifact-type.md
  - governance/adr/ADR-0023-governance-is-self-hosting-never-self-certifying.md
  - governance/adr/ADR-0008-shared-layer-three-way-split.md
  - governance/roadmap.md
resolved-by: ADR-0030
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

## Resolution

`ADR-0030`. **Do not solve this by inventing prefixes ad hoc.** A taxonomy for
normative artifacts instead — three distinct artifact kinds:

- **`GovernancePolicy`** — rules governing Engineering OS itself: acceptance,
  review, release governance.
- **`ModelingPolicy`** — rules governing how domains must be modeled: ontology
  modeling, naming conventions, state machine registration, artifact taxonomy,
  traceability rules.
- **`ProcessPolicy`** — rules governing execution of workflows: feature
  implementation, bug investigation, release, migration.

**The unqualified term "Policy" is avoided in specifications.**

The general question this issue raised — *should artifact type names be
namespaced the way state names are?* — is answered yes, and generalized:

> **A normative artifact type name is always qualified by what it governs.**

`ADR-0025` fixed state names by owning machine; `ADR-0030` fixes normative
artifact type names by what they govern. Two dimensions of one discipline.

The sub-question about `ADR-0023`'s self-modification invariant is answered by
scoping: it constrains `GovernancePolicy` only, so modeling rules are not
accidentally subject to two acceptance cycles.

Opened by this answer: `ISSUE-0051` — `ProcessPolicy` overlaps the M8 workflow
catalogue, using the same names.
