---
id: GLOSSARY
title: Glossary
status: accepted
created: 2026-08-02
updated: 2026-08-02
resolves: [ISSUE-0012, ISSUE-0026]
---

# Glossary

The ubiquitous language of this project.

A methodology that imposes a ubiquitous language on target systems must have one
itself. Every term below has exactly one meaning in this repository. Where the
inherited documents used a term ambiguously, the ambiguity is called out.

## Core structural terms

**Engineering OS** — this repository and its contents: the complete methodology.
Not any single skill within it.

**Skill** — a composable unit of methodology with an explicit contract: inputs,
outputs, preconditions, postconditions, policies consumed, artifacts produced.
A skill lives in `skills/<skill-id>/`.

> **Disambiguation.** The inherited `sources/handoff/BOOTSTRAP.md` states "this is NOT a
> collection of Claude skills" while the architecture centres on a `skills/`
> directory. These are two different meanings of one word:
>
> - **Skill (methodology unit)** — the meaning used throughout this repository.
> - **Agent-runtime skill** — a vendor packaging format, for example a Claude
>   Code `SKILL.md` with frontmatter installed into `~/.claude/skills/`.
>
> The second is a *distribution artifact* produced by `adapters/`, never the
> unit of methodology. When this repository says "skill" without qualification,
> it means the methodology unit. The runtime packaging question is `ISSUE-0001`.

**Workflow** — an ordered composition of skills with gates and exit criteria,
representing one kind of engineering change end to end. Workflows sequence
skills; they contain no methodology of their own.

**Policy** — **never used unqualified in specifications** (`ADR-0030`). Three
distinct normative artifact kinds live in `shared/policies/`:

- **`GovernancePolicy`** — rules governing *Engineering OS itself*: acceptance,
  review, release governance. Cannot modify itself; the currently `Active` one
  governs its successor's acceptance (`ADR-0023`).
- **`ModelingPolicy`** — rules governing *how domains must be modeled*: ontology
  modeling, naming conventions, state machine registration, artifact taxonomy,
  traceability rules. Not tied to one decision, expected to evolve, normative
  rather than historical, **directly consumed by AI agents** (`ADR-0029`).
- **`ProcessPolicy`** — rules governing *execution of workflows*: feature
  implementation, bug investigation, release, migration. Overlaps the workflow
  catalogue — `ISSUE-0051`.

> **The general naming rule for normative artifact types: a name is always
> qualified by what it governs.** `ADR-0025` fixed state names by owning
> machine; `ADR-0030` fixes normative artifact type names the same way.

> **ADRs explain why a policy exists. Policies define the rule that must be
> followed.** An ADR is historical and immutable; a policy is normative and
> evolving. Agents read policies; humans read ADRs for rationale.

**Contract** — a machine-checkable interface definition in `shared/contracts/`:
the shape of a record, or the I/O signature of a skill or workflow.

**Vocabulary** — a closed enumeration in `shared/vocabularies/` with exactly one
definition, for example assertion statuses or risk levels.

**Adapter** — packaging of the methodology for a specific agent runtime.
Contains zero methodology.

**Manifest** — one of three root YAML files describing an Engineering OS
project. Separated by responsibility and lifecycle, not by audience. Explicitly
*not* dependency lock files. Every adopting repository has all three. See
`ADR-0013`.

- **`MANIFEST.yaml`** — the **architectural manifest**: project composition,
  enabled modules, extension points, build pipelines, artifact taxonomy,
  generators, plugins, repository capabilities. Stable; changes rarely. Remains
  the root machine entry point and declares the other two.
- **`BUILD-STATE.yaml`** — the **implementation-state manifest**: milestones,
  progress, blockers, active, completed and pending work, ADR and issue
  references. Changes continuously.
- **`KNOWLEDGE-MANIFEST.yaml`** — the **knowledge-model manifest**: ontology
  modules, vocabularies, knowledge packages, graph modules, bounded contexts,
  capabilities, invariants, state machines, glossary modules, semantic
  dependencies. Changes when semantics change.

