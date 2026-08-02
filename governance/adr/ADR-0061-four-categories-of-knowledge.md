---
id: ADR-0061
title: Four categories of knowledge; the Knowledge Compiler is not an intelligence
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0012, ADR-0015, ADR-0020, ADR-0059, ADR-0060, ISSUE-0073]
---

# ADR-0061 — Four categories of knowledge

**This is a foundational principle.** It precisely defines the boundary between
reasoning and compilation, and completes the epistemological model of
Engineering OS.

## Context

`ADR-0059` distinguished authored from discovered knowledge; `ADR-0060` split
discovery into Mechanical and Interpretive. What was still missing was a single
statement of what kinds of knowledge exist and where each enters the system.

## Decision

Engineering OS distinguishes **four categories of knowledge**.

### Authored Knowledge

Written by humans or AI authors. **Accepted through governance.** Compiled into
the knowledge model.

### Mechanical Knowledge

**Deterministically derived** from Authored Knowledge. Produced by the compiler.
**Always reproducible.**

### Interpretive Knowledge

Architectural hypotheses, discoveries and abstractions proposed through
engineering work. **Never produced by the compiler.** Always enters the system
**through Authoring**.

### Operational Knowledge

Runtime observations, metrics, telemetry and execution history. **Outside the
Engineering Knowledge Model unless explicitly imported as authored knowledge.**

### The boundary

> **The Knowledge Compiler is not an intelligence. It is a deterministic
> semantic compiler.**
>
> **Intelligence remains outside the compiler and participates only through the
> Authoring process.**

## Alternatives considered

**Three categories, folding Operational into Authored.** Rejected: telemetry is
generated continuously by a running system, not authored by anyone. Treating it
as authored would make acceptance meaningless for it, or make acceptance a
bottleneck on a firehose.

**Admit Operational Knowledge directly into the knowledge model.** Rejected: it
is unbounded, changes without any authoring act, and would make the Canonical
Knowledge Model non-reproducible — a compilation would depend on when it ran.

**Allow the compiler limited intelligence** for well-understood inferences.
Rejected, and this is the rejection the principle exists for. A boundary that
admits "a little" interpretation has no defensible position: every subsequent
capability argues from the precedent.

## Consequences

### Positive

- **It states what "AI-first" means here**, which the project had never pinned
  down. Intelligence is real and central — it participates as an *author*, under
  the same acceptance discipline as a human. It is not smuggled into the
  transformation layer.
- Each category has a distinct entry point, trust chain and correction path.
  Authored enters through acceptance; Mechanical through compilation;
  Interpretive through authoring; Operational through explicit import.
- The Canonical Knowledge Model stays mechanically reproducible, which is what
  `ADR-0036`'s conformance and `ADR-0012`'s synchronization checking both
  require.
- Operational Knowledge is named rather than ignored — a category the project
  had no word for, and which every target system produces.

### Negative

- **It sits awkwardly against the inherited evidence hierarchy.** The
  `reconstruct-system-knowledge` prototype ranks *observable runtime behaviour*
  as the **highest-authority evidence**, and its assertion vocabulary includes
  `observed` for exactly this. Placing Operational Knowledge outside the model
  by default means the strongest evidence requires the most work to admit.
  `ISSUE-0073`.
- **"Runtime" now names two different things.** `ADR-0012`'s `runtime` artifact
  kind means temporary compiler output; Operational Knowledge means telemetry
  from a target system. `ADR-0057`'s qualification discipline is one session old
  and already applies. Also `ISSUE-0073`.
- Interpretive Knowledge has a defined path and no tooling, so the category is
  currently aspirational.

### Neutral

- The four categories map onto existing structures without contradiction:
  Authored and Interpretive resolve to `authoritative` artifacts once accepted,
  Mechanical to `derived`.

## Compliance

No compiler stage performs interpretation. No Operational Knowledge enters the
knowledge model except by explicit import as Authored Knowledge. Every piece of
knowledge in the model is identifiable as one of the four categories.
