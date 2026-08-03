# Engineering guidance

**Purpose.** Turn a compiled model into answers and into work: what breaks if I
change this, what should I do about it, in what order, and who does each part.

Everything on this page reads `<project>/build/canonical-knowledge-model.json`.
Compile first:

```bash
python tools/compile.py <project>
```

**No language model participates in any of it.** Every result is derived from
the model by declared queries. Where a decision genuinely requires judgement,
the output says so and defers it to a worker or a human gate rather than
guessing.

---

## 1 · Questions — `tools/ask.py`

```bash
python tools/ask.py <project> questions
python tools/ask.py <project> Q-impact Concept.Order
python tools/ask.py <project> Q-impact Concept.Order --paths
python tools/ask.py <project> Q-impact Concept.Order --json
```

Seventeen queries are declared in `model/queries.md`; `ask.py` implements none
of them. Some take a subject, some apply only to certain entity types, and six
take no subject at all — `Q-unsupported`, `Q-obsolete-decisions`,
`Q-stale-implementation`, `Q-unenforced`, `Q-unaccepted`, `Q-orphan-concepts`.

Three statuses, three meanings: `ok` (answered), `empty` (the question applies
and nothing matched — often the finding), `not-applicable` (wrong subject type,
or the subject is not in the model). `ok` and `empty` exit 0; `not-applicable`
exits 1; an unknown query id exits 2. `--paths` prints the relationship path
behind every row; `--json` adds full provenance, so *how do you know?* is always
answerable.

**Two independent query engines** exist and `tools/check.py` verifies that they
agree on every declared question over the bundled examples. A disagreement is a
build failure, not a warning.

---

## 2 · Recommendations — `tools/advise.py`

```bash
python tools/advise.py <project> recommendations
python tools/advise.py <project> R-change-concept Concept.Order
python tools/advise.py <project> R-audit-model --json
```

Four recommendations are declared in `model/recommendations.md`, each composed
entirely of semantic queries:

| Id | Intent | Subject |
|---|---|---|
| `R-change-concept` | I want to change this Concept | `Concept` |
| `R-change-implementation` | I want to change this implementation | `Artifact` |
| `R-discover` | I want to build an engineering model of this repository | `Artifact` |
| `R-audit-model` | I want to know what this model cannot support | none |

A recommendation prints its steps in order, each naming the query behind it.
**A step that found nothing prints `— nothing`** instead of vanishing, because
the absence is information.

---

## 3 · Plans and task graphs — `tools/plan.py`, `tools/taskgraph.py`

```bash
python tools/plan.py <project> plans
python tools/plan.py <project> P-change-concept Concept.Order
python tools/plan.py <project> P-change-concept Concept.Order --reasoning
python tools/plan.py <project> P-change-concept Concept.Order --json
```

Eight plans are declared in `model/plans.md`. A plan states an objective, a
rationale, its **assumptions** — each marked when the query behind it returned
nothing — and its phased actions with `requires:` ordering between phases.

```text
ASSUMPTIONS
  This decision established the current meaning; check it still stands.
      (none found — the assumption is unverified)
      [Q-rationale]
```

A task graph turns a plan into ordered, assignable work:

```bash
python tools/taskgraph.py <project> P-change-concept Concept.Order
python tools/taskgraph.py <project> P-change-concept Concept.Order --mermaid
python tools/taskgraph.py <project> P-change-concept Concept.Order --json
```

```text
EXECUTION   1 mechanical · 2 reasoning · 1 human   ·   max parallelism 1

  LEVEL 1
    [LLM  ]  T01-understand-validate
              Check that Invariant.PaymentBeforeShipping still hold after the intended change
              done when:  The guarantees constraining this concept are known.
              needs:      C-read-source
```

Each task declares the **capabilities** it requires, never which worker performs
it. `--mermaid` emits a graph you can paste into any Mermaid renderer.

---

## 4 · The whole loop — `tools/direct.py`

```bash
python tools/direct.py <project> intents
python tools/direct.py <project> I-modify-behavior Artifact.CheckoutService
python tools/direct.py <project> I-modify-behavior Artifact.CheckoutService --context=T01
python tools/direct.py <project> I-modify-behavior <subject> --observations=<path.yaml>
```

`direct.py` runs **intent → plan → task graph → worker assignment → execution
context**, and, when observations are supplied, the knowledge update that
follows execution.

> **Use `=` with these flags.** The tool's own help text shows `--context T02`
> with a space; only the `--context=T02` form is parsed. The space form is
> silently ignored.

Four intents are declared:

| Intent | Selects |
|---|---|
| `I-modify-behavior` | `P-change-implementation`, `P-change-concept`, `P-change-capability` |
| `I-onboard` | `P-discover` |
| `I-investigate` | no plan — it says so and stops |
| `I-audit` | no plan — it says so and stops |

`--context=<task-id>` prints the **execution context** for one task: objective,
rationale, assumptions marked `[UNVERIFIED]` where nothing supports them,
evidence, affected nodes, expected output, completion criteria, the allowed
scope, and the capabilities required. A worker receives one task and its
context — never an intent, a plan or a graph.

The footer reports how many engineering decisions were made deterministically
before any worker is involved:

```text
KPI   21 engineering decisions made before the first LLM token
      4 left to workers
```

---

## 5 · Measuring guidance

**Coverage** — how much of the Engineering Question Set a model can answer.
`measure.py` compiles each project itself, so no prior `compile.py` is needed:

```bash
python tools/measure.py <project>
python tools/measure.py <project-a> <project-b>
```

With two or more projects it also names the questions unanswered in *every*
repository measured, and the questions for which **no query is declared at all**
— currently `EQ-08-authorization`, *who is allowed to perform this operation?*

**Stability** — does the model still recommend the same work?

```bash
python tools/guidance.py <project-a> <project-b>
```

It compiles both projects and compares, subject by subject, the *work* each
recommendation names — status plus the sorted ids per action, with prose
excluded. Two recommendations naming the same work in different words are the
same guidance. Comparing a project with itself yields 100 %.

```text
  8 common subjects, 3 subject/recommendation pairs judged

    stable   0
    changed  3

  Guidance Preservation  0%
    changed  Concept.Order  R-change-concept  ok → ok
```

**What this does not measure.** Guidance *correctness* is not measured anywhere
in this repository. Only stability is, and only over subjects whose evidence
nobody touched — a subject the repository changed *should* get different advice.

---

## Failure modes

| Symptom | Exit | Cause and fix |
|---|---|---|
| `no compiled model at <project>/build/canonical-knowledge-model.json` | 1 | run `python tools/compile.py <project>` |
| `unknown query 'X'. Try: questions` | 2 | also `unknown recommendation`, `unknown plan` — the id is not in the declared registry |
| `NOT APPLICABLE — applies to Concept; X is a Artifact` | 1 | the query or recommendation is typed; pick one that applies to your subject |
| `INVALID — unknown intent 'I-nope'` | 1 | list them with `direct.py <project> intents` |
| `intent 'I-investigate' selects no plan` | 0 | expected: two of the four intents have no planning support |
| a plan phase produced nothing | 0 | expected: the step did not apply to your subject, and the planner names which and why |
| `--context T01` printed no execution context | 0 | use `--context=T01` |
