---
id: ADR-0005
title: imports/ and sources/ are frozen provenance and are never edited
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0001]
---

# ADR-0005 — `imports/` and `sources/` are frozen provenance

## Context

The repository was seeded with three prototype skills
(`reconstruct-system-knowledge`, `ontology-driven-development`,
`principal-engineering`) and two source documents (`requirements.md`,
`conversation-summary.md`). `sources/handoff/HANDOFF.md` states the prototypes are to be
treated as "inputs, not final designs".

Analysis found fifteen inconsistencies inside and between these inputs — three
conflicting impact-analysis templates, three incompatible autonomy policies,
duplicated status vocabularies. The natural instinct is to correct them in
place.

Doing so would destroy evidence. Principle 9 requires current state and proposed
state to be kept separate, and Principle 5 treats every source as evidence to be
evaluated rather than truth to be maintained. An input that has been silently
corrected can no longer be evaluated, and the record of what we were actually
given is gone.

## Decision

`imports/` and `sources/` are **frozen**. They are never edited, refactored,
corrected, reformatted or deleted.

- Defects found in them are recorded as issues with the input path in
  `evidence`, never fixed in place.
- Derived work is written elsewhere — `governance/`, and later `shared/` and
  `skills/`.
- The original archives are preserved in `sources/archives/`.
- A future decision to retire an input supersedes this ADR; it does not license
  editing the input.

## Alternatives considered

**Correct inputs in place and move on.** Rejected: destroys the distinction
between what we were given and what we concluded, which is the exact epistemic
discipline this project exists to impose on other systems. It would also make
the fifteen recorded inconsistencies unverifiable.

**Delete the inputs once their content is absorbed.** Rejected: absorption is
incremental across many milestones, and provenance for the resulting contracts
would be lost. `sources/handoff/HANDOFF.md` explicitly frames them as inputs to be consulted.

**Fork each input into an `imports/` original and a `working/` editable copy.**
Rejected as premature duplication. Derived artifacts already serve this purpose
and carry proper front matter; a second parallel copy would drift against both.

## Consequences

### Positive

- Every derived contract can be traced back to the exact text it came from.
- The fifteen recorded inconsistencies remain verifiable against their source.
- The project applies its own evidence discipline to itself.

### Negative

- Known-wrong content stays in the repository indefinitely, and a careless
  reader may treat a frozen prototype as current guidance.
- Duplication between frozen inputs and derived artifacts is permanent.

### Neutral

- `sources/archives/` holds the original zip files; they are redundant with the
  extracted directories but cost little and settle any question of extraction
  fidelity.

## Compliance

`git log --stat -- imports/ sources/` shows no modifications after the initial
commit, other than additions of new frozen inputs. Any issue whose `evidence`
points into these directories must not be resolved by editing them.
