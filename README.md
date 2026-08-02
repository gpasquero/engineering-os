# Engineering OS

An engineering operating system for AI software engineering: a modular,
versioned, reviewable methodology that AI agents and human engineers follow when
evolving software systems.

> **Knowledge is the product. Code is one artifact among many.**

This is not a prompt library and not a collection of prompts packaged for one
agent runtime. It is a methodology — with contracts, policies, composable
skills, orchestrated workflows, and an explicit gate that must be cleared before
any implementation begins.

## Status

**Bootstrap stage — milestone M1 of 11.**

The governance and documentation layer exists. No skills, policies or contracts
have been built yet. See `governance/build-state.md` for exactly what exists
today, and `governance/roadmap.md` for what comes next.

## Start here

| If you are | Read |
|---|---|
| An agent starting a session | `AGENTS.md`, then `governance/session-protocol.md` |
| A human new to the project | `governance/vision.md`, then `governance/glossary.md` |
| Looking for what exists today | `governance/build-state.md` |
| Looking for what is undecided | `governance/issues/index.md` |
| Looking for why something is the way it is | `governance/adr/README.md` |

## How this repository works

This project spans many sessions, and every session begins with no memory of the
previous one. So **the repository is the persistent memory**:

- Every decision is an ADR in `governance/adr/`.
- Every unknown is an issue in `governance/issues/`.
- Every session is logged in `governance/sessions/`.
- Current status lives in exactly one place: `governance/build-state.md`.

Knowledge that exists only in a conversation is treated as lost. When
information is missing, the rule is to **create an issue, not an assumption**.

See `governance/documentation-system.md` for the full specification.

## Layout

```text
governance/    Persistent memory: vision, principles, glossary, ADRs, issues, sessions
imports/       Frozen provenance: the three prototype skills this project began from
sources/       Frozen provenance: original requirements and handoff documents
```

`shared/`, `skills/`, `workflows/`, `model-spec/`, `schemas/`, `validation/`,
`tests/`, `adapters/` and `docs/` are specified in
`governance/repository-architecture.md` and will be created as the milestones
that fill them arrive. Directories are not created empty.

## A note on the two layers

**Layer A** is the methodology — contracts, policies, skills, workflows.
**Layer B** is the knowledge model it produces: a `model/` tree of ontology,
glossary, specifications and traceability.

Both layers exist in every repository that adopts Engineering OS. This one is
distinguished by *also authoring* Layer A: it contains `model-spec/` (the
specification of the tree, which ships to adopters) and `model/` (its own
instance, describing Engineering OS itself).

Knowledge is **repository-local**. Every repository owns the model of its own
domain; there is no central shared model, and multi-repository environments
federate through versioned Knowledge Packages.

See `governance/adr/ADR-0010-repository-local-knowledge-ownership.md`.
