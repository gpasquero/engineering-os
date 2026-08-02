---
id: SESSION-INDEX
title: Session Journal
status: current
created: 2026-08-02
updated: 2026-08-02
---

# Session Journal

Append-only. One file per session, named `SESSION-NNNN-YYYY-MM-DD.md`.

A session log is **immutable once written**. It records what was true at that
point in time. Corrections belong in a later session log, not in an edit.

Session logs are the trajectory record: they answer "how did we get here",
which no other document does. `build-state.md` answers "where are we", and the
ADRs answer "why".

**Highest allocated ID: `SESSION-0001`.**

## Index

| ID | Date | Milestone | Summary |
|---|---|---|---|
| [SESSION-0001](SESSION-0001-2026-08-02.md) | 2026-08-02 | M1 | Repository bootstrap: architecture, documentation system, session protocol, 8 ADRs, 28 issues |

## Reading

At session start, read the most recent one to three logs. Reading the whole
journal is unnecessary; `build-state.md` and `issues/index.md` carry the
current picture.
