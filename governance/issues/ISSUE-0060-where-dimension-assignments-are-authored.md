---
id: ISSUE-0060
title: Where Dimension Assignments are authored, and whether classification stays readable without the compiler
type: question
status: open
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0042-dimension-assignments.md
  - governance/adr/ADR-0017-reference-architecture-not-reference-implementation.md
  - governance/adr/ADR-0014-three-tier-knowledge-model.md
resolved-by: null
---

# ISSUE-0060 — Where Dimension Assignments are authored

## Statement

`ADR-0042` establishes that artifacts are classified by Dimension Assignments,
and that **the Canonical Knowledge Model represents dimensions as graph
relationships rather than embedded metadata**.

That fixes the *representation* in Layer C. It does not say where assignments
are **authored**.

## Why it matters

The Canonical Knowledge Model is derived (`ADR-0037`, Layer C). A derived
artifact cannot be the source of anything. So assignments must originate
somewhere authoritative — and nothing says where.

**There is a direct tension with `ADR-0017`.** It guarantees that *authoritative
artifacts must remain human-readable and usable without executing the compiler*.
If an artifact's classification exists only as a relationship in a compiled
graph, then **a human reading that artifact cannot tell what layer it belongs
to, whether it is authoritative, or who owns it** without running the toolchain.

That is not a small ergonomic cost. It would mean the repository stops being
fully legible as memory (`ADR-0001`) for exactly the properties `ADR-0038` makes
mandatory to know.

## Options

- **Assignments authored in front matter, compiled into graph relationships.**
  The artifact stays legible; the graph gets the relational form. `ADR-0042`
  forbids treating classification as a *property*, but front matter could be
  read as the **source syntax for an assignment** rather than as an embedded
  value. Whether that respects the decision or evades it is the crux.
- **Assignments as separate authored artifacts.** Cleanest against `ADR-0042`,
  and consistent with assignments being versioned and acceptable in their own
  right. Produces one artifact per artifact per dimension, which is a large
  multiplier over a corpus of 110 records.
- **A per-repository assignment registry**, following `ADR-0031`. Assignments
  live in one authoritative specification, projected into the graph. Fewer
  artifacts, and a natural fifth application of the Registry Pattern — but it
  centralizes information about an artifact away from the artifact.
- **Type-level defaults plus per-artifact overrides.** Rejected in `ADR-0042` as
  a property-based framing; would need re-examining as an *assignment* framing.

## The question underneath

**Is front matter a property, or a serialization of a relationship?**

If the former, `ADR-0042` rules it out and legibility must be recovered some
other way. If the latter, most of the tension dissolves and the decision is
about syntax rather than semantics.

## Resolution criteria

An ADR stating where assignments are authored, and how an artifact's
classification remains determinable without running the compiler — or an
explicit decision that it need not be, with `ADR-0017` amended accordingly.
