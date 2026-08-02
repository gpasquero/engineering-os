---
id: MODEL-ENGINEERING-INTENTS
title: Engineering Intents
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0091, ADR-0095, ADR-0096]
---

# Engineering Intents

**Why the developer entered the system** — the first stage of the engineering
loop (`ADR-0095`).

> **Not part of the software knowledge. Part of an engineering session**
> (`ADR-0096`). An intent belongs to a session; a Layer A entity's instances
> belong to a model.

An intent **selects** plans and recommendations. It does not describe software,
and it is not itself a recommendation.

```yaml
engineering-intents:
  - id: I-modify-behavior
    label: Modify behaviour
    asks: What am I changing, and what depends on it?
    selects-plans: [P-change-implementation, P-change-concept, P-change-capability]
    selects-recommendations: [R-change-implementation, R-change-concept]

  - id: I-onboard
    label: Onboard a repository
    asks: What engineering knowledge does this repository contain?
    selects-plans: [P-discover]
    selects-recommendations: [R-discover]

  - id: I-investigate
    label: Investigate a bug
    asks: What is this supposed to do, and what says so?
    selects-plans: []
    selects-recommendations: [R-change-implementation]

  - id: I-audit
    label: Audit the knowledge
    asks: What does this model claim that it cannot support?
    selects-plans: []
    selects-recommendations: [R-audit-model]
```

## Not yet declared

`Add Feature`, `Refactor`, `Migrate`, `Improve Performance`, `Improve Security`,
`Remove Capability`.

**Each is a real intent and none has a plan to select.** Declaring them now would
produce entries that resolve to nothing, which is worse than their absence:
`ADR-0091` forbids a recommendation from filling a gap with advice, and the same
applies here.

They are added when a plan exists for them.

## Debt

**`I-investigate` selects no plan.** Investigating a bug is a real intent with no
planning support, and the registry makes that visible rather than hiding it.

**Intents cannot relate to one another** (`ADR-0096`). *Migrate specialises
Refactor* is inexpressible in a vocabulary, and is the first thing that would
force promotion to an entity.

**Selection is a declared list, not a derivation.** Nothing checks that
`I-modify-behavior` selects every plan that could serve it; adding a plan does
not update the intents that should offer it.
