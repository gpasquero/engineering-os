# Human curation

**Purpose.** Decide, one proposal at a time, what becomes part of the
Authoritative Engineering Model. This is the only stage in Engineering OS where
a person decides anything, and nothing reaches the authoritative model without
passing through it.

> **Honest status.** No human has ever completed a curation session in this
> system. The tool exists, works and refuses to run unattended; every
> reviewer-efficiency figure it reports is therefore **empty**. That is
> deliberate — a scripted session would generate exactly those numbers, and
> nothing simulates them.

---

## Before you start

You need a Candidate Engineering Model in the project directory. Produce one
with either path in [brownfield onboarding](brownfield-onboarding.md):

```bash
python discovery/run.py <repository> <project>          # deterministic
python tools/onboard.py brief <repository> <project>    # with Claude or Codex
```

---

## The interactive session

**Command**

```bash
python tools/curate.py <project>
python tools/curate.py <project> --report
```

**Reads** `<project>/candidate-initial.json`, and `<project>/engineering-review.json`
if a skill produced one.
**Writes** `<project>/curation-session.json`, after every single decision.

The session begins by asking who you are; the name is recorded on the session.
Each proposal is then shown alone:

```text
1/11  Invariant  An issued invoice is never edited
      Invariant.InvoicesAreImmutable

  evidence   docs/adr/0001-invoices-are-immutable.md
             decision
  support    S-inferred
  producer   non-deterministic  claude-code — would not repeat itself
  relation   constrains → Concept.Invoice   S-inferred

  engineering review
    + The ADR states it as an accepted decision.
    − No test asserts it.
    uncertainty: low
    skill recommends: authorize

  decision [a/r/c/d/?/q]
```

| Key | Decision | What is recorded |
|---|---|---|
| `a` | **authorize** — it becomes authoritative | your confidence and your assessment of the evidence quality |
| `r` | **reject** | a reason you type |
| `c` | **correct** — keep it, in your own words | your replacement statement, plus confidence and evidence quality |
| `d` | **defer** | nothing; it returns next session |
| `?` | show the evidence source and locator again | — |
| `q` | save and stop | — |

**`correct` is what makes this a partner rather than a gate.** *Right idea,
wrong words* is the common case, and rejecting it loses the idea.

**Sessions are resumable.** Run the same command again: only undecided and
deferred proposals return. There is no separate resume flag — the tool's own
`--help` text mentions `--resume`, but the code resumes automatically from
`curation-session.json` and the flag has no effect.

---

## The session report

```bash
python tools/curate.py <project> --report
```

```text
CURATION SESSION   unattributed
  proposals generated   1
  reviewed              0
  authorized            0
  corrected             0
  rejected              0
  deferred              0
```

Once a human has actually reviewed something, the report adds review time,
seconds per proposal, **accepted per minute** — the figure onboarding is
optimized for — the number of reviewer corrections, and the distributions of
reviewer confidence and evidence quality.

`--report` works without a terminal, so it is safe in scripts and CI.

---

## Applying what you accepted

At the end of an interactive session you are asked:

```text
  apply to the authoritative model? [y/N]
```

Answering `y` writes one Markdown authoring source per accepted entity into
`<project>/model/`. **An accepted proposal becomes an authoring source, never a
model write** — the compiler stays the only writer of the Canonical Knowledge
Model, and the file you get is one you own and may edit by hand:

```markdown
---
id: Concept.TableAccounts
type: Concept
label: accounts table
attributes:
  locator: pgTable('accounts')
  origin: O-deterministic-rule
  proposed-by: W-domain-interpreter
  proposed-in: T02-interpret
  rule: S1-pgtable-is-a-concept
  source: packages/backend/src/common/database/schema/accounts.ts
  support: S-implemented
relationships: []
---

Proposed by `W-domain-interpreter` in task `T02-interpret` and accepted through
review. Support: `S-implemented`.
```

Then compile:

```bash
python tools/compile.py <project>
```

---

## Bulk authorization without an interactive session

`tools/review.py` inspects a Candidate Engineering Model and applies an
authorized subset non-interactively. It reads
`<project>/candidate-engineering-model.json` — the file `discovery/run.py`
writes — so it works with deterministic discovery output.

```bash
python tools/review.py <project> summary
python tools/review.py <project> show gaps            # also: ambiguities, conflicts
python tools/review.py <project> apply --types=Concept,Invariant --reviewer=NAME
python tools/review.py <project> apply --ids=A,B,C --reviewer=NAME
```

`summary` reports entities and relationships by support classification, by type
and by worker, together with how each support classification must be reviewed:

| Batch-acceptable | Individual review required |
|---|---|
| `S-confirmed-deterministic`, `S-tested`, `S-implemented` | `S-specified`, `S-inferred`, `S-ambiguous`, `S-conflicting`, `S-unknown` |

`apply` **requires** `--reviewer` — an authorization must name who gave it — and
exits 2 without it. It reports what it accepted, what it left, and any coherence
diagnostics:

```text
AUTHORIZED by docs-test
  accepted  4 entities, 0 relationships
  left      7 entities unaccepted
  ! 10 relationship(s) not authorized: an endpoint was not accepted
  written   4 authoring sources to demo/model/
```

**A relationship is authorized only when both of its endpoints are.** An edge to
an unaccepted node would compile to a dangling reference, so it is dropped and
counted rather than written. Optionally restrict by support with
`--support=S-implemented,S-tested`.

Application is idempotent: applying the same authorized set again produces the
same files.

---

## Failure modes

| Symptom | Exit | Cause and fix |
|---|---|---|
| `Human Curation requires a human.` | 1 | no terminal attached. This is by design; use `--report`, or `tools/review.py` for non-interactive authorization |
| `no Candidate Engineering Model in <project>.` | 1 | wrong project directory, or discovery has not run. The message prints both commands that produce one |
| `no candidate model at <project>/candidate-engineering-model.json` | 1 | `tools/review.py` reads the file `discovery/run.py` writes; onboarding ingest writes `candidate-initial.json` instead — curate that with `tools/curate.py` |
| `--reviewer is required` | 2 | `tools/review.py apply` will not run anonymously |
| you authorized entities but no relationships were written | 0 | expected: an endpoint was not accepted. The diagnostic line names how many were dropped |
