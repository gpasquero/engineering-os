---
id: ACCEPT-NNNN
artifact: path/or/identifier
artifact-revision: <commit sha, version or content hash>
reviewer: <name or handle — never the author>
acceptance-date: YYYY-MM-DD
decision: accepted | rejected | accepted-with-exceptions
related-adrs: []
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-NNNN — Title

## Artifact

What is being accepted, and at which revision. Be precise: acceptance applies to
a revision, not to an artifact in perpetuity.

## Decision

`accepted`, `rejected` or `accepted-with-exceptions`.

## Rationale

Why the reviewer accepted. Not a restatement of what the artifact says — the
grounds on which it was judged adequate.

## Condition 1 — reviewer approval

Who approved, and how the approval was given. The reviewer must not be the
author (`ADR-0023`).

## Condition 2 — traceability

The motivating issue, ADR or requirement this revision answers.

## Condition 3 — validation summary

Which deterministic validations were applicable, and their results. Where no
validator exists for this artifact type, state that none were applicable — that
satisfies the condition (`ADR-0021`).

## Exceptions

Anything accepted despite not meeting a normal expectation. Each exception must
say what it covers and, where relevant, when it expires. Empty is the normal
case.

## Notes

Anything a future reader needs in order to judge how much this acceptance is
worth.
