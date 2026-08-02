---
id: EXTERNAL-AIDESK-ONBOARDING-FINDINGS
title: Findings — two-stage Discovery, and a refuted conclusion
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0090, ADR-0105, ADR-0106, ADR-0107, ADR-0108, ADR-0109]
---

# Findings — two-stage Discovery

```sh
python3 discovery/run.py /Users/willy/Localsources/ai-desk external/ai-desk-onboarding \
    --strategy=suite-level
```

## The conclusion this session refutes

`SESSION-0039` concluded:

> *Deterministic extraction is better than a human at coverage and worse at
> abstraction. That is the deterministic ceiling.*

**That was wrong.** It measured the limit of one rule, not the limit of
determinism.

The abstraction the human produced was **already in the repository**:

```text
describe('account lockout & brute-force protection')
  it('locks the account on the 5th wrong password for exactly 15 minutes')
  it('per-agent isolation: locking agent A does not affect agent B')
  ...
```

Rule `R1` read `it()` names and proposed eight invariants. **Rule `R3` reads the
`describe` block and proposes one — the same one the human wrote.**

## The measurement, over identical input

One Mechanical Engineering Model, digest `dd47744e6bc66150`. Two interpreters.
**Neither is probabilistic.**

| | case-level (`R1`) | suite-level (`R3`) |
|---|---|---|
| entities | 271 | **203** |
| invariants | 99 | **31** |
| auth invariants | 19 | **5** |

### Did the deterministic rule recover what a human wrote?

| Human's invariant | `R1` case-level | `R3` suite-level |
|---|---|---|
| account lockout | no | **YES** |
| tenant isolation | yes | **YES** |
| refresh token rotation | no | **YES** |
| JWT security | no | **YES** |

**Four of four**, with no language model.

`R3` proposes `RLS tenant isolation (integration)` — the invariant `SESSION-0039`
reported as *"missed entirely"* and attributed to a limit of determinism. It was
missed because `R1` looked at `it()` names and the concept was in a `describe`
block.

## What the two-stage split made possible

The comparison above is only meaningful because **both interpreters read exactly
the same input** (`ADR-0108`).

| | Stage |
|---|---|
| **Mechanical Engineering Model** | facts: 4 packages, 61 dependencies, 28 module directories, 161 routes, 34 tables, 70 test suites with their `describe` blocks and cases, 27 environment references, 62 documents |
| **Interpretive Discovery** | reads **only** that model; opens no file |

Before the split, a bad abstraction and a missing fact were the same failure.
**Now they have different owners**: `R1`'s failure was interpretation — the fact
it needed was extracted and it did not use it.

## Origin recording

Every proposal records **what kind of process produced it** (`ADR-0109`):

```text
[origin]  {'O-deterministic-rule': 394}
```

**394 of 394 assertions are exactly reproducible.** When a probabilistic
interpreter is added, that number will fall, and the fall will be visible and
attributable — which is the point.

Reported as **counts by kind, never a score** (`ADR-0090`). A model that is 100%
deterministic is not better than one that is 60%; it is differently composed.

## The applied slice

**16 entities authorized** from 203, compiled to an 18-node CKM. The plan for
*"add OAuth"* now surfaces:

```text
Invariant.AccountLockoutBruteForceProtection
Invariant.JwtSecurity
Invariant.PasswordPolicyRegisterdto
Invariant.RefreshTokenRotation
```

**Concepts, not transcriptions** — and derived, not authored.

## What is still genuinely unreachable

**Not proven unreachable — unreached, and recorded as such.**

| Gap | Why |
|---|---|
| **prose invariants** | No rule reads document prose. A guarantee stated only in an ADR and asserted by no test is invisible. `Invariant.NoUserEnumeration` — from *"wrong password and wrong email return the same error"* — survives at case level and is absorbed at suite level |
| workflows | No rule proposes them from the mechanical model |
| runtime behaviour | The mechanical model contains no runtime observation |

**The suite-level rule loses detail the case-level rule keeps.** Neither
dominates: `R3` reaches the concept, `R1` reaches the specific guarantee. **A
third rule proposing both — the concept, with its cases as constituent
assertions — is the obvious next deterministic step**, and it is not built,
because this session's purpose was to measure, not to keep optimising.

## What this changes about the argument for a probabilistic interpreter

**It weakens it, honestly.**

`SESSION-0039` argued the case was evidential. It was not: the evidence
supported *a better rule*, and a better rule delivered it.

**The case must now be made against `R3`, over the same mechanical model, and
measured the same way.** That is exactly the comparison `ADR-0108` was written to
make possible — and it is a harder bar than the one this project set for itself
yesterday.
