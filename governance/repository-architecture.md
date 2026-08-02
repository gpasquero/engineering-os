---
id: REPO-ARCH
title: Repository Architecture
status: accepted
created: 2026-08-02
updated: 2026-08-02
related: [ADR-0004, ADR-0005, ADR-0006]
---

# Repository Architecture

This document defines what this repository contains, what belongs where, and
what must never appear in it.

It describes the **target** structure. Directories are created only when they
receive meaningful content, so the working tree is always a subset of the tree
below. `governance/build-state.md` records which parts exist today.

## The two-layer rule

The single most important structural rule in this project.

**Layer A — the product.** This repository. It contains the methodology:
contracts, policies, skills, workflows, schemas, tests.

**Layer B — the output.** The `model/` tree that the Engineering OS produces
*inside a target repository* when it is applied: ontology, glossary, bounded
contexts, specifications, traceability, impact analyses.

These are different things and are never mixed.

This repository therefore contains **`model-spec/`** — the specification and a
copyable scaffold of the `model/` tree — and never a live `model/` directory of
its own. Confusing the two was the central ambiguity in the inherited design
documents. See `ADR-0006`.

## Target structure

```text
engineering-os/
├── README.md                   Entry point
├── AGENTS.md                   Agent entry point; points at the session protocol
├── GLOSSARY.md                 -> governance/glossary.md (root pointer, M2)
├── MANIFEST.yaml               Registry of skills, workflows, contracts (M2)
│
├── governance/                 PERSISTENT MEMORY — the subject of M1
│   ├── vision.md               Why this exists
│   ├── principles.md           Non-negotiable rules
│   ├── glossary.md             Ubiquitous language of the project itself
│   ├── repository-architecture.md   This document
│   ├── documentation-system.md      How knowledge is recorded
│   ├── session-protocol.md          How a session starts and ends
│   ├── roadmap.md                   Milestone sequence
│   ├── build-state.md               Current status (overwritten)
│   ├── inherited-decisions.md       Pre-M1 decisions awaiting ADR context
│   ├── adr/                    Decision records
│   ├── issues/                 Open questions, inconsistencies, gaps, risks
│   ├── sessions/               Append-only session journal
│   └── design/                 Working proposals, not yet decisions
│
├── shared/                     M2–M3
│   ├── contracts/              Normative, machine-checkable interfaces
│   ├── policies/               Normative prose, referenced and never inlined
│   └── vocabularies/           Closed enumerations, single source
│
├── skills/                     M4–M7 — one directory per skill
├── workflows/                  M8 — one directory per workflow
├── model-spec/                 M2 — specification + scaffold of the Layer B tree
├── templates/                  Document templates used by skills
├── schemas/                    M9 — JSON Schema for machine validation
├── validation/                 M9 — rules and scripts
├── tests/                      M10 — scenarios, fixtures, expectations
├── adapters/                   M11 — packaging only, zero methodology content
├── docs/                       M11 — user-facing guides
│
├── imports/                    FROZEN — the three prototype skills
└── sources/                    FROZEN — original requirements and archives
```

## Directory contracts

**`governance/`** — the persistent memory. Anything a future session must know
lives here. This is the only directory a session is required to read in full.

**`shared/`** is split three ways deliberately, because the three kinds of
content have different normativity and different failure modes:

- `contracts/` — machine-checkable interfaces (record shapes, skill I/O). A
  violation is detectable by a validator.
- `policies/` — normative prose that skills **reference by path** and must never
  inline. Inlining policy text is the duplication this architecture exists to
  eliminate.
- `vocabularies/` — closed enumerations (assertion statuses, risk levels, gate
  decisions) with exactly one definition each.

**`skills/`** — each skill is a directory containing an instruction body and a
machine-readable contract declaring inputs, outputs, preconditions,
postconditions, the policies it consumes and the artifacts it produces. A skill
without a contract is not composable.

**`workflows/`** — ordered compositions of skills with gates and exit criteria.
Workflows contain no methodology of their own; they sequence skills.

**`adapters/`** — packaging for a specific runtime (Claude Code, AGENTS.md, MCP)
and nothing else. The methodology stays runtime-neutral so that a runtime change
never rewrites the core. The choice of runtimes is unresolved — see `ISSUE-0001`.

**`imports/` and `sources/`** — frozen provenance. Never edited, never
refactored, never corrected. They record what we were given, not what we now
believe. Correcting an input in place would destroy the distinction between
current state and proposed state. See `ADR-0005`.

## What must never appear here

- A live `model/` directory. This repository is Layer A. See `ADR-0006`.
- Secrets, credentials, tokens, personal data or production identifiers, in any
  directory, including examples and fixtures.
- Methodology content inside `adapters/`.
- Duplicated policy text inside a skill.
- Edits to `imports/` or `sources/`.

## Unresolved structural questions

These are recorded as issues and must not be silently assumed:

- `ISSUE-0001` — runtime target, which determines whether `adapters/` is real.
- `ISSUE-0002` — the composition primitive, which determines whether
  `workflows/` holds prose or executable definitions.
- `ISSUE-0003` — what `MANIFEST.yaml` actually is.
- `ISSUE-0004` — where the Layer B `model/` tree lives for a target system.
- `ISSUE-0005` — whether this repository ships executable code at all.
