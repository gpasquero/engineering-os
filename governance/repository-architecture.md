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
**federate** through Knowledge Packages.

A **Knowledge Package is a published interface between repositories**
(`ADR-0019`). It never exports authoritative assets — those stay editable only
in their owning repository. It exports a stable projection derived from the
canonical model:

```text
Authoritative Assets → Compiler → Canonical Model → Knowledge Package → Consumer
```

Its format is a **stable, versioned specification independent of the compiler
implementation**, so compilers may evolve provided they emit conforming
packages. Packages version the specification, the exported knowledge model and
compatibility information, and never expose compiler internals.

The specification itself is M13 work. What earlier milestones must respect is
only that nothing couples the eventual package format to compiler internals.

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

## Authoring, acceptance and compilation

```text
Authoring    → non-deterministic
Compilation  → deterministic
```

AI agents are **authors, exactly like human engineers**, and authors are
inherently non-deterministic. A generator may never invoke an agent — that would
make it non-deterministic.

**Authoritative status is conferred by acceptance, not by authorship and not by
a commit** (`ADR-0020`).

```text
Draft → Under Review → Accepted → Active → Superseded → Archived
```

This is the lifecycle of a **revision**, and it is independent of the artifact
taxonomy. An artifact is *authoritative* because of its taxonomy; a revision is
*Active* because of its lifecycle. Exactly one revision of an artifact is
`Active` at a time.

Acceptance is an engineering decision, not a Git operation. It requires all
three of:

1. explicit reviewer approval
2. traceability to the motivating issue, ADR or requirement
3. successful validation of all applicable deterministic checks

Condition 3 turns on **applicability**: where no deterministic validator exists,
none are applicable and the condition is satisfied. Not an exception — the
normal reading, which means the acceptance model never changes as tooling
arrives (`ADR-0021`).

**Self-certification is prohibited.** Engineering OS never assumes an AI agent
can accept its own work.

Acceptance is recorded in an **Acceptance Record** under
`governance/acceptance/` (`ADR-0021`), and is itself traceable knowledge.

**Governance is self-hosting but never self-certifying** (`ADR-0023`).
Governance policies are Authoritative Artifacts following the same lifecycle,
and **the currently `Active` policy always governs the acceptance of the next
revision** — so no policy can silently relax the rules under which it is
accepted.

**The acceptance process terminates at the Acceptance Record** (`ADR-0024`). A
record is never itself subject to an additional record — it derives its
authority from the decision it records. This is the base case, not an exception.

The chain of retrospective trust terminates at **`ACCEPT-0001`**, the single
permitted retrospective acceptance, covering the bootstrap corpus at a named
revision (`ADR-0022`).

## Every state belongs to exactly one state machine

**There is no global concept of "state"** (`ADR-0025`). There are independent
state machines, each owning its own vocabulary. State names may coincide only
when explicitly namespaced:

```text
ArtifactLifecycle.Active     ADRLifecycle.Accepted
IssueLifecycle.Open          AcceptanceLifecycle.Recorded
CompilerExecution.Completed
```

**The same textual label never implies semantic equivalence across machines.**

`shared/vocabularies/` is therefore organised **by state machine**, not as one
global list of states.

This is a fundamental modeling rule for the entire Engineering OS: it governs
how skills model lifecycles and state machines in target domains, not only how
this repository names its own. It exists because the project caught the same
class of collision three times — "skill", "authoritative", and the document
status vocabularies — and the third time identified the shared root cause.

The naming of the artifact/revision machine (`ISSUE-0044`) and the inventory of
machines this repository owns (`ISSUE-0045`) are open.

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
│   ├── acceptance/             Acceptance Records — the trust chain
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

- `ISSUE-0044` — whether the state machine is `ArtifactLifecycle` or
  `RevisionLifecycle`. Blocks `shared/vocabularies/`.
- `ISSUE-0045` — the inventory of state machines, and how a new one is
  introduced in this repository and in an adopting one.
- `ISSUE-0007` — versioning granularity, now also covering what identifies a
  **revision**.
- `ISSUE-0031` — the scope of this repository's own `model/`, and its overlap
  with `governance/`.
- `ISSUE-0037` — hand-maintained projections, until generators exist.
- `ISSUE-0002` — the composition primitive, which determines whether
  `workflows/` holds prose or executable definitions.
- `ISSUE-0001` — runtime target, which determines whether `adapters/` is real.
- `ISSUE-0036` — reference implementation language. **Deferred**, not open.

Resolved: `ISSUE-0003` (`ADR-0009`→`ADR-0013`), `ISSUE-0004` (`ADR-0010`),
`ISSUE-0005` (`ADR-0012`), `ISSUE-0028` and `ISSUE-0035` (`ADR-0016`),
`ISSUE-0030` (`ADR-0013`), `ISSUE-0032` (`ADR-0017`), `ISSUE-0033` (`ADR-0015`),
`ISSUE-0034` (`ADR-0014`).
