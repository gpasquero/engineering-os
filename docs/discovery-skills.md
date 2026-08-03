# Discovery: rules, skills, and using Claude or Codex

**Purpose.** Explain the two stages of discovery, the deterministic rules that
ship with Engineering OS, and the exact contract for running a frontier model as
an Interpretive Discovery worker.

---

## The two stages, and the boundary between them

**Mechanical Discovery** (`discovery/mechanical.py`) reads source and records
*facts*: packages, dependencies, module directories, routes, table declarations,
test suites and their cases, configuration references and documents. Each fact
carries its file and its locator. It names nothing as a Concept, a Capability or
an Invariant. Re-running it reproduces the same model, and the model carries a
`digest` that proves it.

Where those facts live is **declared, not coded**: `discovery/stacks.yaml` holds
the Stack Profiles, and `discovery/mechanical.py` holds seven extraction kinds.
Two profiles exist — `S-node-nest-drizzle` and `S-java-spring-jpa`. Anything else
is refused.

**Interpretive Discovery** (`discovery/interpretive.py`) reads **only the
Mechanical Model** and proposes engineering meaning. It never opens a source
file. That boundary is what makes extraction quality and interpretation quality
separately measurable, and what makes two interpreters comparable over identical
input.

Both stages run together:

```bash
python discovery/run.py <repository> <project>
python discovery/run.py <repository> <project> --strategy=both-levels
```

---

## The deterministic rules

Every proposal records the rule that produced it, in its `rule` attribute, and
carries `origin: O-deterministic-rule`.

| Rule | What it proposes |
|---|---|
| `S1-package-is-a-context` | a workspace package becomes a `BoundedContext` |
| `S1-module-is-a-capability` | a module directory becomes a `Capability` |
| `S1-pgtable-is-a-concept` | a table declaration becomes a `Concept` |
| `S2-controller-implements-module` | a controller file with routes becomes an `Artifact` implementing its module |
| `S4-spec-validates-module` | a test suite becomes an `Artifact` validating its module |
| `S3-adr-directory-is-a-decision` | a document under `docs/adr` becomes an `ADR`; a non-accepted status is recorded as an ambiguity |

Invariants are proposed by one of three interchangeable strategies, selected with
`--strategy`:

| Strategy | Rule | Behaviour |
|---|---|---|
| `suite-level` *(default)* | `R3-describe-names-the-invariant` | one `Invariant` per `describe` block, with its rule-stating cases as evidence. Lower volume, higher abstraction |
| `case-level` | `R1-case-states-a-rule` | one `Invariant` per rule-stating test case. High volume, low abstraction |
| `both-levels` | `R4-both-levels` | both, related by `specializes`: the block names the concept, each case keeps the specific guarantee |

A test case "states a rule" when its name contains one of a fixed set of verbs
(`rejects`, `must`, `never`, `always`, `cannot`, `locks`, `prevents`, `requires`,
`returns the same`, `does not`, `fails`, `isolation`, `enforce`).

A final pass reports **gaps** — absence, proposing no knowledge. It records
modules with no test suite, tables with no tenant column, and three standing
gaps the rule set cannot close by construction: workflows, runtime behaviour and
prose invariants.

**This is a small interpreter, and its limits are visible.** Deterministic
discovery exercises 5 of the 23 metamodel entity types and has never proposed an
`Actor` or a `Policy`. Nothing it produces answers *why does this system work
this way?*

---

## Discovery Skills

`discovery/skills/skills.yaml` declares 11 **Discovery Skills** — engine-independent
investigation contracts. A skill states its objective, required inputs, the parts
of the Mechanical Model it may use as evidence, the questions it must answer, its
permitted tools, the entity types it may propose, its provenance rules, its
uncertainty vocabulary and its stopping condition. **No model or vendor is named
in any of them.**

Each skill declares a level: level 1 is repository-specific and disposable;
levels 2 and 3 are reusable technology and domain skills. Ten skills are level 2;
`DS-brownfield-onboarding` is level 1 and is the only one marked
`nondeterministic: true`.

