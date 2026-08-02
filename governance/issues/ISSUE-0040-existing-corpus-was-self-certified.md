---
id: ISSUE-0040
title: The entire existing corpus was self-certified and has no acceptance record
type: risk
status: resolved
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0018-acceptance-confers-authoritative-status.md
  - governance/sessions/SESSION-0004-2026-08-02.md
resolved-by: ADR-0022
---

# ISSUE-0040 — The existing corpus was self-certified

## Statement

`ADR-0018` prohibits self-certification and requires that every authoritative
artifact carry an acceptance record satisfying three conditions: explicit
reviewer approval, traceability to a motivating issue or ADR, and successful
deterministic validation.

**Every artifact currently in this repository was authored by an agent and
committed by that same agent.** None has a reviewer approval, and none has an
acceptance record. That includes all nineteen ADRs — among them `ADR-0018`
itself.

## Why it matters

The repository does not satisfy the rule it just adopted. This is not a
technicality: `ADR-0014`'s three-tier model treats the authoritative tier as
trustworthy, and `ADR-0018` says trust comes from acceptance. If the entire
corpus lacks acceptance, the authoritative tier currently rests on nothing.

Left unaddressed, the project would carry a permanent silent exception to its
own foundational principle — and would have no honest answer when an adopter
asks whether Engineering OS follows its own rules.

## Options

- **Retroactive bulk acceptance.** One acceptance record covering the M1–M2
  corpus, with the project owner as reviewer, traceable to the sessions that
  produced it. Cheap and honest about what actually happened: the owner did read
  and direct this work, even if no acceptance step was recorded at the time.
- **Per-artifact retroactive acceptance.** Most rigorous, and disproportionate
  for a corpus this size.
- **Grandfather clause**, recorded as an explicit exception with an expiry.
  Honest, but leaves the foundational tier untrusted for as long as it lasts.
- **Do nothing.** Rejected. A silent exception to a foundational principle is
  exactly the drift the project exists to prevent.

The first option is the most proportionate. It requires that `ISSUE-0041`
(acceptance record shape) be settled first, since there is nothing yet to write
the record into.

## A note on ordering

`ADR-0018` cannot accept itself without circularity. Whatever mechanism resolves
this must state its own base case — the first acceptance is necessarily made
under a rule that is not yet in force.

## Resolution

`ADR-0022`, realised as **`ACCEPT-0001`** — the repository's trust root.

**Engineering OS cannot retroactively invent history**, so the repository
bootstraps trust explicitly instead. A single Bootstrap Acceptance Record covers
the corpus at revision `2b6484f`, stating that the artifacts were produced
collaboratively during the bootstrap phase, were reviewed and directed by the
project owner, that formal Acceptance Records did not yet exist, and that this
record establishes the initial trusted baseline.

**This is the only retrospective acceptance permitted.** All future authoritative
revisions follow the normal workflow.

The record is scoped to a **named revision** and explicitly cannot accept work
created after it — otherwise a one-time trust root would become a standing
exemption from acceptance.

The circularity noted above is stated in the record rather than concealed: the
first acceptance is necessarily made under a rule not yet in force.
