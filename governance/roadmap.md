---
id: ROADMAP
title: Roadmap
status: accepted
created: 2026-08-02
updated: 2026-08-02
supersedes: sources/handoff/ROADMAP.md (pre-M1, ten "Deliveries")
related: [ADR-0009, ADR-0010]
---

# Roadmap

Milestones are sequential. Each ends with an updated build state and a session
log. Nothing is generated in one pass.

A milestone must not start while an issue marked `blocking` names it in
`blocks`. Check `governance/issues/index.md` first.

## M1 — Repository architecture and documentation system

**Complete.** Define how this project remembers.

Repository architecture and the two-layer rule; documentation system; session
protocol; governance skeleton; ADRs for decisions made; all known open questions
recorded as issues. No skills, policies or contracts.

## M2 — Foundational contracts, manifests and the compiler interface

**Unblocked.** `ISSUE-0038`, `ISSUE-0039`, `ISSUE-0040` and `ISSUE-0041` are
resolved by `ADR-0020` through `ADR-0023`, and the trust root `ACCEPT-0001`
exists.

**Unblocked.** `ISSUE-0053` is resolved by `ADR-0032`: a Registry Specification
is authoritative and a Registry Projection is derived, so each manifest gets one
artifact kind.

`ISSUE-0049` gates the state machine specifications and `shared/vocabularies/`;
`ISSUE-0054` gates anything depending on the metamodel. The compiler interface
specification, `model-spec/`, the manifests and the remaining contracts can
proceed.

**Registry Pattern evaluation** (`ADR-0031`): every extensible concept —
skills, workflows, state machines, policies, contracts, vocabularies, ontology
modules, capabilities, invariants, Knowledge Packages — is assessed for
Registry + Specification modeling before being modeled another way.

- **Compiler interface specification** (`ADR-0017`) — language-independent, and
  the substitute for shipping executable tooling in this milestone
- The three manifests: `MANIFEST.yaml`, `BUILD-STATE.yaml`,
  `KNOWLEDGE-MANIFEST.yaml` (`ADR-0013`), with `BUILD-STATE.yaml` marked as a
  hand-maintained projection under `ISSUE-0037`
- `model-spec/` — the authoritative source tree specification and scaffold
  (`ADR-0014`)
- Skill contract and workflow contract, including write-scope declaration
- Evidence record, conflict record, traceability record contracts
- **Acceptance Record contract** (`ADR-0021`, `ISSUE-0042`)
- **State Machine Registry** — a **Registry Specification** (authoritative) plus
  its **Registry Projection** (derived), the latter indexed from a section of
  `KNOWLEDGE-MANIFEST.yaml` (`ADR-0028`, `ADR-0032`). Machine specifications are
  separate artifacts.
  Includes defining the shape of three fields that do not yet have one:
  transition rules, related ontology concepts, authoritative specification.
- `shared/vocabularies/` — **grouped by state machine** (`ADR-0025`), never as
  one global list. Covers assertion statuses, confidence, risk, gate decisions,
  change types, **artifact kinds** (`ADR-0012`) and
  **`ArtifactRevisionLifecycle`** (`ADR-0020`, `ADR-0026`)
- One canonical impact-analysis template

**No executable tooling.** `ADR-0017` defers the implementation language, so
manifest validation and index generation move to M9.

Must be resolved within this milestone: `ISSUE-0007`, `ISSUE-0011` (the licence
gap), `ISSUE-0013`, `ISSUE-0014`, `ISSUE-0015`, `ISSUE-0018`, `ISSUE-0019`,
`ISSUE-0031`.

Design constraints: nothing built here may preclude federation (`ISSUE-0029`);
every artifact declares its kind (`ADR-0012`); every authoritative artifact
must be readable and editable without the compiler (`ADR-0017`).

## M3 — Shared policies

**Unblocked.** `ISSUE-0051` is resolved by `ADR-0033`: a ProcessPolicy governs a
Workflow, and the two are independent artifact types.

Three normative artifact kinds (`ADR-0030`):

