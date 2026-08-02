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

**Workflow** — **executable orchestration**: an ordered composition of skills
with gates and exit criteria, representing one kind of engineering change end to
end. Workflows sequence skills and contain no methodology of their own — the
normative rules live in the `ProcessPolicy` artifacts a workflow references
(`ADR-0033`). This prevents implementation procedures from becoming the source
of engineering policy.

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
  implementation, bug investigation, release, migration. **A ProcessPolicy
  governs a Workflow; the two are independent artifact types.** A Workflow
  references ProcessPolicies and never embeds normative rules; a ProcessPolicy
  never embeds execution steps (`ADR-0033`).

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
produced by compilation, and **a graph conforming to the Metamodel** rather than
an arbitrary one (`ADR-0036`). **Never edited by humans.** Always reproducible from
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

**Registry** — a first-class concept that never contains the complete
specification; it references independently versioned specifications
(`ADR-0031`). **The word names two artifacts, and they have different kinds**
(`ADR-0032`):

- **Registry Specification** — **authoritative**. Defines registry identity,
  semantic purpose, ownership, membership rules, required metadata, constraints,
  relationships and extension rules. *This is what governs the registry.*
- **Registry Projection** — **derived**. The generated index of the entities
  currently registered. *This is what humans browse.*

```text
Registry Specification → Knowledge Compiler → Registry Projection
    (authoritative)                              (derived)
```

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

## The four semantic layers

**Every artifact belongs to exactly one layer** (`ADR-0037`).

**Layer A — Engineering OS Metamodel.** Defines *the language*. Authored at
`model/metamodel/` in this repository, versioned with Engineering OS. Adopting
repositories never modify it; they instantiate it.

**Layer B — Repository Knowledge Model.** Defines *a specific domain*, using
that language. Each repository owns its own (`ADR-0010`).

**Layer C — Canonical Knowledge Model.** The compiler-generated semantic
representation of Layer B, conforming to Layer A (`ADR-0036`).

**Layer D — Derived Projections.** Knowledge Explorer, documentation, Registry
Projections, search, Knowledge Packages, validation reports, future AI
interfaces.

> **Layers classify artifacts, not directories** (`ADR-0039`). A directory may
> hold artifacts of several layers. Repository layout is an implementation
> concern; the semantic layer is an architectural one.

**Cross-Cutting Infrastructure** — Governance, Tooling, Automation, Validation,
Testing, CI/CD. **Orthogonal to the semantic layers**: they intersect them but
are not themselves layers. ADRs, Issues, Acceptance Records and Sessions are
governance artifacts — inputs to the Engineering OS process, not part of any
target domain's semantic model. Their Semantic Layer is `None (Not Applicable)`.

**Architectural Dimension** — a **first-class semantic entity** defining one
independent axis of classification. Not merely a taxonomy (`ADR-0041`).

**Dimensions must be specified before they can be instantiated.** A
**`DimensionSpecification`** is a first-class metamodel entity declaring ten
fields: identifier, purpose, governed entity types, **value model**,
**assignment semantics**, cardinality, constraints, relationships,
**serialization strategy**, **validation rules** (`ADR-0048`). Every Dimension
Assignment instantiates one.

> **Dimensions are a scarce architectural resource. Creating one requires an
> ADR** (`ADR-0049`). A concept becomes a Dimension only if all five conditions
> hold: it classifies many independent artifact types; its values are
> **orthogonal to other classifications**; it evolves independently; it is
> useful for querying, navigation or validation; and multiple values exist
> across repository artifacts. Otherwise it is modelled as metadata, a property,
> a relationship, or a dedicated metamodel entity.

**Dimensions are added by registration, never by modifying compiler logic** — a
**Dimension Registry Specification** (authoritative) with a generated
**Dimension Registry Projection**, following the Registry Pattern.

Candidates: Semantic Layer · Artifact Taxonomy · Lifecycle · Compilation Phase ·
Abstraction Level · Governance Status · Ownership · Authority · Visibility ·
Representation. **None has been evaluated against the five conditions** —
`ISSUE-0065`.

