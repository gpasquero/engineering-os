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

## The four-layer semantic architecture

**Layers classify semantic artifacts, not directories** (`ADR-0039`). A
directory may contain artifacts of several layers; repository layout is an
**implementation** concern while the semantic layer is an **architectural** one.
The compiler classifies artifacts, not folders.

**Every *semantic* artifact belongs to exactly one layer.** Cross-cutting
artifacts belong to none.

| Layer | Name | Defines |
|---|---|---|
| **A** | Engineering OS Metamodel | **the language** |
| **B** | Repository Knowledge Model | **a specific domain**, using that language |
| **C** | Canonical Knowledge Model | compiler-generated semantic representation of Layer B |
| **D** | Derived Projections | Knowledge Explorer, documentation, Registry Projections, search, Knowledge Packages, validation reports, future AI interfaces |

```text
Layer A   model/metamodel/          ArtifactType · RegistrySpecification ·
                                    Policy · Workflow · Skill · Capability ·
                                    StateMachine · Vocabulary · Ontology · …
             ↓
          Knowledge Compiler
             ↓
Layer C   Canonical Knowledge Model   (conforming to Layer A)
             ↓
Layer D   Explorer · Documentation · Indexes · Packages · Validation · Search
```

Layer B is each repository's own knowledge model, expressed in the Layer A
language and compiled into Layer C.

### The Metamodel

**Layer A belongs to Engineering OS itself.** It is authored at
`model/metamodel/`, is an authoritative artifact, is versioned with Engineering
OS, and evolves through the same governance as every other authoritative
artifact.

> **Adopting repositories never modify the metamodel. They instantiate it.**

This is why `model/` in *this* repository contains Layer A content: Engineering
OS's domain genuinely is the metamodel. The shorthand "`model/` is Layer B"
holds for adopters, not here.

### `model-spec/` and `model/`

- **`model-spec/`** — the specification and copyable scaffold *of* a Layer B
  tree. Ships to adopters.
- **`model/`** — this repository's own tree, containing `metamodel/`.

### Cross-Cutting Infrastructure

`governance/`, `tests/`, `scripts/`, `tooling/`, `ci/` and editor configuration
are **orthogonal to the semantic layers** (`ADR-0039`). ADRs, Issues, Acceptance
Records and Sessions are governance artifacts: inputs to the Engineering OS
*process*, not part of the semantic model of a target domain.

| | |
|---|---|
| **Semantic Layers** | A, B, C, D |
| **Cross-Cutting Infrastructure** | Governance · Tooling · Automation · Validation · Testing · CI/CD |

These intersect the semantic layers but are not themselves layers. Both sets are
examples rather than closed — `ISSUE-0057`.

## Architectural Dimensions

**Artifacts are classified along multiple independent axes simultaneously**
(`ADR-0040`), rather than forced into a single hierarchy:

Semantic Layer · Artifact Taxonomy · Lifecycle · Governance Status · Ownership ·
Authority · Visibility · Compilation Phase

An ADR is Governance / Authoritative Artifact / `Active` / Owner: Architecture /
Visibility: Public / Compiler Phase: Input / **Layer: None**. A Workflow
Specification is Semantic / Layer B / Authoritative Artifact / `Active` /
Owner: Domain / Compiler Phase: Input.

This is the general form of a fix applied five times locally: every earlier
vocabulary collision came from one classification being asked to do several
jobs.

**Dimensions are first-class entities, added by registration** (`ADR-0041`) —
never by modifying compiler logic. They must be **specified before they can be
instantiated**: a `DimensionSpecification` is a metamodel entity with ten fields,
and every assignment instantiates one (`ADR-0048`).

**Dimensions are a scarce architectural resource** (`ADR-0049`). A concept
becomes a Dimension only if it classifies many independent artifact types, is
orthogonal to other classifications, evolves independently, is useful for
querying or validation, and takes multiple values across artifacts.

**Dimensions enter the metamodel only through a Dimension Review** (`ADR-0051`),
producing one of four outcomes: accepted, or rejected and modelled as metadata,
a relationship, or another metamodel entity.

## Engineering Gates

A **Gate** is a review process applied to the introduction or modification of an
architectural concept — a first-class metamodel concept (`ADR-0054`). Each
defines purpose, scope, triggering conditions, required evidence, evaluation
criteria, resulting decision and produced artifacts.

| Gate | Questions it declares |
|---|---|
| Metamodel Position Gate | Which metamodel entity does it instantiate? Which semantic layer owns it? |
| Compiler Impact Review *(future)* | Which compiler phase consumes it? Which produces it? |
| Dimension Review | Does it satisfy the Dimension criteria? Is another construct more appropriate? |
| Acceptance Review | Is it authoritative? Has it been reviewed? Does it satisfy applicable validation? |

**Questions belong to Gates, not to artifacts** (`ADR-0055`). A purely semantic
concept never encounters a compiler question, because that gate is not triggered
for it. **Triggering conditions are the enforcement surface.**

The metamodel models Gate **independently from the rules a gate executes**.

## Principle → Policy → Process → Artifact

Three levels of engineering knowledge (`ADR-0056`):

