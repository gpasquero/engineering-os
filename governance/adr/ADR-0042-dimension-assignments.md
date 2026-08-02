---
id: ADR-0042
title: Artifacts are classified by Dimension Assignments, not by embedded values
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0058]
related: [ADR-0017, ADR-0036, ADR-0040, ADR-0041, ADR-0043, ISSUE-0060]
---

# ADR-0042 — Dimension Assignments

## Context

`ADR-0039` disallowed path inference as an architectural basis for
classification, and `ADR-0040` established that artifacts are classified along
multiple dimensions. `ISSUE-0058` asked how an artifact's classification reaches
the compiler, and offered four options: front matter per artifact, declaration
per artifact type, both split by variance, or a separate classification manifest.

All four treat classification as a **property of the artifact**. That framing is
the defect.

## Decision

> **Artifacts do not "contain" dimension values. Artifacts are classified by
> Dimension Assignments.**

**Dimension Assignments are explicit semantic relationships.**

```text
Artifact
   ↓
Dimension Assignment
   ↓
Dimension
   ↓
Dimension Value
```

### Why the distinction matters

- **Assignments are versioned.**
- **Assignments may change without changing the artifact identity.**
- **Dimensions evolve independently.**
- **Validation applies to assignments, not to artifacts themselves.**

### Representation

**The Canonical Knowledge Model represents dimensions as graph relationships
rather than embedded metadata.**

This aligns naturally with the future ontology and knowledge graph.

## Alternatives considered

All four options recorded in `ISSUE-0058` are rejected for one shared reason:
each models classification as something an artifact *has*.

**Front matter on every artifact** — makes reclassification an edit to the
artifact, so its identity and its classification cannot vary independently.

**Declaration per artifact type** — cannot express per-artifact variation, and
still embeds the value in a type definition rather than relating the two.

**Both, split by variance** — the option `ISSUE-0058` judged most likely. It
would have required a rule for which dimension goes where, which is a
consequence of the wrong framing rather than a design decision.

**A separate classification manifest** — closest in shape, but a manifest of
values is still values, not relationships, and it separates the assignment from
both things it relates.

## Consequences

### Positive

- **Reclassifying an artifact does not touch the artifact.** Its identity, its
  revision history and its acceptance are unaffected by a change in how it is
  classified — which is what makes assignments versionable in their own right.
- **Validation has a precise target.** A constraint applies to an assignment,
  not to a file, so a violation names the relationship that is wrong.
- Dimensions and artifacts evolve on independent schedules, which is what
  `ADR-0041`'s registration model assumes.
- The canonical model becomes a graph of relationships rather than a document
  store with metadata — the natural form for `ADR-0036`'s conformance
  requirement and for the ontology work ahead.

### Negative

- **Where assignments are authored is unstated.** The decision fixes their
  *representation* in Layer C. If they exist only as graph relationships in a
  compiled artifact, then **a human reading an authoritative artifact cannot
  determine its classification without running the compiler** — which tensions
  directly with `ADR-0017`'s guarantee that authoritative artifacts remain
  usable without the toolchain. `ISSUE-0060`.
- Three entities where there was one: artifact, assignment, dimension. Every
  classification is now a relationship to author, validate and traverse.
- Assignments are versioned, so they need their own lifecycle and, under
  `ADR-0020`, potentially their own acceptance.

### Neutral

- This is the third time an issue's own candidate answers were all rejected in
  favour of reframing, after `ISSUE-0053` and `ISSUE-0056`. Each time the issue
  had converged on a plausible mechanism while the defect was in the framing.

## Compliance

No artifact embeds a dimension value as a property. Every classification is an
explicit Dimension Assignment relating an artifact to a dimension and a value.
The canonical model represents assignments as graph relationships. Validation
targets assignments.
