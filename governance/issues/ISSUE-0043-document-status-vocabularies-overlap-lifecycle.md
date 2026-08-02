---
id: ISSUE-0043
title: The project's document status vocabularies overlap the revision lifecycle
type: inconsistency
status: resolved
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/documentation-system.md
  - governance/adr/ADR-0020-artifact-taxonomy-and-revision-lifecycle-are-independent.md
resolved-by: ADR-0025
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

## Resolution

`ADR-0025`, and it addresses the root cause rather than this symptom.

**Every state belongs to exactly one state machine. There is no global concept
of "state."** State names may coincide only if explicitly namespaced:

```text
ArtifactLifecycle.Active     IssueLifecycle.Open
ADRLifecycle.Accepted        AcceptanceLifecycle.Recorded
```

> The same textual label must never imply semantic equivalence across state
> machines.

`shared/vocabularies/` therefore defines vocabularies **grouped by state
machine**, not as one global list.

The three "overlapping" vocabularies identified above are retroactively
legitimate — they were always separate state machines, merely never named as
such. The second option listed above was in effect chosen, and generalized: not
just issue status, but *every* vocabulary is its own machine.

The live contradiction dissolves without renaming anything. Nineteen ADRs marked
`ADRLifecycle.Accepted` never conflicted with one revision being
`ArtifactLifecycle.Active`; the two were never the same state.

This is now a **fundamental modeling rule for the entire Engineering OS**,
governing how skills model state machines in target domains as well.

Opened by this answer: `ISSUE-0044` (`ArtifactLifecycle` conflicts with
`ADR-0020`'s revision framing) and `ISSUE-0045` (the state machine inventory is
not fixed).
