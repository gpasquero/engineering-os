---
id: TEST-query-schema
title: Invalid query declarations must fail
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0088]
---

# Invalid query declarations must fail

`ADR-0088` §4: **an unknown field fails. It is never silently ignored.**

`tools/check-query-schema.py` feeds each declaration below to the validator and
requires the expected message. A declaration that starts passing is a regression
in the schema, not a fix.

```yaml
cases:
  - name: unknown field
    expect: "unknown field 'depth'"
    query: {id: Q-x, question: q, subject: none, rationale: r, depth: 3,
            steps: [{select: {all: true}}]}

  - name: unknown operator
    expect: "unknown operator 'wander'"
    query: {id: Q-x, question: q, subject: none, rationale: r,
            steps: [{wander: {}}]}

  - name: two operators in one step
    expect: "exactly one operator per step"
    query: {id: Q-x, question: q, subject: none, rationale: r,
            steps: [{select: {all: true}, keep: {type: Concept}}]}

  - name: bad direction
    expect: "must be one of ['in', 'out', 'both']"
    query: {id: Q-x, question: q, subject: none, rationale: r,
            steps: [{traverse: {direction: sideways}}]}

  - name: non-positive hop limit
    expect: "must be a positive integer"
    query: {id: Q-x, question: q, subject: none, rationale: r,
            steps: [{traverse: {max-hops: 0}}]}

  - name: unknown node type
    expect: "is not a declared metamodel entity"
    query: {id: Q-x, question: q, subject: none, rationale: r,
            steps: [{select: {type: Wombat}}]}

  - name: unknown predicate
    expect: "is not a registered predicate"
    query: {id: Q-x, question: q, subject: none, rationale: r,
            steps: [{traverse: {predicate: wibbles-at}}]}

  - name: bad output mode
    expect: "must be one of ['nodes', 'edges', 'induced-subgraph']"
    query: {id: Q-x, question: q, subject: none, rationale: r, output: pictures,
            steps: [{select: {all: true}}]}

  - name: missing required field
    expect: "missing required field 'rationale'"
    query: {id: Q-x, question: q, subject: none, steps: [{select: {all: true}}]}

  - name: select with two selectors
    expect: "exactly one of ['all', 'subject', 'id', 'type'] required"
    query: {id: Q-x, question: q, subject: none, rationale: r,
            steps: [{select: {all: true, type: Concept}}]}

  - name: unknown field inside an edge spec
    expect: "unknown field 'colour'"
    query: {id: Q-x, question: q, subject: none, rationale: r,
            steps: [{keep: {has-edge: {colour: blue}}}]}

  - name: applies-to naming an unknown type
    expect: "is not a declared metamodel entity"
    query: {id: Q-x, question: q, subject: required, rationale: r,
            applies-to: [Wombat], steps: [{select: {subject: true}}]}
```
