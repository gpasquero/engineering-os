---
id: ACCEPT-0031
artifact: SESSION-0035 — the Task Graph
artifact-revision: d4954ebdb773ed2d4bcf8e82d4249c7c86d33925
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0095, ADR-0096, ADR-0097]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0031 — The Task Graph

## Artifact

The work of `SESSION-0035`, at revision
**`d4954ebdb773ed2d4bcf8e82d4249c7c86d33925`**.

Scope:

- Task Graph generation
- The capability-based execution model
- The `EngineeringIntent` registry
- The runtime execution graph

### Scope boundary

This record covers revision `d4954eb` and nothing after it.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- This session **successfully separates engineering reasoning from engineering
  execution.**
- **The deterministic architecture remains intact.**
- The direction is correct.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

| Item | Decision |
|---|---|
| Task Graph, capability model, runtime graph | `ADR-0097` |
| `EngineeringIntent` registry | `ADR-0096`, accepting the proposal as recommended |
| The loop the graph sits inside | `ADR-0095` |

## Condition 3 — validation summary

236 records verified across the standard governance checks. 17 fixtures, 9
negative, golden outputs, deterministic rebuild. Eleven registries. Task graph
output verified byte-identical across runs. The metamodel unchanged for a fourth
milestone.

## Exceptions

None.

## Notes

**The project is redirected again: from planning to orchestration.**

`ADR-0098` gives the Engineering Director the loop; `ADR-0099` makes workers
capabilities rather than vendors and assignment a deterministic match;
`ADR-0100` separates governance from work; `ADR-0101` establishes the two-way
contract — an Execution Context out, Execution Observations back, and **workers
never touching the model.**
