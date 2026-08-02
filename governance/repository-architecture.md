---
id: REPO-ARCH
title: Repository Architecture
status: accepted
created: 2026-08-02
updated: 2026-08-02
related: [ADR-0004, ADR-0005, ADR-0009, ADR-0010]
---

# Repository Architecture

This document defines what this repository contains, what belongs where, and
what must never appear in it.

It describes the **target** structure. Directories are created only when they
receive meaningful content, so the working tree is always a subset of the tree
below. `governance/build-state.md` records which parts exist today.

## The two-layer rule

The single most important structural rule in this project.

**Layer A — the methodology.** Contracts, policies, skills, workflows, schemas,
tests. Authored here.

**Layer B — the knowledge model.** The `model/` tree the methodology produces:
ontology, glossary, bounded contexts, specifications, traceability, impact
analyses.

These are different things and are never mixed.

**Both layers exist in every repository that adopts Engineering OS, including
this one.** What distinguishes this repository is not that it lacks Layer B — it
is that this repository *also authors* Layer A.

So this repository contains both:

- **`model-spec/`** — the Layer A specification and copyable scaffold *of* the
  Layer B tree. Part of the methodology; ships to adopters.
- **`model/`** — this repository's own Layer B instance, describing Engineering
  OS itself.

`model-spec/` is the specification; `model/` is an instance of it. They are
adjacent and similarly named, and they will be confused unless the distinction
is restated wherever both appear. See `ADR-0010`, which supersedes `ADR-0006`.

## Knowledge ownership

`model/` is **always repository-local**. Knowledge is owned by the repository
that owns the domain.

```text
engineering-os/     model/  -> describes Engineering OS itself
banking-system/     model/  -> describes the banking domain
crm/                model/  -> describes the CRM domain
```

There is no shared central model directory. Multi-repository environments
**federate** through versioned Knowledge Packages — exports of ontology, graph,
glossary, specifications and metadata that let one repository reference another
without sharing its internal source of truth.

Federation does not exist yet (`ISSUE-0029`), but nothing built in `model-spec/`
or `MANIFEST.yaml` may preclude it.

## Engineering OS is a knowledge compiler

Not a documentation project, and not a documentation generator. It is an
**executable engineering framework** whose pipelines, validators, generators,
analyzers and visualizers are first-class code (`ADR-0012`).

Knowledge exists in **three tiers** (`ADR-0014`):

```text
Repository Assets          AUTHORITATIVE — human-authored, human-readable
        ↓                  includes model/, governance/
Knowledge Compiler         deterministic
        ↓
Canonical Knowledge Model  DERIVED — internal representation, never hand-edited,
        ↓                  never inside model/, always reproducible
Derived Artifacts          DERIVED — website, indexes, graph, reports, caches,
                           agent context
```

Compiler stages: parsing → normalization → validation → semantic linking.

Derived artifacts are produced *from the canonical model*, never directly from
the authoritative assets. The documentation website is one projection among many.
**No consumer is privileged.**

## Authoring versus compilation

```text
Authoring    → non-deterministic
Compilation  → deterministic
```

AI agents are **authors, exactly like human engineers**, and authors are
inherently non-deterministic. An authored artifact becomes authoritative only
after **human acceptance and version control**; from that point the compiler
must produce identical outputs from identical authoritative state (`ADR-0015`).

A generator may never invoke an agent — that would make it non-deterministic.

## Reference architecture, not reference implementation

The architecture depends on **no specific implementation language** (`ADR-0017`).
The compiler exposes a stable interface permitting multiple implementations; the
reference implementation language is deliberately deferred (`ISSUE-0036`).

Two constraints follow, and they are permanent:

- **An adopting repository does not need the toolchain to consume Engineering
  OS.** It is required only to generate or validate derived artifacts.
- **Authoritative artifacts must remain human-readable and usable without
  executing the compiler.** This is what keeps `ADR-0001` true forever: a
  session reconstructs context by reading the repository, with no tooling.

## Artifact taxonomy

Every artifact in the repository has exactly one kind (`ADR-0012`):

| Kind | Authored by | In version control | Deletable |
|---|---|---|---|
| **Authoritative** | Humans, and agents under review | Yes | No — it is the source |
| **Derived** | Deterministically generated | Per artifact | Yes, rebuildable |
| **Runtime** | Produced during execution | No | Yes, temporary |
| **Cached** | Produced to avoid recomputation | No | Yes, rebuildable |

