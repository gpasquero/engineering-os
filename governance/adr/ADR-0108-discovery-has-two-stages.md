---
id: ADR-0108
title: Discovery has two stages; Interpretive Discovery operates exclusively on the Mechanical Model
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0060, ADR-0081, ADR-0103, ADR-0105, ADR-0107]
---

# ADR-0108 — Discovery has two stages

## Context

`SESSION-0039` concluded that deterministic extraction is *"better than a human
at coverage and worse at abstraction"* and called that **the deterministic
ceiling**.

> **That is not the limit of deterministic Discovery. It is the limit of the
> current deterministic Discovery Workers.**

**The correction is demonstrable.** Rule `R1` read `it()` case names and proposed
eight invariants where a human wrote one. The abstraction the human produced was
**already in the file**:

```text
describe('account lockout & brute-force protection')
  it('increments the failed counter on wrong password')
  it('locks the account on the 5th wrong password for exactly 15 minutes')
  ...
```

A rule reading the `describe` block reaches the human's abstraction exactly. **The
ceiling was a property of the rule, not of determinism.**

## Decision

**Discovery is two stages.**

| Stage | Produces | Reads |
|---|---|---|
| **Mechanical Discovery** | a reproducible **Mechanical Engineering Model** | source files |
| **Interpretive Discovery** | proposed engineering knowledge | **exclusively the Mechanical Model** |

### The Mechanical Model contains facts, not engineering vocabulary

*This file declares a `describe` block with this text containing these `it`
cases.* **Not** *this is an invariant.*

Mechanical Discovery records what a repository **contains**. Naming any of it as
a Concept, Capability or Invariant is interpretation, and belongs to the second
stage.

### Interpreters never read source

**This is the load-bearing constraint.** An interpreter that could reach the
repository would make the Mechanical Model an optimisation rather than an
interface.

Because interpreters see only the Mechanical Model:

- **extraction quality and interpretation quality are measured separately** — a
  missing fact is an extractor defect, a bad abstraction is an interpreter
  defect, and today they are indistinguishable;
- **deterministic and probabilistic interpretation are comparable over identical
  input**, which is the only way that comparison means anything;
- **provenance stays clean** — an interpretation cites mechanical facts, and each
  fact cites its file;
- **each stage evolves independently.**

The Mechanical Model is to Discovery what the Canonical Knowledge Model is to the
platform (`ADR-0081`): **the interface everything downstream consumes.**

### Relationship to `ADR-0060`

`ADR-0060` split Mechanical Discovery from Interpretive Discovery and mapped them
to compilation and authoring. **This applies the same split one layer down**, to
the discovery of a repository, and the mapping holds: mechanical extraction is
compilation-like and reproducible; interpretation proposes, and proposals need
review.

## Alternatives considered

**Keep one stage and write better rules.** Rejected. Better rules would have
raised the measurement and left it unattributable — the improvement could be
credited to extraction or to interpretation and nothing would distinguish them.

**Let interpreters read source when the Mechanical Model lacks a fact.**
Rejected, and it is the tempting shortcut. It would make every comparison between
interpreters invalid, because they would no longer share an input.

**Make the Mechanical Model an internal representation rather than a serialized
artifact.** Rejected: it must be inspectable to be a measurement boundary, and
reproducible to be a fair input.

## Consequences

### Positive

- **The premature conclusion is corrected with a mechanism, not a retraction.**
  The ceiling can now be measured, and it will be measured against a fixed input.
- **A probabilistic interpreter becomes an experiment rather than a leap**: same
  Mechanical Model, different interpreter, comparable output.
- A missing fact and a bad abstraction become different defects with different
  owners.

### Negative

- **The Mechanical Model's vocabulary is itself a design choice**, and one that
  constrains every interpreter downstream. A fact nobody extracted is invisible
  to interpretation however good the interpreter — the ceiling moves rather than
  disappearing.
- Two artifacts where there was one, and the intermediate one must be maintained.

### Neutral

- No existing decision changes. `ADR-0107`'s three worker kinds survive, now
  assigned to stages.

## Compliance

`discovery/mechanical.py` produces a serialized Mechanical Engineering Model.
`discovery/interpretive.py` **takes it as its only input** and never opens a
source file. **No claim about a deterministic ceiling is made without naming the
rules that produced it.**
