---
id: ISSUE-0039
title: The explicitly-configured governance policy mechanism does not exist
type: gap
status: resolved
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M3]
evidence:
  - governance/adr/ADR-0018-acceptance-confers-authoritative-status.md
resolved-by: ADR-0023
---

# ISSUE-0039 — The governance policy mechanism does not exist

## Statement

`ADR-0018` prohibits self-certification "unless an explicit governance policy
enables it", and permits trusted automated acceptance "only through explicitly
configured governance rules".

No such mechanism exists. There is no governance policy artifact, no place to
configure one, and no definition of what a governance rule may express.

## Why it matters

The prohibition names an escape hatch with nothing behind it. Two failure modes
follow, in opposite directions:

- Because the hatch cannot be opened, **every acceptance requires a human
  forever**, which will not scale and will eventually be bypassed informally —
  the worst outcome, since the bypass would be undocumented.
- Or an implementer invents an ad-hoc mechanism under time pressure, and the
  safety property `ADR-0018` establishes is weakened by whatever they happened
  to build.

## Open sub-questions

- Where is a governance policy declared? `MANIFEST.yaml` is the architectural
  manifest and plausibly the right home, but acceptance policy is arguably
  neither architecture nor knowledge nor build state — it may need a fourth
  location, which `ADR-0013` would have to be revisited to allow.
- What can a rule express? Artifact kinds, paths, reviewer identity, check
  results, risk level?
- Who may change a governance policy, and does *that* change itself require
  acceptance? The regress needs a defined base case.
- Are policies repository-local, like knowledge, or organizational?

That third question is the interesting one: a governance policy that can be
edited by the party it constrains provides no guarantee at all.

## Resolution

`ADR-0023`. **Governance is self-hosting but never self-certifying.**

Governance policies are themselves Authoritative Artifacts and follow exactly the
same acceptance lifecycle. **A governance policy cannot modify itself.** Every
change must be proposed separately, undergo review, receive an Acceptance
Record, and become `Active` only after acceptance.

The question this issue identified as the interesting one — *who may change a
policy, and does that change require acceptance* — is answered by ordering:

> **The currently Active governance policy always governs the acceptance of the
> next revision.**

This guarantees that no policy can silently relax the rules under which it is
accepted. The base case is the trust root, `ACCEPT-0001`.

Notably, no new concept was needed: policies reuse the artifact taxonomy, the
revision lifecycle and the Acceptance Record unchanged.
