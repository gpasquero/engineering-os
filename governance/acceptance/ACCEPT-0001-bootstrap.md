---
id: ACCEPT-0001
artifact: engineering-os bootstrap corpus (entire repository)
artifact-revision: 2b6484f
reviewer: gpasquero (project owner)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0022, ADR-0020, ADR-0021, ADR-0023]
related-issues: [ISSUE-0040, ISSUE-0009]
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0001 — Bootstrap corpus

**This is the trust root of the repository.** Every later acceptance chains back
to this record.

## Artifact

The complete contents of the `engineering-os` repository at revision
**`2b6484f`** — the bootstrap corpus.

This comprises milestone M1 (repository architecture and documentation system),
the architectural decisions taken while M2 was blocked (`ADR-0001` through
`ADR-0019`), the issue corpus (`ISSUE-0001` through `ISSUE-0041`), the session
journal (`SESSION-0001` through `SESSION-0005`), and the frozen provenance in
`imports/` and `sources/`.

### Scope boundary

**This record covers revision `2b6484f` and nothing after it.**

Artifacts created after that revision — including `ADR-0020` through `ADR-0023`,
this record, and everything else in the commit that introduces them — are **not**
covered. They are `Under Review` until accepted through the normal workflow.

This boundary is stated explicitly because a bootstrap record that pre-accepted
future work would convert a one-time trust root into a standing exemption from
acceptance, defeating its purpose (`ADR-0022`).

## Decision

**`accepted`.**

## Rationale

Per `ADR-0022`, Engineering OS cannot retroactively invent history. The
repository must instead bootstrap trust explicitly.

This record states that:

- **the artifacts were produced collaboratively during the bootstrap phase;**
- **they were reviewed and directed by the project owner;**
- **formal Acceptance Records did not yet exist;**
- **this record establishes the initial trusted baseline of the repository.**

The bootstrap corpus was not produced autonomously. Every architectural decision
in it originated with the project owner, who supplied the answers recorded in
`ADR-0009` through `ADR-0019` and directed the work at each step. What was
missing was not review — it was the *recording* of review, because the mechanism
for recording it did not yet exist.

This record supplies that recording, honestly and once.

## Condition 1 — reviewer approval

Approval given by the project owner (`gpasquero`), who directed the creation of
this record and specified its required content in the session that produced
`ADR-0020` through `ADR-0023`.

The record was authored by the agent and approved by the owner. **This is not
self-certification**: the author and the reviewer are different parties, which
is the requirement (`ADR-0023`).

## Condition 2 — traceability

- `ISSUE-0040` — the entire existing corpus was self-certified and had no
  acceptance record.
- `ADR-0022` — a single Bootstrap Acceptance Record establishes the trust root.
- `ADR-0018`, carried forward by `ADR-0020` — acceptance confers authoritative
  status.

## Condition 3 — validation summary

**No deterministic validators exist.** The reference implementation language is
deferred (`ISSUE-0036`), so no validation tooling has been built.

Per `ADR-0021`, where no deterministic validator exists none are applicable, and
condition 3 is satisfied. This is the normal reading of applicability, not an
exception.

Non-deterministic checks were nonetheless run during the bootstrap sessions and
are recorded in the session journal: identifier-to-filename consistency,
bidirectional ADR-to-issue traceability, supersession pair symmetry, relative
link resolution and referenced-path existence. These are *evidence*, not
satisfaction of condition 3.

## Exceptions

**One, and it is inherent to being a trust root.**

The bootstrap corpus was accepted as a single body rather than per artifact.
This asserts less per artifact than individual review would, and the weakness is
permanent — it cannot be strengthened later without the per-artifact review that
`ADR-0022` rejected as disproportionate.

No expiry. A trust root that expires is not a trust root.

## Notes

**On circularity.** `ADR-0022` and `ADR-0021` define the rules this record
follows, and both fall outside the revision this record covers. The first
acceptance is necessarily made under a rule not yet in force. `ADR-0022` states
this rather than concealing it.

**On the regress.** An Acceptance Record is itself an Authoritative Artifact and
by the letter of `ADR-0020` would require its own acceptance. `ADR-0022` asserts
this record as the base case. The general question is unresolved —
`ISSUE-0042`.

**On what a reader should conclude.** This baseline is exactly as trustworthy as
the project owner's assertion that they reviewed and directed the bootstrap
work. It claims nothing more.
