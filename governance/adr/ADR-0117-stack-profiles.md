---
id: ADR-0117
title: Where mechanical facts live is declared by a Stack Profile, never coded
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0077, ADR-0083, ADR-0086, ADR-0108, ADR-0110, ADR-0116]
---

# ADR-0117 — Stack Profiles

## Context

Mechanical Acquisition is *"the reproducible engineering observation layer"*. It
was also, until this decision, **a hard-coded description of one repository**.

`discovery/mechanical.py` contained the literals `packages/*/package.json`,
`packages/backend/src/modules`, `*.controller.ts`, `pgTable(`, `*.spec.ts` and
`process.env.`. Every one of them is a fact about **ai-desk**, not about
software.

The consequence is not subtle. Pointed at any repository that is not a Node
workspace laid out exactly that way, the extractor returned **a model with
nothing in it** — and an empty Mechanical Model is indistinguishable from a
repository that contains nothing.

The reviewer's direction was explicit: **avoid optimizing around ai-desk**, and
judge architecture by whether a team on a real Brownfield system would notice
(`ADR-0116`). A team whose repository is not ai-desk currently gets an empty
model. Nothing available scores higher on that test.

## Decision

**Mechanical Acquisition holds mechanism. A Stack Profile holds where the facts
live, and it is data.**

`discovery/stacks.yaml` declares profiles. `discovery/mechanical.py` implements
**eight extraction kinds** and knows no path, no framework and no file
extension:

| Kind | Extracts |
|---|---|
| `manifest-json` · `manifest-xml` | packages and their dependencies |
| `dirs-under` | module directories, from a root or a marker file |
| `routes` | verb, path and a file-level prefix |
| `declaration-blocks` | named declarations and the members that follow them |
| `test-suites` | suites, declared subjects, and cases |
| `regex-set` | configuration references |
| `documents` | documents, headings and header fields |

**A profile is selected by detection, not by argument.** Which stack a repository
is written in is a fact about the repository, so it is recorded in the model
(`stackProfile`) rather than supplied by whoever ran the tool.

**Mechanical Acquisition refuses when no profile matches.** It does not return an
empty model:

> An empty model and an unrecognised stack are opposite findings, and only one
> of them is about the repository.

## Rationale

This is the sixth application of a pattern that has been correct every time:
validation rules (`ADR-0077`), registries (`ADR-0083`), queries (`ADR-0086`),
recommendations (`ADR-0091`), plans (`ADR-0094`) — mechanism in code, decisions
in data.

It also protects the property the two-stage split exists for. **Interpretive
Discovery reads the Mechanical Model exclusively** (`ADR-0108`) and never learns
which profile produced it. The vocabulary — eight keys — is therefore the
portability boundary, and the claim this decision makes testable is:

> **A new stack costs a declaration and no interpreter change.**

## Consequences

**A profile can be wrong, and wrongness is now visible.** The first Java profile
named the repository after its framework's BOM, because a Maven module inherits
from a parent whose `artifactId` appears first. It also found zero module
directories, because it guessed at directory *names*. Both were corrected by
editing a declaration.

**A profile must not fabricate.** The first Java profile substituted a test
class's name for a missing declared subject. That converts *absence* into
*content*, and it is the one thing a mechanical layer may never do. The rule is
now stated where it can be applied to future profiles:

> **A fallback that supplies an identifier where a statement is missing does not
> improve coverage. It manufactures evidence.**

**One profile per repository is already known to be insufficient.** The first
repository this was tried on hosts a Java backend, a TypeScript frontend and a
Python service. Detection returns one profile. Recorded as a gap rather than
solved, because a single repository is not enough evidence (`ADR-0119`).

**The vocabulary version becomes `2.0.0`.** The facts are unchanged — the Node
profile reproduces the previous extractor's output **identically across all eight
keys** — but a versioned contract whose producer changed shape declares it
(`ADR-0110`).

## Compliance

- `discovery/stacks.yaml` declares every profile; `discovery/mechanical.py`
  contains no repository path, framework name or file extension outside
  `SKIP_DIRS`.
- `extract()` records `stackProfile` in the model and raises when detection
  fails.
- The `S-node-nest-drizzle` profile reproduces the pre-decision extractor's
  output on ai-desk, key for key.