- **Principles** — stable architectural truths.
- **Policies** — normative rules derived from them.
- **Processes** — operational procedures implementing those policies.

This is why ADRs, Policies and Gates exist without overlapping
responsibilities: ADRs record how content came to be, Policies hold the rules,
Gates are the processes. Every policy cites its principle; every process cites
its policy.

**Artifacts do not contain dimension values.** They are classified by
**Dimension Assignments** — explicit semantic relationships (`ADR-0042`):

```text
Artifact → Dimension Assignment → Dimension → Dimension Value
```

Assignments are versioned and may change without changing artifact identity;
validation targets assignments, not artifacts. The Canonical Knowledge Model
represents them as graph relationships rather than embedded metadata.

**Dimensions are independent, not isolated** (`ADR-0044`). Values are never
derived from one another, but dimensions may declare relationships describing
compatibility, applicability or constraints — **descriptive, never
inferential**. Inference Rules, if ever introduced, are their own artifact type.

**Front matter is an interchange syntax, not the semantic model** (`ADR-0045`).
An authoritative artifact exposes a **Human Representation**: a canonical
serialization of selected assignments, so the repository stays understandable
without the compiler.

```text
Dimension Assignment → Canonical Serialization → Artifact Front Matter
```

## Two orthogonal hierarchies

**The metamodel defines what exists. The compiler defines how it is
transformed. Neither embeds concepts belonging to the other** (`ADR-0053`).

**Semantic hierarchy** (`ADR-0052`) — one recurring pattern across the
framework:

```text
Definition → Instance → Assignment
```

| Definition | Instance | Assignment |
|---|---|---|
| Dimension Specification | Dimension | Dimension Assignment |
| State Machine Specification | State Machine | State Assignment |
| Policy Specification | Policy | *Policy Assignment (future)* |

**Compilation hierarchy** — orthogonal:

```text
Authoritative Semantic Model → Canonical Knowledge Model → Projection
```

Registry Projections, the Knowledge Explorer, documentation and search indexes
are **compilation products, not semantic concepts**.

Every new concept answers: **semantic, compilation, or both?** Only concepts
genuinely in both appear in both, with explicit correspondence.

## Three representations of knowledge

| Representation | Is |
|---|---|
| **Semantic** | the canonical graph |
| **Authoring** | the human-editable source artifacts |
| **Presentation** | generated views — Explorer, documentation, indexes, registry projections |

**The compiler maintains semantic equivalence across all three.** They are
different views of the same knowledge, not different knowledge (`ADR-0047`).
A discrepancy between representations is a compiler defect.

This is how the project optimizes for human authoring, machine reasoning and
generated documentation at once without duplicating semantics.

## Three semantic levels

A different axis from the four layers (`ADR-0043`):

| Level | Defines | Examples |
|---|---|---|
| **1 — Metamodel** | entity *types* | `Artifact`, `Dimension`, `Registry`, `Policy`, `Workflow`, `Skill` |
| **2 — Model** | *instances* | `ADR-0040`, a `GovernancePolicy`, a workflow |
| **3 — Classification** | *assertions about instances* | *belongs to Layer A*, *is Active*, *owned by Architecture* |

**This prevents classification systems from becoming part of the object model
itself**, and lets dimensions, classifications and assertions evolve
independently. The Knowledge Graph represents the three as distinct node types.

> **Always use the qualified names** (`ADR-0046`): **Abstraction Level**
> classifies abstraction, **Semantic Layer** classifies position in the
> knowledge architecture. No renaming was required — only qualification.

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

Layers B, C and D are the three tiers `ADR-0014` established, preserved by
`ADR-0037`: authoritative repository assets, the compiler-generated canonical
model, and the projections derived from it. The canonical model is never
hand-edited and never lives inside `model/`.

Compiler stages: parsing → normalization → validation → semantic linking.

**The Canonical Knowledge Model is not an arbitrary graph. It is a graph
conforming to the Engineering OS Metamodel** (`ADR-0036`):

```text
Engineering OS Metamodel  →  Canonical Knowledge Model  →  projections
```

The Metamodel is **the ontology of Engineering OS itself** — its purpose is not
to describe software systems but to describe *how Engineering OS describes
software systems* (`ADR-0035`). It is the **contract between authoring and
compilation**, and it must exist before the compiler interface is finalized, so
that the compiler compiles into it rather than inventing its own structure.

**Process gate:** every new concept is positioned in the metamodel before a new
artifact type is introduced. Where the metamodel lives is unresolved —
`ISSUE-0055`.

Derived artifacts are produced *from the canonical model*, never directly from
the authoritative assets. Consumers include the knowledge graph, search index,
cross-reference index, impact database, validation reports, agent context,
documentation website and the **Knowledge Explorer** (`ADR-0034`) — a
per-repository navigable projection that every adopting repository generates over
its own domain. **No consumer is privileged.**

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

This is `ArtifactRevisionLifecycle`, the lifecycle of a **revision**, and it is
independent of the artifact taxonomy (`ADR-0026`).

**An Artifact is an identity that may own many Revisions, and has no lifecycle
of its own** — only metadata: identifier, ownership, revision history. A
Revision has exactly one lifecycle state. "What state is this artifact in?" is a
malformed question.

