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

This repository is **Layer A** — the methodology. What the methodology produces
inside a target system is **Layer B** — a `model/` tree of ontology, glossary,
specifications and traceability. This repository specifies and scaffolds that
tree in `model-spec/`; it never contains a live `model/` of its own.

Confusing the two was the central ambiguity in the inherited design. See
`governance/adr/ADR-0006-two-layer-architecture.md`.
