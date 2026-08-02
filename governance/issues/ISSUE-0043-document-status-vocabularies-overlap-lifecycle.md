---
id: ISSUE-0043
title: The project's document status vocabularies overlap the revision lifecycle
type: inconsistency
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/documentation-system.md
  - governance/adr/ADR-0020-artifact-taxonomy-and-revision-lifecycle-are-independent.md
resolved-by: null
---

# ISSUE-0043 — Document status vocabularies overlap the revision lifecycle

## Statement

`governance/documentation-system.md` defines three status vocabularies, written
in M1 before the revision lifecycle existed:

| Document type | Status values |
|---|---|
| ADR | `proposed`, `accepted`, `superseded`, `rejected` |
| Issue | `open`, `resolved`, `deferred`, `closed` |
| Governance document | `accepted`, `current`, `proposal`, `superseded` |

`ADR-0020` defines a fourth — the **revision lifecycle**: `Draft`,
`Under Review`, `Accepted`, `Active`, `Superseded`, `Archived`.

These overlap without agreeing. An ADR marked `status: accepted` is, in lifecycle
terms, `Active` — the current governing revision. An ADR marked
`status: proposed` is `Under Review` or `Draft`. `superseded` appears in three
vocabularies at once.

## Why it matters

`shared/vocabularies/` is an M2 deliverable and will encode the lifecycle as a
closed vocabulary. Encoding it beside three overlapping legacy vocabularies
guarantees that every schema, validator and projection downstream inherits the
ambiguity.

It is also a live confusion in this repository right now: `ADR-0020` says exactly
one revision is `Active` at a time, while nineteen ADRs are simultaneously
marked `status: accepted`.

## Options

- **Adopt the revision lifecycle universally**, replacing the ADR and governance
  status vocabularies. One vocabulary for every artifact. Cleanest, and the most
  churn — every front matter block in `governance/` changes.
- **Keep issue status separate, unify the rest.** Issue status genuinely
  describes something else — whether a *question* is answered, not whether a
  *revision* governs. `open`/`resolved`/`deferred`/`closed` may be a legitimately
  distinct axis.
- **Map rather than replace.** Keep the existing vocabularies and define a
  mapping to lifecycle states. Least churn; leaves two names for one concept,
  which is the failure `ISSUE-0038` was opened to prevent.

The second option is the most likely correct, but the distinction it rests on —
that an issue's status is not a revision lifecycle — has not been confirmed.

## Resolution criteria

An ADR fixing which vocabularies exist, what each governs, and how the
documentation system is updated. Must precede `shared/vocabularies/`.
