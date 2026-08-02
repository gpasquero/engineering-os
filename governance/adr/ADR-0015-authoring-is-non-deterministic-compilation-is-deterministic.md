---
id: ADR-0015
title: Authoring is non-deterministic; compilation is deterministic
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0033]
related: [ADR-0012, ADR-0014, ISSUE-0009]
---

# ADR-0015 — Authoring is non-deterministic; compilation is deterministic

**This is an explicit architectural principle**, not merely a resolution.

## Context

`ADR-0012` requires every executable pipeline to be deterministic. Engineering
OS is a framework for AI software engineering, and agent output is not
deterministic. `ISSUE-0033` recorded that the boundary between the two was
undefined, and warned that drawing it too wide would make the requirement
unenforceable while drawing it too narrowly would leave agent-produced
artifacts outside the taxonomy entirely.

## Decision

**Determinism applies to the compiler, not to the author.**

AI agents are **authors**, exactly like human engineers. Authors are inherently
non-deterministic.

Once an authored artifact has been reviewed and committed, it becomes an
**authoritative artifact**. From that point forward the Knowledge Compiler must
behave deterministically: given the same authoritative repository state, it must
always produce identical outputs.

```text
Authoring     → non-deterministic
Compilation   → deterministic
```

**No additional artifact category is required.** The four kinds in `ADR-0012`
stand.

**AI-generated content becomes authoritative only after human acceptance and
version control.** Acceptance is the transition; the commit is the record of it.

## Alternatives considered

**A fifth artifact kind for agent-produced, not-yet-reviewed output.**
Considered in `ISSUE-0033` and rejected. It would encode a *workflow state* as
an *artifact kind*, and the two are different things: an unreviewed draft is not
a different kind of artifact, it is an artifact that has not yet been accepted.
Adding the category would also require every generator, validator and manifest
to reason about a state that only exists between authoring and review.

**Requiring agent output to be deterministic** — for example by fixing seeds or
constraining generation. Rejected as both infeasible and pointless: the value of
an agent author is judgement, and judgement that is reproducible by construction
is not judgement.

**Dropping the determinism requirement.** Rejected: it is what makes derived
artifacts verifiable, and without it `ADR-0012`'s continuous synchronization
check cannot exist.

## Consequences

### Positive

- The determinism requirement becomes enforceable, because it applies only to
  code that can satisfy it.
- **Agents and humans are treated identically as authors.** This is a stronger
  statement than it appears: it means the methodology's review, traceability and
  acceptance machinery applies uniformly, with no special-casing for AI output.
  There is no separate "AI content" pathway to maintain.
- The taxonomy stays at four kinds.
- Version control becomes the boundary marker, which is observable and
  auditable — you can always tell whether an artifact is authoritative by asking
  whether it is committed.

### Negative

- **This makes human acceptance a hard architectural requirement**, and the
  project has not defined who accepts, on what basis, or what review means in
  practice. `ISSUE-0009` (human-in-the-loop authority) is now load-bearing for
  the architecture and not only for the methodology.
- An unreviewed agent artifact sitting in a working tree has no defined status.
  This is acceptable — it is simply not yet authoritative — but tooling must not
  assume that everything on disk is authoritative.
- A generator may never invoke an agent, because that would make the generator
  non-deterministic. Any pipeline stage that would benefit from judgement must
  instead be restructured as authoring followed by compilation.

### Neutral

- Nothing changes for purely human-authored artifacts; the decision formalizes
  what was already implicit for them.

## Compliance

No generator invokes an agent. No artifact is treated as authoritative before it
is committed. Agent-authored and human-authored artifacts are subject to the
same review and traceability requirements, with no separate pathway for either.
