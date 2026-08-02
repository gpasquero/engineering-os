---
id: ISSUE-0072
title: How an authoritative artifact declares the Principles it establishes
type: gap
status: deferred
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0058-principles-are-semantic-entities-not-artifacts.md
  - governance/adr/ADR-0060-mechanical-and-interpretive-discovery.md
  - governance/adr/ADR-0045-human-representation-and-front-matter-as-interchange-syntax.md
resolved-by: null
defers-to: [M2]
debt: architectural
---

# ISSUE-0072 — How artifacts declare the Principles they establish

> **Architectural debt** (`ADR-0062`). Deferred because it is not needed to
> build the next deliverable. Reopen when implementation requires it.

## Statement

`ADR-0058` establishes that the Knowledge Compiler **extracts Principles from
authoritative artifacts**.

`ADR-0060` narrows that: extracting a **declaration** is Mechanical Discovery;
**recognising** a recurring principle is Interpretive Discovery, and therefore
authoring rather than compilation.

So Principles must be **declared**. Nothing says how.

## Why it matters

Principles are a metamodel entity and M2 work. The compiler cannot extract what
no artifact declares, and the declaration form determines what the Metamodel
Position Gate asks of an ADR.

**Fifty-nine ADRs currently declare nothing.** The three principles `ADR-0056`
names — the Registry Pattern, `Definition → Instance → Assignment`, semantic
versus compilation architecture — exist only as prose across `ADR-0027`,
`ADR-0028`, `ADR-0031`, `ADR-0052` and `ADR-0053`.

## The retrospective problem

This has the shape of `ISSUE-0040`, where the entire corpus predated a rule it
then failed. That was resolved by a single bootstrap acceptance
(`ACCEPT-0001`) — an explicit, one-time trust root rather than a pretence that
history was different.

The same choice arises here, and the same options apply: declare retroactively,
declare going forward only, or accept that principles established before the
mechanism existed are found by Interpretive Discovery instead.

The third is the most honest and the most expensive: it means the Registry
Pattern enters as a *proposal* and goes through acceptance like any other.

## Options

- **Front matter declaration**, per `ADR-0045` — an `establishes:` field listing
  principle identifiers. Consistent with the existing serialization model, and
  it makes the declaration visible without the compiler.
- **A structured section** in the ADR body. More expressive, harder to parse
  deterministically.
- **Declaration in the Principle's own registry**, with ADRs referenced rather
  than referencing. Inverts the direction; a principle would then be registered,
  which sits oddly with `ADR-0058`'s "not an artifact".

## Open sub-questions

- Does a Principle have a stable identifier, and who allocates it?
- Can two ADRs declare the same Principle? `ADR-0058` says one principle may
  emerge from several artifacts, so presumably yes — which requires identity to
  be shared rather than derived from the declaring artifact.
- Does declaring a Principle require passing a Gate, as `ADR-0049` requires for
  a Dimension?

## Resolution criteria

An ADR defining the declaration form, the identity scheme for Principles, and
how the existing corpus is handled.