Generated artifacts are **never** sources of truth. Every one declares its
authoritative inputs, its generator, whether it is reproducible, and whether it
is safe to delete and regenerate. Pipelines are deterministic — though the
boundary against non-deterministic agent work is unresolved (`ISSUE-0033`).

No derived artifact is ever edited by hand.

## The three manifests

Separated by responsibility and lifecycle, not by audience (`ADR-0013`):

| Manifest | Responsibility | Lifecycle |
|---|---|---|
| `MANIFEST.yaml` | Project composition, enabled modules, extension points, build pipelines, artifact taxonomy, generators, plugins, repository capabilities | **Stable** — changes rarely |
| `BUILD-STATE.yaml` | Milestones, progress, blockers, active/completed/pending work, ADR and issue references | **Continuous** |
| `KNOWLEDGE-MANIFEST.yaml` | Ontology modules, vocabularies, knowledge packages, graph modules, bounded contexts, capabilities, invariants, state machines, glossary modules, semantic dependencies | **Per domain change** |

`MANIFEST.yaml` remains the root machine entry point and declares the other two,
so everything stays discoverable from a single root. It is not a dependency lock
file.

Every adopting repository has all three, leaving unused sections empty.

**`BUILD-STATE.yaml` is a generated projection, not a source.** Governance
documents — roadmap, ADRs, issues, milestones — remain authoritative
(`ADR-0016`):

```text
Governance Documents → Knowledge Compiler → BUILD-STATE.yaml
```

The same rule applies to every index that restates content held elsewhere.
Because no generator exists yet, these are hand-maintained under an explicit
transitional-debt exception, registered in `ISSUE-0037`.

One overlap is still open: `KNOWLEDGE-MANIFEST.yaml` against `model/` and
`governance/glossary.md` (`ISSUE-0031`).

## Target structure

```text
engineering-os/
├── README.md                   Human entry point
├── AGENTS.md                   Agent entry point; points at the session protocol
├── MANIFEST.yaml               Machine entry point; architectural manifest (M2)
├── BUILD-STATE.yaml            Implementation state (M2) — see ISSUE-0035
├── KNOWLEDGE-MANIFEST.yaml     Knowledge model manifest (M2) — see ISSUE-0031
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
├── model-spec/                 M2 — Layer A specification + scaffold of the Layer B tree
├── model/                      M11 — this repository's own Layer B knowledge model
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

- A knowledge model belonging to another repository. `model/` here describes
  Engineering OS and nothing else. Cross-repository knowledge arrives through
  federation, never by copying another repository's model. See `ADR-0010`.
- Secrets, credentials, tokens, personal data or production identifiers, in any
  directory, including examples and fixtures.
- Methodology content inside `adapters/`.
- Duplicated policy text inside a skill.
- Edits to `imports/` or `sources/`.

## Unresolved structural questions

These are recorded as issues and must not be silently assumed:

- `ISSUE-0009` — who accepts an artifact, and what review means. Load-bearing
  for the architecture since `ADR-0015`, because the authoritative tier is only
  as trustworthy as acceptance makes it.
- `ISSUE-0031` — the scope of this repository's own `model/`, and its overlap
  with `governance/`.
- `ISSUE-0037` — hand-maintained projections, until generators exist.
- `ISSUE-0002` — the composition primitive, which determines whether
  `workflows/` holds prose or executable definitions.
- `ISSUE-0029` — the Knowledge Package format that federation depends on.
- `ISSUE-0001` — runtime target, which determines whether `adapters/` is real.
- `ISSUE-0036` — reference implementation language. **Deferred**, not open.

Resolved: `ISSUE-0003` (`ADR-0009`→`ADR-0013`), `ISSUE-0004` (`ADR-0010`),
`ISSUE-0005` (`ADR-0012`), `ISSUE-0028` and `ISSUE-0035` (`ADR-0016`),
`ISSUE-0030` (`ADR-0013`), `ISSUE-0032` (`ADR-0017`), `ISSUE-0033` (`ADR-0015`),
`ISSUE-0034` (`ADR-0014`).
