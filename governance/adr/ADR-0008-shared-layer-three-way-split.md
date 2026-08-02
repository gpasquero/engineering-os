---
id: ADR-0008
title: Split shared/ into contracts, policies and vocabularies
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0024]
related: [ADR-0006]
---

# ADR-0008 — Split `shared/` into contracts, policies and vocabularies

## Context

`governance/design/proposed-architecture.md` lists `shared/` as a single undifferentiated
directory. The inherited roadmap's first delivery requires "MANIFEST.yaml" and
"shared contracts", and the second requires "shared policies" — two different
kinds of content with no distinct home (`ISSUE-0024`).

The inherited prototypes show why the distinction matters. The twelve assertion
statuses are defined twice — once with definitions in
`imports/reconstruct-system-knowledge/SKILL.md`, once without in
`references/evidence-model.md` — and the two "minimum evidence records" in
`references/evidence-model.md` and `templates/evidence-record.yaml` disagree on
their defaults. This is exactly the duplication that `sources/handoff/DECISIONS.md` promised to
eliminate with "shared policies instead of duplicated prompt text", inside the
very artifacts that promised it.

The failure has three distinct shapes, and they need three distinct treatments.

## Decision

`shared/` is split three ways, by normativity and failure mode.

**`shared/contracts/`** — machine-checkable interface definitions: record
shapes, skill and workflow I/O signatures. A violation is mechanically
detectable. Validated by `schemas/` from M9.

**`shared/policies/`** — normative prose constraining how work is done. Stored
once and **referenced by path**. Inlining policy text into a skill is
forbidden; it is the duplication this architecture exists to prevent.

**`shared/vocabularies/`** — closed enumerations with exactly one definition
each: assertion statuses, confidence levels, risk levels, gate decisions, change
types. Any document using a term from a vocabulary references it rather than
restating it.

## Alternatives considered

**One flat `shared/` directory.** Rejected: it is what the inherited design
proposed, and it provides no place to express that a vocabulary is closed while
a policy is prose, or that a contract is machine-checkable while a policy is
not.

**Two-way split (contracts and policies), with vocabularies inside contracts.**
Rejected: a vocabulary's failure mode is *restatement with drift*, not
*structural violation*. Keeping vocabularies separate and small makes them
cheap to reference and obvious to audit, which is the whole remedy for
`ISSUE-0018`.

**Vocabularies as data files only, with no prose.** Deferred rather than
rejected. The serialization format for vocabularies is an M2 question; this ADR
fixes the location and the single-source rule, not the file format.

## Consequences

### Positive

- Each of the three duplication failures observed in the prototypes has a
  specific structural remedy.
- Machine-checkable content is separated from prose, so M9 validation has a
  clear target.
- "Reference, do not inline" becomes an enforceable rule with a path to point
  at.

### Negative

- Three directories to navigate instead of one, and borderline content will
  provoke placement arguments.
- Heavy cross-referencing makes individual skill documents less readable
  standalone — a real cost, traded for the elimination of drift.

### Neutral

- Placement disputes are resolved by asking how a violation would be detected:
  mechanically (contract), by review (policy), or by comparing two definitions
  (vocabulary).

## Compliance

No enumeration is defined in more than one file. No skill inlines the text of a
policy. Every contract has, or is scheduled to have, a schema in `schemas/`.
