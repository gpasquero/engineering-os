---
id: ISSUE-0041
title: The shape and location of an acceptance record are undefined
type: gap
status: resolved
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0018-acceptance-confers-authoritative-status.md
resolved-by: ADR-0021
---

# ISSUE-0041 — The acceptance record is undefined

## Statement

`ADR-0018` requires that acceptance "become part of the knowledge model and be
traceable", and that it record explicit reviewer approval, traceability to the
motivating issue or ADR, and successful validation of applicable deterministic
checks.

Nothing defines what an acceptance record *is*: its fields, its location, its
artifact kind, or how it is linked to the artifact it accepts.

## Why it matters

Without it, `ADR-0018` is unimplementable and `ISSUE-0040` cannot be resolved —
there is nowhere to write the retroactive acceptance.

It is also an M2 contract: `shared/contracts/` must define it alongside the
evidence, conflict and traceability records.

## Open sub-questions

- **Artifact kind.** An acceptance record is hand-authored, so `authoritative`
  by kind — but then it requires its own acceptance, and the regress needs a
  base case. Alternatively acceptance records are a special kind exempt from
  acceptance, which weakens the taxonomy.
- **Location.** In `governance/`? Beside the artifact? In `model/` as knowledge?
  `ADR-0018` says acceptance is part of the knowledge model, which points to
  `model/` — but `governance/` artifacts need acceptance too, and a governance
  document depending on `model/` inverts the current layering.
- **Granularity.** Per artifact, per change, or per session? Per-change is the
  most likely useful unit and maps naturally onto the impact-analysis change ID.
- **Validation results.** Condition 3 requires successful deterministic checks,
  but no checks exist until M9. Is condition 3 vacuously satisfied until then,
  or does it block acceptance entirely?

That last question needs an answer immediately, because it determines whether
*any* artifact can be accepted before M9.

## Resolution

`ADR-0021`. **Acceptance Records are first-class Authoritative Artifacts** with
a dedicated specification, located under `governance/acceptance/`.

Fourteen minimum fields, from `id` and artifact revision through reviewer,
decision, rationale, related ADRs and issues, validation summary, exceptions,
supersession links, and `signatures` as a future extension.

**The condition 3 question is answered by applicability, not by exception.** The
requirement is "all *applicable* deterministic validations". Where no
deterministic validator exists, none are applicable, and condition 3 is
satisfied. This is the normal reading — as tooling evolves, additional checks
become applicable automatically without any change to the acceptance model.

That reading matters: treating condition 3 as blocking would have made every
artifact unacceptable before M9, including the decision needed to bootstrap the
trust root.

The location question resolved to `governance/`, not `model/`.

**The regress is not settled.** An Acceptance Record is itself an Authoritative
Artifact and would by the letter of `ADR-0020` require its own acceptance —
`ISSUE-0042`.
