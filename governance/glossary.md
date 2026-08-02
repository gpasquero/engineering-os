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

**Manifest** — the registry of skills, workflows and contracts with their
versions. Its exact content is unresolved — see `ISSUE-0003`.

## The two layers

**Layer A / the product** — this repository. The methodology itself.

**Layer B / the model** — the `model/` artifact tree the methodology produces
*inside a target repository*: ontology, glossary, bounded contexts,
specifications, traceability, impact analyses.

**`model-spec/`** — the Layer A specification and scaffold *of* the Layer B tree.
This repository contains `model-spec/` and never a live `model/`.

**Target repository** — the software system the Engineering OS is applied to.
Distinct from this repository in every case.

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