Only `DS-brownfield-onboarding` has a runner (`tools/onboard.py`). The other ten
are declared contracts without an implementation in this repository.

---

## Running a frontier model as a worker

Engineering OS never calls a model. **There is no API key, no vendor SDK and no
network access anywhere in this repository.** The worker runs in whatever tool
you already use, and `tools/onboard.py` is the contract at both ends of it.

```bash
python tools/onboard.py brief  <repository> <project>   # what the worker may see
# → run the worker in Claude Code or Codex, save its JSON
python tools/onboard.py ingest <project> <worker-output.json>
```

**What the worker may read.** `mechanical-engineering-model.json`, and any file
that model references. The Mechanical Model is the **evidence boundary**: the
worker may open what the model points at and must go no further, because a
proposal citing something outside it cannot be checked.

**What the worker must return** — one JSON document. The briefing states the
schema verbatim; this is its shape:

```json
{
  "skill": "DS-brownfield-onboarding",
  "mechanicalModelDigest": "60116bae4c791115",
  "worker": "claude-code",
  "proposals": [
    {
      "id": "Invariant.InvoicesAreImmutable",
      "type": "Invariant",
      "label": "An issued invoice is never edited",
      "source": "docs/adr/0001-invoices-are-immutable.md",
      "locator": "decision",
      "uncertainty": "low",
      "for": ["The ADR states it as an accepted decision."],
      "against": ["No test asserts it."],
      "recommendation": "authorize"
    }
  ],
  "relationships": [
    {"from": "Invariant.InvoicesAreImmutable", "predicate": "constrains",
     "to": "Concept.Invoice", "source": "docs/adr/0001-invoices-are-immutable.md",
     "uncertainty": "low"}
  ]
}
```

Required on every proposal: `id`, `type`, `label`, `source`, `uncertainty`,
`for`, `against`. Required on every relationship: `from`, `predicate`, `to`,
`source`.

**Enforced at ingestion**, with nothing written when any check fails:

| Rule | Message on violation |
|---|---|
| the digest must match the current Mechanical Model | `digest mismatch: the worker saw 'X', this project has 'Y'` |
| `source` must appear in the Mechanical Model | `source 'X' is not in the Mechanical Model — the worker went outside the evidence boundary` |
| `uncertainty` is `high`, `medium` or `low` | `uncertainty must be high, medium or low` |
| no numeric self-assessment | `'confidence' is not permitted — Engineering OS has no confidence scores` |
| `type` must be a metamodel entity | `type 'X' is not a metamodel entity` |
| ids must be unique | `duplicate id` |
| at least one proposal | `no proposals returned` |

> **Note a real inconsistency:** the briefing tells the worker the allowed types
> are `Concept`, `Capability`, `Invariant`, `ADR`, `Actor` and `Evidence` (from
> the skill's `proposal-types`), while `tools/onboard.py` additionally accepts
> `BoundedContext`, `Artifact`, `Policy` and `Workflow`. Following the briefing
> is always safe; the extra four are accepted but undocumented in the contract.

**Two deliverables come out of ingestion:** `candidate-initial.json` — what is
proposed — and `engineering-review.json` — the argument for and against each
proposal. The second is the one a reviewer's time is actually spent against, and
it is what makes [curation](curation.md) fast.

**The contract in one line:** the worker investigates, the worker proposes, the
worker never authorizes, and the worker never writes to the authoritative model.

---

## Failure modes

| Symptom | Cause and fix |
|---|---|
| `no Stack Profile matches …` | unsupported stack; add a profile to `discovery/stacks.yaml` |
| `unknown strategy 'x'` | exit code 2; use `suite-level`, `case-level` or `both-levels` |
| discovery output is nearly empty | the profile matched but its globs found nothing. Check the paths declared for your profile in `discovery/stacks.yaml` against your repository's real layout |
| `… is not valid JSON` | save only the JSON document, without prose or a code fence |
| a rejected ingest lists one problem and no others | the validator stops accumulating per-proposal problems after the first failure; fix it and re-run to see the next |
