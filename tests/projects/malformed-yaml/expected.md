---
id: TEST-malformed-yaml
exercises: ADR-0078 — structural errors are reported at Parsing, never at Resolution
outcome: fail
expected-phase: parsing
expected-errors:
  - "must be list, got str"
---
**A negative fixture, and the one that proves the phase boundary.**
`relationships` is a string. Under the old regex parser this was silently an
empty list and the file compiled to a node with no edges — a structural defect
reinterpreted as a valid model.
