---
id: ADR-0060
title: Mechanical Discovery is compilation; Interpretive Discovery is authoring
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0071]
related: [ADR-0015, ADR-0020, ADR-0058, ADR-0059, ADR-0061, ISSUE-0072]
---

# ADR-0060 — Mechanical and Interpretive Discovery

## Context

`ADR-0059` established that Engineering OS maximizes discovered knowledge, and
listed six kinds. `ISSUE-0071` recorded that they fall on both sides of a line:
traceability and dependency graphs follow declared links, while architectural
patterns and semantic clusters are judgements.

`ADR-0020` requires the compiler to be deterministic and forbids a generator
invoking an agent. Either discovery is algorithmic, or that rule needed
qualifying.

## Decision

**The word "discovery" conflates two fundamentally different activities.**
Engineering OS distinguishes them explicitly.

### Mechanical Discovery

Knowledge **derivable exclusively from authoritative artifacts using
deterministic algorithms**.

Traceability · dependency graphs · impact graphs · registry projections ·
transitive relationships · consistency checks · ontology expansion · validation
reports.

**Mechanical Discovery belongs to the Knowledge Compiler.** Its output is
deterministic and becomes part of the Canonical Knowledge Model.

### Interpretive Discovery

Knowledge requiring **interpretation, analogy, abstraction or architectural
judgment**.

Architectural patterns · recurring design principles · semantic clusters ·
potential simplifications · candidate abstractions · emergent concepts.

> **Interpretive Discovery is Authoring.**

Its output is a **proposal** — another authoritative artifact entering the normal
Engineering OS workflow. It is reviewed. It is accepted or rejected. Only after
acceptance does it become authoritative; only after compilation does it become
part of the Canonical Knowledge Model.

### Nothing requires modification

- the compiler remains deterministic;
- authoring remains non-deterministic;
- acceptance remains the trust boundary;
- the Canonical Knowledge Model remains mechanically reproducible.

## Clarification to ADR-0058

`ADR-0058` states that the Knowledge Compiler **extracts** Principles from
authoritative artifacts. That is true where principles are **declared**:
extracting a declaration is mechanical.

**Recognising** that several artifacts describe one recurring principle is
Interpretive Discovery, and therefore authoring — not compilation. A reader of
`ADR-0058` alone could take "extracts" to mean "recognises", which is now wrong.

Recorded as the sixth correction in the ADR index.

## Alternatives considered

**Qualify `ADR-0020`'s determinism rule** to admit non-deterministic compiler
stages. Rejected: determinism is what makes derived artifacts verifiable and
`ADR-0012`'s synchronization check possible. Weakening it to accommodate one
capability would cost the property the whole derived tier rests on.

**Drop the interpretive discoveries from `ADR-0059`'s ambition.** Rejected: they
are the most valuable ones. The Registry Pattern took six independent arrivals
across nine sessions before a human noticed it.

**Let the compiler invoke an agent for interpretive stages.** Rejected —
`ADR-0015` forbids it, and the prohibition exists precisely so that a
compilation result is never a judgement in disguise.

## Consequences

### Positive

- **Every existing principle survives untouched**, which is the strongest
  possible outcome for a conflict between two accepted decisions.
- Interpretive Discovery gains a defined path: propose, review, accept, compile.
  An agent-proposed architectural pattern is an ordinary authoritative artifact,
  subject to the same acceptance as any other.
- It names what this project has been doing manually. The Registry Pattern and
  the reframing pattern were Interpretive Discoveries; each became an ADR, was
  accepted, and only then became architecture.
- The compiler's scope is now bounded by a testable criterion — *derivable
  exclusively by deterministic algorithm* — rather than by intuition.

### Negative

- **Interpretive Discovery has no tooling and no defined proposal form.** The
  path exists in principle; nothing says what an agent-produced proposal looks
  like or how it is distinguished from a human-authored one at review time.
- **How an artifact declares the Principles it establishes is undefined**, and
  the existing corpus of fifty-nine ADRs declares none. `ISSUE-0072`.
- The boundary will be argued at the margin. Ontology expansion is listed as
  mechanical, but expansion rules encode judgements made when the ontology was
  authored — the determinism is real, the neutrality is not.

### Neutral

- This is the reading `ISSUE-0071` recorded as the one that would preserve every
  rule. The second time an issue's own suggested answer was adopted, after
  `ISSUE-0045`.

## Compliance

No compiler stage performs interpretation. Every Interpretive Discovery enters
as a proposal through the normal acceptance workflow. Nothing enters the
Canonical Knowledge Model except by deterministic derivation from accepted
authoritative artifacts.
