# Brownfield onboarding

**Purpose.** Build an engineering model of a repository that already exists —
one nobody on the team fully understands any more.

```text
Existing repository
  → Mechanical Discovery          facts only, reproducible, interprets nothing
  → Interpretive Discovery        proposes engineering meaning (deterministic, or a frontier model)
  → Candidate Engineering Model   nothing here is true yet
  → Human Curation                a person decides, one proposal at a time
  → Proposal application          accepted proposals become authoring sources
  → Compiler → CKM → knowledge products
```

Initial onboarding is deliberately slow. Its purpose is to establish
understanding that later changes maintain *incrementally* — see
[continuous acquisition](continuous-acquisition.md).

Throughout this page, `external/demo` is the **project directory**: where
Engineering OS writes. The repository you analyse is never modified.

---

## Step 0 · Check that your stack is supported

Mechanical Discovery finds facts where a **Stack Profile** says they live.
`discovery/stacks.yaml` declares exactly two:

| Profile | Detected by |
|---|---|
| `S-node-nest-drizzle` | `packages/backend/package.json` |
| `S-java-spring-jpa` | `pom.xml` or `backend/pom.xml` |

Anything else is **refused**, not degraded:

```text
no Stack Profile matches /path/to/repo.
  Mechanical Acquisition refuses rather than returning an empty
  model: an empty model and an unrecognised stack are opposite
  findings, and only one of them is about the repository.
```

Exit code 1. Adding a stack is a declaration in `discovery/stacks.yaml`, not
code — but you have to write it. **Only one profile is detected per repository**,
so a polyglot monorepo is only partly covered.

---

## Step 1 · Write the briefing (and the Mechanical Model)

**Command**

```bash
python tools/onboard.py brief examples/brownfield-demo external/demo
```

**Output location** — two files in `external/demo/`:

- `mechanical-engineering-model.json` — packages, dependencies, module
  directories, routes, tables, test suites and their cases, configuration
  references and documents. Each fact carries its file and locator. The model
  carries a `digest`; re-extracting the same repository reproduces it exactly.
- `onboarding-brief.md` — everything a frontier model is allowed to see, the
  five questions it must answer, and the exact JSON schema it must return.

**Expected result**

```text
  briefing written  external/demo/onboarding-brief.md
  mechanical model  external/demo/mechanical-engineering-model.json  (3 documents, 2 suites)
```

Your own repository works identically:

```bash
python tools/onboard.py brief /path/to/your/repo external/yourrepo
```

---

## Step 2 · Produce a Candidate Engineering Model

Two paths. They are not exclusive — run both and compare.

### 2a · Deterministic (no model needed)

```bash
python discovery/run.py examples/brownfield-demo external/demo
python discovery/run.py examples/brownfield-demo external/demo --strategy=both-levels
```

Six named rules read **only** the Mechanical Model and propose entities and
relationships. `--strategy` selects how test suites become invariants:
`suite-level` (default), `case-level` or `both-levels`. See
[discovery skills](discovery-skills.md).

**Expected result**

```text
[mechanical]  …/examples/brownfield-demo
    packages         1
    …
    digest           60116bae4c791115
[interpretive] strategy 'suite-level', reading only the mechanical model
[candidate]   11 entities · 10 relationships
              0 ambiguities · 4 gaps
[written]     external/demo/mechanical-engineering-model.json
              external/demo/candidate-engineering-model.json
              external/demo/candidate-initial.json
```

`candidate-initial.json` is the file every downstream tool reads;
`candidate-engineering-model.json` is the same content under a descriptive name.

### 2b · With Claude Code or Codex

Engineering OS does **not** call a model. It writes a briefing you paste in, and
validates the JSON you get back. There is no API key and no network call.

1. Open `external/demo/onboarding-brief.md` in your Claude Code or Codex session
   and follow it.
2. Save the model's JSON reply — only the JSON, no prose and no code fence.
3. Ingest it:

```bash
python tools/onboard.py ingest external/demo external/demo/worker-output.json
```

**Expected result**

```text
  accepted  1 proposal(s), 1 relationship(s)
  uncertainty  low 1
  candidate    external/demo/candidate-initial.json
  review       external/demo/engineering-review.json

  Nothing is authoritative yet. Next:
    python tools/curate.py external/demo
```

Ingestion produces two artifacts: the **Candidate Engineering Model** (what is
proposed) and the **Engineering Review** (the argument for and against each
proposal, which is what a reviewer's time is actually spent on).

If a deterministic candidate already existed, it is preserved as
`candidate-initial.deterministic.json` before being replaced.

---

## Step 3 · Check where you are, at any time

```bash
python tools/onboard.py status external/demo
```

```text
  external/demo
    ✓    mechanical model       4 KB
    ✓    worker briefing        3 KB
    ✓    candidate model        1 KB
    ✓    engineering review     1 KB
    —    curation session
    —    authoritative model
```

---

## Step 4 · Curate, apply and compile

```bash
python tools/curate.py external/demo      # requires a terminal and a human
python tools/compile.py external/demo
```

Curation is the only stage where anything is decided; it has its own page:
[curation](curation.md). If you would rather authorize in bulk without an
interactive session, use `tools/review.py` — also covered there.

After compiling you have the full knowledge product set in
`external/demo/build/`, and you can ask questions and request guidance exactly
as in the [quick start](quickstart.md).

---

## Failure modes

| Symptom | Exit | Cause and fix |
|---|---|---|
| `no Stack Profile matches …` | 1 | unsupported stack. The project directory is still created, but nothing is written into it |
| `unknown strategy 'x'; try ['both-levels', 'case-level', 'suite-level']` | 2 | typo in `--strategy` |
| `… is not valid JSON` | 1 | the worker's reply was saved with prose or a code fence around it. Save only the JSON document |
| `digest mismatch: the worker saw 'X', this project has 'Y'` | 1 | the repository changed after the briefing was written. Re-run `brief`, re-run the worker |
| `source 'X' is not in the Mechanical Model — the worker went outside the evidence boundary` | 1 | a proposal cites a file the Mechanical Model does not reference. The boundary is deliberate: a proposal nobody can check does not enter |
| `'confidence' is not permitted — Engineering OS has no confidence scores` | 1 | use `uncertainty: high\|medium\|low` |
| `no mechanical model in <project>. Run \`brief\` first.` | 1 | `ingest` was pointed at a project where `brief` never ran |

**Nothing is written when ingestion is rejected.** Fix the worker's output and
run `ingest` again — the command is safe to repeat.
