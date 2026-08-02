# Evidence model

Use structured records for assertions, sources, conflicts, and coverage.

## Assertion statuses

- confirmed
- implemented
- specified
- tested
- observed
- externally-defined
- inferred
- proposed
- unknown
- conflicting
- deprecated
- generated

## Confidence values

- high
- medium
- low

## Minimum evidence record

```yaml
id: evidence-0001
subject: example:Concept
assertion: "Natural-language assertion"
status: confirmed
confidence: high
scope: example-context
evidence:
  - type: source
    path: src/example.py
    symbol: Example
    lines: "10-42"
  - type: test
    path: tests/test_example.py
    symbol: test_example_invariant
external_sources: []
conflicts: []
notes: ""
```
