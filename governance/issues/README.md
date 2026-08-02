---
id: ISSUE-README
title: Issues
status: current
created: 2026-08-02
updated: 2026-08-02
related: [ADR-0003]
---

# Issues

An issue records something the repository does not know.

The governing rule: **if information is missing, create an issue — do not
assume.** An open issue is a standing instruction to a future session not to
quietly decide the question.

See `index.md` for the current list. Use `_template.md` for new issues.

**Highest allocated ID: `ISSUE-0028`.** IDs are sequential and never reused,
including for closed issues.

## Type

| Type | Meaning |
|---|---|
| `question` | An unknown that requires a decision by the project owner |
| `inconsistency` | Two or more sources disagree |
| `gap` | Something required is absent |
| `risk` | A known hazard that has not yet caused harm |

## Severity

| Severity | Meaning |
|---|---|
| `blocking` | The milestone named in `blocks` **cannot start** until this is resolved |
| `high` | Must be resolved **within** the milestone named in `blocks` |
| `medium` | Should be resolved in the named milestone; work can proceed around it |
| `low` | Cosmetic or deferrable |

## Status

| Status | Meaning |
|---|---|
| `open` | Unresolved. Do not assume an answer. |
| `resolved` | Answered; `resolved-by` names the ADR or document that answers it |
| `deferred` | Deliberately postponed; must name the milestone it defers to |
| `closed` | No longer relevant; must state why |

## Rules

- Files are never moved between directories on status change. Status lives in
  front matter, because moving a file breaks every inbound link.
- IDs are never renumbered.
- When an ADR resolves an issue, set `resolved-by` here **and** list the issue
  in the ADR's `resolves`. A one-sided link is a defect.
- `evidence` cites the file paths that establish the issue. For inconsistencies,
  cite every conflicting source.
- Never resolve an issue by editing a file in `imports/` or `sources/`. Those
  are frozen — see `ADR-0005`.
