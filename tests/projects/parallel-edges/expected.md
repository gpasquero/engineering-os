---
id: TEST-parallel-edges
exercises: ADR-0088 §3 — two different predicates between the same pair of nodes
outcome: pass
expected-nodes: 4
expected-edges: 5
expected-queries:
  Q-rationale:
    subject: Invariant.Both
    rows: [ADR.Twice]
  Q-status:
    subject: Concept.Target
    rows: []
---
**`ADR.Twice` both `establishes` and `supersedes`-relates to the same invariant**,
and `Artifact.Impl` both `validates` and `references` the same concept.

The previous `with` implementation matched one edge and then **looked up an
arbitrary edge between the same two nodes** to report it. With parallel edges
that could select the wrong one and evaluate it against the specification.

`Q-rationale` uses `with` to report `superseded-by`. If the engine confused
`establishes` with the parallel edge, this fixture would report the wrong
predicate — or a superseded-by that does not exist.
