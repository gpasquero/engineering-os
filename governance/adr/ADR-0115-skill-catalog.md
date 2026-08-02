---
id: ADR-0115
title: Discovery Skills are a composable catalog; domain skills are knowledge packages
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0019, ADR-0031, ADR-0037, ADR-0108, ADR-0110, ADR-0113]
---

# ADR-0115 — The Skill catalog

## Context

Nine Discovery Skills exist as a flat list. The direction is to treat them as
**one of the primary strategic assets** of Engineering OS, organised as a
**reusable, composable catalog** — and to distinguish two kinds.

## Decision

### Skills compose into a pipeline

```text
Repository Survey + Technology + Architecture + Domain + Capability
  + Invariant + Decision + Gap
        ↓
Candidate Engineering Model
```

Composition is declared: a skill states which skills' output it may consume.
**Today only `DS-gap-discovery` and `DS-candidate-synthesis` consume other
skills' output**, which is what makes the rest independently runnable
(`ADR-0113`) — and composition must not erode that.

> **The implementation model remains replaceable. The Discovery Skills do not.**

### General and Domain skills

| | Knows about | Example |
|---|---|---|
| **General** | software, in any domain | Repository Survey, Architecture Discovery |
| **Domain** | a domain's engineering knowledge | Banking, ERP, Healthcare, Kubernetes, GeneXus, PostgreSQL, E-commerce |

> **These are not parser plugins. They are engineering knowledge packages.**

A domain skill knows what a domain's systems usually contain, what its
invariants usually are, and what its absences usually mean. **A banking skill
knows to ask about idempotency, settlement windows and audit retention** — and
that not finding them is a finding.

### Domain skills enrich without changing the metamodel

**This is the constraint that makes them safe.** A domain skill proposes
`Concept`, `Capability` and `Invariant` like any other — the metamodel is
unchanged, and the domain lives in **what is asked and what is recognised**, not
in new entity types.

The metamodel has been unchanged for twelve milestones. **A domain skill that
required an entity would be evidence the domain does not fit**, and would be a
question before it was an entity (`ADR-0085`).

### A domain skill is close to a Knowledge Package

`ADR-0019` defines a Knowledge Package as a published interface between
repositories. A domain skill is a **published interface between domains** — and
the relationship is worth naming now so it is not discovered later.

They are not merged here: a Knowledge Package exports *knowledge about a
system*; a domain skill exports *how to investigate a kind of system*.

## Alternatives considered

**Domain skills as parser plugins.** Rejected explicitly. A parser plugin
extracts syntax; a domain skill carries engineering judgement about what a
domain's systems mean.

**Domain-specific metamodel extensions.** Rejected. It would fork Layer A per
domain, and `ADR-0037` says adopters instantiate the metamodel rather than
modify it.

**One skill per domain, monolithic.** Rejected for the same reason `ADR-0113`
rejected one onboarding prompt: untestable in parts, unattributable in failure.

## Consequences

### Positive

- **The catalog becomes the asset rather than any model that runs it.**
- Domain knowledge accumulates **without touching the metamodel or the
  compiler**, which is the only way it can accumulate safely.
- A domain skill is a plausible commercial unit — the strongest long-term
  differentiator named so far.

### Negative

- **No domain skill exists.** The category is declared and empty, and a category
  with no members is a hypothesis.
- **Composition is declared and untested.** Nine skills have run in one order,
  once; whether a different composition produces a coherent candidate model is
  unknown.
- **Domain skills carry the strongest bias risk in the system.** A skill that
  knows what banking systems *usually* contain will propose what it expects, and
  `ADR-0110`'s curation is the only thing between that and the model.

### Neutral

- No metamodel change. Skills gain a `kind` and a `composes-with` field.

## Compliance

`discovery/skills/skills.yaml` declares each skill's `kind` — `general` or
`domain` — and what it composes with. **A domain skill proposes only existing
metamodel types.**
