---
id: ADR-0052
title: The semantic hierarchy and the compilation hierarchy are orthogonal pipelines
status: accepted
date: 2026-08-02
supersedes: ADR-0050
superseded-by: null
resolves: [ISSUE-0066]
related: [ADR-0032, ADR-0037, ADR-0047, ADR-0053]
---

# ADR-0052 — Two orthogonal hierarchies

## Context

`ADR-0050` established a four-stage modeling hierarchy:
`Definition → Instance → Assignment → Projection`.

`ISSUE-0066` recorded that it did not accommodate `ADR-0032`'s Registry
Specification, and that the same Registry Projection appeared in two different
pairings — once with the Registry Specification and once as the fourth stage of
the hierarchy. Both could not be complete.

The issue asked where the Registry Specification sits. The answer is that the
hierarchy was mixing two concerns.

## Decision

**`ADR-0050`'s hierarchy is incomplete because it mixes two different
concerns.**

`Definition → Instance → Assignment` belongs to the **semantic model**.
**Projection belongs to the compilation model.**

Therefore **Projection is not part of the semantic hierarchy**. There are two
orthogonal pipelines.

### Semantic hierarchy

```text
Definition
    ↓
Instance
    ↓
Assignment
```

### Compilation hierarchy

```text
Authoritative Semantic Model
    ↓
Canonical Knowledge Model
    ↓
Projection
```

**Registry Projections, the Knowledge Explorer, documentation, search indexes
and similar outputs are compilation products, not semantic concepts.**

> This separation keeps the metamodel independent from compiler architecture.

## What survives from ADR-0050

The first three stages, and the examples that used them:

| Definition | Instance | Assignment |
|---|---|---|
| Dimension Specification | Dimension | Dimension Assignment |
| State Machine Specification | State Machine | State Assignment |
| Policy Specification | Policy | *Policy Assignment (future)* |

Also the rule that future extensible concepts are evaluated against the
hierarchy before new modeling structures are introduced, and the pre-commitment
on `Policy Assignment`.

**What changes** is the fourth stage. Registry Projections move to the
compilation hierarchy, where they belong alongside every other compiler output.

## Alternatives considered

The four options recorded in `ISSUE-0066`:

**The Registry Specification is orthogonal to the hierarchy.** Closest to
correct, and incomplete — it identified *an* orthogonality without seeing that
the hierarchy itself contained the mixture.

**A fifth stage.** Rejected: it would have made the semantic hierarchy carry a
compilation concept explicitly rather than accidentally.

**The Registry Specification is the Definition stage.** Rejected: it contradicts
`ADR-0048`, and a registry is a container of definitions, not one.

**Per-concept hierarchies with the registry above them.** Subsumed. Once
Projection leaves, the registry question becomes a compilation question.

## Consequences

### Positive

- **The metamodel stops depending on compiler architecture.** A change to how
  projections are produced no longer touches the semantic hierarchy, which is the
  independence `ADR-0053` generalizes.
- `ISSUE-0066`'s double-pairing disappears: Registry Projection appears once, in
  the compilation pipeline, alongside the Explorer and documentation.
- The compilation hierarchy restates `ADR-0037`'s Layers B → C → D and
  `ADR-0047`'s three representations in one pipeline, so three descriptions of
  the same flow now agree.
- Three stages is easier to hold than four, and each stage is now the same kind
  of thing.

### Negative

- **`ADR-0050` is superseded one session after acceptance.** `ACCEPT-0013`
  accepted it while `ISSUE-0066` was already recorded against it — the shortest
  acceptance-to-supersession interval in the project.
- **"Authoritative Semantic Model" is a new term for something already named.**
  It denotes what `ADR-0037` calls Layers A and B and `ADR-0047` calls the
  Authoring Representation. Three names for one thing is the pattern that has
  bitten this project six times; the metamodel work must reconcile them.
- Two pipelines to keep straight, where readers had just learned one.

### Neutral

- No artifact changes location or kind. Only which pipeline describes it.

## Compliance

No semantic concept includes a projection stage. No compilation product appears
in the semantic hierarchy. The metamodel defines the semantic hierarchy without
reference to compiler outputs.