> **Independence is not isolation** (`ADR-0044`). Dimension *values* are never
> derived from one another, but dimensions **may** declare semantic
> relationships describing compatibility, applicability or constraints. Those
> relationships are **descriptive, never inferential** — they never imply
> automatic classification. No dimension derives another's value unless an
> explicit **Inference Rule** exists, and Inference Rules, if ever introduced,
> are their own first-class artifact type.

**Dimension Assignment** — the explicit semantic relationship by which an
artifact is classified. **Artifacts do not contain dimension values**
(`ADR-0042`):

```text
Artifact → Dimension Assignment → Dimension → Dimension Value
```

Assignments are versioned, may change without changing artifact identity, and
are what validation targets. The Canonical Knowledge Model represents them as
**graph relationships rather than embedded metadata**.

**Human Representation** — a **canonical serialization** of selected semantic
assignments, exposed by an authoritative artifact so the repository stays
understandable without executing the compiler (`ADR-0045`). It is **not the
semantic source of truth**.

```text
Dimension Assignment → Canonical Serialization → Artifact Front Matter
```

> **Front matter is an interchange syntax, not the semantic model.** The
> compiler reconstructs relationships from it; the relationship exists
> independently of it. Which classifications must be serialized is unstated —
> `ISSUE-0063`.

## The three semantic levels

Distinct from the four layers, and a different axis (`ADR-0043`).

**Level 1 — Metamodel.** Defines entity *types*: `Artifact`, `Dimension`,
`Registry`, `Policy`, `Workflow`, `Skill`.

**Level 2 — Model.** Defines *instances*: `ADR-0040`, a specific
`GovernancePolicy`, the Compiler Interface Workflow.

**Level 3 — Classification.** Defines *semantic assertions about instances*:
*belongs to Layer A*, *is Authoritative*, *is Active*, *owned by Architecture*.

**This separation prevents classification systems from becoming part of the
object model itself.** The Knowledge Graph represents the three as distinct node
types rather than flattening them into object properties.

> **Levels are not layers, and both names are always qualified** (`ADR-0046`).
> **Abstraction Level** classifies abstraction; **Semantic Layer** classifies
> semantic position in the knowledge architecture. No renaming — only
> qualification, the same discipline applied to state names (`ADR-0025`) and
> normative artifact types (`ADR-0030`).

**Semantic hierarchy** — the recurring three-stage pattern across the framework
(`ADR-0052`):

```text
Definition → Instance → Assignment
```

| Definition | Instance | Assignment |
|---|---|---|
| Dimension Specification | Dimension | Dimension Assignment |
| State Machine Specification | State Machine | State Assignment |
| Policy Specification | Policy | *Policy Assignment (future)* |

**Compilation hierarchy** — orthogonal to the semantic one:

```text
Authoritative Semantic Model → Canonical Knowledge Model → Projection
```

**Registry Projections, the Knowledge Explorer, documentation and search indexes
are compilation products, not semantic concepts.** Future extensible concepts
are evaluated against the semantic hierarchy before new modeling structures are
introduced.

**Engineering Gate** — a **review process applied to the introduction or
modification of an architectural concept** (`ADR-0054`). A first-class metamodel
concept. Every Gate defines purpose, scope, triggering conditions, required
evidence, evaluation criteria, resulting decision and produced artifacts. The
metamodel models Gate **independently from the rules executed by that Gate**.

Instances: **Metamodel Position Gate** (`ADR-0035`), **Dimension Review**
(`ADR-0051`), **Artifact Definition Review** (`ADR-0038`→`ADR-0055`),
**Acceptance Review** (`ADR-0020`), **Compiler Impact Review** *(future)*.

> **Evaluation questions belong to Gates, not to artifacts** (`ADR-0055`). Every
> Gate declares which questions apply, so a purely semantic concept never
> encounters a compiler question. Triggering conditions decide what is asked.

**Dimension Review** — an instance of Gate: the standard procedure by which a
proposed Dimension enters the metamodel (`ADR-0051`). Produces one of four outcomes: accepted as a
Dimension, or rejected and modelled as metadata, as a relationship, or as
another metamodel entity. `ADR-0049`'s five criteria are **mandatory**
evaluation criteria. Whether a Review is a distinct artifact type or a
structured ADR is unresolved — `ISSUE-0067`.

