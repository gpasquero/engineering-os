---
id: ADR-0056
title: Three levels of engineering knowledge — Principle, Policy, Process
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0029, ADR-0030, ADR-0046, ADR-0054, ADR-0055, ISSUE-0069, ISSUE-0070]
---

# ADR-0056 — Principle, Policy, Process

**This is one of the central organizing concepts of the Engineering OS
metamodel.** It explains why ADRs, Policies and Gates all exist without
overlapping responsibilities.

## Context

`ADR-0029` separated ADRs from Policies: ADRs explain *why*, policies define the
rule. `ADR-0054` then introduced Gates as review processes, and `ADR-0055` moved
evaluation questions into them.

Three kinds of normative content now existed — decisions, rules, procedures —
with no statement of how they relate. `ADR-0046` had also recorded that three
ADRs applying one naming discipline meant the discipline was a rule that
belonged somewhere other than an ADR.

## Decision

Engineering OS distinguishes **three levels of engineering knowledge**.

### 1. Principles — stable architectural truths

Registry Pattern · `Definition → Instance → Assignment` · Semantic versus
Compilation Architecture

### 2. Policies — normative engineering rules derived from those principles

Naming Policy · Dimension Review Policy · Acceptance Policy

### 3. Processes — operational procedures implementing those policies

Dimension Review · Acceptance Review · Metamodel Position Gate

### The hierarchy

```text
Principle
    ↓
Policy
    ↓
Process
    ↓
Artifact
```

## Alternatives considered

**Two levels — policies and processes — with principles left in ADRs.**
Rejected: a principle stated only in an ADR is history, and `ADR-0029`
established that the ADR corpus is not the operational specification. The
Registry Pattern is not a decision anyone should have to reconstruct from a
supersession chain.

**Treat gates as policies.** Rejected: a policy states what must hold; a gate is
the procedure that checks it. `ADR-0054` already separated Gate from the rules
it executes, and this makes that separation general.

**One flat body of normative content.** Rejected — it is the current state, and
it is why the same naming discipline was decided three times in three separate
ADRs.

## Consequences

### Positive

- **It explains the artifact types the project already has.** ADRs record how a
  level's content came to be; Policies hold rules; Gates are processes. Three
  things that had accumulated independently now have distinct responsibilities.
- The overdue naming-discipline policy (`ADR-0046`) gets a level to live at, and
  so does every rule extracted from a repeatedly-applied ADR.
- Derivation is directional: a policy cites the principle it derives from, a
  process cites the policy it implements. That makes the corpus traversable
  rather than merely indexed.
- It complements `ADR-0055`: questions belong to Gates because Gates are
  processes, and processes implement policies rather than restating them.

### Negative

- **"Level" is used again for a different scheme.** `ADR-0046` established
  Abstraction Level as a qualified name precisely so that "level" would not be
  ambiguous. This is a second scheme, unqualified. `ISSUE-0069`.
- **"Process" is used again.** `ADR-0033` recorded *Workflow executes Process* as
  descriptive prose, not a declared type. Process is now a level. Whether a
  workflow's process is this Process is unstated. Also `ISSUE-0069`.
- **Whether Principles are a first-class artifact type is unstated**, and it
  matters: three of the examples are currently `Active` ADRs. If Principles
  become artifacts, the relationship to the ADRs recording them needs defining.
  `ISSUE-0070`.
- A fourth stage — `Artifact` — appears in the hierarchy without being one of
  the three levels. It is the thing produced, not a level of knowledge, and the
  diagram does not say so.

### Neutral

- No existing artifact changes. The hierarchy names relationships that already
  hold.

## Compliance

Every normative rule states the principle it derives from. Every process states
the policy it implements. No principle is stated only in an ADR once its policy
exists.
