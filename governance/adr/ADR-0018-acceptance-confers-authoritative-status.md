---
id: ADR-0018
title: Acceptance confers authoritative status; compilation remains deterministic
status: accepted
date: 2026-08-02
supersedes: ADR-0015
superseded-by: null
resolves: [ISSUE-0009]
related: [ADR-0014, ISSUE-0038, ISSUE-0039, ISSUE-0040, ISSUE-0041]
---

# ADR-0018 — Acceptance confers authoritative status

**This is a foundational architectural principle.** The entire three-tier model
of `ADR-0014` rests on the authoritative tier being trustworthy, and this ADR
defines what makes it so.

## Context

`ADR-0015` established that authoring is non-deterministic and compilation is
deterministic, and that an artifact becomes authoritative once "reviewed and
committed". It then drew a consequence that turns out to be wrong: that version
control is the boundary marker, so one can tell whether an artifact is
authoritative by asking whether it is committed.

`SESSION-0004` recorded the resulting gap in blunt terms: **nothing prevented an
agent from committing its own output and thereby self-certifying it as
authoritative.** Every artifact in this repository was produced that way.

`ISSUE-0009` had asked who holds authority at a gate. The answer reframes the
question — the issue is not gate authority, it is what acceptance *is*.

## Decision

**Acceptance is a first-class engineering concept and is modeled explicitly.**

**Authoritative status is not determined by who created an artifact. It is
determined by an explicit acceptance process.**

### Artifact lifecycle

```text
Draft → Under Review → Accepted → Authoritative → Superseded → Archived
```

### Acceptance is an engineering decision, not a Git operation

**A commit alone does not make an artifact authoritative.**

### Three conditions

Acceptance requires all of:

1. **Explicit reviewer approval.**
2. **Traceability** to the motivating issue, ADR or requirement.
3. **Successful validation** of all applicable deterministic checks.

### Who may accept

The reviewer may be a human today. Future versions may allow trusted automated
acceptance policies, but **only through explicitly configured governance rules**.

**Engineering OS must never assume that an AI agent can accept its own work by
default. Self-certification is prohibited unless an explicit governance policy
enables it.**

### Acceptance is knowledge

Acceptance itself becomes part of the knowledge model and is traceable.

## What survives from ADR-0015

The determinism principle carries forward unchanged:

```text
Authoring    → non-deterministic
Compilation  → deterministic
```

So do: AI agents are authors exactly like human engineers; no fifth artifact
kind is required; a generator may never invoke an agent.

**What changes** is the boundary marker. Version control is no longer what makes
an artifact authoritative — acceptance is, and the commit is at most a record of
it. The determinism boundary now sits at the *acceptance* transition rather than
the *commit* transition.

## Alternatives considered

**Commit as acceptance**, per `ADR-0015`. Rejected: it is observable and cheap,
but it permits self-certification by construction, which is precisely the
failure being closed. An agent with write access could confer authority on its
own output, and the authoritative tier would mean nothing.

**Trust-based agent acceptance** — allow agents to accept work by default, with
audit after the fact. Rejected: it inverts the safe default. Automated
acceptance remains possible, but only when explicitly enabled by governance
rules, never as the baseline.

**Binary authoritative / not-authoritative, with no lifecycle.** Rejected: it
cannot express *under review*, and it cannot express *superseded* — a state the
ADR corpus of this very repository already needs.

## Consequences

### Positive

- **Self-certification is prohibited by default.** The gap found in
  `SESSION-0004` is now named and closed at the level of principle.
- The authoritative tier becomes trustworthy for a stated reason, so
  `ADR-0014`'s three-tier model rests on something.
- Acceptance becomes traceable knowledge rather than an invisible social act.
- The lifecycle can express states the project already needs — `Superseded` is
  what three ADRs in this repository already are.

### Negative

- **Acceptance records are new artifacts that do not exist**, and their shape and
  location are undefined — `ISSUE-0041`.
- **The governance-rules mechanism does not exist.** The prohibition names an
  escape hatch — "explicitly configured governance rules" — with nothing behind
  it. `ISSUE-0039`.
- **Everything already in this repository was self-certified**, and now has no
  valid acceptance record. That is a live compliance gap, not a hypothetical —
  `ISSUE-0040`.
- **`authoritative` now names two different things**: a lifecycle state here, and
  an artifact kind in `ADR-0012`. This is the same class of collision as the
  overloaded word "skill" resolved in M1, and must be settled before either
  vocabulary is written — `ISSUE-0038`.
- Acceptance adds real friction to every artifact. For a solo author it may feel
  like ceremony; the cost is accepted deliberately, because the alternative is
  an authoritative tier that means nothing.

### Neutral

- Nothing changes for the compiler, which continues to consume whatever the
  authoritative tier contains.

## Compliance

No artifact is treated as authoritative without a recorded acceptance satisfying
the three conditions. No agent accepts its own work unless an explicit
governance policy permits it. Acceptance records are traceable to the motivating
issue, ADR or requirement.
