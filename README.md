# Engineering OS

> **We preserve an engineering team's ability to make correct decisions as
> software evolves.**

Most engineering knowledge is not written down. It lives in the people who made
the decisions, and it leaves when they do. Engineering OS builds a durable,
attributable engineering model of a system you already have — and then keeps it
alive as the system changes, so that six months later an engineer can ask a
difficult question and get an answer nobody had to rediscover.

**Apache-2.0** · Python 3.9+ · **zero dependencies** · no network calls, no API keys

**Claude Code:** `/plugin marketplace add gpasquero/engineering-os` then
`/plugin install engineering-os@engineering-os`
**Codex, or any other agent:** one `curl` into its skills directory — see §5.

---

## 1 · What Engineering OS is

Engineering OS:

- **acquires engineering understanding** from systems that already exist;
- turns **reviewed** knowledge into an **Authoritative Engineering Model**;
- compiles that model into a **Canonical Knowledge Model** (CKM);
- generates a **navigable human view**, plus OWL, SHACL, graphs and indexes;
- **answers engineering questions** about the system;
- produces **engineering guidance** — what to do next, and what to check first;
- **maintains understanding incrementally** as commits land;
- **detects drift** by periodically re-deriving understanding and challenging
  what the model claims.

### What it is not

- **Not a coding model.** It writes no application code.
- **Not a replacement for Claude or Codex.** It has no model of its own.
- **Not a documentation generator.** Documentation describes; this answers
  questions and recommends work.
- **Not merely a repository knowledge graph.** A graph stores nodes. This
  carries provenance on every assertion, requires a human to authorize each one,
  and challenges itself over time.

**Claude, Codex and other frontier models are *workers* operating under
Engineering OS.** They investigate and they propose. They never authorize, and
nothing they produce enters the authoritative model without a person accepting
it. The authoritative model stays deterministic.

---

## 2 · MVP status

Honest, as of this release.

### Implemented and tested

| | |
|---|---|
| Mechanical Discovery | reproducible fact extraction; **two stack profiles** — see limitations |
| Deterministic Interpretive Discovery | six rules, proposals with provenance |
| Human Curation | `tools/curate.py`; authorize · reject · correct · defer |
| Proposal application | authorization, coherence rejection, atomic authoring sources |
| The compiler | six phases, 17 regression fixtures, deterministic output |
| Knowledge products | CKM · OWL · SHACL · Mermaid · indexes · Explorer HTML |
| Engineering Questions | 17 declared queries, two independent engines that must agree |
| Engineering Guidance | 4 recommendations, 8 plans, task graphs, worker routing |
| Continuous Acquisition | incremental; **100 % Understanding Retention** over 10 real commits |
| Periodic Reacquisition · Drift | 15 drift classes, each routed to a plan |

### Experimental

- **Brownfield Onboarding Skill** (`tools/onboard.py`) — the contract and the
  validation gate are implemented and tested. The skill has **not yet been run
  end to end with a frontier model on a real system.**
- **Engineering Guidance quality.** Stability is measured (80 % over untouched
  subjects across ten commits). **Correctness is not measured at all.**

### Simulated or not yet validated by a human

- **Human Curation has never been completed by an external reviewer.** The tool
  exists and refuses to run unattended. Every reviewer-efficiency figure it
  reports is therefore **empty**, and that is deliberate — nothing simulates it.

### Planned but unavailable

- Additional stack profiles beyond Node/NestJS/Drizzle and Java/Spring/JPA.
- Organization-level questions spanning several systems.
- Evidence sources other than repositories (runtime, incidents, issue trackers).

### Validation performed

| Repository | Stack | What was measured |
|---|---|---|
| `ai-desk` | Node · NestJS · Drizzle | full lifecycle; 10-commit longitudinal benchmark |
| `wa-b2b` | Java 21 · Spring Boot · JPA | onboarding benchmark, 453 proposals, **no metamodel change required** |

**2 of 9 engineering questions answered on `wa-b2b`, 3 of 9 on `ai-desk`.** Those
numbers are low and they are published on purpose.

---

