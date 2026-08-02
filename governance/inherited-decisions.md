---
id: INHERITED-DECISIONS
title: Inherited Decisions
status: accepted
created: 2026-08-02
updated: 2026-08-02
source: sources/handoff/DECISIONS.md (pre-M1)
related: [ISSUE-0027]
---

# Inherited Decisions

The pre-M1 `sources/handoff/DECISIONS.md` recorded ten decisions as bare bullet points, with no
context, alternatives or consequences. They are treated as **accepted but
undocumented**: binding, but not yet defensible.

Each must be converted into a proper ADR before the milestone that depends on
it. Tracked as `ISSUE-0027`.

| # | Decision | Owed to | Converted |
|---|---|---|---|
| 1 | Repository-first approach | M1 | `ADR-0001` |
| 2 | Incremental deliveries | M1 | `ADR-0002` (documentation system) |
| 3 | Shared policies instead of duplicated prompt text | M3 | Pending |
| 4 | Small composable skills | M2 | Pending |
| 5 | Workflows orchestrate skills | M8 | Pending |
| 6 | OWL models semantics | M3 | Pending |
| 7 | SHACL validates graph instances | M3 | Pending |
| 8 | Engineering specifications capture behavior | M3 | Pending |
| 9 | Mandatory impact analysis | M5 | Pending |
| 10 | Knowledge update is part of Done | M3 | Pending, blocked by `ISSUE-0010` |

## Why these are not simply adopted

An undocumented decision cannot be evaluated, and will be re-litigated by every
future session that encounters a reason to doubt it. Decisions 6 and 7 in
particular commit the project to a specific semantic technology stack without
recording what alternatives were considered — a commitment large enough to
deserve an explicit rationale.

Until converted, these decisions hold. They are not open questions. They are
answers whose reasoning was not preserved.
