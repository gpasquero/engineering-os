---
id: ISSUE-0028
title: The issue index is maintained by hand and will drift
type: risk
status: open
severity: low
created: 2026-08-02
updated: 2026-08-02
blocks: [M9]
evidence:
  - governance/issues/index.md
  - governance/documentation-system.md
resolved-by: null
---

# ISSUE-0028 — The issue index is maintained by hand

## Statement

`governance/issues/index.md` duplicates the front matter of every issue file. It
is written by hand and nothing verifies that it matches.

The same applies to the highest-allocated-ID counters in
`governance/issues/README.md`, `governance/adr/README.md` and
`governance/sessions/README.md`.

## Why it matters

The index is read at session start and is therefore load-bearing. A stale index
would misreport what is blocking, which is worse than having no index at all —
a session could start a milestone that an open issue blocks.

This is the project's own instance of the duplication problem it identifies in
`ISSUE-0018`.

## What we know

- The index exists because the session protocol needs a single readable
  overview; reading 28 files at session start is not practical.
- The duplication is accepted deliberately as a temporary trade, not overlooked.

## New evidence (ADR-0012, ADR-0013)

`ADR-0012` makes this a general solved problem rather than a local one. Under
the artifact taxonomy, a hand-maintained index that duplicates content held
elsewhere is simply a **derived artifact authored by hand** — the one thing the
taxonomy forbids. The build pipeline is required to verify continuously that
derived artifacts stay synchronized with their authoritative sources.

`ADR-0013` supplies the consumer: `BUILD-STATE.yaml` needs blockers and progress,
both of which are computable from issue front matter and the roadmap.

The remaining question is not *whether* to generate but *from what*, which is
`ISSUE-0035`. This issue should be resolved by that decision plus the generator,
not independently.

## Options

- **Generate the index** from front matter in M9, alongside the other validation
  tooling.
- **Validate rather than generate** — keep it hand-written, fail a check when it
  disagrees with the files.
- **Drop the index** and rely on directory listing plus front matter. Loses the
  session-start overview.

## Resolution criteria

Either a generator or a validation rule in `validation/`, so that the index
cannot silently disagree with the issue files.
