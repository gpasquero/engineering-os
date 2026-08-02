---
id: ISSUE-0068
title: ADR-0038's mandatory compiler-phase question conflicts with the semantic/compiler separation
type: inconsistency
status: resolved
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0053-semantic-architecture-is-separate-from-compiler-architecture.md
  - governance/adr/ADR-0038-four-questions-for-every-new-artifact-type.md
  - governance/adr/ADR-0035-engineering-os-metamodel.md
resolved-by: ADR-0055
---

# ISSUE-0068 — The compiler-phase question conflicts with the separation

## Statement

`ADR-0038` requires every new artifact type to answer four questions before
acceptance, the fourth being **"which compiler phase consumes or produces
it?"** — and states that **an unanswerable question is a rejection, not a gap to
fill later**.

`ADR-0053` establishes that the metamodel defines what exists and the compiler
defines how it is transformed, and that **neither embeds concepts belonging to
the other**.

A purely semantic concept may have no compiler phase. Under `ADR-0038` it is
rejected. Under `ADR-0053` it is exactly what it should be.

## Why it matters

`ADR-0038` governs the acceptance of every new artifact type, and M2 introduces
several — `DimensionSpecification`, Dimension Review, the manifests, the
contracts. Each must answer question 4.

If the honest answer for a semantic concept is "none", the rule as written
rejects it.

## The precedent that probably applies

`ADR-0039` faced the same shape. `ADR-0037` had required every artifact to
belong to exactly one Semantic Layer; the methodology artifacts had none; and
the resolution was that **`None (Not Applicable)` is a valid answer** for
artifacts that are genuinely orthogonal, while a genuinely undetermined answer
remains a rejection.

The same distinction fits here — but `ADR-0039` made it for question 1 only, and
nothing extends it to question 4.

## The deeper question

`ADR-0038`'s four questions predate `ADR-0053` by four sessions. Two of them —
Semantic Layer and Compilation Phase — are now known to belong to *different
architectures*.

Asking both of every artifact type may itself be the mixing `ADR-0053` forbids:
a single gate that requires every concept to declare a position in both
architectures, whether or not it belongs to both.

`ADR-0053`'s own three questions — semantic, compilation, or both — may be the
correct replacement for `ADR-0038`'s framing rather than an addition to it.

## Three gates now overlap

- `ADR-0035` — position the concept in the Metamodel first.
- `ADR-0038` — answer four questions.
- `ADR-0053` — answer three questions.

Nothing states how they compose, whether they are applied in order, or what
happens when one admits a concept another rejects.

## Resolution

`ADR-0055`, which takes the deeper reading this issue offered rather than the
narrower fix.

> **The questions defined by `ADR-0038` are not mandatory for every artifact.
> They are conditional. Every Gate declares which questions apply.**

| Gate | Questions |
|---|---|
| Metamodel Position Gate | Which metamodel entity does it instantiate? Which semantic layer owns it? |
| Compiler Impact Review | Which compiler phase consumes it? Which produces it? |
| Dimension Review | Does it satisfy the Dimension criteria? Is another construct more appropriate? |
| Acceptance Review | Is it authoritative? Has it been reviewed? Does it satisfy applicable validation? |

**Questions belong to Gates rather than to artifacts.** A purely semantic
concept never encounters a compiler question, because the Compiler Impact Review
is not triggered for it.

Extending `ADR-0039`'s `None (Not Applicable)` precedent — this issue's likely
answer — was rejected as the smaller fix: it would still ask the question.

The three-gate overlap resolves into **triggering** rather than composition:
which gates apply, not how they combine.

`ADR-0038` is superseded. Its four questions survive, redistributed to the gates
that own them.

**Newly load-bearing:** triggering conditions are now the entire enforcement
surface, and `ADR-0054` lists the field without saying what may appear in one.