## Principle, Policy, Engineering Process

```text
ADR establishes Principle → motivates Policy → governs Engineering Process
    → produces Artifacts
```

**Principle** — a **semantic relationship that emerges from accepted
architectural knowledge**. **Not an artifact** (`ADR-0058`). Principles belong
to the semantic model, not the document taxonomy: they are first-class semantic
entities in the metamodel, **extracted by the Knowledge Compiler** from
authoritative artifacts and navigable **independently of the documents that
established them**. One principle may emerge from several ADRs.

**Policy** — a normative engineering rule motivated by one or more Principles.

**Engineering Process** — an operational procedure implementing a Policy.
Dimension Review, Acceptance Review, the Metamodel Position Gate. Distinguished
from a **Business Process**, which belongs to an adopting repository's domain.
A **Workflow Execution** is the act of running one.

This explains why ADRs, Policies and Gates exist without overlapping: ADRs
record how content came to be, Policies hold rules, Gates are Engineering
Processes.

## Naming Qualification

> **Whenever a concept belongs to a specific architectural dimension, its
> published name includes that dimension whenever ambiguity is possible**
> (`ADR-0057`).

Not a renaming strategy — a **semantic qualification** strategy. The short name
may be used informally where context is unambiguous; **the qualified name is
canonical**.

Canonical names: Abstraction Level · Semantic Layer · Engineering Process ·
Business Process · Engineering Gate · Workflow Execution · Artifact Revision
Lifecycle · State Machine Lifecycle · Compiler Phase · Knowledge Representation.

This closed a class of defect the project had hit **eight times**.

## Authored versus discovered knowledge

**Authored knowledge** — explicitly written: ADRs, Policies, Specifications.

**Discovered knowledge** — found by the compiler: Principles, traceability,
dependency graphs, architectural patterns, impact graphs, semantic clusters.

> **Engineering OS maximizes discovered knowledge.** The compiler's higher
> purpose is revealing architectural knowledge that exists implicitly across
> many authoritative artifacts but was never written as a single document
> (`ADR-0059`).

How discovery is produced — declared or inferred — and whether it can be
deterministic is unresolved: `ISSUE-0071`.

## Semantic architecture versus compiler architecture

> **The metamodel defines what exists. The compiler defines how it is
> transformed. Neither embeds concepts belonging to the other** (`ADR-0053`).

Every new concept first answers: **is this a semantic concept, a compilation
concept, or both?** Only concepts genuinely belonging to both appear in both
architectures, and their correspondence is **explicit rather than implicit**.

## The three representations of knowledge

**Semantic Representation** — the canonical graph.

**Authoring Representation** — the human-editable source artifacts.

**Presentation Representation** — generated views: Knowledge Explorer,
documentation, search indexes, registry projections.

> **The compiler is responsible for maintaining semantic equivalence across
> these.** They are different views of the same knowledge, **not different
> knowledge** (`ADR-0047`). This is how Engineering OS optimizes simultaneously
> for human authoring, machine reasoning and generated documentation without
> duplicating semantics.

Whether Representation is an independent dimension or a grouping of Semantic
Layers is unresolved — `ISSUE-0064`.

> **The term was redefined.** Under `ADR-0010`, "Layer A" meant the methodology
> and "Layer B" the knowledge model. `ADR-0037` redefines Layer A as the
> Metamodel. The former Layer A content — `shared/`, `skills/`, `workflows/`,
> `templates/`, `schemas/`, `governance/` — currently has **no layer**
> (`ISSUE-0056`).

**`model-spec/`** — the Layer A specification and copyable scaffold *of* a Layer
B tree. Ships to adopters.

**`model/`** — a repository's own tree. For adopters it is Layer B; for
Engineering OS it also holds `metamodel/`, because this repository's domain is
the metamodel.

**Target repository** — the software system Engineering OS is applied to. May be
this repository, when the methodology is applied to itself.

**Knowledge ownership** — knowledge is owned by the repository that owns the
domain. There is no shared central model. See `ADR-0010`.

**Federation** — how multi-repository environments exchange knowledge without
sharing a model: by exporting and referencing Knowledge Packages.

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
