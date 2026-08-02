---
id: ISSUE-0062
title: Four dimensions remain undefined, deferred through three consecutive issues
type: gap
status: open
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0040-architectural-dimensions.md
  - governance/adr/ADR-0041-dimensions-are-registered-first-class-entities.md
  - governance/adr/ADR-0044-independence-is-not-isolation.md
  - governance/issues/ISSUE-0057-dimension-set-is-not-fixed.md
  - governance/issues/ISSUE-0059-dimension-independence-and-overlaps.md
resolved-by: null
---

# ISSUE-0062 — Four dimensions remain undefined

## Statement

`ADR-0040` named eight dimensions. Four have never been defined:

**Governance Status** · **Ownership** · **Authority** · **Visibility**

Two suspected overlaps remain open:

- **`Governance Status` versus `Lifecycle`.** `ArtifactRevisionLifecycle` has
  `Draft`, `Under Review`, `Accepted`, `Active`, `Superseded`, `Archived` — which
  is governance status by another name.
- **`Ownership` versus `Authority`.** `ADR-0040`'s worked example gives
  `Owner: Architecture` and no `Authority` value at all. `ADR-0044` adds
  *"Ownership may constrain Governance Policies"* without defining either term.

## This is the third consecutive deferral

| Issue | Raised the question | Resolved by | Outcome |
|---|---|---|---|
| `ISSUE-0057` | problem 2 of 3 | `ADR-0041` | Carried to `ISSUE-0059` |
| `ISSUE-0059` | part 2 of 2 | `ADR-0044` | Carried to `ISSUE-0062` |
| `ISSUE-0062` | — | — | Open |

Each resolution answered the structural question and deferred the definitional
one. That is defensible individually and a pattern collectively: **the mechanism
for dimensions has been decided three times over while half the initial
dimensions remain undefined.**

## Why it matters

`ADR-0041` makes dimensions registered entities requiring eight fields each. The
Dimension Registry Specification is M2 work, and its first registrations are
these eight dimensions. Four of them cannot be registered.

If `Governance Status` and `Lifecycle` are one axis, registering both would put
a duplicate into the registry on day one — the failure `ADR-0040` exists to
prevent, in the artifact meant to prevent it.

## Open sub-questions

- Is `Governance Status` distinct from `ArtifactRevisionLifecycle`? If so, what
  does it range over — the artifact, the acceptance, or the governance process?
- Are `Ownership` and `Authority` one dimension or two? *Who owns a thing* and
  *who may change it* is a real distinction, but nothing says it is intended.
- Does `Visibility` range over artifacts, over projections, or over both? A
  public artifact with a private projection is coherent and unaddressed.
- What is each one's value domain and cardinality — the fields `ADR-0041`
  requires?

## Resolution criteria

Definitions for all four, or removal of those that turn out to be duplicates —
with the eight `ADR-0041` fields filled for each survivor. Must precede the
Dimension Registry Specification.
