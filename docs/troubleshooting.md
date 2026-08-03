# Troubleshooting

Every failure below is one you can reproduce. Each entry gives the message you
will actually see, why it happens, and what to do.

**First step for anything unexplained:**

```bash
python tools/check.py
```

Exit code 0 means the installation itself is sound and the problem is in your
project or your inputs.

---

## Compilation

### Malformed YAML front matter

```text
[parsing]    0 nodes, 1 structural diagnostic(s)
[FAILED]     1 diagnostic(s):
    (parsing) bad.md: key 'relationships' must be list, got str
```

`relationships:` must be a YAML **list** of single-key mappings, not a string.
A related one:

```text
    (parsing) a.md: attributes must be scalar; ['source'] are not
```

Attribute values must be scalars — no lists, no nested mappings.

Both are reported at **Parsing**, before any semantic work, and the file
contributes no nodes. Values beginning with a YAML indicator character (`*`,
`&`, `@`, `` ` ``, a leading `"`) need quoting. Exit code 1.

### Unknown entity type or unregistered predicate

```text
    (resolution) w.md: 'Widget' is not a metamodel entity [VR-0001]
    (resolution) a.md: predicate 'invented-link' has no registered parent (ADR-0071) [VR-0002]
```

`type` must be one of the 23 types in `model/metamodel/entities/`, and every
predicate must appear in `model/metamodel/relationship-vocabulary.md`. The
vocabulary is enforced, not advisory.

### Unresolved and inconsistent references

```text
    (resolution) a.md: 'references' points at unknown node 'Concept.Missing' [VR-0003]
    (resolution) duplicate node id 'Concept.Same' declared 2 times [VR-0004]
    (resolution) loop.md: 'scoped-to' on 'BC.Loop' points at itself [VR-0005]
    (resolution) step.md: a WorkflowStep must declare 'executes' [VR-0006]
```

Ids are case-sensitive and unique within a project. Containment and revision
edges may not point at their own node. A `WorkflowStep` exists only to position
a `Skill`, so it must execute one.

Reproduce any of these against the shipped fixtures in
`tests/projects/<name>/`, each of which documents what it exercises in
`expected.md`.

---

## Wrong project directory

**This one is silent, and it is the most common confusion.**

```bash
python tools/compile.py exmaples/tiny     # typo
```

```text
[discovery]  0 authoring sources
[parsing]    0 nodes, 0 structural diagnostic(s)
[ckm]        0 nodes, 0 edges
[projection] canonical-knowledge-model.json, …
```

Exit code **0**. `compile.py` creates the directory it was given and emits an
empty model rather than reporting that nothing is there. If your model suddenly
has 0 nodes, check the path first — and delete the stray directory the typo
created.

Two related points:

- **Project paths resolve against the repository root**, not your shell's
  working directory. `myproject` means `<checkout>/myproject`. Absolute paths
  work everywhere.
- `python tools/compile.py --help` is treated as a project path and **creates a
  directory literally named `--help`**. Use `python tools/compile.py --phases`
  for the phase listing. `tools/curate.py --help`, `tools/measure.py --help` and
  `tools/test.py --help` are also parsed as project arguments; `tools/test.py
  --help` exits with a `FileNotFoundError` traceback. Tools with a real `--help`
  are `check.py`, `smoke.py`, `ask.py`, `advise.py`, `direct.py`, `plan.py`,
  `taskgraph.py`, `onboard.py`, `review.py`, `lifecycle.py`, `longitudinal.py`,
  `guidance.py` and `drift-queue.py`.

---

## Queries and guidance

### `no compiled model`

```text
no compiled model at <project>/build/canonical-knowledge-model.json
run: python3 tools/compile.py <project>
```

`ask.py`, `advise.py`, `plan.py`, `taskgraph.py`, `direct.py` and
`drift-queue.py --plan=` read the compiled CKM; they do not compile.
`measure.py` and `guidance.py` compile the project themselves.

### Query not applicable

```text
  NOT APPLICABLE — applies to Artifact, ArtifactRevision; Concept.Order is a Concept
  status: not-applicable · Q-status
```

**This is not an error.** Queries are typed, and a typed refusal is more useful
than an empty answer. Exit code 1. The same message with a different ending —
`no node 'Concept.Nope' in this model` — means the subject id does not exist.

A related non-error: `status: empty` means the question applied and nothing
matched. That is frequently the finding, not a fault.

### Unknown registry reference

```text
unknown query 'Q-nope'. Try: questions
unknown recommendation 'R-nope'. Try: recommendations
unknown plan 'P-nope'. Try: plans
  INVALID — unknown intent 'I-nope'
```

Exit code 2 (1 for the intent case). Every id comes from a declared registry;
list them with `questions`, `recommendations`, `plans`, `intents`.

### A plan phase produced nothing

```text
  ── VERIFY: Confirm the guarantees survived   requires: change
       (nothing to do — no query returned anything)
```

Expected. A step that cannot apply to your subject is named, never silently
skipped.

---

## Discovery and onboarding

### Unsupported stack profile

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

### Empty discovery output

The profile matched but the statistics are all zero, or nearly:

```text
[mechanical]  /path/to/repo
    packages         1
    routes           0
    tables           0
    testSuites       0
[candidate]   1 entities · 0 relationships
```

The profile's globs did not match your layout. Compare the `glob` entries for
your profile in `discovery/stacks.yaml` against the real paths in your
repository — for the Node profile these are
`packages/backend/src/**/*.controller.ts`,
`packages/backend/src/common/database/schema/*.ts`,
`packages/backend/src/**/*.spec.ts` and `docs/**/*.md`. Vendor and build
directories (`node_modules`, `target`, `dist`, `build`, `.git`, …) are always
skipped.

### Digest mismatch on ingest

```text
  rejected — 1 problem(s)

    digest mismatch: the worker saw 'deadbeef', this project has '60116bae4c791115'.
    The repository changed after the briefing was written — re-run `brief` and re-run the worker.

  Nothing was written. Fix the worker's output and run ingest again.
```

Exit code 1. The Mechanical Model is the agreed evidence, and a proposal made
against a different one cannot be checked. Re-run `brief`, re-run the worker,
re-run `ingest`.

Other ingestion rejections, all with the same "nothing was written" guarantee:

| Message | Fix |
|---|---|
| `… is not valid JSON` | save only the JSON document, no prose, no code fence |
| `source 'X' is not in the Mechanical Model — the worker went outside the evidence boundary` | cite a file the Mechanical Model references |
| `uncertainty must be high, medium or low` | never a number |
| `'confidence' is not permitted — Engineering OS has no confidence scores` | remove it |
| `no mechanical model in <project>. Run \`brief\` first.` | wrong project directory |

Only the first per-proposal problem is reported; fix it and re-run to see the
next.

### `no Candidate Engineering Model in …`

```text
no Candidate Engineering Model in <project>.
  There is nothing to curate yet. Produce proposals first:
    python discovery/run.py <repository> <project>      # deterministic
    python tools/onboard.py brief <repository> <project>  # with Claude or Codex
```

Wrong project directory, or discovery has not run. Note that `tools/review.py`
reads `candidate-engineering-model.json` (written by `discovery/run.py`) while
`tools/curate.py` reads `candidate-initial.json` (written by both paths).

### Curation refuses to run

```text
Human Curation requires a human.
  This tool refuses to run without a terminal.
```

Exit code 1. **By design.** Use `--report` for the session summary, which works
without a terminal, or `tools/review.py apply --reviewer=NAME` for
non-interactive authorization.

---

## Stale bytecode cache

Symptom: `tools/check.py` reports

```text
  FAIL  deterministic generation
```

or a change you made to a `.py` file appears to have no effect.

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
        → a decision record is inconsistent; see docs/troubleshooting.md
```

List them:

```bash
python tools/check-governance.py
```

Findings are one of: a document with no front matter or unparseable front
matter, an id that disagrees with its filename, a gap in a numbered sequence
that the index does not explain, a dangling reference between records, a
supersession recorded on only one side, an index row count that disagrees with
the number of files, or a **broken Markdown link** — for example a link to a
`docs/` page that does not exist. This check runs inside both `tools/check.py`
and `tools/test.py`, so a broken link in `README.md` fails the whole suite.

---

## Still stuck

```bash
python tools/check.py        # is the installation sound?
python tools/test.py         # 17 fixtures, both query engines, governance
python tools/smoke.py --keep # the whole documented path, workspace preserved
```

`tools/test.py --accept` rewrites the golden outputs. Only run it when you have
deliberately changed the compiler's output and have reviewed the diff.
