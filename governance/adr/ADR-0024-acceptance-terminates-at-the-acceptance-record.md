---
id: ADR-0024
title: The acceptance process terminates at the Acceptance Record
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0042]
related: [ADR-0020, ADR-0021, ADR-0022, ADR-0023]
---

# ADR-0024 — The acceptance process terminates at the Acceptance Record

**This is an explicit architectural invariant.**

## Context

`ADR-0021` makes Acceptance Records first-class Authoritative Artifacts.
`ADR-0020` requires every authoritative revision to be accepted before it is
`Active`.

Together these imply that every Acceptance Record needs an Acceptance Record,
without end. `ISSUE-0042` recorded the regress and noted that `ADR-0022`
asserted `ACCEPT-0001` as a base case for that record specifically, not as a
general rule.

## Decision

Acceptance Records are authoritative governance artifacts, but they are
**explicitly excluded from recursive acceptance**.

An Acceptance Record derives its authority from **the acceptance decision it
records**. Requiring one to accept itself creates an infinite regress with no
architectural value.

> **The acceptance process terminates at the Acceptance Record. Acceptance
> Records are never themselves subject to an additional Acceptance Record.**

**This is not an exception. It is the base case of the acceptance model.**

## Alternatives considered

All four were recorded in `ISSUE-0042`.

**A distinct artifact kind exempt from acceptance.** Rejected: it would add a
fifth artifact kind to carry a property that belongs to one document type, and
`ADR-0018` already rejected a fifth kind once for encoding a workflow concern as
an artifact concern.

**Ordering, as in `ADR-0023`** — each record accepted under the authority of the
preceding one. Rejected despite its symmetry with the governance invariant: it
buys nothing. `ADR-0023`'s ordering exists to stop a policy relaxing the rules
governing its own acceptance; an Acceptance Record has no rules to relax, since
it *is* the acceptance.

**Batch acceptance** — a session's records accepted by the next record.
Rejected: it reduces the regress to a slow chain rather than removing it, and
leaves the final record in any chain unaccepted regardless.

## Consequences

### Positive

- **The model has a well-defined trust root**, and the termination is principled
  rather than pragmatic. A signature needs no counter-signature.
- No new artifact kind, no ordering machinery, no special-case status. The
  regress is removed by recognising what an Acceptance Record already is.
- `ACCEPT-0001`'s base-case status becomes a consequence of a general rule
  rather than an assertion about one file.

### Negative

- **An Acceptance Record is the one artifact nothing checks.** It is authored,
  it confers authority, and no separate process reviews it. A record naming a
  reviewer who did not in fact approve would be a governance violation
  detectable only by asking that reviewer — nothing mechanical prevents it. This
  is the irreducible cost of having a trust root at all, and it is why the
  `reviewer` field must name a real, askable party.
- A mistaken Acceptance Record cannot be corrected through the normal process.
  It is superseded by a later record, which is itself unaccepted. Correction is
  therefore as fast and as unchecked as the original error.

### Neutral

- `signatures`, named as a future extension in `ADR-0021`, is the natural place
  to reduce the forgery surface later. Nothing here depends on it.

## Compliance

No Acceptance Record has an Acceptance Record. Every Acceptance Record names a
real reviewer who can be asked whether they approved. The acceptance chain of
any artifact is exactly one record deep.
