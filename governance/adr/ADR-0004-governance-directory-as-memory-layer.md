---
id: ADR-0004
title: Persistent memory lives in governance/ and the repository root stays minimal
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0001, ADR-0002]
---

# ADR-0004 — Persistent memory lives in `governance/`

## Context

The inherited repository kept seven Markdown files at the root: `README.md`,
`AGENTS.md`, `BOOTSTRAP.md`, `BUILD-STATE.md`, `DECISIONS.md`, `HANDOFF.md`
and `ROADMAP.md`. The target architecture adds `shared/`, `skills/`, `workflows/`,
`model-spec/`, `templates/`, `schemas/`, `validation/`, `tests/`, `adapters/`
and `docs/`.

Left alone, the root would mix the project's memory with the project's product,
and would keep growing as governance documents multiply — ADR indexes, issue
indexes, session logs, protocols.

## Decision

All persistent-memory documents live under `governance/`. The repository root
holds only entry points.

- Root retains `README.md` (human entry point) and `AGENTS.md` (agent entry
  point, rewritten to point at `governance/session-protocol.md`).
- The seven inherited root documents are **restructured**, not edited in place.
  Their originals are preserved unchanged in `sources/handoff/` as frozen
  provenance under `ADR-0005`, because issues cite them as evidence and that
  evidence must remain verifiable.
- `BOOTSTRAP.md` and `HANDOFF.md` are restructured into `governance/vision.md`.
- `DECISIONS.md` becomes `governance/inherited-decisions.md` plus ADRs.
- `ROADMAP.md` becomes `governance/roadmap.md`, renumbered M1–M11.
- `BUILD-STATE.md` becomes `governance/build-state.md`.
- `design/` becomes `governance/design/` — working proposals, not decisions.
- No root pointer stubs are left behind.

## Alternatives considered

**Keep everything at root.** Rejected: preserves the inherited reading order at
the cost of an unnavigable root once ten product directories arrive.

**Migrate with root pointer stubs.** Rejected: nothing in the repository is
tracked by git yet and there are no external references to the old paths, so the
stubs would be permanent clutter bought for no benefit. Reconsider only if
external links to the old paths appear.

**Name the directory `docs/` or `memory/`.** `docs/` rejected because it is
reserved for user-facing guides in M11 and would conflate memory with
documentation. `memory/` rejected as unconventional and unclear to human
contributors.

## Consequences

### Positive

- One directory to read to reconstruct context, which makes the session
  protocol expressible as "read `governance/`".
- Root stays legible as the product grows.
- Memory and product are visibly separate concerns.

### Negative

- Every path in the inherited documents is now stale. The old files are
  untracked and uncommitted, so no git history is lost, but any external
  reference to them breaks.
- One extra directory level on the most frequently read documents.

### Neutral

- `imports/` and `sources/` remain at root as frozen provenance (`ADR-0005`).

## Compliance

The repository root contains no Markdown file other than `README.md`,
`AGENTS.md`, and — from M2 — `MANIFEST.yaml` and a `GLOSSARY.md` pointer. Any
new memory document is created under `governance/`.
