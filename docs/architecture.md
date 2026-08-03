# Architecture

**Purpose.** Explain how Engineering OS is put together, so you can predict what
each command will do and where a result came from.

This page is a working map, not a rationale. The reasoning behind every
structural choice lives in `governance/adr/` — 148 decision records, indexed in
`governance/adr/README.md`, each explaining *why* a rule exists. The customer-
facing narrative is `LIFECYCLE.md`.

---

## Five separated responsibilities

The whole product is one pipeline with five responsibilities that are never
allowed to blur into each other. That separation is the architecture; everything
else is detail.

| Responsibility | Where it lives | What it may do | What it may never do |
|---|---|---|---|
| **Mechanical extracts** | `discovery/mechanical.py`, `discovery/stacks.yaml` | record facts — packages, modules, routes, tables, test suites, config references, documents, each with file and locator | name anything as engineering knowledge |
| **Interpretive hypothesizes** | `discovery/interpretive.py`, `discovery/skills/`, `tools/onboard.py` | propose engineering meaning, with evidence and an argument | read the repository directly, or decide anything |
| **Curation authorizes** | `tools/curate.py`, `tools/review.py`, `compiler/apply/` | accept, reject, correct or defer each proposal; write authoring sources | be run by a script — curation refuses without a terminal |
| **Continuous preserves** | `discovery/continuous.py`, `discovery/drift.py`, `tools/lifecycle.py`, `tools/longitudinal.py` | propose only what changed; challenge the model with a fresh look | apply a retraction, or replace the curated model |
| **Guidance consumes** | `compiler/query/`, `compiler/recommend/`, `compiler/plan/`, `compiler/taskgraph/`, `compiler/direct/` | answer questions, recommend work, derive plans and task graphs | write to the model, or involve a language model |

Two boundaries carry most of the weight:

- **Interpretive Discovery reads only the Mechanical Model.** It never opens a
  source file. That is what makes extraction quality and interpretation quality
  separately measurable, and two interpreters comparable over identical input.
- **An accepted proposal becomes an *authoring source*, never a model write.**
  The compiler stays the only writer of the Canonical Knowledge Model, and the
  file a reviewer accepted is an ordinary Markdown file they own.

---

## The compiler

`tools/compile.py` is orchestration only; the compiler is `compiler/`.

```bash
python tools/compile.py --phases
```

**Six phases**, each consuming the previous phase's product:

| Phase | Consumes | Produces |
|---|---|---|
| **Authoring** *(not executed by the compiler)* | human intent | authoring sources |
| **Discovery** | authoring sources | a source set |
| **Parsing** | a source set | structurally valid assertions |
| **Resolution** | assertions | a resolved assertion set |
| **Canonical Knowledge Model** | resolved assertions | the semantic model |
| **Projection** | the semantic model | derived artifacts |

**Thirteen features** are registered across those phase boundaries, and each
declares its own invariants and its determinism property. `--phases` prints all
of them; the list is:

`registry loading` · `source discovery` · `front-matter parsing` ·
`declarative rule execution` · `edge resolution` · `canonical knowledge model` ·
`JSON projection` · `OWL projection` · `SHACL projection` · `graph projection` ·
`index projection` · `knowledge explorer projection` · `semantic query execution`

Properties worth relying on:

- **Structural errors are reported at Parsing, never at Resolution.** A
  `relationships:` key that is a string fails as a structural defect rather than
  being reinterpreted as an empty list.
- **No edge is created that was not asserted**, and only when its target
  resolves.
- **Validation is declarative.** Seven validation rules (`VR-0001`…`VR-0007`)
  are data, not Python; each diagnostic reports the rule id that produced it.
- **Output is order-stable and carries no timestamp.** Two compilations of the
  same sources are byte-identical, and `tools/check.py` verifies it.

---

## Registries — the metamodel is data

The compiler knows three *extraction kinds*; it does not know the shape of any
particular registry file. `model/metamodel/registries.md` declares which
registries exist, where they live and how each is read. **Twenty registries** are
declared, including:

| Registry | Contents |
|---|---|
| `REG-entity-types` | the 23 metamodel entity types |
| `REG-relationship-predicates` | 74 predicates, each specialising one of 18 core relationship types |
| `REG-validation-rules` | 7 declarative validation rules |
| `REG-queries` | 17 semantic queries |
| `REG-recommendations`, `REG-plans`, `REG-engineering-intents` | 4, 8 and 4 respectively |
| `REG-engineering-questions` | the 9-question contract the product is measured by |
| `REG-drift-categories` | 15 drift classes and their plan routing |
| `REG-workers`, `REG-worker-capabilities`, `REG-task-kinds` | 12, 9 and 11 |
| `REG-support-classification`, `REG-assertion-origins` | 8 and 5 |

Adding a registry is a data change; adding an extraction kind is a compiler
change and is meant to be rare. The same principle governs Stack Profiles: a new
stack costs a declaration in `discovery/stacks.yaml`, not an interpreter change.

---

## The semantic layer

`tools/ask.py`, `tools/advise.py`, `tools/plan.py`, `tools/taskgraph.py` and
`tools/direct.py` implement **no** question, recommendation, plan or task. Each
is a renderer over a declared registry executed by `compiler/`. That is why
adding a question is a Markdown edit and why the tools cannot disagree with the
registry.

**Two independent query engines** exist and must agree on every declared query
over the bundled examples — status, rows, paths, ordering, edges and
diagnostics. `tools/check.py` and `tools/test.py` verify it; a disagreement is a
build failure.

---

## Provenance and trust

Every assertion in the model carries where it came from: `source`, `locator`,
the `worker` and `task` that produced it, its **support classification**
(`S-implemented`, `S-tested`, `S-inferred`, …) and whether its producer was
non-deterministic. Support classification also decides review mode: three
classifications may be accepted in batch, five require individual review.

- Probabilistic workers produce **proposals only**; their output is validated
  and quarantined as a candidate.
- **A proposal's own confidence never authorizes it** — numeric confidence
  scores are rejected at intake.
- The applier is the only component that writes authoring sources; the compiler
  writes only into `build/`.
- Engineering OS makes **no network calls** and reads no credentials.

---

## Repository layout

| Directory | What it is |
|---|---|
| `compiler/` | the compiler, query engine, planner, task graph, applier |
| `discovery/` | mechanical + interpretive discovery, stack profiles, skill contracts |
| `tools/` | every command in the documentation |
| `model/metamodel/` | the 23 entity types, the relationship vocabulary, the registry declarations |
| `model/*.md` | declared registries: queries, plans, recommendations, questions, drift classes, workers |
| `tests/` | 17 regression fixtures with golden outputs |
| `governance/` | ADRs, issues, sessions, acceptance records — the project's memory |
| `examples/` | `tiny`, `vertical-slice`, `brownfield-demo` |
| `external/` | onboarding and benchmark results |
| `imports/`, `sources/` | frozen provenance; never edited |

---

## Where to read further

- `LIFECYCLE.md` — the ten-stage customer lifecycle and its honest status.
- `governance/adr/README.md` — the indexed decision corpus, starting with the
  foundational records.
- `discovery/ARCHITECTURE.md` — the discovery subsystem in more depth.
- `model/metamodel/entities/*.md` — one specification per entity type.
