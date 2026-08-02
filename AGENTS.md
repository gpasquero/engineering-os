# AGENTS

## Before doing anything

Read **`governance/session-protocol.md`** and follow it.

It defines the reading order that reconstructs context, and the closing steps
that preserve it. This file deliberately does not restate that list, because a
duplicated reading order drifts from the real one — the failure recorded in
`ISSUE-0023`.

## The four rules that override everything

1. **Reconstruct context exclusively by reading this repository.** Never rely on
   conversation history, prior summaries, or a claim that something was decided
   earlier. If the repository does not say it, it is not established.

2. **If information is missing, create an issue — do not assume.**
   `governance/issues/` is the mechanism. An open issue is a standing
   instruction not to quietly decide the question.

3. **Record decisions as you make them.** An ADR written later is an ADR not
   written. See `governance/adr/`.

4. **Never work directly on `main`.** Use `feat/*`, `fix/*` or `chore/*`.

## Never

- Edit anything in `imports/` or `sources/`. They are frozen provenance
  (`ADR-0005`). Defects found there become issues, not fixes.
- Start a milestone while an open issue marked `blocking` names it in `blocks`.
  Check `governance/issues/index.md` first.
- Put secrets, credentials, personal data or production identifiers into any
  artifact, including examples and fixtures.
- Generate everything in one pass. Work proceeds milestone by milestone.

## Ending a session

The session is not finished until `governance/build-state.md` is updated and a
session log exists in `governance/sessions/`. The bar:

> If the next session is a different agent with no context, can it read the
> repository and continue without asking a question that was already answered?

Full checklist in `governance/session-protocol.md`.
