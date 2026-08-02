---
id: ISSUE-0039
title: The explicitly-configured governance policy mechanism does not exist
type: gap
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M3]
evidence:
  - governance/adr/ADR-0018-acceptance-confers-authoritative-status.md
resolved-by: null
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

## Resolution criteria

An ADR defining where governance policies live, what they may express, and who
may change them — including the base case that terminates the regress. Feeds the
autonomy and escalation policy in M3.
