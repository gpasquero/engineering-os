# Troubleshooting

Every failure below is one you can reproduce. Each entry gives the message you
will actually see, why it happens, and what to do.

**First step for anything unexplained:** `python tools/check.py`. Exit code 0
means the installation is sound and the problem is in your project or inputs.

---

## Malformed YAML front matter

```text
[parsing]    0 nodes, 1 structural diagnostic(s)
[FAILED]     1 diagnostic(s):
    (parsing) bad.md: key 'relationships' must be list, got str
    (parsing) a.md: attributes must be scalar; ['source'] are not
```

`relationships:` must be a YAML **list** of single-key mappings, not a string.
Attribute values must be scalars — no lists, no nested mappings. Values
beginning with a YAML indicator character (`*`, `&`, `@`, `` ` ``, a leading
`"`) need quoting.

Both are reported at **Parsing**, before any semantic work, so the file
contributes no nodes at all. Exit code 1. Fixtures:
`tests/projects/malformed-yaml/`, `tests/projects/bad-attributes/`.

---

## Unknown registry references in a model

```text
    (resolution) w.md: 'Widget' is not a metamodel entity [VR-0001]
    (resolution) a.md: predicate 'invented-link' has no registered parent (ADR-0071) [VR-0002]
    (resolution) a.md: 'references' points at unknown node 'Concept.Missing' [VR-0003]
    (resolution) duplicate node id 'Concept.Same' declared 2 times [VR-0004]
    (resolution) loop.md: 'scoped-to' on 'BC.Loop' points at itself [VR-0005]
    (resolution) step.md: a WorkflowStep must declare 'executes' [VR-0006]
```

`type` must be one of the 23 types in `model/metamodel/entities/`; every
predicate must appear in `model/metamodel/relationship-vocabulary.md`. Ids are
case-sensitive and unique within a project. Containment and revision edges may
not point at their own node. Each fixture in `tests/projects/` documents what it
exercises in `expected.md`.

## Unknown registry references on the command line

```text
unknown query 'Q-nope'. Try: questions
unknown recommendation 'R-nope'. Try: recommendations
unknown plan 'P-nope'. Try: plans
  INVALID — unknown intent 'I-nope'
```

Exit code 2 (1 for the intent case). List valid ids with `questions`,
`recommendations`, `plans`, `intents`.

---

## Wrong project directory

**This one is silent, and it is the most common confusion.**

```bash
python tools/compile.py exmaples/tiny     # typo
```

```text
[discovery]  0 authoring sources
[ckm]        0 nodes, 0 edges
```

Exit code **0**. `compile.py` creates the directory it was given and emits an
empty model rather than reporting that nothing is there. If your model suddenly
has 0 nodes, check the path first — and delete the stray directory the typo
created.

- **Project paths resolve against the repository root**, not your shell's
  working directory. `myproject` means `<checkout>/myproject`. Absolute paths
  work everywhere.
- `python tools/compile.py --help` is parsed as a project path and **creates a
  directory literally named `--help`**. Use `--phases` instead. `curate.py`,
  `measure.py` and `test.py` also parse `--help` as a project argument, and
  `tools/test.py --help` exits with a `FileNotFoundError` traceback. Tools with
  a working `--help`: `check.py`, `smoke.py`, `ask.py`, `advise.py`, `direct.py`,
  `plan.py`, `taskgraph.py`, `onboard.py`, `review.py`, `lifecycle.py`,
  `longitudinal.py`, `guidance.py`, `drift-queue.py`.

---

## `no compiled model`

```text
no compiled model at <project>/build/canonical-knowledge-model.json
run: python3 tools/compile.py <project>
```

`ask.py`, `advise.py`, `plan.py`, `taskgraph.py`, `direct.py` and
`drift-queue.py --plan=` read the compiled CKM; they do not compile.
`measure.py` and `guidance.py` compile the project themselves.

---

## Query not applicable

```text
  NOT APPLICABLE — applies to Artifact, ArtifactRevision; Concept.Order is a Concept
  status: not-applicable · Q-status
```

**Not an error.** Queries are typed, and a typed refusal is more useful than an
empty answer. Exit code 1. The variant `no node 'Concept.Nope' in this model`
means the subject id does not exist.

`status: empty` (exit 0) means the question applied and nothing matched — often
the finding. Likewise, a plan phase printing `(nothing to do — no query returned
anything)` is expected: a step that cannot apply is named, never skipped.

---

## Unsupported stack profile

```text
no Stack Profile matches /path/to/repo.
  Mechanical Acquisition refuses rather than returning an empty
  model: an empty model and an unrecognised stack are opposite
  findings, and only one of them is about the repository.
```

Exit code 1. Only `S-node-nest-drizzle` (detected by
`packages/backend/package.json`) and `S-java-spring-jpa` (detected by `pom.xml`
or `backend/pom.xml`) exist. The project directory is still created, but nothing
is written into it. Adding a stack is a declaration in `discovery/stacks.yaml`.
Only one profile is detected per repository, so a polyglot monorepo is only
partly covered.

---

## Empty discovery output

The profile matched but the statistics are zero or nearly zero:

```text
[mechanical]  /path/to/repo
    routes           0
    tables           0
    testSuites       0
[candidate]   1 entities · 0 relationships
```

The profile's globs did not match your layout. Compare the `glob` entries for
your profile in `discovery/stacks.yaml` against your real paths — for the Node
profile: `packages/backend/src/**/*.controller.ts`,
`packages/backend/src/common/database/schema/*.ts`,
`packages/backend/src/**/*.spec.ts`, `docs/**/*.md`. Vendor and build
directories (`node_modules`, `target`, `dist`, `build`, `.git`, …) are always
skipped.

---

## Digest mismatch on onboarding ingest

```text
  rejected — 1 problem(s)

    digest mismatch: the worker saw 'deadbeef', this project has '60116bae4c791115'.
    The repository changed after the briefing was written — re-run `brief` and re-run the worker.

  Nothing was written. Fix the worker's output and run ingest again.
```

Exit code 1. The Mechanical Model is the agreed evidence; a proposal made
against a different one cannot be checked. Other ingestion rejections, all with
the same "nothing was written" guarantee:

| Message | Fix |
|---|---|
| `… is not valid JSON` | save only the JSON document, no prose, no code fence |
| `source 'X' is not in the Mechanical Model — the worker went outside the evidence boundary` | cite a file the Mechanical Model references |
| `uncertainty must be high, medium or low` | never a number |
| `'confidence' is not permitted — Engineering OS has no confidence scores` | remove it |
| `no mechanical model in <project>. Run \`brief\` first.` | wrong project directory |

Only the first per-proposal problem is reported; fix it and re-run to see the
next.

---

## Nothing to curate, or curation refuses

```text
no Candidate Engineering Model in <project>.
  There is nothing to curate yet. Produce proposals first: …
```

Wrong project directory, or discovery has not run. Note that `tools/review.py`
reads `candidate-engineering-model.json` (written by `discovery/run.py`) while
`tools/curate.py` reads `candidate-initial.json` (written by both paths).

```text
Human Curation requires a human.
  This tool refuses to run without a terminal.
```

Exit code 1, **by design**. Use `--report` for the session summary, which works
without a terminal, or `tools/review.py apply --reviewer=NAME` for
non-interactive authorization.

---

## Stale bytecode cache

Symptom: `tools/check.py` reports `FAIL deterministic generation`, or an edit to
a `.py` file appears to have no effect.

**On macOS, Python may cache bytecode outside the repository**, so deleting
`__pycache__` inside the checkout is not enough:

```bash
ls ~/Library/Caches/com.apple.python$(pwd)
rm -rf ~/Library/Caches/com.apple.python$(pwd)
find . -name __pycache__ -type d -prune -exec rm -rf {} +
```

Then re-run `python tools/check.py`.

---

## Governance consistency failures

```text
  FAIL  governance consistency             15 governance finding(s)
```

List them with `python tools/check-governance.py`. Findings are: missing or
unparseable front matter, an id disagreeing with its filename, a gap in a
numbered sequence the index does not explain, a dangling reference, a
supersession recorded on only one side, an index row count that disagrees with
the file count, or a **broken Markdown link** — including a link to a `docs/`
page that does not exist. This check runs inside both `tools/check.py` and
`tools/test.py`, so one broken link in `README.md` fails the whole suite.

---

## Still stuck

```bash
python tools/check.py        # is the installation sound?
python tools/test.py         # 17 fixtures, both query engines, governance
python tools/smoke.py --keep # the whole documented path, workspace preserved
```

`tools/test.py --accept` rewrites the golden outputs. Run it only when you have
deliberately changed the compiler's output and reviewed the diff.