- **`ModelingPolicy`** — the rules already decided: artifact taxonomy, lifecycle
  ownership, state machine registration, naming conventions, traceability
  requirements. Source material spans `ADR-0012`, `ADR-0020`, `ADR-0025`,
  `ADR-0026`, `ADR-0027`, `ADR-0028` and `ADR-0031`.
- **`GovernancePolicy`** — acceptance, review and release governance. The first
  is accepted under the trust root `ACCEPT-0001` and thereafter governs its own
  successor (`ADR-0023`).
- **`ProcessPolicy`** — normative execution rules. Referenced *by* workflows,
  never embedding execution steps (`ADR-0033`). M8 depends on these existing
  first, or workflows will be written with rules inlined.

The inherited policy list — evidence, research, ontology, constraint-placement,
write-scope, autonomy and escalation, secrets and privacy, traceability,
verification, knowledge-update — must be **reclassified** across these three
kinds. Several entries are genuinely ambiguous and the classification is real
work, not a formality.

Agents primarily consume policies rather than ADRs (`ADR-0029`), so M4 skills
depend on this milestone more directly than on the decision corpus.

## M4 — Discovery skills

`understand-request`, `research-domain`, `reconstruct-domain`

## M5 — Impact and design skills

`model-ontology`, `analyze-impact`, `design-change`, `plan-implementation`

## M6 — Architecture review skills

`review-architecture`, `challenge-design`

## M7 — Implementation and verification skills

`implement-change`, `verify-change`, `update-knowledge`

## M8 — Workflows

`feature`, `bug`, `behavior-change`, `refactoring`, `integration`,
`architecture-evolution`

Blocked by `ISSUE-0002`. Depends on `ISSUE-0016`, and on the M3 ProcessPolicies
that each workflow references (`ADR-0033`).

## M9 — Schemas, validation and the reference implementation

Schemas for the manifests, skills, workflows and records; validation rules; and
the **first executable tooling**, deferred here from M2 by `ADR-0017`.

Requires `ISSUE-0036` (reference implementation language) to be un-deferred.
Clears the projection debt registered in `ISSUE-0037`.

## M10 — Scenario tests

Blocked by `ISSUE-0006`.

## M11 — Engineering OS self-model

Apply Engineering OS to itself: build this repository's own `model/` describing
the framework (`ADR-0010`).

This precedes the v1 release deliberately. If the methodology cannot produce a
coherent knowledge model of itself, it does not work, and that must be
discovered before release rather than after. Scope is open — `ISSUE-0031`,
which includes the unresolved question of whether `governance/` overlaps
`model/`.

## M12 — Documentation, adapters and v1 release

User guides, `adapters/`, licence, changelog, and the **Knowledge Explorer** — a
per-repository projection of the Canonical Knowledge Model that every adopting
repository generates over its own domain (`ADR-0034`). Depends on `ISSUE-0001`
and `ISSUE-0011`.

## M13 — Knowledge Packages and federation

The **published package specification** — versioned, and independent of any
compiler implementation (`ADR-0019`) — plus the exchange protocol that lets
repositories reference one another without sharing their source of truth.

Conformance to the specification is what makes `ADR-0017`'s
multiple-implementations promise testable.

## Mapping from the inherited roadmap

The pre-M1 `sources/handoff/ROADMAP.md` numbered ten "Deliveries". They are
preserved here as milestones, offset by one because M1 did not previously exist.

| Inherited | Now |
|---|---|
| Delivery 1 — Blueprint, MANIFEST, shared contracts | M2 |
| Delivery 2 — Shared policies | M3 |
| Delivery 3 — Discovery skills | M4 |
| Delivery 4 — Impact & design | M5 |
| Delivery 5 — Architecture review | M6 |
| Delivery 6 — Implementation & verification | M7 |
| Delivery 7 — Workflows | M8 |
| Delivery 8 — Schemas | M9 |
| Delivery 9 — Scenario tests | M10 |
| Delivery 10 — Documentation and v1 release | M12 |

M11 and M13 are new, added when `ADR-0010` established repository-local
knowledge ownership and federation. The former Delivery 10 moved from M11 to
M12 so that the self-model precedes the release.

The term "Delivery" is deprecated. See `governance/glossary.md`.