## Compilation terms

**Knowledge compiler** — what Engineering OS is, architecturally. It compiles
authoritative assets into a canonical knowledge model, from which all derived
artifacts are produced. Not a documentation generator. See `ADR-0014`.

**Authoritative Knowledge Model** — tier 1. The repository assets: human-authored
knowledge describing the domain. `model/` belongs here, as does `governance/`.
Artifact kind `authoritative`; always human-readable; never generated.

**Canonical Knowledge Model** — tier 2. The compiler's internal representation,
produced by compilation. **Never edited by humans.** Always reproducible from
the authoritative assets. Lives under generated artifacts and **never inside
`model/`**. Its serialization is an implementation decision. Artifact kind
`derived`.

**Derived Artifacts** — tier 3. Projections of the canonical model.

> **Disambiguation.** Two of the three tiers are derived. "The model" is
> ambiguous and should not be used unqualified — say *authoritative knowledge
> model*, *canonical knowledge model*, or `model/`.

**Authoring** — producing an artifact. Non-deterministic. Done by humans **and
by AI agents, which are authors in exactly the same sense**. Authoring alone
confers no authority.

**Acceptance** — the explicit engineering decision that confers authoritative
status. **Not a Git operation**; a commit alone does not make an artifact
authoritative. Requires explicit reviewer approval, traceability to the
motivating issue or ADR, and successful validation of applicable deterministic
checks. Is itself knowledge, and traceable. See `ADR-0018`.

**State machine** — the owner of a state vocabulary. **Every state belongs to
exactly one state machine, and there is no global concept of "state"**
(`ADR-0025`). State names may coincide across machines only when explicitly
namespaced — `ADRLifecycle.Accepted`, `ArtifactRevisionLifecycle.Active`,
`IssueLifecycle.Open`. **The same textual label never implies semantic
equivalence across machines.** This is a fundamental modeling rule for the whole
Engineering OS, including how skills model state in target domains.

**Artifact** — an **identity** that may own many Revisions. It has metadata —
identifier, ownership, revision history — and **no lifecycle of its own**. Only
its revisions transition through states (`ADR-0026`).

**Revision** — an identifiable version of an artifact. The unit the lifecycle
applies to, and the unit that is accepted. A revision has exactly one lifecycle
state. What identifies a revision is undefined — `ISSUE-0007`.

**`ArtifactRevisionLifecycle`** — the state machine governing revisions. Named
after the entity it governs, per the naming rule in `ADR-0026`, which applies to
every versioned object in Engineering OS.

**Registry** — an **authoritative index of semantic entities**. A Registry never
contains the complete specification; it references independently versioned
specifications (`ADR-0031`).

| The Registry answers | The Specification answers |
|---|---|
| what exists, where it lives, relationships, ownership, status, version | complete semantics, constraints, examples, rationale, evolution |

**Registry Pattern** — one of the core architectural patterns. Every extensible
concept is evaluated for Registry + Specification modeling rather than embedding
complete definitions inside manifests or indexes. It minimizes duplication,
enables modular evolution, and gives humans and agents one navigation model for
every concept. Whether a Registry is `authoritative` or `derived` is contested
across three ADRs — `ISSUE-0053`.

**Knowledge Explorer** — a future surface intended to expose registries for
navigation independently from the specifications they reference (`ADR-0031`).
Named with a requirement, not yet defined — `ISSUE-0052`.

**State Machine Registry** — the source of truth for state machines, and a
**section of `KNOWLEDGE-MANIFEST.yaml`**, because a state machine is part of the
semantic model of the domain: not project metadata, not build metadata, but
knowledge (`ADR-0028`). The manifest **indexes and relates** machines;
individual specifications remain separate artifacts, whose location is open
(`ISSUE-0049`). Machines are **registered, not enumerated**: each registers its identifier, owner,
governed entity, purpose, vocabulary, transition rules, authoritative
specification, related ontology concepts and related workflows. The framework
validates registrations rather than enumerating every possible lifecycle, and
documentation, visualizations, ontology navigation and validation are generated
from it. The same mechanism serves Engineering OS and every adopting repository
(`ADR-0027`). Its location is open — `ISSUE-0047`.

