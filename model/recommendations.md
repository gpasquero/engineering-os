---
id: MODEL-RECOMMENDATIONS
title: Engineering Recommendations
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
artifact-kind: authoritative
established-by: [ADR-0086, ADR-0089, ADR-0091]
---

# Engineering Recommendations

**Questions produce knowledge. Recommendations produce engineering guidance.**

> Every item in a recommendation traces to a declared query and a path in the
> model. **Nothing is asserted that a query did not find** (`ADR-0091`).

A recommendation is composed entirely of semantic queries. The engine holds no
recommendation logic; adding a recommendation is a data change.

## Consumers

The semantic layer recommends **engineering actions**. Execution engines consume
them — a developer doing the work, an AI agent running a workflow, a CI pipeline
gating a change. **Engineering OS stays independent of any particular runtime.**

## Actions

A closed vocabulary. Each names what a consumer should *do* with the rows a query
returns.

| Action | Means |
|---|---|
| `review` | read these before deciding |
| `inspect` | look at these; they may need to change |
| `validate` | check that these still hold |
| `update` | these will be wrong unless changed |
| `verify` | confirm these still pass |
| `investigate` | these are unexplained and may be a problem |

## The recommendations

```yaml
recommendations:
  - id: R-change-concept
    intent: I want to change this Concept
    applies-to: [Concept]
    rationale: >
      Changing a concept changes the meaning everything downstream was built
      against. The decisions come first because they are the only step that can
      tell you not to.
    steps:
      - action: review
        query: Q-rationale
        because: the decision that established this, and whether it still stands
      - action: validate
        query: Q-constraints
        because: guarantees that must survive the change
      - action: verify
        query: Q-tests
        because: tests that protect the current behaviour
      - action: update
        query: Q-specifications
        because: specifications that will become inconsistent
      - action: inspect
        query: Q-impact
        because: everything reachable from this, directly or transitively

  - id: R-change-implementation
    intent: I want to change this implementation
    applies-to: [Artifact]
    rationale: >
      An implementation is constrained by things stated elsewhere by someone
      else. An engineer changing code rarely reads them, which is the gap this
      recommendation exists to close.
    steps:
      - action: review
        query: Q-assumptions
        because: invariants constraining what this represents
      - action: verify
        query: Q-tests
        because: tests that validate this artifact
      - action: inspect
        query: Q-impact
        because: what depends on this
      - action: investigate
        query: Q-evidence
        because: the sources this artifact's claims rest on

  - id: R-discover
    intent: I want to build an engineering model of this repository
    applies-to: [Artifact]
    rationale: >
      Discovery is an engineering process, not a parser (ADR-0105). Structure is
      derived first because it is mechanical and constrains what interpretation
      is plausible; gaps are identified last because they are defined by what the
      earlier steps did not produce.
    steps:
      - action: extract
        query: Q-provenance
        because: the repository and what is already known about it
      - action: interpret
        query: Q-evidence
        because: sources from which engineering knowledge may be proposed
      - action: identify-gaps
        query: Q-unsupported
        because: assertions the candidate model would carry without support

  - id: R-audit-model
    intent: I want to know what this model cannot support
    applies-to: []
    rationale: >
      Runs the model's own honesty checks. Every step should ideally return
      nothing; a non-empty result is a gap in the knowledge base rather than in
      the system it describes.
    steps:
      - action: investigate
        query: Q-unsupported
        because: invariants asserted with no evidence at all
      - action: investigate
        query: Q-unenforced
        because: invariants nothing is recorded as enforcing
      - action: investigate
        query: Q-unaccepted
        because: revisions no acceptance record reaches
      - action: investigate
        query: Q-stale-implementation
        because: artifacts implementing a rationale that no longer stands
      - action: investigate
        query: Q-obsolete-decisions
        because: superseded decisions still reflected in what is built
```

## What a recommendation may not do

- **It may not add knowledge.** A step whose query returns nothing reports
  nothing. A recommendation never fills a gap with advice.
- **It may not rank by confidence** (`ADR-0090`).
- **It may not contain domain logic.** A recommendation *about* Kubernetes is one
  whose subject is Kubernetes, composed of domain-neutral queries.

## Debt

**Step order is a judgement encoded as data with nothing to check it.**
Declaring *review decisions before inspecting tests* asserts an engineering
practice that no evidence in this repository supports.

**A recommendation inherits the bluntness of its queries.** `Q-tests` names a
file rather than a test in the Kubernetes model, and `R-change-implementation`
will present that with more authority than the query deserves.

**`R-audit-model` has an empty `applies-to`**, meaning it takes no subject. That
overloads the field: *applies to nothing* and *applies to everything* are written
the same way.
