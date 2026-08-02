---
id: ADR-0007
title: Keep the methodology runtime-neutral and isolate packaging in adapters/
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ISSUE-0001, ISSUE-0002, ADR-0006]
---

# ADR-0007 — Runtime-neutral core with an adapter boundary

## Context

`sources/handoff/BOOTSTRAP.md` states plainly: "This is NOT a collection of Claude skills."

Yet all three inherited prototypes *are* Claude Code skills. Each is a
`SKILL.md` with `name` / `description` / `argument-hint` frontmatter, and each
README instructs the reader to copy the directory into `~/.claude/skills/`.

The contradiction is real and unresolved (`ISSUE-0001`). It cannot be settled by
inspection, because it is a product decision about who the system is for and how
it is distributed. But M2 cannot wait for it: contracts, vocabularies and the
model specification are needed regardless of runtime.

## Decision

The methodology core is **runtime-neutral**. Runtime-specific packaging is
confined to `adapters/`.

1. Nothing in `shared/`, `skills/`, `workflows/`, `model-spec/`, `templates/` or
   `schemas/` may depend on a specific agent runtime, tool name, frontmatter
   dialect or installation path.
2. `adapters/<runtime>/` contains packaging and nothing else: frontmatter
   generation, installation layout, invocation conventions. Zero methodology.
3. Which runtimes are supported is deferred to `ISSUE-0001`. This ADR decides
   the *boundary*, not the *targets*.
4. If `ISSUE-0001` later resolves to a single runtime, `adapters/` may collapse
   to one entry — but the boundary remains, so that the core stays portable.

This is what "not a collection of Claude skills" is taken to mean: Claude Code
may be a distribution channel; it is not the product.

## Alternatives considered

**Author directly as Claude Code skills.** Rejected: contradicts `sources/handoff/BOOTSTRAP.md`,
and couples years of methodology work to one vendor's packaging format, which
has already changed shape more than once.

**Block M2 until `ISSUE-0001` is answered.** Rejected: the contracts and
vocabularies needed for M2 are runtime-independent, so blocking would stall real
work on a question that does not affect it.

**Invent a bespoke runtime for the Engineering OS.** Rejected as far out of
scope, and it would make adoption strictly harder than reusing an existing agent
runtime.

## Consequences

### Positive

- `ISSUE-0001` stops blocking M2 and M3.
- The methodology survives a change of agent runtime.
- The `sources/handoff/BOOTSTRAP.md` constraint is honoured concretely rather than rhetorically.

### Negative

- Some indirection cost: a skill cannot simply be dropped into
  `~/.claude/skills/` without an adapter build step, which is a real ergonomics
  loss during development.
- The adapter layer is unvalidated until M11, so the neutrality claim is
  untested for a long time. There is a genuine risk of writing "neutral" content
  that turns out to encode one runtime's assumptions.

### Neutral

- `ISSUE-0002` (the composition primitive) remains open and still blocks M8,
  because how a workflow invokes a skill may well be runtime-dependent.

## Compliance

No file outside `adapters/` names a specific agent runtime, vendor tool or
installation path. Reviewed by hand until M9, then by a validation rule.
