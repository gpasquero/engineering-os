---
id: ISSUE-0011
title: Audience, licence and distribution model are undefined
type: question
status: open
severity: medium
created: 2026-08-02
updated: 2026-08-02
blocks: [M11]
evidence:
  - sources/handoff/README.md
  - sources/handoff/BOOTSTRAP.md
resolved-by: null
---

# ISSUE-0011 — Audience, licence and distribution model are undefined

## Statement

No document states who the Engineering OS is for — a solo engineer, a team, or
an enterprise — nor whether it is public or internal. There is no `LICENSE`, no
`CONTRIBUTING.md`, and no stated contribution model.

## Why it matters

Determines M11's scope. Also shapes earlier decisions: a public project needs a
licence before any external contribution, and an enterprise audience implies
access control over the knowledge model (`ISSUE-0004`).

## What we know

- `sources/handoff/BOOTSTRAP.md` states the ambition to build "the best AI software engineering
  system ever built", which suggests a public artifact, but does not say so.
- The repository has no remote configured.

## Options

- **Public open source** — needs a licence chosen before external contribution.
- **Internal to one organization** — no licence pressure; audience assumptions
  can be narrower.
- **Public methodology, private applications** — the OS is open, the knowledge
  models it produces are not.

## Resolution criteria

An ADR naming the audience and the distribution model, plus a `LICENSE` file if
the answer is public.
