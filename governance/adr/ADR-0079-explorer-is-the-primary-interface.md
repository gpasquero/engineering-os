---
id: ADR-0079
title: The Knowledge Explorer is the primary interface to the Canonical Knowledge Model
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0047, ADR-0052, ADR-0059, ADR-0072]
---

# ADR-0079 — The Explorer is the primary interface

## Context

The Explorer began as a visualization of generated files. It has become useful
enough to answer questions that no other artifact in the repository can.

## Decision

**The Knowledge Explorer is the primary interface to the Canonical Knowledge
Model**, not a visualization of generated output.

It progressively exposes **semantic navigation**:

| Question | Requires |
|---|---|
| *Why does this relationship exist?* | the predicate's core type, category and definition |
| *Show provenance* | which source, at which revision, asserted this |
| *Show everything derived from this concept* | transitive closure over derivation |
| *Show impact if this node changes* | transitive closure over incoming edges |
| *Show acceptance history* | the acceptance chain reaching this node |

**It remains a projection** (`ADR-0072`). Being the primary interface does not
make it authoritative — it makes it the projection most worth investing in.

### Why this matters beyond convenience

`ADR-0059` commits Engineering OS to **maximizing discovered knowledge**. A
graph nobody can traverse discovers nothing. Impact and provenance queries are
where the Canonical Knowledge Model stops being a file and starts answering
questions the repository could not answer before.

## Alternatives considered

**Keep the Explorer as inspection output.** Rejected: it makes the model's value
depend on someone reading JSON.

**Build a query language or an API first.** Rejected as premature. The questions
above are known and enumerable; a query language is the generalisation of
answers nobody has implemented yet.

**Make the Explorer authoritative.** Rejected — it would invert `ADR-0072`. A
projection that becomes a source of truth is precisely the failure
`ISSUE-0037` records five times over.

## Consequences

### Positive

- Impact and provenance are **derived rather than remembered**, which is what a
  reconstruction methodology is for.
- Each query is a concrete, testable requirement on the model. *Show provenance*
  requires provenance to be **in** the model, and it currently is not.

### Negative

- **Every query is a demand on the Canonical Knowledge Model.** Provenance and
  acceptance history are not represented today, so the Explorer will expose gaps
  before it exposes answers — which is useful and will read as unfinished.
- A self-contained HTML page has limits. Transitive closure over a large graph in
  the browser will not scale, and the point at which it stops is unknown.

### Neutral

- The Explorer remains generated and self-contained (`ADR-0017`).

## Compliance

`compiler/emitters/explorer/` implements semantic navigation. Each query is
tested by a fixture in the regression suite. The Explorer never becomes a source
of truth.