**Revision lifecycle** — a closed vocabulary of six states (`ADR-0020`):
`Draft` → `Under Review` → `Accepted` → `Active` → `Superseded` → `Archived`.

- **Accepted** — the revision has successfully completed the acceptance process.
- **Active** — the accepted revision is the current governing revision for that
  artifact. Exactly one revision of an artifact is `Active` at a time.

The distinction matters because an accepted revision may immediately become
superseded by a newer accepted revision.

> **The two axes are independent.** An artifact is *authoritative* because of its
> **taxonomy**; a revision is *Active* because of its **lifecycle**. A
> hand-authored ontology file is an Authoritative Artifact whether its current
> revision is `Draft`, `Active` or `Archived`.
>
> The lifecycle state formerly called `Authoritative` was renamed `Active` to
> end that collision (`ISSUE-0038`).

**Acceptance Record** — the artifact that records an acceptance, under
`governance/acceptance/` with the prefix `ACCEPT-`. A first-class Authoritative
Artifact, and **the point at which the acceptance process terminates**: an
Acceptance Record is never itself subject to an additional Acceptance Record. It
derives its authority from the decision it records. This is the base case of the
acceptance model, not an exception (`ADR-0024`).

**Trust root** — `ACCEPT-0001`, the single permitted retrospective acceptance,
covering the bootstrap corpus at a named revision. Every later acceptance chains
back to it (`ADR-0022`).

**Governance policy** — an Authoritative Artifact that constrains how work is
accepted. Follows the same lifecycle as any other. **The currently `Active`
policy always governs the acceptance of the next revision**, so no policy can
silently relax the rules under which it is accepted. Governance is
**self-hosting but never self-certifying** (`ADR-0023`).

**Self-certification** — an author accepting its own work. **Prohibited** unless
an explicit governance policy enables it. Engineering OS never assumes an AI
agent may accept its own output by default.

**Reviewer** — whoever grants explicit approval during acceptance. A human
today. Automated acceptance is possible only through explicitly configured
governance rules, a mechanism that does not yet exist (`ISSUE-0039`).

**Projection** — any artifact derived from the canonical knowledge model:
knowledge graph, search index, cross-reference index, impact database,
validation reports, agent context, documentation website. The website is one
projection, not the model.

**Artifact kind** — a closed vocabulary of four (`ADR-0012`):

- **Authoritative** — human-authored source of truth. Never generated.
- **Derived** — deterministically generated. Never edited by hand, never a
  source of truth, always rebuildable.
- **Runtime** — temporary, produced during execution. Not committed.
- **Cached** — rebuildable, produced to avoid recomputation. Not committed.

**Determinism** — the requirement that the compiler produce identical outputs
from identical authoritative repository state. **Applies to compilation, never
to authoring.** A generator may therefore never invoke an agent. See `ADR-0015`.

**Projection** (of governance) — a machine-readable view generated from
authoritative governance documents, such as `BUILD-STATE.yaml` or an index.
Never a source. Where a generator does not yet exist, a projection may be
hand-maintained as declared transitional debt — `ISSUE-0037`.

**Reference architecture** — what Engineering OS defines. The architecture
depends on no implementation language; the compiler exposes a stable interface
permitting multiple implementations. Distinguished from a *reference
implementation*, of which there will initially be one, in a language
deliberately deferred (`ISSUE-0036`). See `ADR-0017`.

## The two layers

**Layer A / the methodology** — contracts, policies, skills, workflows, schemas,
tests. Authored in this repository.

**Layer B / the knowledge model** — the `model/` tree the methodology produces:
ontology, glossary, bounded contexts, specifications, traceability, impact
analyses.

Both layers exist in **every** repository that adopts Engineering OS, including
this one. This repository is distinguished by also *authoring* Layer A.

