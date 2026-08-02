---
id: ISSUE-0007
title: Versioning granularity and compatibility policy are undefined
type: question
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - sources/handoff/BOOTSTRAP.md
  - sources/handoff/DECISIONS.md
resolved-by: null
---

# ISSUE-0007 — Versioning granularity is undefined

## Statement

`sources/handoff/BOOTSTRAP.md` requires that "everything must be versioned". No document states
what unit carries a version, what scheme it uses, or what happens when versions
disagree.

## Why it matters

`MANIFEST.yaml` (`ISSUE-0003`) is expected to record versions, so this must be
answered within M2. It also determines whether a skill can declare a dependency
on a specific contract version.

## What we know

- The architecture has several candidate version-bearing units: the repository,
  a skill, a workflow, a contract, a vocabulary.
- Nothing yet references anything else by version.

## Options

- **Whole-repository semver only** — simplest; a change to one skill bumps
  everything; no independent evolution.
- **Per-component semver** — skills, workflows and contracts version
  independently; enables precise dependency declarations; requires compatibility
  resolution and a manifest that records it.
- **Repository version plus contract versions** — only the machine-checkable
  interfaces version independently. Middle path.

## Extended by ADR-0020 and ADR-0021

The revision lifecycle applies to **revisions**, and an Acceptance Record
carries an `artifact revision` field. Nothing defines what identifies a
revision.

This is a distinct question from component versioning, but it is close enough
that one ADR should settle both:

- Is a revision a commit SHA, a content hash, or a declared version?
- A commit SHA is unambiguous but couples the knowledge model to Git, which
  `ADR-0018` deliberately decoupled acceptance from.
- A content hash is VCS-independent but unreadable, and changes on
  whitespace-only edits.
- A declared version is readable but must be maintained by the author, and
  nothing would prevent two different contents claiming one revision.

Until this is settled, `ACCEPT-0001` uses a commit SHA — a pragmatic choice for
a trust root, not a decision.

## Resolution criteria

An ADR naming the version-bearing units, the scheme, what a breaking change
means for a prose artifact, and how a version mismatch is detected and handled.