An artifact is *authoritative* because of its taxonomy; a revision is *Active*
because of its lifecycle. Exactly one revision of an artifact is `Active` at a
time.

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
ArtifactRevisionLifecycle.Active    ADRLifecycle.Accepted
IssueLifecycle.Open                 AcceptanceLifecycle.Recorded
CompilerExecutionLifecycle.Completed
```

**The same textual label never implies semantic equivalence across machines.**

`shared/vocabularies/` is therefore organised **by state machine**, not as one
global list of states.

This is a fundamental modeling rule for the entire Engineering OS: it governs
how skills model lifecycles and state machines in target domains, not only how
this repository names its own. It exists because the project caught the same
class of collision three times — "skill", "authoritative", and the document
status vocabularies — and the third time identified the shared root cause.

**The State Machine Registry is a section of `KNOWLEDGE-MANIFEST.yaml`**
(`ADR-0028`), because a state machine is part of the semantic model of the
domain — not project metadata, not build metadata, but **knowledge**. The
manifest indexes and relates machines; individual specifications remain separate
artifacts (`ISSUE-0049`).

This sharpens the three-manifest split into a decision test: **architecture /
implementation status / semantic structure.**

**State machines are registered, not enumerated** (`ADR-0027`). Every machine
registers its identifier, owner, governed entity, purpose, vocabulary,
transition rules, authoritative specification, related ontology concepts and
related workflows. The framework validates registrations rather than
enumerating every possible lifecycle, and documentation, visualizations,
ontology navigation and validation are generated from the registry.

The same mechanism serves Engineering OS and every adopting repository.

## ADRs versus Policies

> **ADRs explain *why* a policy exists. Policies define the rule that must be
> followed** (`ADR-0029`).

Three normative artifact kinds live in `shared/policies/` (`ADR-0030`):

| Kind | Governs |
|---|---|
| `GovernancePolicy` | Engineering OS itself — acceptance, review, release |
| `ModelingPolicy` | how domains must be modeled |
| `ProcessPolicy` | execution of workflows |

**The unqualified term "Policy" is never used in specifications.** A normative
artifact type name is always qualified by what it governs — the same discipline
`ADR-0025` applies to state names.

Unlike an ADR, a policy is not tied to a single decision, is expected to evolve,
is normative rather than historical, and is **directly consumed by AI agents**.
Policies reference the ADRs they originated from but are not generated from them.

**Agents primarily consume Policies. Humans read ADRs for rationale.**

This exists so the accumulated ADR history never becomes the operational
specification — a corpus of 31 decisions with five supersessions is a record of
how a specification came to be, not a specification.

## The Registry Pattern

**A Registry never contains the complete specification** — it references
independently versioned ones (`ADR-0031`). The word names **two artifacts of
different kinds** (`ADR-0032`):

| Artifact | Kind | Holds |
|---|---|---|
| **Registry Specification** | authoritative | identity, semantic purpose, ownership, membership rules, required metadata, constraints, relationships, extension rules |
| **Registry Projection** | derived | the generated index of entities currently registered |

The projection is what humans browse; the specification governs the registry.
This reconciles `ADR-0016` (generated indexes are derived) with `ADR-0031`
(registries are first-class) without superseding either.

| The Registry answers | The Specification answers |
|---|---|
| what exists | complete semantics |
| where it lives | constraints |
| relationships | examples |
| ownership | rationale |
| status, version | evolution |

**Every extensible concept is evaluated for Registry + Specification modeling**
rather than embedding complete definitions inside manifests or indexes.

The pattern was rediscovered four times — skills indexed by `MANIFEST.yaml`,
state machines registered rather than enumerated, the registry indexing
specifications held elsewhere, and policies following the same shape — before
being named.

`governance/issues/index.md` and `governance/adr/README.md` are Registry
Projections maintained by hand because no compiler exists — the debt registered
in `ISSUE-0037`. Their Registry Specifications do not exist yet either.

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
│   ├── policies/               Modeling, governance and process policies
│   └── vocabularies/           Closed enumerations, single source
│
├── skills/                     M4–M7 — one directory per skill
├── workflows/                  M8 — one directory per workflow
├── model-spec/                 M2 — specification + scaffold of a Layer B tree
├── model/
│   └── metamodel/              M2 — LAYER A, the Engineering OS Metamodel
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

> **Implementation guidance, not architecture** (`ADR-0039`). A directory does
> not determine an artifact's semantic layer. What follows is convention: useful,
> and revisable without changing what anything means.

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

- `ISSUE-0049` — where state machine specifications live, and their boundary
  with `shared/vocabularies/`. Blocks `shared/vocabularies/`.
- `ISSUE-0069` — "Level" and "Process" are reused for new schemes. **Seventh
  terminology collision**, and the metamodel must not inherit it.
- `ISSUE-0070` — whether Principles are a first-class artifact type, and how
  they relate to the ADRs currently recording them.
- `ISSUE-0063` — the minimum set of classifications that must be serialized.
- `ISSUE-0048` — no mechanism for correcting part of an `Active` ADR.
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