## 3 · Core concepts

You need these eleven to use the product. You do not need to read any decision
record.

| Concept | What it is |
|---|---|
| **Mechanical Model** | Facts only — packages, modules, routes, tables, tests, config, documents, each with file and locator. Names nothing as knowledge. Reproducible. |
| **Candidate Engineering Model** | Proposed engineering meaning. **Nothing here is true yet.** |
| **Human Curation** | A person accepts, rejects, corrects or defers each proposal. The only stage where anything is decided. |
| **Authoritative Engineering Model** | What survived curation. Markdown authoring sources you own and can edit. |
| **Canonical Knowledge Model (CKM)** | The compiled, queryable form of the authoritative model. Derived — never edited. |
| **Engineering Questions** | The declared questions the product is measured by. *What breaks if I change this? Which invariant protects this?* |
| **Engineering Guidance** | Recommendations, plans and task graphs derived from the model. What to do next. |
| **Initial Acquisition** | First onboarding of a system. Slow and expensive on purpose. |
| **Continuous Acquisition** | After a commit: only what changed is proposed, preserving the meaning onboarding established. |
| **Periodic Reacquisition** | Onboarding-quality discovery run again — to **challenge** the model, never to replace it. |
| **Knowledge Drift** | What a fresh look disagrees with. A work queue, not a document. |

The full customer lifecycle is in **[`LIFECYCLE.md`](LIFECYCLE.md)**. Deeper
architecture lives in [`docs/architecture.md`](docs/architecture.md) and, for
readers who want the reasoning, `governance/adr/`.

---

## 4 · Requirements

| | |
|---|---|
| **Operating systems** | macOS and Linux. Windows is untested; WSL should work. |
| **Python** | **3.9 or newer** |
| **System dependencies** | none |
| **Python dependencies** | **none.** A pure-Python PyYAML is vendored in `vendor/` |
| **Optional** | an installed `PyYAML` (faster parsing) · `rdflib`, only to regenerate metamodel diagrams |
| **Git** | required only for Continuous Acquisition against a real history |
| **Claude / Codex** | required only for the non-deterministic Onboarding Skill |
| **API keys** | **none.** Engineering OS makes no network calls of any kind |
| **Repository access** | read-only filesystem access to a local checkout. Nothing is ever written to the system you analyse |

**Claude or Codex requirements.** You need a working Claude Code or Codex
session — a subscription or CLI authentication you already have. Engineering OS
does not call them. It writes a briefing you paste in, and validates the JSON
you get back. No key is stored or read.

Verify everything:

```bash
python3 --version          # 3.9 or newer
git --version              # optional
python -c "import yaml; print(yaml.__version__)"
eos check      # verifies all of the above and much more
```

---

## 5 · Installation

**Nothing is cloned, nothing is compiled, nothing is `pip install`ed.** Pick the
line that matches your tool.

### Claude Code — no terminal at all

```
/plugin marketplace add gpasquero/engineering-os
/plugin install engineering-os@engineering-os
```

Claude Code fetches and caches it, loads **five separate skills**, and puts
**`eos` on your `PATH`**.

### Claude Code — as a plain skill

```bash
mkdir -p ~/.claude/skills/engineering-os && curl -fsSL \
  https://github.com/gpasquero/engineering-os/archive/refs/heads/main.tar.gz \
  | tar xz -C ~/.claude/skills/engineering-os --strip-components=1
```

### Codex

```bash
mkdir -p ~/.agents/skills/engineering-os && curl -fsSL \
  https://github.com/gpasquero/engineering-os/archive/refs/heads/main.tar.gz \
  | tar xz -C ~/.agents/skills/engineering-os --strip-components=1
```

Codex scans `~/.agents/skills` for user skills, and `.agents/skills` inside a
repository for project ones. Invoke it with `$engineering-os`, or just describe
the task and let it select.

### Anything else

Same download, anywhere you like, plus `eos` on your `PATH`:

