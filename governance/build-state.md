---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: discovery-skills
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**Discovery Skills** (`ADR-0113`) — engine-independent investigation contracts.
**The Skill belongs to Engineering OS; the model is only a worker
implementation.**

## The blind benchmark — the final interpreter comparison

A separate agent with **no access to this conversation**, given the frozen
Mechanical Model and two Skill contracts, forbidden every prior interpreter
output.

| interpreter | props | invar | distrib | gaps | reproducible |
|---|---|---|---|---|---|
| case-level `R1` | 271 | 99 | 0 | 9 | exactly |
| suite-level `R3` | 203 | 31 | 0 | 9 | exactly |
| **both-levels `R4`** | **302** | **130** | 0 | 9 | **exactly** |
| claude (contaminated) | 4 | 2 | 2 | 0 | no |
| **claude (blind)** | **20** | 13 | **11** | **7** | no |

**Contamination suppressed the earlier result rather than inflating it.** The
contaminated worker avoided ground the rules had covered; the blind one, given a
contract and no such knowledge, investigated the whole model.

**13 of 13 blind invariants have no deterministic counterpart** — nearest word
overlap never exceeds 0.31. They are different kinds of statement:
`RejectsA7CharPasswordBelowMinimum` against
`SecretsAreNeverRecoverableFromStorage`.

## The blind worker audited its own input

Four of its seven gaps concern the **Mechanical Model**, not the repository —
`F-fact-absent` reported unprompted by the interpreter.

**It found a real bug in the extractor**, reading only a 137 KB JSON file:
*"the extractor appears to attribute every column in a file to every table
declared in it."* Correct — `csat_surveys` and `csat_responses` both carried the
same 15 columns. **Fixed**; they now carry 10 and 8. Vocabulary version `1.1.0`.

It also found an unresolved contradiction: *the schema suite asserts "exports
exactly 20 tables" while the model lists 34.* **Neither the repository nor any
deterministic rule states this.**

## Six contract defects, found by the worker executing the contract

| Defect | State |
|---|---|
| The output schema has no `specializes` field, yet the contract mandates it | ✅ fixed |
| `proposal-types` is silently violable | ✅ declared types now validated; **enforcing worker output remains open** |
| Stopping conditions and count guidance are in tension | ✅ bounds added; **the tension is real and now visible rather than resolved** |
| "Placed" and "characterised" are undefined — not comparable across runs | ✅ both given tests |
| A question is asked that no permitted evidence can answer | ✅ now instructs reporting a gap |
| The `csat` extraction artefact | ✅ extractor fixed |

**The worker found more contract defects than the author had.**

## What exists

| Area | State |
|---|---|
| **`discovery/skills/skills.yaml`** | **9 skills**, 11 required fields, **no model or vendor named** |
| **`tools/check-skills.py`** | Validates completeness, vendor-neutrality, independent runnability, declared types |
| **`tools/compare-interpreters.py`** | **Refuses to compare interpreters that saw different Mechanical Models** — and refused on its first run |
| `discovery/mechanical.py` | Facts only, vocabulary `1.1.0`, reproducible |
| `discovery/interpretive.py` | 6 named rules, 3 comparable strategies |
| `external/…/experiment/blind/` | Frozen input, blind output, `BENCHMARK-BLIND.md` |
| Registries | **19** |
| `model/metamodel/` | 23 of 27 entities — **unchanged for eleven milestones** |

## Interpreter experimentation stops here

The question — *do different worker classes contribute different forms of
knowledge?* — is answered: **13 of 13, zero overlap.** Further comparison would
refine a number nobody is waiting on.

## What does not exist

**Continuous Acquisition and Periodic Reacquisition.** Two of three modes
declared and unbuilt; **the Knowledge Drift Report cannot be meaningful until at
least one incremental update has happened.**

**Worker-output validation.** A skill declares `proposal-types` and nothing
checks that a worker honoured it — the worker caught its own violation on
self-check.

**The navigable knowledge product** from a broad authorized model.

## Blocking

**Nothing.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. Nineteen registries, zero generated |

## Debt discovered while building

| Question | Where |
|---|---|
| **Nothing verifies a worker honoured its contract**; only the output shape is checkable | `ADR-0113` |
| Exhaustive stopping conditions and bounded proposal counts genuinely conflict | `BENCHMARK-BLIND.md` |
| Engine independence is asserted and untested until a second engine runs a Skill | `ADR-0113` |
| The frontend and widget contribute nothing to the Mechanical Model — a third of the repository is invisible | blind gap report |
| `schema.spec.ts` claims 20 tables, the model lists 34, and the model cannot distinguish drift from a stale assertion | blind gap report |

## Next action

**The acquisition lifecycle**, not another interpreter. Initial → authorize a
substantial model → compile and generate the navigable product → run the Director
→ one bounded change → Continuous Acquisition → Periodic Reacquisition → the
first Knowledge Drift Report.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
