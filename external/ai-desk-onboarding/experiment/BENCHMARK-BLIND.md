---
id: EXPERIMENT-BLIND-BENCHMARK
title: The blind benchmark — final interpreter comparison
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0108, ADR-0109, ADR-0110, ADR-0113]
---

# The blind benchmark

**The final interpreter comparison.** Its purpose was to validate the
experimental method and the Discovery Skill contract — **not to search for a
universal winner.**

## The run was genuinely blind

| Condition | How |
|---|---|
| same frozen Mechanical Model | `INPUT-mechanical-model.json`, digest `dd47744e6bc66150` |
| fresh worker context | a separate agent with no access to this conversation |
| no prior interpreter output | forbidden by instruction; `R1`/`R3`/`R4` results, `FINDINGS`, `BENCHMARK` and the candidate model all named as off-limits |
| no benchmark conclusions | same |
| explicit Skill contract | `DS-architecture-discovery` and `DS-invariant-discovery`, verbatim from `discovery/skills/skills.yaml` |
| structured output | a declared YAML schema |
| provenance and uncertainty | required per proposal; `population-compared` **mandatory** for any distribution claim |

**This is the condition `SESSION-0041` could not meet**, and every conclusion
there was weaker for it.

## The measurement

```sh
python3 tools/compare-interpreters.py external/ai-desk-onboarding
```

| interpreter | props | invar | concept | guaran | distrib | gaps | reproducible |
|---|---|---|---|---|---|---|---|
| case-level `R1` | 271 | 99 | 0 | 0 | 0 | 9 | exactly |
| suite-level `R3` | 203 | 31 | 0 | 0 | 0 | 9 | exactly |
| **both-levels `R4`** | **302** | **130** | **31** | **99** | 0 | 9 | **exactly** |
| claude (contaminated) | 4 | 2 | 0 | 0 | 2 | 0 | no |
| **claude (blind)** | **20** | 13 | 0 | 0 | **11** | **7** | no |

**The blind run produced five times the proposals and five times the
distribution-level claims of the contaminated one** — 11 of its 20 carrying an
explicit `population-compared` field naming the population and its size. The contaminated worker had
constrained itself to avoid ground the deterministic rules had covered; the blind
worker, given a contract and no such knowledge, investigated the whole model.

**That is the finding about method**: contamination did not inflate the earlier
result, it suppressed it.

## Complementarity is total, not partial

**13 of 13 blind invariants have no deterministic counterpart.** Nearest word
overlap with any of `R4`'s 130 never exceeds 0.31.

They are different *kinds* of statement:

| `R4` (deterministic) | blind (probabilistic) |
|---|---|
| `LocksTheAccountOnThe5ThWrongPassword` | `RepeatedFailedLoginsLockTheAccountWithoutRevealingWhichCredentialWasWrong` |
| `RejectsA7CharPasswordBelowMinimum` | `SecretsAreNeverRecoverableFromStorage` |
| — | `NoDataCrossesATenantBoundary` |
| — | `SoftDeletedRecordsAreInvisibleToEveryReadPath` |

`R4` transcribes what a test asserts. The blind worker states **what must be true
of the system**, synthesized across tables, routes and suites at once.

**Neither is a better version of the other.** `R4` is exhaustive over tests and
blind to everything else; the blind worker is selective and reaches statements no
test names.

## The blind worker audited its own input

Four of its seven gaps are about the **Mechanical Model**, not the repository —
`F-fact-absent` reported by the interpreter, unprompted:

**A contradiction it could not resolve.** *The schema suite asserts "exports
exactly 20 tables" while the mechanical model lists 34.* Either the barrel export
is stale or the assertion is. **Neither the repository nor any deterministic rule
states this**; it required comparing a test's claim against an extracted count.

**An extraction artefact.** `csat_surveys` and `csat_responses` carry
byte-identical column sets — *"almost certainly a mechanical extraction artefact:
two table declarations in one file, with the extractor attributing every column
in the file to both."* **That is a real defect in `discovery/mechanical.py`**,
found by a worker reading only its output.

**Under-extraction.** `JWT_ACCESS_SECRET` is referenced only from a test file, so
*"production code almost certainly reads these through a config layer the
extractor did not follow."*

**A whole boundary invisible.** The frontend and widget contribute zero suites,
zero routes and zero tables — *"roughly a third of the file count of the
repository is invisible to every invariant proposed here."*

> **This is the two-stage split paying off in the direction nobody designed it
> for.** `ADR-0110` said classify a failure before calling it one; the blind
> worker classified four of its own.

## What it confirmed independently

**All five ADRs carry status `Proposed`** while the code implements them — found
independently by the deterministic rules, the contaminated worker and now the
blind worker. **Three interpreters, three methods, one finding.**

## Six contract defects, reported by the worker executing the contract

**This is what the run existed to surface** (`ADR-0113`), and the worker found
more than the author had.

| # | Defect | Fixed |
|---|---|---|
| 1 | **The output schema has no field for `specializes`**, yet `DS-invariant-discovery`'s provenance clause mandates it. The worker added the key anyway and flagged the contradiction | ✅ schema renamed |
| 2 | **`proposal-types` is silently violable.** A proposal was initially typed `Capability` under a skill permitting only `Invariant`; the worker caught it on self-check and nothing in the contract would have | ✅ `check-skills.py` now validates the declared types; enforcing worker output remains open |
| 3 | **Stopping conditions and count guidance are in tension.** *Every module placed and every route family characterised* forced 28 modules and 26 families; the requested 8–15 was impossible | ✅ per-skill `proposal-count` added; **the tension is real and is now visible rather than resolved** |
| 4 | **"Placed" and "characterised" are undefined**, so a one-line list satisfies the same words. **Not comparable across runs** | ✅ both given tests |
| 5 | **`DS-architecture-discovery` asks which boundaries are enforced and names no evidence that can answer it.** The Mechanical Model carries no guard, decorator or authorisation metadata | ✅ the question now instructs reporting a gap rather than inferring |
| 6 | **The `csat` extraction artefact** — see below | ✅ extractor fixed |

**Two of six were unfixable by editing the contract**: type enforcement needs a
validator on worker *output*, and the count/stopping tension is a genuine design
conflict now stated rather than hidden.

## The extractor bug, found by reading only its output

> *"the extractor appears to attribute every column in a file to every table
> declared in it"*

**Correct.** `csat-surveys.ts` declares two tables; the extractor reported both
with the same fifteen columns. Fixed by slicing each declaration's body:

```text
csat_surveys    10 columns    csat_responses    8 columns
```

**A blind worker, reading a 137 KB JSON file and nothing else, found a defect in
the extractor that produced it.** The Mechanical Model vocabulary version moved
to `1.1.0` and the digest changed — which is the versioned contract behaving as
`ADR-0110` requires.

## Conclusion, and the stopping point

**The method works and the contract is usable.** Blindness materially changed the
result, so the experimental design matters and is now validated.

**Interpreter experimentation stops here.** The question — *do different worker
classes contribute different forms of knowledge?* — is answered: **13 of 13, zero
overlap.**

Further comparison would refine a number nobody is waiting on. **The next
bottleneck is the acquisition lifecycle**, not the interpreter.
