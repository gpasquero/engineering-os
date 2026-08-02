---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: discovery-two-stage
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**Two-stage Discovery** (`ADR-0108`), with **assertion origin recorded**
(`ADR-0109`).

## A conclusion was refuted

`SESSION-0039` claimed a **deterministic ceiling**: *better than a human at
coverage, worse at abstraction.*

**It measured one rule.** The abstraction was already in the repository:

```text
describe('account lockout & brute-force protection')
```

| Human's invariant | `R1` case-level | `R3` suite-level |
|---|---|---|
| account lockout | no | **YES** |
| tenant isolation | yes | **YES** |
| refresh token rotation | no | **YES** |
| JWT security | no | **YES** |

**Four of four, with no language model.** Including the one `SESSION-0039`
reported as *"missed entirely"* — missed because `R1` read `it()` names and the
concept was in a `describe` block.

## The measurement is only possible because of the split

```sh
python3 discovery/run.py /Users/willy/Localsources/ai-desk external/ai-desk-onboarding \
    --strategy=suite-level
```

| Stage | Reads | Produces |
|---|---|---|
| **Mechanical** | source files | Mechanical Engineering Model, digest `dd47744e6bc66150` |
| **Interpretive** | **only the Mechanical Model** | proposed engineering knowledge |

**Interpreters never open a file.** That constraint is what makes two
interpreters comparable and what separates a missing fact from a bad abstraction.

| Interpreter, same input | entities | invariants |
|---|---|---|
| case-level `R1` | 271 | 99 |
| **suite-level `R3`** | **203** | **31** |

## What exists

| Area | State |
|---|---|
| **`discovery/mechanical.py`** | Facts only: 4 packages · 61 deps · 28 modules · 161 routes · 34 tables · 70 suites with `describe` blocks · 27 env refs · 62 documents |
| **`discovery/interpretive.py`** | 6 named rules, **two comparable invariant strategies**. Reads no file |
| `discovery/candidate.py` | Candidate model with content digest and origin statistics |
| `compiler/apply/` · `tools/review.py` | Authorization and application as authoring sources |
| **`model/assertion-origins.md`** | 4 origin kinds. **394 of 394 assertions reproducible** |
| `model/support-classification.md` | 8 kinds — 3 batch, 3 individual, 1 gap-only |
| `compiler/emitters/` | json · owl · mermaid · explorer · **shacl** · **indexes** |
| `external/ai-desk-onboarding/` | Mechanical model · candidate model · 16 authored sources · CKM · 6 products |
| `tests/` | 17 fixtures, 9 negative, golden for 6 emitters |
| Registries | **16** |
| `model/metamodel/` | 23 of 27 entities — **unchanged for nine milestones** |

## The plan improved, and in the right way

```text
Invariant.AccountLockoutBruteForceProtection
Invariant.JwtSecurity
Invariant.PasswordPolicyRegisterdto
Invariant.RefreshTokenRotation
```

**Concepts, not transcriptions** — and derived rather than authored.

## What is unreached, not unreachable

| Gap | Why |
|---|---|
| **prose invariants** | No rule reads document prose. A guarantee stated only in an ADR and asserted by no test is invisible |
| both levels at once | `R3` reaches the concept, `R1` the specific guarantee. **Neither dominates**, and a rule proposing both is the obvious next deterministic step |
| workflows · runtime behaviour | No rule and no observation |

## The argument for a probabilistic interpreter is now weaker

`SESSION-0039` called it evidential. **It was not** — the evidence supported *a
better rule*, and a better rule delivered it.

The case must be made **against `R3`, over the same Mechanical Model**. That is a
harder bar than the one this project set for itself, and `ADR-0108` exists to
enforce it.

## Blocking

**Nothing.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. Sixteen registries, zero generated |

## Debt discovered while building

| Question | Where |
|---|---|
| **The Mechanical Model's vocabulary is itself a ceiling** — a fact nobody extracted is invisible to every interpreter | `ADR-0108` |
| Origin is self-reported; nothing verifies it. **Re-running is the check and nothing runs it** | `assertion-origins.md` |
| Four origin kinds will prove insufficient; hybrids have no entry | `ADR-0109` |
| `R3` loses detail `R1` keeps; the combination is unbuilt | `ai-desk-onboarding/FINDINGS.md` |

## Next action

**A rule that proposes both levels** — the concept, with its cases as
constituent assertions. Then a rule that reads prose. **Then, if still justified,
a probabilistic interpreter** — measured against `R3`.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
