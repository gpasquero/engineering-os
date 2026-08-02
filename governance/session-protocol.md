---
id: SESSION-PROTOCOL
title: Session Protocol
status: accepted
created: 2026-08-02
updated: 2026-08-02
related: [ADR-0001, DOC-SYSTEM]
---

# Session Protocol

This project spans many sessions. Each session begins with no memory.

This document defines how a session starts, works and ends.

## Rule zero

**Reconstruct context exclusively by reading this repository.**

Do not rely on conversation history, prior summaries, or anything a user says
they told you before. If the repository does not say it, it is not established.

If a needed fact is missing, **create an issue — do not assume.**

## Session start

Read in this order. Do not skip, and do not begin work before finishing.

1. `README.md` — what this project is.
2. `governance/vision.md` — why it exists and what "done" means directionally.
3. `governance/principles.md` — the non-negotiable rules.
4. `governance/glossary.md` — the meaning of every overloaded term. Read this
   before interpreting any other document.
5. `governance/repository-architecture.md` — what belongs where.
6. `governance/documentation-system.md` — how to record what you learn.
7. `governance/roadmap.md` — the milestone sequence.
8. `governance/build-state.md` — what exists today and what is next.
9. `governance/issues/index.md` — every open question, especially `blocking`.
10. `governance/adr/README.md` — the decision index; read any ADR relevant to
    the current milestone.
11. The most recent 1–3 files in `governance/sessions/` — recent trajectory.

Only then look at `imports/` and `sources/`, and only if the current task
requires the original inputs.

## During the session

- Work on the milestone named in `governance/build-state.md`, unless the user
  redirects.
- Before assuming an answer to anything, search `governance/issues/`. If an
  issue is `open`, respect it as open — do not quietly decide it.
- When a decision is made, write the ADR **in the same session**. An
  undocumented decision is a decision that will be re-litigated.
- When an unknown appears, create the issue immediately, before continuing.
- Never edit `imports/` or `sources/`.
- Never work directly on `main`. Use a `feat/*`, `fix/*` or `chore/*` branch.

## Session end

Complete every item. A session that skips these has not finished.

1. **Update `governance/build-state.md`** — current milestone, what is now
   complete, what is next. Overwrite; do not append.
2. **Write a session log** in `governance/sessions/` using `_template.md`.
   Record what was done, what was decided, what was learned, what is open, and
   the recommended next action.
3. **Update `governance/issues/index.md`** — add new issues, update statuses.
4. **Verify bidirectional links** — every ADR written this session lists the
   issues it `resolves`, and each of those issues names it in `resolved-by`.
5. **Confirm no knowledge is left only in conversation.** Anything a future
   session would need must now be in a file.

## Handoff quality bar

The test for a finished session is:

> If the next session is a different agent with no context, can it read the
> repository and continue without asking a single question that was already
> answered?

If not, the session is not finished.