```bash
mkdir -p ~/.engineering-os && curl -fsSL \
  https://github.com/gpasquero/engineering-os/archive/refs/heads/main.tar.gz \
  | tar xz -C ~/.engineering-os --strip-components=1
export PATH="$HOME/.engineering-os/bin:$PATH"
```

Then paste `SKILL.md` — or any file in `skills/` — into your agent's
instructions. **The skills name no model vendor**; the contract is identical
whichever model reads it.

## One package, four shapes

The same folder is all of them, which is why there is nothing to choose between:

| File | Read by |
|---|---|
| `SKILL.md` at the root | Codex, and Claude Code when installed as a plain skill |
| `skills/*/SKILL.md` | Claude Code's plugin loader — five namespaced skills |
| `.claude-plugin/` | the Claude Code marketplace, so nothing has to be cloned |
| `bin/eos` | every one of them, and your shell |

Skills are the unit. **The plugin manifest is a shipping label, not
architecture** — it exists so a Claude Code user never has to leave the chat.

Then just ask, in plain language:

> *Onboard this repository — I want to understand what it does and why.*
> *What breaks if I change the billing module?*
> *Is the model still accurate after these commits?*

| Workflow | For |
|---|---|
| `brownfield-onboarding` | build a model of a system nobody fully understands |
| `engineering-questions` | impact, dependencies, rationale, unsupported claims |
| `engineering-guidance` | what to read and check **before** changing something |
| `curate-proposals` | help a human authorize what is true |
| `maintain-understanding` | keep it current, and challenge it |

Verify any installation:

```bash
eos check        # or  ~/.agents/skills/engineering-os/bin/eos check
eos --help
```

**Why nothing needs installing:** Engineering OS is Python, uses only the
standard library, and vendors a pure-Python YAML. It makes no network calls and
reads no credentials.

`eos check` verifies Python, dependencies, all 20 registries, the
engineering-question set, discovery skills, plans, deterministic generation and
compiler health. In a full checkout it also checks governance consistency and
all 17 fixtures; those are **contributor** checks, and a downloaded copy that
omits them reports it rather than failing.

```text
Engineering OS is installed and healthy (all checks passed)
```

<details>
<summary>For contributors</summary>

```bash
git clone https://github.com/gpasquero/engineering-os.git
cd engineering-os
./eos check
```

`pip install -r requirements.txt` is optional and only makes YAML parsing
faster; an installed PyYAML always wins over the vendored copy.

</details>

See [`docs/installation.md`](docs/installation.md) and
[`docs/troubleshooting.md`](docs/troubleshooting.md).

---

## 6 · Quick start

About ten minutes. Uses `examples/tiny`, a small model bundled with the
repository.

```bash
# 1 · authoring sources → compiler → CKM and every knowledge product
eos compile examples/tiny
```

```text
[projection] canonical-knowledge-model.json, explorer.html, graph.md,
             indexes.json, model.ttl, shapes.ttl
```

```bash
# 2 · open the navigable Explorer
open examples/tiny/build/explorer.html        # macOS
xdg-open examples/tiny/build/explorer.html    # Linux
```

```bash
# 3 · ask an Engineering Question
eos ask examples/tiny Q-impact Concept.Order
```

```text
What breaks if I change this?
  subject: Concept.Order

  Invariant.PaymentBeforeShipping  (Invariant)  1 hop(s)

  status: ok · 1 row(s), 0 edge(s) · Q-impact
```

```bash
# 4 · request Engineering Guidance
eos advise examples/tiny R-change-concept Concept.Order
```

You now have the whole loop: **authoring sources → compiler → CKM → Explorer →
one question answered → one guidance result.**

List what else you can ask:

```bash
eos ask examples/tiny questions
eos advise examples/tiny recommendations
eos direct examples/tiny intents
```

More in [`docs/quickstart.md`](docs/quickstart.md).

---

## 7 · Brownfield onboarding

**The most important workflow.** Take a system you already have and build an
engineering model of it.

```text
Existing repository
  → Mechanical Acquisition        facts, reproducible, interprets nothing
  → Brownfield Onboarding Skill   Claude or Codex proposes, with evidence
  → Candidate Engineering Model   nothing true yet
  → Human Curation                a person decides, one proposal at a time
  → Proposal application          authorized proposals become authoring sources
  → Authoritative Engineering Model
  → Compiler → CKM → knowledge products
```

