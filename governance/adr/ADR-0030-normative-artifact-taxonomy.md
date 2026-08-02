---
id: ADR-0030
title: A taxonomy for normative artifacts; normative artifact type names are always qualified
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0050]
related: [ADR-0008, ADR-0023, ADR-0025, ADR-0029, ISSUE-0051]
---

# ADR-0030 — A taxonomy for normative artifacts

**This establishes the general naming rule for normative artifact types.**

## Context

`ISSUE-0050` recorded that "policy" had come to name three different things:
governance policies (`ADR-0023`), Modeling Policies (`ADR-0029`), and the
process policies listed for M3.

This was the fourth vocabulary collision in the project, after "skill"
(`ISSUE-0012`), "authoritative" (`ISSUE-0038`) and the state vocabularies
(`ISSUE-0043`). It was the first caught in the same session it was created.

`ADR-0025` had solved the class for *state* names by namespacing to the owning
machine. Nothing equivalent governed *artifact type* names.

## Decision

**Do not solve this by inventing prefixes ad hoc.** Establish a taxonomy for
normative artifacts instead.

Three different concepts, modeled explicitly as **different artifact kinds**:

### `GovernancePolicy`

Rules governing **Engineering OS itself**.

Acceptance governance · review governance · release governance.

### `ModelingPolicy`

Rules governing **how domains must be modeled**.

Ontology modeling · naming conventions · state machine registration · artifact
taxonomy · traceability rules.

### `ProcessPolicy`

Rules governing **execution of workflows**.

Feature implementation workflow · bug investigation workflow · release workflow ·
migration workflow.

### The naming rule

**Avoid the unqualified term "Policy" in specifications.**

> **This is the general naming rule for normative artifact types: a normative
> artifact type name is always qualified by what it governs.**

## Alternatives considered

**Ad-hoc prefixes as each collision appears.** Rejected explicitly. It is what
the project did three times already, and each patch left the underlying pattern
in place to recur.

**One `Policy` type with a `kind` discriminator field.** Rejected: these are
different artifact kinds with different lifecycles and different consumers. A
`GovernancePolicy` cannot modify itself and governs its successor's acceptance
(`ADR-0023`); a `ModelingPolicy` is expected to evolve freely (`ADR-0029`).
Collapsing them into one type with a field would put those incompatible
invariants on the same artifact.

**Keep the unqualified term and disambiguate by context.** Rejected: it is
exactly what "skill" and "authoritative" required abandoning.

## Consequences

### Positive

- **The naming rule generalizes**, which is the general form `ISSUE-0050` asked
  for. `ADR-0025` fixed state names by owning machine; this fixes normative
  artifact type names by what they govern. Two dimensions of the same discipline.
- `ADR-0029`'s Modeling Policy becomes precisely one of three rather than an
  unqualified type occupying the whole word.
- The `GovernancePolicy` invariant from `ADR-0023` — cannot self-modify, the
  `Active` one governs its successor — is now unambiguously scoped, and does not
  accidentally constrain modeling rules.

### Negative

- **`ProcessPolicy` overlaps `workflows/`.** Its examples — feature
  implementation, bug investigation, release, migration — are the same names as
  the M8 workflow catalogue. Whether a ProcessPolicy governs a workflow, or *is*
  the workflow's normative half, is undefined. `ISSUE-0051`.
- **`shared/policies/` now holds three artifact kinds** with no stated structure.
  Flat with the kind in front matter, or three subdirectories, is an M3 decision
  and is left open here.
- **The M3 policy list must be reclassified**, and some entries are genuinely
  ambiguous. Evidence and research policies could be modeling or process;
  verification could be process or governance. That classification is M3 work,
  not a formality.

### Neutral

- No existing rule changes. Only the type names and their boundaries.

## Compliance

No specification uses the unqualified term "Policy". Every normative artifact
type name states what it governs. Every policy artifact declares which of the
three kinds it is.
