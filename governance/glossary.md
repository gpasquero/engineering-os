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

**Policy** — normative prose that constrains how work is done, stored once in
`shared/policies/` and referenced by path. Never inlined into a skill.

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
artifacts are produced. Not a documentation generator. See `ADR-0011`.

**Canonical knowledge model** — the internal representation produced by
compilation, and the primary product of the pipeline. Every consumer reads this;
none parses authoritative assets directly. Its relationship to `model/` is
unresolved — `ISSUE-0034`.

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

**Determinism** — the requirement that a pipeline produce identical outputs from
identical authoritative inputs. Applies to compilation, not to agent-executed
engineering work; the boundary is unresolved — `ISSUE-0033`.

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

**Knowledge Package** — a versioned export of a repository's ontology, graph,
glossary, specifications and metadata, letting another repository reference it
without access to its internal source of truth. Format undefined —
`ISSUE-0029`.

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
