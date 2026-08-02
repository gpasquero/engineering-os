---
id: ISSUE-0063
title: The minimum set of classifications that must be serialized is unstated
type: gap
status: deferred
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0045-human-representation-and-front-matter-as-interchange-syntax.md
  - governance/adr/ADR-0038-four-questions-for-every-new-artifact-type.md
  - governance/adr/ADR-0001-repository-is-persistent-memory.md
resolved-by: null
defers-to: [M2]
debt: architectural
---

# ISSUE-0063 — The minimum serialized classification set is unstated

> **Architectural debt** (`ADR-0062`). Deferred because it is not needed to
> build the next deliverable. Reopen when implementation requires it.

## Statement

`ADR-0045` says every authoritative artifact **"may expose a Human
Representation of selected classifications"**.

Two words carry the gap. **"May"** leaves it optional. **"Selected"** leaves it
partial, without saying selected by whom or against what criterion.

## Why it matters

`ADR-0045` exists to satisfy `ADR-0017` and `ADR-0001`: the repository must stay
understandable without executing the compiler. An optional, partial mechanism
guarantees that only when it happens to be used.

`ADR-0038` makes four classifications mandatory to know for every artifact type:

1. which layer owns it
2. authoritative or derived
3. what metamodel entity it instantiates
4. which compiler phase consumes or produces it

An artifact can satisfy `ADR-0045` while serializing none of those four, and
would then be exactly as opaque as the graph-only option that `ISSUE-0060`
rejected.

## The tension in one line

**`ADR-0038` decides what must be knowable. `ADR-0045` decides what may be
visible. Nothing connects them.**

## Options

- **A mandatory minimum set**, at least `ADR-0038`'s four. Directly satisfies
  `ADR-0001`; adds required front matter to every artifact.
- **Mandatory per artifact type, declared in the metamodel.** Each type states
  which classifications it serializes, which suits dimensions that are constant
  across a type. Requires reading the type definition to know what to expect.
- **Optional, with a validation rule** that a projection cannot claim
  human-readability unless a set is serialized. Defers the problem to M9 and
  leaves the corpus unreadable until then.
- **Optional as written.** Only defensible if `ADR-0001`'s legibility guarantee
  is understood as weaker than it reads.

## A related question

`ADR-0045` says the semantic relationship exists *independently* of the
serialization. So a serialization can be **incomplete** without being **wrong**.
Whether it can be *stale* — present but disagreeing with the assignment — is a
different matter, and nothing yet checks it.

## Resolution criteria

An ADR stating the minimum classifications every authoritative artifact must
serialize, or an explicit decision that the minimum is empty with the
consequences for `ADR-0001` accepted.
