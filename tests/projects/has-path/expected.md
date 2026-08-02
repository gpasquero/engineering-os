---
id: TEST-has-path
exercises: keep/reject has-path — filter a row on a property several hops away
outcome: pass
expected-nodes: 4
expected-edges: 3
expected-queries:
  Q-stale-implementation:
    rows: [Artifact.Stale]
    status: ok
  Q-obsolete-decisions:
    rows: [ADR.Old]
    status: ok
---
`has-edge` is single-hop, and the query pipeline cannot return to an earlier
stage. **A row cannot be filtered on a property two hops away while still being
returned** — which is exactly what *which implementation artifacts no longer
match their original design rationale?* requires.

`has-path` takes an ordered sequence of edge specs and keeps rows from which such
a path exists.

The fixture is domain-neutral: `Artifact.Stale` represents a `Concept` whose
establishing `ADR` has been superseded.
