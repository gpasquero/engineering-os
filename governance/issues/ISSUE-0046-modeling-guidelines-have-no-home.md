---
id: ISSUE-0046
title: Core modeling guidelines are declared across scattered ADRs with no home document
type: gap
status: resolved
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M3]
evidence:
  - governance/adr/ADR-0025-every-state-belongs-to-exactly-one-state-machine.md
  - governance/adr/ADR-0026-artifact-revision-lifecycle.md
resolved-by: ADR-0029
---

# ISSUE-0046 — Core modeling guidelines have no home

## Statement

Two ADRs now declare rules that govern modeling across the entire Engineering
OS, including target domains:

- `ADR-0025` — "a fundamental modeling rule for the entire Engineering OS":
  every state belongs to exactly one state machine.
- `ADR-0026` — "a core modeling guideline": the lifecycle belongs to a revision,
  not an artifact; state machines are named after the entity they govern.

No document collects them. A skill modeling a target domain would have to read
the full ADR corpus to discover the rules it must follow.

## Why it matters

These are not decisions *about this repository*. They are rules the methodology
imposes on every system it is applied to — which is precisely the content that
belongs in `shared/policies/`, referenced by skills rather than rediscovered.

The set will keep growing. Two in two sessions, with the ontology and
constraint-placement policies of M3 certain to add more.

Leaving them scattered also weakens them: an ADR records *why a decision was
made*, and is read once. A policy states *what must be done*, and is read every
time. The same text serves the two purposes badly.

## What we know

- `ADR-0008` established `shared/policies/` for normative prose referenced by
  path and never inlined.
- The M3 policy list already includes an ontology policy and a
  constraint-placement policy, both of which are modeling guidance.
- The inherited `reconstruct-system-knowledge` prototype carries modeling rules
  of its own in `references/ontology-guidelines.md`, which is frozen provenance
  and will need extracting.

## Open sub-questions

- One `modeling-guidelines` policy, or several by topic (state machines,
  identity and revisions, ontology, constraint placement)?
- How does a policy stay in sync with the ADR that established it? The ADR is
  the rationale; the policy is the rule. Duplicating the rule risks the drift
  `ADR-0016` addressed for projections.

That second question is the interesting one: a policy may be the first artifact
that is legitimately *derived* from ADRs.

## Resolution

`ADR-0029`. Engineering OS gains a new first-class artifact type: the **Modeling
Policy**, in `shared/policies/`.

> **ADRs explain *why* a policy exists. Policies define the rule that must be
> followed.**

Unlike an ADR, a Modeling Policy is not tied to a single decision, is **expected
to evolve**, is **normative rather than historical**, and is **directly consumed
by AI agents**. Policies explicitly reference the ADRs they originated from.

Agents primarily consume Policies; humans read ADRs for rationale.

The sub-question this issue raised — how a policy stays in sync with its ADR,
and whether a policy is the first legitimately *derived* artifact — is answered
in the negative. **Policies reference ADRs; they are not generated from them**,
because a policy is expected to evolve past the decision that created it. The
divergence is intended.

The rationale is concrete: at 29 ADRs with five supersessions and one partial
correction, deriving the currently applicable rules from the decision history is
archaeology. This prevents the ADR corpus from becoming the operational
specification.

Opened by this answer: `ISSUE-0050` — "policy" now names at least three
different artifact kinds.
