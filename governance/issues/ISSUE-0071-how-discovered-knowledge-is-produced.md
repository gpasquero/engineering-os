---
id: ISSUE-0071
title: How discovered knowledge is produced, and whether discovery can be deterministic
type: question
status: resolved
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2, M9]
evidence:
  - governance/adr/ADR-0059-authored-versus-discovered-knowledge.md
  - governance/adr/ADR-0058-principles-are-semantic-entities-not-artifacts.md
  - governance/adr/ADR-0020-artifact-taxonomy-and-revision-lifecycle-are-independent.md
resolved-by: ADR-0060
---

# ISSUE-0071 — How discovered knowledge is produced

## Statement

`ADR-0058` says the Knowledge Compiler **extracts** Principles from
authoritative artifacts. `ADR-0059` generalizes: the compiler **discovers**
Principles, traceability, dependency graphs, architectural patterns, impact
graphs and semantic clusters, and Engineering OS should **maximize** discovered
knowledge.

Neither says how.

## Why it matters

`ADR-0020` requires the compiler to be **deterministic** — the same
authoritative repository state must always produce identical outputs — and
`ADR-0015`, carried forward by `ADR-0020`, forbids a generator from invoking an
agent.

The listed discoveries do not obviously satisfy that. Traceability and
dependency graphs are mechanical: they follow declared links. **Architectural
patterns and semantic clusters are not.** A pattern is a judgement that several
things are the same kind of thing, and that judgement is what the project's
human reviewer has been making for nineteen sessions.

Either discovery is algorithmic, or `ADR-0020`'s determinism rule needs
qualifying. Both are consequential and neither has been chosen.

## The spectrum

| Discovery | Mechanism | Deterministic? |
|---|---|---|
| Traceability | follows declared references | yes |
| Dependency graphs | follows declared dependencies | yes |
| Impact graphs | transitive closure over dependencies | yes |
| Principles | **declared** by ADRs, or **inferred** across them | depends |
| Architectural patterns | recognition of recurring structure | not obviously |
| Semantic clusters | similarity over a graph | not obviously |

Principles sit at the hinge. If an ADR declares *"this establishes the Registry
Pattern"*, extraction is parsing and determinism holds. If the compiler infers
that four ADRs describe one pattern, it is doing what a reviewer did — and doing
it non-deterministically.

## Open sub-questions

- Are Principles declared in authoritative artifacts, or inferred from them?
- If some discovery is non-deterministic, is it still the compiler's work, or a
  separate agent-executed activity that produces authored artifacts for review?
  `ADR-0015` would suggest the latter: authoring is non-deterministic,
  compilation is deterministic, and an agent-produced pattern would be an
  authored artifact awaiting acceptance.
- **`ADR-0059` says "maximize" with no limit.** How is a discovered assertion
  validated? What prevents a confident falsehood entering the Canonical
  Knowledge Model with the authority of derivation?
- Is confidence represented? The inherited prototypes carry a confidence
  vocabulary (`high`/`medium`/`low`) that has no home yet.

## The reading that may resolve it

`ADR-0015`'s split already anticipates this. **Deterministic discovery is
compilation; non-deterministic discovery is authoring.** A pattern proposed by
an agent would be an authored artifact entering the normal acceptance workflow,
and only accepted patterns would be compiled.

That preserves every existing rule. It also means `ADR-0059`'s more ambitious
discoveries are not compiler features at all — which may or may not be the
intent.

## Resolution

`ADR-0060`, **adopting the reading recorded above.**

> The word "discovery" conflates two fundamentally different activities.

**Mechanical Discovery** — derivable exclusively from authoritative artifacts by
deterministic algorithm. Traceability, dependency graphs, impact graphs,
registry projections, transitive relationships, consistency checks, ontology
expansion, validation reports. **Belongs to the Knowledge Compiler.**

**Interpretive Discovery** — requiring interpretation, analogy, abstraction or
architectural judgment. Architectural patterns, recurring design principles,
semantic clusters, candidate abstractions, emergent concepts. **Is Authoring.**
Its output is a proposal entering the normal workflow: reviewed, accepted or
rejected, authoritative only after acceptance, in the Canonical Knowledge Model
only after compilation.

**No principle requires modification.** The compiler stays deterministic,
authoring stays non-deterministic, acceptance stays the trust boundary, and the
Canonical Knowledge Model stays mechanically reproducible.

Second time an issue's own suggested reading was adopted, after `ISSUE-0045`.

Newly open: how an artifact **declares** the Principles it establishes
(`ISSUE-0072`), since extraction is mechanical only where declaration exists.