**Initial onboarding is slow and expensive. That is correct.** Its purpose is to
establish durable understanding that every later change maintains
*incrementally* — the ten-commit benchmark maintains a model for **13–15 % of
the cost** of re-deriving it each time.

Try it now against the bundled demo repository:

```bash
eos onboard examples/brownfield-demo external/demo
```

**Output:** `external/demo/mechanical-engineering-model.json` and
`external/demo/onboarding-brief.md`.

Then either path — or both:

**Deterministic (no model needed):**

```bash
eos discover examples/brownfield-demo external/demo
```

**With Claude or Codex** — open `external/demo/onboarding-brief.md` in your
session, follow it, save the JSON reply, then:

```bash
eos ingest external/demo path/to/worker-output.json
```

Either way you get `candidate-initial.json` — and, from the skill, also
`engineering-review.json`. Check where you are at any point:

```bash
eos status external/demo
```

Then curate and compile:

```bash
eos curate external/demo     # requires a terminal and a human
eos compile external/demo
```

Per-step purpose, inputs, outputs, failure modes and how to resume safely:
**[`docs/brownfield-onboarding.md`](docs/brownfield-onboarding.md)**.

**Your own repository** works the same way, if its stack is supported:

```bash
eos onboard /path/to/your/repo external/yourrepo
```

If the stack is not recognised, Mechanical Acquisition **refuses** rather than
returning an empty model — an empty model and an unrecognised stack are opposite
findings. See §21.

---

## 8 · Using Claude or Codex for Interpretive Discovery

**Supported: Claude Code and Codex, or any tool where you can paste a briefing
and get JSON back.** Engineering OS never calls a model itself.

- **Skill contracts:** `discovery/skills/skills.yaml`. The onboarding skill is
  `DS-brownfield-onboarding`.
- **Invoke:** `eos onboard <repo> <project>` writes
  `onboarding-brief.md`. Open it in your Claude Code or Codex session and follow
  it.
- **Context to provide:** the briefing, and `mechanical-engineering-model.json`
  beside it. **The Mechanical Model is the evidence boundary** — the worker may
  open files it references and must go no further.
- **Output schema:** stated verbatim in the briefing — `proposals[]` with `id`,
  `type`, `label`, `source`, `locator`, `uncertainty`, `for[]`, `against[]`,
  `recommendation`; plus optional `relationships[]`.
- **Where proposals go:** save the JSON anywhere; `ingest` writes
  `candidate-initial.json` and `engineering-review.json` into the project.
- **Provenance:** every proposal must cite a `source` in the Mechanical Model
  and a `locator` within it. Ingestion **rejects** anything else.

**Prohibited, and enforced at ingestion:**

| Prohibited | What happens |
|---|---|
| a numeric `confidence`, `score` or `probability` | rejected — `uncertainty` is `high`/`medium`/`low` only |
| a `source` outside the Mechanical Model | rejected — the worker left the evidence boundary |
| a `for` without an `against` | rejected — a case that only argues *for* is not a review |
| a stale Mechanical Model digest | rejected — the repository changed; re-brief |
| writing to the model directly | impossible — `ingest` writes only candidates |

**The contract:** the worker *investigates*; the worker *proposes*; the worker
**never authorizes**; the worker **never writes to the authoritative model**.

More in [`docs/discovery-skills.md`](docs/discovery-skills.md).

---

## 9 · Human curation

```bash
eos curate external/demo
eos curate external/demo --report      # summary of a finished session
```

**Reads:** `candidate-initial.json`, and `engineering-review.json` if present.
**Writes:** `curation-session.json` in the same project.

Each proposal is shown alone, with its evidence source and locator, its
relationships, whether its producer was non-deterministic, and — when a skill
produced one — the argument **for and against**.

