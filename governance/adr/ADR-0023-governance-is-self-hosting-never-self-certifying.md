---
id: ADR-0023
title: Governance is self-hosting but never self-certifying
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0039]
related: [ADR-0020, ADR-0021, ADR-0022]
---

# ADR-0023 — Governance is self-hosting but never self-certifying

**This is an explicit architectural invariant.**

## Context

`ADR-0018` prohibited self-certification "unless an explicit governance policy
enables it". `ISSUE-0039` recorded that no such mechanism existed, and raised the
question that makes it hard: **who may change a governance policy, and does that
change itself require acceptance?** A policy that can be edited by the party it
constrains provides no guarantee at all.

## Decision

**Governance policies are themselves Authoritative Artifacts.** They follow
exactly the same acceptance lifecycle as every other authoritative artifact.

**A governance policy cannot modify itself.**

Every governance policy change must:

- be proposed separately;
- undergo review;
- receive an Acceptance Record;
- become `Active` only after acceptance.

> **The currently Active governance policy always governs the acceptance of the
> next revision.**

This guarantees that **no policy can silently relax the rules under which it is
accepted**.

Governance is therefore **self-hosting but never self-certifying**.

## Alternatives considered

**Exempt governance policies from the acceptance lifecycle.** Rejected: it is
the failure `ISSUE-0039` identified. A policy the constrained party can edit
freely is decorative.

**Require a higher authority to accept policy changes** — an external approver
outside the normal reviewer set. Rejected as unnecessary: the invariant that the
*outgoing* policy governs the acceptance of its own replacement already prevents
silent relaxation, without inventing a second authority tier that would itself
need governing.

**Store governance policies outside the repository.** Rejected: it breaks
`ADR-0001`, and it would make policy unreadable to a session reconstructing
context from the repository alone.

**Allow a policy to relax itself if the relaxation is explicit.** Rejected: an
explicit relaxation accepted *under the relaxed rule* is indistinguishable from
a silent one in its effect. The point of the invariant is the ordering, not the
visibility.

## Consequences

### Positive

- **A policy can never authorize its own acceptance.** The rule in force at the
  moment of acceptance is always the previous one, which is the whole guarantee.
- The mechanism `ADR-0018` named now exists in principle: automated acceptance
  becomes possible through a policy that was itself accepted under the prior
  policy.
- No new concept is introduced. Governance policies reuse the artifact
  taxonomy, the revision lifecycle and the Acceptance Record unchanged, which is
  strong evidence those abstractions were drawn correctly.
- It generalizes: the same ordering invariant applies to any self-referential
  artifact, not only policies.

### Negative

- **Policy change is deliberately slow.** Two acceptance cycles are needed to
  change how acceptance works — one to accept the new policy, and the new policy
  only governs from the next revision onward.
- The first policy has no predecessor to govern its acceptance. It depends on
  the trust root in `ADR-0022`, which makes that record load-bearing for the
  entire governance chain.
- No governance policy exists yet, so the invariant currently governs nothing.
  The first will arrive in M3.

### Neutral

- This does not by itself permit automated acceptance. It defines the only route
  by which such a permission could ever become `Active`.

## Compliance

No governance policy revision is accepted under itself. Every policy change has
its own Acceptance Record, granted under the previously `Active` policy. The
Bootstrap Acceptance Record is the only base case.
