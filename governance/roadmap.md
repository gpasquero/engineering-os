---
id: ROADMAP
title: Roadmap
status: accepted
created: 2026-08-02
updated: 2026-08-02
supersedes: sources/handoff/ROADMAP.md (pre-M1, ten "Deliveries")
---

# Roadmap

Milestones are sequential. Each ends with an updated build state and a session
log. Nothing is generated in one pass.

A milestone must not start while an issue marked `blocking` names it in
`blocks`. Check `governance/issues/index.md` first.

## M1 — Repository architecture and documentation system

**Status: in progress.** Define how this project remembers.

- Repository architecture and the two-layer rule
- Documentation system: document types, IDs, front matter, lifecycle
- Session protocol
- Governance skeleton: vision, principles, glossary, roadmap, build state
- ADRs for decisions made
- All known open questions and inconsistencies recorded as issues

No skills, policies or contracts. Explicitly out of scope.

## M2 — Foundational contracts and manifest

**Blocked by `ISSUE-0003` and `ISSUE-0004`.** `ISSUE-0007`, `ISSUE-0013`,
`ISSUE-0014`, `ISSUE-0015`, `ISSUE-0018` and `ISSUE-0019` must be resolved
within it. `ADR-0007` removed `ISSUE-0001` as a blocker by fixing the
runtime-neutral boundary.

- `MANIFEST.yaml` and its meaning
- Skill contract and workflow contract
- Evidence record, conflict record, traceability record contracts
- `shared/vocabularies/` — single-source assertion statuses, confidence, risk,
  gate decisions, change types
- `model-spec/` — the Layer B tree specification and scaffold
- One canonical impact-analysis template

## M3 — Shared policies

- Evidence, research, ontology, constraint-placement, write-scope,
  autonomy and escalation, secrets and privacy, traceability, verification,
  knowledge-update policies

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

Depends on `ISSUE-0016` (three conflicting change-type taxonomies).

## M9 — Schemas and validation

JSON Schema for manifest, skills, workflows and records; validation rules;
issue-index generator (`ISSUE-0028`).

## M10 — Scenario tests

Depends on `ISSUE-0006` — how a prompt-based methodology is tested is unsolved.

## M11 — Documentation, adapters and v1

User guides, `adapters/`, licence, changelog. Depends on `ISSUE-0001` and
`ISSUE-0011`.

## Mapping from the inherited roadmap

The pre-M1 `sources/handoff/ROADMAP.md` numbered ten "Deliveries". They are preserved here as
milestones, offset by one because M1 did not previously exist.

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
| Delivery 10 — Documentation and v1 release | M11 |

The term "Delivery" is deprecated. See `governance/glossary.md`.