| Key | Decision |
|---|---|
| `a` | **authorize** — it becomes authoritative |
| `r` | **reject** — with a recorded reason |
| `c` | **correct** — keep it, with *your* statement instead |
| `d` | **defer** — undecided; it returns next session |
| `?` | show the evidence path again |
| `q` | save and stop |

The reviewer names themselves at the start and is recorded on the session.
**Sessions are resumable** — run the same command again and only undecided and
deferred proposals return.

**It refuses to run without a terminal**, by design.

> **Human Curation has not been validated by an external reviewer.** No human
> has completed a session in this system. Every reviewer-efficiency figure the
> tool reports is currently empty, and nothing fills it in but a person.

More in [`docs/curation.md`](docs/curation.md).

---

## 10 · Applying accepted knowledge

At the end of a curation session you are asked whether to apply. You can also
inspect and apply explicitly:

```bash
eos apply <project> summary
eos apply <project> show ambiguities
eos apply <project> apply --types=Capability,Invariant --reviewer=NAME
eos apply <project> apply --ids=Concept.Order,Capability.Billing --reviewer=NAME
```

What application does:

- **verifies authorization** — nothing is applied without an explicit accepted
  set and a named reviewer;
- **rejects incoherent proposals** — a relationship whose other end was not
  authorized does not enter;
- **detects stale proposals** — a Mechanical Model digest that no longer matches
  the repository;
- **writes authoring sources** — one Markdown file per entity, under
  `<project>/model/`, which **you own and may edit by hand**;
- **is idempotent** — applying the same authorized set again changes nothing;
- **never partially writes** — a rejected proposal simply does not appear.

Then compile:

```bash
eos compile external/demo
```

---

## 11 · Generating the knowledge products

```bash
eos compile <project>
eos compile --phases        # what the compiler does, in order
```

Everything lands in `<project>/build/`:

| File | What it is |
|---|---|
| `canonical-knowledge-model.json` | the CKM — the queryable semantic model |
| `model.ttl` | OWL ontology |
| `shapes.ttl` | SHACL shapes |
| `graph.md` | Mermaid graph |
| `indexes.json` | registry and entity projections |
| **`explorer.html`** | **the navigable web experience** |

**Authoritative:** `<project>/model/*.md` — your authoring sources.
**Derived:** everything in `build/`. Never edit it; it is overwritten.

Open the Explorer — a single self-contained file, no server required:

```bash
open <project>/build/explorer.html          # macOS
xdg-open <project>/build/explorer.html      # Linux
```

To serve it instead:

```bash
python -m http.server 8000 --directory <project>/build
# then browse http://localhost:8000/explorer.html
```

---

## 12 · Asking engineering questions

```bash
eos ask <project> questions                     # list them
eos ask <project> Q-impact Concept.Order        # ask one
eos ask <project> Q-impact Concept.Order --paths
eos ask <project> Q-impact Concept.Order --json
```

Three outcomes, and they mean different things:

| Status | Meaning |
|---|---|
| `ok` | answered, with rows and the path to each |
| `empty` | the question applies and **nothing matched** |
| `not-applicable` | the question does not apply to this subject type |

Every row carries its path and provenance, so the next question — *how do you
know?* — is always answerable.

Measure how much a model can answer:

```bash
eos measure <project>
```

---

## 13 · Requesting engineering guidance

```bash
eos direct <project> intents
eos direct <project> I-modify-behavior Concept.Order
eos advise <project> recommendations
eos advise <project> R-change-concept Concept.Order
```

`direct.py` runs the complete loop: **intent → plan → task graph → worker
assignment → execution context**.

**No language model participates in producing a plan.** Every decision is
derived from the model. Where a decision genuinely requires judgement, the plan
says so and defers it to a worker or a human gate rather than guessing — and a
step that cannot apply to your subject is **named**, never silently skipped.

More in [`docs/engineering-guidance.md`](docs/engineering-guidance.md).

---

## 14 · Continuous acquisition

After a change lands, maintain the model instead of rebuilding it.

```bash
eos maintain <before-repo> <after-repo> <project>
```

`<before-repo>` and `<after-repo>` are two checkouts — typically a detached
`git worktree` at the previous commit and your working tree. **Your repository
is never modified.**

