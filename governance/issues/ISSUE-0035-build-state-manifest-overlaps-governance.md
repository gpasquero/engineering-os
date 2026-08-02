---
id: ISSUE-0035
title: BUILD-STATE.yaml duplicates content that governance/ already owns
type: inconsistency
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0013-three-manifests-by-responsibility.md
  - governance/build-state.md
  - governance/issues/index.md
  - governance/roadmap.md
resolved-by: null
---

# ISSUE-0035 — `BUILD-STATE.yaml` duplicates `governance/`

## Statement

`ADR-0013` defines `BUILD-STATE.yaml` as holding milestones, implementation
progress, blockers, active work, completed work, pending work, and references to
the ADRs and issues affecting delivery.

Every one of those already exists in `governance/`:

| `BUILD-STATE.yaml` content | Already owned by |
|---|---|
| Milestones | `governance/roadmap.md` |
| Implementation progress, completed and pending work | `governance/build-state.md` |
| Blockers | `governance/issues/index.md`, and `blocks` in issue front matter |
| References to ADRs and issues | Both indexes |

Two artifacts claiming the same content is the duplication failure recorded in
`ISSUE-0018` and `ISSUE-0028`, now at the level of the repository's own status.

## Why it matters

Both are M2-adjacent, and the status of the project is the one thing a session
must be able to trust. If the Markdown and the YAML disagree, a session starting
from `governance/build-state.md` and a pipeline reading `BUILD-STATE.yaml` would
form different pictures of what is blocked.

It also strains `ADR-0004`, which put memory in `governance/` and kept the root
minimal. `BUILD-STATE.yaml` is memory by any honest reading.

## Options

- **`BUILD-STATE.yaml` is derived; `governance/` stays authoritative.** The
  Markdown documents and issue front matter are the source, and the YAML is
  generated from them under `ADR-0012`. Preserves the session protocol
  unchanged and closes `ISSUE-0028` in the same move. Requires that everything
  the pipeline needs be expressible in front matter.
- **`BUILD-STATE.yaml` is authoritative; the Markdown is a projection.** Machine
  content becomes primary and `governance/build-state.md` becomes a derived
  rendering. Cleaner for tooling; makes the memory layer depend on the compiler
  existing, and a human can no longer simply edit the build state.
- **Both authoritative, different scopes.** Rejected on sight — this is the
  drift failure the artifact taxonomy exists to prevent, and it should not be
  chosen by default merely because it requires no work.

The first option is the most consistent with `ADR-0001` (the repository is the
memory, readable without tooling) and with `ADR-0012` (derived artifacts are
generated from authoritative sources).

## Resolution criteria

An ADR naming which artifact is authoritative, what artifact kind the other is,
and — if the Markdown remains authoritative — what front matter must carry so
the YAML is fully derivable.
