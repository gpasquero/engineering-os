---
id: ISSUE-0042
title: Whether an Acceptance Record itself requires acceptance is unresolved
type: question
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0021-acceptance-record-specification.md
  - governance/adr/ADR-0020-artifact-taxonomy-and-revision-lifecycle-are-independent.md
  - governance/acceptance/ACCEPT-0001-bootstrap.md
resolved-by: null
---

# ISSUE-0042 — Does an Acceptance Record require acceptance?

## Statement

`ADR-0021` establishes that Acceptance Records are **first-class Authoritative
Artifacts**.

`ADR-0020` establishes that an authoritative revision becomes `Active` only
through acceptance, and that acceptance is recorded in an Acceptance Record.

Together these imply that every Acceptance Record requires an Acceptance Record,
without end.

## Why it matters

The regress is not academic. `ACCEPT-0001` is the trust root of the entire
repository, and `ADR-0022` asserts it as the base case — but asserts it for that
record specifically, not as a general rule. Every subsequent acceptance record
inherits the unresolved question.

`ADR-0023` solved the analogous problem for governance policies by ordering:
the previously `Active` policy governs the acceptance of the next revision. No
equivalent ordering has been stated for acceptance records themselves.

## Options

- **Acceptance Records are self-attesting.** The record *is* the acceptance, so
  requiring acceptance of it is circular by construction — as a signature needs
  no counter-signature. Simplest, and probably right, but it makes Acceptance
  Records an exception to `ADR-0020`, which currently admits none.
- **A distinct artifact kind exempt from acceptance.** Makes the exemption
  structural rather than special-cased, at the cost of a fifth artifact kind —
  which `ADR-0018` already rejected once for a different purpose.
- **Ordering, as in `ADR-0023`.** Each acceptance record is accepted under the
  authority established by the preceding one, chaining back to `ACCEPT-0001`.
  Most consistent with the governance invariant, and the most machinery.
- **Batch acceptance.** A session's records are accepted together by the next
  record. Reduces the regress to a slow chain rather than removing it.

## Why it blocks M2

`shared/contracts/` must define the Acceptance Record contract in M2, and the
contract cannot state the artifact's own lifecycle obligations while this is
open.

## Resolution criteria

An ADR stating whether an Acceptance Record requires acceptance, and if not, on
what principled basis it is exempt — not merely that the regress is
inconvenient.
