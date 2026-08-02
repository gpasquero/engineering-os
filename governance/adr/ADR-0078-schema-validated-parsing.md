---
id: ADR-0078
title: Authoring sources are parsed with a real parser and schema-validated before semantic resolution
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0017, ADR-0045, ADR-0073, ADR-0077]
---

# ADR-0078 — Schema-validated parsing

## Context

The parser reads front matter with regular expressions. It works on well-formed
input and has no notion of malformed input: a mistyped key is silently absent, a
list that is not a list is silently empty.

**Parser complexity leaks into compiler logic** when this is not fixed early.
Every downstream phase starts defending against shapes the parser should have
rejected.

## Decision

Three changes, in order, **before the authoring language is expanded**:

1. **Parse front matter with a real YAML parser.** No regular expressions over
   structure.
2. **Introduce schemas for authoritative artifacts.** A schema declares required
   keys, types and permitted values.
3. **Validate against the schema before semantic resolution.** Structural
   validity is a precondition of the Resolution phase, not a concern within it.

### Two kinds of error, kept apart

| Phase | Answers | Example |
|---|---|---|
| **Parsing** | is this a well-formed artifact? | `relationships` is a string, not a list |
| **Resolution** | is what it asserts true of the model? | `scoped-to` points at a node that does not exist |

**Reporting a structural error as a semantic one is a diagnostic failure**, and
`ADR-0073` already requires each phase to declare its invariants. This gives the
Parsing phase invariants worth declaring.

### On the dependency

Using a YAML library does not commit Engineering OS to Python or to YAML.
`ADR-0017` holds: this is a **reference architecture, not a reference
implementation**, and `ISSUE-0036` leaves the implementation language open.
`tools/` and `compiler/` are cross-cutting infrastructure at Semantic Layer
`None` (`ADR-0039`).

What the decision does commit to is that **front matter is a serialization**
(`ADR-0045`) with a declared grammar, rather than whatever the regexes happen to
accept.

## Alternatives considered

**Keep regex parsing and add validation after it.** Rejected: it validates the
parser's interpretation rather than the file. A key the regex never looked for
cannot be reported missing.

**Write a hand-rolled YAML subset parser** to avoid the dependency. Rejected —
that is how a compiler acquires a second, worse YAML implementation.

**Move to a purpose-built authoring syntax.** Rejected as far too early. The
authoring form must stay readable without tooling (`ADR-0017`), and Markdown with
YAML front matter already satisfies that.

## Consequences

### Positive

- **Malformed input is rejected with a diagnostic naming the file, key and
  problem**, instead of being silently reinterpreted.
- Schemas are declarative and become authoritative artifacts in their own right,
  reviewable without reading the parser.
- It removes a whole class of defect from the Resolution phase before that phase
  grows.

### Negative

- **A third-party dependency enters the reference implementation.** It is
  bounded to Parsing and stated here so the boundary is visible.
- Schemas must be maintained alongside the entity specifications, and **nothing
  yet checks that a schema agrees with the specification it encodes.** That is a
  new hand-maintained projection — the exact debt `ISSUE-0037` records, created
  in the same session that reclassified it as an architectural violation.

### Neutral

- No authoring source changes. Existing files must already satisfy the schemas.

## Compliance

`compiler/parser/` uses a YAML parser and validates against
`compiler/parser/schemas/` before returning. Structural errors are reported at
the Parsing phase and never reach Resolution.
