# Quick start

**Purpose.** Go from a fresh checkout to a compiled knowledge model, an answered
engineering question and a guidance result, in about ten minutes, using the
bundled `examples/tiny` project.

**Before you start:** [installation](installation.md), and `python tools/check.py`
exiting 0.

---

## Conventions used everywhere in this documentation

- **Run every command from the repository root.** Every tool resolves a relative
  `<project>` path against the *repository root*, not against your shell's
  working directory. Absolute paths also work.
- A **project** is a directory containing `model/` (authoring sources you own)
  and, after compilation, `build/` (generated products you never edit).
- `python` means the interpreter in your activated virtual environment.

---

## 1 · Compile the example

**Command**

```bash
python tools/compile.py examples/tiny
```

**Input** `examples/tiny/model/*.md` — thirteen Markdown files, one per entity.

**Expected result**

```text
[registries] 20 registries: assertion-origins 5, core-relationship-types 18, …
[discovery]  13 authoring sources
[parsing]    13 nodes, 0 structural diagnostic(s)
[resolution] 7 rules executed, 0 violation(s)
[ckm]        13 nodes, 16 edges
[projection] canonical-knowledge-model.json, explorer.html, graph.md, indexes.json, model.ttl, shapes.ttl
```

**Output location** `examples/tiny/build/`:

| File | What it is |
|---|---|
| `canonical-knowledge-model.json` | the CKM — the queryable semantic model |
| `model.ttl` | OWL ontology |
| `shapes.ttl` | SHACL shapes |
| `graph.md` | a Mermaid graph, coloured by entity family |
| `indexes.json` | registry and entity projections |
| `explorer.html` | a self-contained navigable view |

Compilation is deterministic: run it twice and the files are byte-identical.
Exit code is 0 on success and 1 when the compiler reports diagnostics.

To see what the compiler does and in which order:

```bash
python tools/compile.py --phases
```

---

## 2 · Open the Explorer

```bash
open examples/tiny/build/explorer.html        # macOS
xdg-open examples/tiny/build/explorer.html    # Linux
```

It is one self-contained HTML file — no server, no assets, no network. If you
prefer to serve it:

```bash
python -m http.server 8000 --directory examples/tiny/build
# then browse http://localhost:8000/explorer.html
```

---

## 3 · Ask an engineering question

```bash
python tools/ask.py examples/tiny questions
python tools/ask.py examples/tiny Q-impact Concept.Order
```

**Expected result**

```text
What breaks if I change this?
  subject: Concept.Order

  Invariant.PaymentBeforeShipping  (Invariant)  1 hop(s)

  status: ok · 1 row(s), 0 edge(s) · Q-impact
```

Add `--paths` to see the relationship path that produced each row, and `--json`
for machine-readable output including full provenance:

```bash
python tools/ask.py examples/tiny Q-impact Concept.Order --paths
python tools/ask.py examples/tiny Q-impact Concept.Order --json
```

**Three statuses, and they mean different things.**

| Status | Exit code | Meaning |
|---|---|---|
| `ok` | 0 | answered, with rows |
| `empty` | 0 | the question applies and nothing matched — often the finding |
| `not-applicable` | 1 | the question does not apply to this subject type, or the subject is not in the model |

`Q-status` applies only to `Artifact` and `ArtifactRevision`, so asking it about
a `Concept` is answered honestly rather than silently:

```text
  NOT APPLICABLE — applies to Artifact, ArtifactRevision; Concept.Order is a Concept
```

---

## 4 · Request engineering guidance

```bash
python tools/advise.py examples/tiny recommendations
python tools/advise.py examples/tiny R-change-concept Concept.Order
```

**Expected result** — five steps, each naming the query behind it, and each
step that found nothing saying so rather than disappearing:

```text
I want to change this Concept
  subject: Concept.Order

  REVIEW  — nothing
      the decision that established this, and whether it still stands   (Q-rationale)
  VALIDATE  guarantees that must survive the change
      Invariant.PaymentBeforeShipping  (Invariant) via constrains
      (Q-constraints)
  …
  status: ok · 2 item(s) across 5 step(s) · R-change-concept
```

---

## 5 · See how much the model can answer

```bash
python tools/measure.py examples/tiny
python tools/measure.py examples/tiny examples/vertical-slice
```

This compiles each project itself and scores it against the nine declared
Engineering Questions. `examples/tiny` answers 5 of 9; `examples/vertical-slice`
answers 7 of 9. With two or more projects it also reports which questions are
unanswered *everywhere*, and which have no declared query at all.

---

## What else is there

```bash
python tools/direct.py examples/tiny intents        # the four developer intents
python tools/plan.py  examples/tiny plans           # the eight engineering plans
```

`examples/vertical-slice` is a larger authored model (28 nodes) and is the
better example to read when you want to see every entity type used together.
`examples/brownfield-demo` is a small fake Node/NestJS/Drizzle repository used
by the onboarding documentation.

Next: [brownfield onboarding](brownfield-onboarding.md) to build a model of a
system you already have, or [greenfield](greenfield.md) to author one by hand.

---

## Failure modes

| Symptom | Cause and fix |
|---|---|
| `no compiled model at <project>/build/canonical-knowledge-model.json` | run `python tools/compile.py <project>` first — `ask.py` and `advise.py` read the compiled CKM, they do not compile |
| `[discovery]  0 authoring sources` | the project path is wrong. `compile.py` **creates** a missing directory instead of failing, so a typo yields an empty model with exit code 0 |
| `unknown query 'X'. Try: questions` | exit code 2; the id is not in the declared registry |
| `NOT APPLICABLE — no node 'X' in this model` | the subject id does not exist; ids are case-sensitive and look like `Concept.Order` |
