---
id: ADR-0001
title: The repository is the persistent memory of the project
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0022]
related: [ADR-0002, ADR-0003]
---

# ADR-0001 — The repository is the persistent memory of the project

## Context

This project spans many sessions. Each session begins with no memory of the
previous one. Agents change, contexts are truncated, and conversation summaries
are lossy and unreviewable.

The inherited `sources/handoff/AGENTS.md` already gestured at this by mandating a four-file
reading order, but the files it named carried almost no content: `sources/handoff/BUILD-STATE.md`
was 18 lines, `sources/handoff/DECISIONS.md` was 12 bullet points with no rationale, and the
strongest statements of intent lived in `sources/handoff/BOOTSTRAP.md`, which the reading order
omitted entirely.

`sources/handoff/README.md` also described this repository as a "bootstrap repository … a
handoff intended to initialize the repository before implementation begins",
while `sources/handoff/ROADMAP.md` treated it as the product itself through a v1 release
(`ISSUE-0022`).

## Decision

This repository **is** the product, and it **is** the memory.

1. Context is reconstructed exclusively by reading the repository. Conversation
   history is never a source of truth.
2. Every decision produces an ADR, every unknown produces an issue, every
   session produces a session log, every delivery updates the build state.
3. When information is missing, an issue is created. Assuming an answer is a
   process violation.
4. Knowledge that exists only in a conversation is treated as lost.

## Alternatives considered

**Rely on conversation handoff summaries.** Rejected: not durable, not
diffable, not reviewable, and unavailable to a different agent or a human
reader. It is the failure mode this decision exists to prevent.

**Track memory in an external tool** (wiki, issue tracker, project board).
Rejected for the memory layer: it splits the source of truth away from the
artifacts it describes, and it cannot be read by an agent that has been given
only the repository. See `ADR-0003`.

**Keep the repository as a pure bootstrap handoff** and build the real product
elsewhere. Rejected: it would immediately reproduce the same memory problem in
the new location, and nothing in the inherited documents justifies the split.

## Consequences

### Positive

- Any agent or human with the repository can continue the work.
- Decisions become reviewable and are not silently re-litigated.
- The project practises the epistemic discipline it prescribes to target
  systems.

### Negative

- Real overhead per session. Writing the ADR and the session log is not
  optional, and a hurried session will be tempted to skip it.
- The repository grows a substantial governance layer before producing any
  methodology content.

### Neutral

- `README.md` is rewritten to describe a product at bootstrap stage, rather
  than a bootstrap package.

## Compliance

A session complies if, at its end, a reader of the repository alone can state:
what exists, what is next, what is unresolved, and why every decision was made.
The test is in `governance/session-protocol.md`.