What happens: the Mechanical Model is re-extracted, a delta is computed, and
**only what changed is proposed** — carrying the same meaning the onboarding
established. Removals are **never applied automatically**; they are proposals a
human reviews.

Check that understanding survived:

```bash
eos measure <project>
python tools/longitudinal.py <repo> <project> <commit> ...   # the frozen benchmark
```

More in [`docs/continuous-acquisition.md`](docs/continuous-acquisition.md).

---

## 15 · Periodic reacquisition and knowledge drift

Re-derive understanding at onboarding quality — **to challenge the maintained
model, never to replace it.** `tools/lifecycle.py` runs this as its final
stages, writing `candidate-reacquisition.json` and
`knowledge-drift-report.json`.

Turn the report into work:

```bash
eos drift <project>
eos drift <project> --plan=P-review-unsupported
```

```text
P-discover                 123 item(s)   from D-implementation-without-knowledge
P-establish-enforcement      9 item(s)   from D-invariant-without-enforcement
P-review-unsupported         1 item(s)   from D-unsupported-assertion
NOT ROUTED — D-new-knowledge (104): additive; curation alone suffices
```

Fifteen drift classes, each routed to an Engineering Plan. **Nothing a
reacquisition produces is applied.**

More in [`docs/knowledge-drift.md`](docs/knowledge-drift.md).

---

## 16 · Greenfield usage

**Only manual authoring is supported.** There is no greenfield automation, and
none is claimed.

Create `<project>/model/` and write one Markdown file per entity — concepts,
capabilities, invariants, decisions — then compile. `examples/tiny/model/` is a
complete worked example of every entity type, and is the right thing to copy.

```bash
mkdir -p myproject/model
cp examples/tiny/model/*.md myproject/model/
# edit them to describe your system, then:
eos compile myproject
eos advise myproject recommendations
```

Ask for guidance **before** implementing, and keep the model current as work
completes. More in [`docs/greenfield.md`](docs/greenfield.md).

---

## 17 · Common workflows

| Goal | Start here |
|---|---|
| Onboard an existing repository | `tools/onboard.py brief` → [onboarding](docs/brownfield-onboarding.md) |
| Investigate a bug | `eos direct <project> I-investigate <subject>` |
| Add a feature / modify behaviour | `eos direct <project> I-modify-behavior <subject>` |
| Architecture review | `eos advise <project> R-audit-model` |
| Inspect impact | `eos ask <project> Q-impact <subject> --paths` |
| Review unsupported knowledge | `eos ask <project> Q-unsupported` |
| Update the model after a change | `tools/lifecycle.py` → [continuous](docs/continuous-acquisition.md) |
| Rerun full acquisition | `tools/lifecycle.py` → [drift](docs/knowledge-drift.md) |
| Generate the navigable web | `eos compile <project>` → `build/explorer.html` |

---

## 18 · Repository structure

| Directory | What it is | Edit? |
|---|---|---|
| `compiler/` | the compiler, query engine, planner, applier | product code |
| `discovery/` | mechanical + interpretive discovery, stack profiles, skills | product code |
| `tools/` | every command in this README | product code |
| `model/metamodel/` | the 23 entity types and their specifications | **do not change casually** |
| `model/*.md` | declared registries: queries, plans, recommendations, questions | extend, carefully |
| `discovery/stacks.yaml` | Stack Profiles | **add yours here** |
| `discovery/skills/` | Discovery Skill contracts | **add yours here** |
| `<project>/model/` | **your authoring sources** | **yes — this is yours** |
| `<project>/build/` | generated products | **never — overwritten** |
| `examples/` | `tiny`, `vertical-slice`, `brownfield-demo` | copy from |
| `tests/` | 17 regression fixtures with golden outputs | add fixtures |
| `governance/` | decision records, sessions, acceptance | project history |
| `external/` | onboarding and benchmark results | research artifacts |

---

