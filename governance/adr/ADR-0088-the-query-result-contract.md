---
id: ADR-0088
title: The query result contract — path provenance, applicability, limits and parity
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0044, ADR-0073, ADR-0077, ADR-0081, ADR-0084, ADR-0086, ADR-0087]
---

# ADR-0088 — The query result contract

## Context

`ADR-0086` made the query engine the semantic API. **It is now part of the
product contract**, and real-system findings are about to depend on it.

Seven defects were identified in its semantics. **Every one produces a plausible
answer that is wrong** — the worst failure mode a semantic API can have, because
nothing looks broken.

## Decision

### 1. A traversal result carries the whole path, not one predicate

The previous result recorded a single `via`: the first predicate on the path.
**For a multi-hop answer that reports the first edge as if it explained the whole
dependency.**

A row now carries the **complete ordered path** — every traversed edge, in order,
each with its direction and **the reason it matched the step's specification**.
Plus `hops` and `origin`.

> **Path provenance is never reduced to one predicate.**

`via` remains as a convenience and is defined as *the first predicate of the
recorded path*. The path is authoritative.

### 2. Edge output returns edges actually traversed

Previously `output: edges` returned the **induced subgraph** between all result
node identifiers — which includes relationships the query never followed, and
therefore explains an answer with edges that did not produce it.

`output: edges` now returns exactly the edges the traversal walked, deduplicated,
in traversal order.

**`output: induced-subgraph` is a separate, explicit mode.** It remains available
because it is genuinely useful, and it is never the default.

### 3. `with` evaluates the edge it is considering

The previous implementation matched an edge, then **looked up an arbitrary edge
between the same two nodes** to report it. Two nodes may have several predicates
between them, so it could evaluate the wrong parallel edge.

`with` now evaluates and reports the edge in hand, and returns `{id, predicate}`
rather than a bare identifier.

### 4. Query declarations are validated

A declarative schema checks operator names, permitted and required fields per
operator, direction values, positive hop limits, output modes, referenced node
and relationship types, and exactly one operator per step.

> **An unknown field fails. It is never silently ignored.**

### 5. Applicability is distinguished from emptiness

A query declares which subject types it supports. Every execution returns one of
four statuses:

| Status | Means |
|---|---|
| `ok` | valid query, results |
| `empty` | valid query, no results — **often the finding** |
| `not-applicable` | the query does not apply to this subject type |
| `invalid` | the declaration or the subject is malformed |

> **An empty result must never hide an applicability error.**

### 6. Determinism and limits are defined

| Concern | Rule |
|---|---|
| **cycles** | a node is visited once; the first path reaching it wins |
| **equal-length paths** | tie broken by the lexicographically smallest predicate sequence, then node sequence |
| **duplicates** | a node appears at most once per result |
| **ordering** | `(hops, id)` |
| **maximum depth** | 16 by default, per-query override |
| **maximum results** | 1000 by default, per-query override |
| **truncation** | emits a diagnostic — **never silent** |

**Unbounded traversal is not the default.** A real Kubernetes model is much
larger than a 28-node fixture.

### 7. Parity is a public invariant

The two engines are compared on **result nodes, result edges, full paths,
ordering, diagnostics and applicability status** — not only on final identifiers.

## Alternatives considered

**Fix only the defects that produce visibly wrong output.** Rejected. Defects 1,
2 and 3 all produce output that *looks* right, which is precisely why they must
be fixed before a real model is interpreted.

**Make traversal unbounded and add limits when a large model needs them.**
Rejected: the limit is cheap now and the first large model is the worst moment to
discover it is missing.

**Return `not-applicable` as an empty result with a warning.** Rejected — it is
the conflation the decision exists to remove. A caller that cannot distinguish
them will report *nothing depends on this* when the truth is *this question does
not apply here*.

**Compare engines on a canonical hash rather than field by field.** Rejected: a
hash reports that something differs, and the useful information is what.

## Consequences

### Positive

- **Answers become explainable.** A path is a chain of edges a reader can follow;
  a `via` is a claim.
- Malformed queries fail at load rather than returning plausible results.
- **The empty result becomes trustworthy**, which matters because several of the
  most valuable questions are ones whose answer *should* be empty.
- The limits make the Kubernetes milestone survivable.

### Negative

- **The result shape changes, and every consumer with it** — the CLI, the
  Explorer, the fixtures and the parity check. Golden outputs are rewritten in
  bulk, which is exactly the change a golden suite makes expensive and safe.
- **Paths are larger than the rows that carry them.** A 5-hop result now carries
  five edge records per row, and nothing yet prunes them.
- Two engines must now agree on far more, so parity is harder to hold.

### Neutral

- No question changes meaning. Eleven declared queries keep their semantics; what
  changes is what the answer contains and what the engine refuses.

## Compliance

`compiler/query/schema.yaml` declares the query grammar. `compiler/query/`
implements the result contract. `tools/check-engines.py` compares the full
result. A fixture exercises two different predicates between the same pair of
nodes.
