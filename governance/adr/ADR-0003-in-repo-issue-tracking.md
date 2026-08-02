---
id: ADR-0003
title: Open questions are tracked as in-repository Markdown issues
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0001, ADR-0002]
---

# ADR-0003 — Open questions are tracked as in-repository Markdown issues

## Context

The governing process rule is: *if information is missing from the repository,
create an issue instead of assuming*. That rule requires a place to put issues.

At the time of this decision the repository has no git remote and no commits, so
a hosted issue tracker is not merely a preference — it is unavailable.

More fundamentally, `ADR-0001` states that an agent given only the repository
must be able to reconstruct full context. Open questions are the single most
important part of that context, because they mark exactly where a future session
must not assume.

## Decision

Issues are Markdown files in `governance/issues/`, one per issue, named
`ISSUE-NNNN-slug.md`, with front matter declaring `type`, `status`, `severity`,
`blocks`, `evidence` and `resolved-by`.

- Status is flat, carried in front matter. Files are **not** moved between
  `open/` and `closed/` directories, because moving a file breaks every link to
  it.
- `governance/issues/index.md` provides the session-start overview.
- An issue with `severity: blocking` and a milestone in `blocks` prevents that
  milestone from starting.
- Resolution links to the ADR or document that answers the question.

## Alternatives considered

**GitHub Issues.** Rejected now: requires a remote that does not exist, and it
moves the most context-critical knowledge out of the artifact an agent is given.
Can be added later as a mirror without changing the source of truth.

**Both, with in-repo canonical.** Rejected for now as premature: it adds
synchronization machinery and a drift surface before there is any audience to
justify it. Revisit at M11 with `ISSUE-0011`.

**A single `open-questions.md` register.** Rejected: it cannot carry per-issue
status, severity, evidence or resolution links, and it produces merge conflicts
on every concurrent edit.

**`open/` and `closed/` subdirectories.** Rejected: file moves break inbound
links from ADRs and session logs, which is precisely the traceability this
system exists to preserve.

## Consequences

### Positive

- Issues are versioned, diffable, reviewable and offline-readable.
- Issue state and the decisions that resolve it live in the same history.
- Works with no remote, no account and no network.

### Negative

- No notifications, no assignment, no external visibility.
- `index.md` is maintained by hand and will drift — tracked as `ISSUE-0028`.
- Concurrent sessions on separate branches can allocate the same ID.

### Neutral

- Mirroring to a hosted tracker later remains possible and does not require
  restructuring.

## Compliance

Every unknown encountered in a session exists as a file in
`governance/issues/` before the session ends. No milestone starts while an
issue marked `blocking` names it in `blocks`.