**`model-spec/`** — the Layer A specification and copyable scaffold *of* the
Layer B tree. Part of the methodology; ships to adopters.

**`model/`** — a Layer B instance. Always repository-local. This repository's
`model/` describes Engineering OS itself.

> **Disambiguation.** `model-spec/` is the specification; `model/` is an
> instance of it. Both live here and are one character apart in prose. State
> which one you mean.

**Target repository** — the software system the Engineering OS is applied to.
May be this repository, when the methodology is applied to itself.

**Knowledge ownership** — the rule that knowledge is owned by the repository
that owns the domain. There is no shared central model. See `ADR-0010`.

**Federation** — how multi-repository environments exchange knowledge without
sharing a model: by exporting and referencing Knowledge Packages.

**Knowledge Package** — a **published interface between repositories**, and a
derived artifact. It exports a stable projection derived from the Canonical
Knowledge Model, and **never** exports authoritative assets, which stay editable
only in their owning repository. Its purpose is interoperability, not editing.

Its format is a **stable, versioned specification independent of the compiler
implementation**: compilers may evolve provided they emit conforming packages,
as different compilers emit binaries conforming to one published specification.
Packages version the specification, the exported knowledge model and
compatibility information, and never expose compiler internals. See `ADR-0019`.

## Epistemic terms

**Evidence** — any artifact consulted to support an assertion: code, tests,
schemas, migrations, documentation, tickets, contracts, standards, runtime
observation. Evidence is never automatically truth.

**Assertion** — a statement about a target system, carrying a status and a
confidence.

**Assertion status** — the epistemic standing of an assertion. A closed
vocabulary inherited from the prototypes: `confirmed`, `implemented`,
`specified`, `tested`, `observed`, `externally-defined`, `inferred`, `proposed`,
`unknown`, `conflicting`, `deprecated`, `generated`. Canonical definition is
owed to `shared/vocabularies/` in M2; currently duplicated across two files —
see `ISSUE-0018`.

**Confidence** — `high`, `medium`, `low`.

**Conflict** — credible evidence supporting incompatible interpretations.
Recorded, never silently resolved.

**Traceability** — the bidirectional link from an assertion to the evidence that
supports it, and onward to the specifications and tests that depend on it.

## Change terms

**Change** — a unit of engineering work with an identifier, an impact analysis
and a gate decision.

**Impact analysis** — the mandatory pre-implementation assessment across
semantics, invariants, behavior, contracts, data, dependencies, security,
operations, tests, documentation and compatibility. Three conflicting templates
were inherited — see `ISSUE-0013`.

**Gate / gate decision** — the explicit permission to implement:
`ready`, `ready-with-mitigations`, `blocked`.

**Invariant** — a rule that must hold, independent of the layer enforcing it.

**Constraint placement** — the decision about *which* layer enforces a
constraint: ontology, validation shape, engineering specification, state
machine, authorization policy, database constraint, API contract, application
logic, operational policy, or test.

## Project-management terms

**Milestone** — a numbered unit of work in `governance/roadmap.md` (`M1`, `M2`).
Supersedes the term "Delivery" used in the inherited roadmap.

**Delivery** — deprecated. The inherited `sources/handoff/ROADMAP.md` numbered ten "Deliveries";
these are now milestones `M2`–`M11`. See `governance/roadmap.md` for the
mapping.

**Session** — one working period. Begins by reading the repository and ends by
updating it. See `governance/session-protocol.md`.

**Issue** — a recorded unknown: question, inconsistency, gap or risk. The unit
of "we do not know this yet".

**ADR** — Architecture Decision Record. The unit of "we decided this, and here
is why".

## Terms deliberately not yet defined

The following appear in inherited documents but cannot be defined until their
governing issue is resolved. Using them as if defined is an assumption:

- **Composition primitive** — how a workflow actually invokes a skill
  (`ISSUE-0002`).
- **Definition of Done** — asserted as existing but never stated
  (`ISSUE-0010`).
- **Scenario test** — named as a deliverable with no meaning attached
  (`ISSUE-0006`).
