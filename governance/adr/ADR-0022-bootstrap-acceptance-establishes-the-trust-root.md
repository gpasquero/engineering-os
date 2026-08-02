---
id: ADR-0022
title: A single Bootstrap Acceptance Record establishes the repository trust root
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0040]
related: [ADR-0020, ADR-0021, ADR-0023]
---

# ADR-0022 — Bootstrap acceptance establishes the trust root

## Context

`ADR-0018`, carried forward by `ADR-0020`, requires every authoritative revision
to carry an Acceptance Record with an explicit reviewer, and prohibits
self-certification.

`ISSUE-0040` recorded that the entire existing corpus fails this rule. Every
artifact in the repository was authored by an agent and committed by that same
agent, with no reviewer and no acceptance record — including `ADR-0018` itself,
which cannot accept itself without circularity.

## Decision

**Engineering OS cannot retroactively invent history.** The repository therefore
**explicitly bootstraps trust**.

A single **Bootstrap Acceptance Record** covers the bootstrap corpus, stating
that:

- the artifacts were produced collaboratively during the bootstrap phase;
- they were reviewed and directed by the project owner;
- formal Acceptance Records did not yet exist;
- this record establishes the initial trusted baseline of the repository.

**This is the only retrospective acceptance permitted.** All future authoritative
revisions follow the normal acceptance workflow.

This avoids rewriting history while creating a well-defined trust root.

### Scope is bounded by a named revision

The record names the exact repository revision it covers. **It cannot accept
work that did not yet exist when it was written.**

This is stated explicitly because a bootstrap record that pre-accepted future
work would defeat its own purpose: it would convert a one-time trust root into a
standing exemption from acceptance. Artifacts created after the named revision
are `Under Review` until accepted normally.

## Alternatives considered

**Per-artifact retroactive acceptance.** Rejected as disproportionate. It would
also be less honest: it would imply a per-artifact review that did not take
place, whereas the bootstrap phase was genuinely a single collaborative effort.

**A grandfather clause with an expiry.** Rejected: it leaves the foundational
tier untrusted for the duration, and an expiry that arrives with the work
unfinished would either be extended or ignored.

**Rewrite history so the corpus appears to have been accepted.** Rejected
absolutely. It is the failure mode the project exists to prevent, and it would
falsify the evidence that the methodology is built on.

**Do nothing and carry a silent exception.** Rejected: a silent exception to a
foundational principle is precisely the drift this project is designed to make
impossible.

## Consequences

### Positive

- The authoritative tier rests on something explicit and readable, rather than
  on nothing.
- The trust root is a single, auditable artifact. Anyone can read exactly what
  was assumed and when.
- **It is honest about what happened.** The owner did read and direct the
  bootstrap work; only the recording step was missing.
- It terminates the circularity: the first acceptance is necessarily made under
  a rule not yet in force, and the record says so rather than hiding it.

### Negative

- The trust root is broad. A single record covering a whole corpus asserts less
  per artifact than individual review would, and that weakness is permanent —
  it cannot be strengthened later without the per-artifact review that was
  rejected as disproportionate.
- It depends entirely on the owner's assertion. That is unavoidable for a trust
  root, but it means the baseline is exactly as trustworthy as that assertion.

### Neutral

- Being an Authoritative Artifact, the Bootstrap Acceptance Record inherits the
  regress recorded in `ISSUE-0042`. As the trust root, it is the natural base
  case — but that is asserted here, not settled.

## Compliance

Exactly one Bootstrap Acceptance Record exists, and it names the repository
revision it covers. No second retrospective acceptance is ever created. Every
artifact revision created after that named revision follows the normal
acceptance workflow.