## 19 · Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `no Stack Profile matches …` | your stack is not one of the two supported. Add a profile to `discovery/stacks.yaml` |
| YAML parse error in a source | a value beginning with `"` or `*` needs quoting |
| `unknown registry reference` | an id that no registry declares — check spelling |
| `no Candidate Engineering Model in …` | wrong project directory, or discovery has not run |
| `digest mismatch` on ingest | the repository changed after briefing. Re-run `brief`, re-run the worker |
| `not-applicable` from a query | the question does not apply to that subject type — not an error |
| **deterministic-generation mismatch** | stale bytecode. macOS caches outside the repo: `rm -rf ~/Library/Caches/com.apple.python$(pwd)` |
| discovery output is empty | the profile matched but found nothing — check paths in `stacks.yaml` |
| a plan phase produced nothing | the step did not apply to your subject; the planner names which and why |

Full guide: [`docs/troubleshooting.md`](docs/troubleshooting.md).

---

## 20 · Security and trust model

- **Probabilistic workers produce proposals only.** Claude and Codex cannot
  write knowledge; they return JSON that is validated and quarantined as a
  candidate.
- **Humans authorize.** Nothing becomes authoritative without a named reviewer.
- **The applier is the only component that writes authoring sources.**
- **The compiler is side-effect-free** — it reads sources and writes only into
  `build/`.
- **Generated products are derived** and always reproducible from sources.
- **Provenance is preserved** on every assertion: source, locator, worker,
  support, and whether the producer was non-deterministic.
- **No worker self-certifies.** A proposal's own confidence never authorizes it.
- **Engineering OS makes no network calls and reads no credentials.** It needs
  read-only access to a local checkout and writes only inside its own project
  directory.

---

## 21 · Current limitations

Stated plainly.

- **Human Curation has not been validated by an independent third-party
  engineer.** Reviewer-efficiency metrics are empty.
- **Two stack profiles only** — Node/NestJS/Drizzle and Java/Spring/JPA. Other
  stacks are refused, not degraded.
- **A repository may host several stacks; only one profile is detected.**
- **The Brownfield Onboarding Skill has not been run end to end with a frontier
  model on a real system.** The contract and gate are tested; the loop is not.
- **Deterministic discovery exercises 5 of 23 metamodel entity types.** It has
  never proposed an `Actor` or a `Policy`.
- **The most valuable questions are unanswered.** *Why does this system work this
  way?* returns nothing on both benchmarked repositories, and *who is allowed to
  perform this operation?* has no query at all.
- **Guidance correctness is unmeasured.** Only its *stability* is.
- **Organization-level questions** spanning several systems are not implemented.
- **No production hardening.** No packaging, no daemon, no multi-user story.
- **Onboarding does not discover all engineering knowledge, and does not claim
  to.** It surfaces what evidence supports; the rest still lives in people.

---

## 22 · Contributing and extending

| To add | Where | Note |
|---|---|---|
| a **Stack Profile** | `discovery/stacks.yaml` | declaration only — no code |
| a **deterministic extractor** | `discovery/mechanical.py` | only if no existing extraction kind fits |
| a **Discovery Skill** | `discovery/skills/skills.yaml` | start at level 1: one repository, disposable |
| an **Engineering Question** | `model/engineering-questions.md` | see below |
| a **recommendation** | `model/recommendations.md` | composed of declared queries |
| a **fixture** | `tests/projects/<name>/` | with `expected.md` and golden outputs |

Run `eos check` before and after any change.

**Two rules that matter more than the rest:**

**Do not change the metamodel to accommodate one repository.** Twenty-three
entity types have absorbed two unrelated stacks without modification. If a
system seems to need a twenty-fourth, the far more likely explanation is that it
is being modelled wrongly.

**The Engineering Question Set is a contract.** Its text, membership, thresholds
and query mappings change only by deliberate review — a question can be made to
pass by pointing it at a different query, which is exactly why it is protected.

---

## 23 · License

**Apache License 2.0.** See [`LICENSE`](LICENSE).

---

<sub>Verify a clean installation end to end at any time with
`eos smoke` — it runs the whole documented path in a temporary
workspace and reports whether a third-party engineer can complete it.</sub>
