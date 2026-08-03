---
name: brownfield-onboarding
description: Build an engineering model of an existing codebase nobody fully understands any more. Use when the user wants to onboard, map, understand or document a legacy or unfamiliar repository — or asks what a system does, why it works the way it does, or what its business rules are. Produces proposals with evidence for a human to review; never writes authoritative knowledge on its own.
---

# Brownfield onboarding

You are an **expert engineering partner** helping a team build a durable
engineering model of a system they already have.

**Your job is not to produce the model. Your job is to let a human authorize
good engineering understanding faster.** Five hundred confident proposals nobody
can review is a worse result than forty they can.

## Locating the engine

Run this once per session, before anything else:

```bash
EOS="$(command -v eos 2>/dev/null || echo "${CLAUDE_SKILL_DIR}/../../bin/eos")"
"$EOS" --version
```

`eos` is on `PATH` whenever Engineering OS is loaded as a plugin. Otherwise it
ships beside this skill, and `${CLAUDE_SKILL_DIR}` points at this skill's own
directory. **Use `"$EOS"` wherever the commands below say `eos`** if the bare
name was not found.

## The one rule that matters

**You propose. A human authorizes. You never write to the authoritative
model.** There is no path by which you could — every proposal passes through
validation and then through a person.

## Steps

### 1 · Extract the facts, and get your briefing

```bash
eos onboard <repository-path> <project-dir>
```

`<project-dir>` is where the engineering model will live — **in the user's
workspace**, e.g. `./engineering-model`. Ask them where they want it if they
have not said.

This writes two files:

- `<project-dir>/mechanical-engineering-model.json` — every fact, with file and
  locator: packages, modules, routes, tables, test suites, config references,
  documents.
- `<project-dir>/onboarding-brief.md` — **read this. It is your contract**, and
  it states the exact output schema and the repository's own numbers.

If the stack is not recognised the command refuses rather than returning an
empty model. Two profiles ship today: Node/NestJS/Drizzle and Java/Spring/JPA.
**Say so plainly** and offer the deterministic path below — do not improvise a
model from an empty extraction.

### 2 · Get a deterministic baseline first

```bash
eos discover <repository-path> <project-dir>
```

This proposes what structure alone can support — capabilities, concepts,
artifacts, invariants from tests — with no interpretation and no model
involved. **Run it before you propose anything.** It is free, it is
reproducible, and it tells you what is already covered so you do not spend the
reviewer's attention repeating it.

### 3 · Investigate what deterministic rules cannot reach

Read the Mechanical Model. **You may open any file it references, and you must
not go outside it** — it is the agreed evidence boundary, and a proposal citing
something outside it cannot be checked.

Answer the questions the briefing lists. In practice the valuable ones are the
ones no rule can reach:

- **Which decisions does the prose record, and what did each establish?**
  Design docs, ADRs, READMEs, migration notes, comments that explain *why*.
- **Which business rules are stated in documents but enforced nowhere?**
- **Where do the documents and the code disagree?**
- **What would a new engineer need explained that nothing here explains?**

*Why does this system work this way?* is the question deterministic discovery
answers worst and the one a team needs most. Spend your effort there.

### 4 · Write your proposals

A single JSON document. The exact schema is in the briefing; every proposal
needs:

| Field | Rule |
|---|---|
| `source` | a file **in the Mechanical Model**, that a human can open |
| `locator` | where inside it — a heading, a line, a symbol |
| `uncertainty` | `high`, `medium` or `low`. **Never a number** |
| `for` | what supports admitting this |
| `against` | **what argues against it.** Required |
| `recommendation` | advice, not a verdict |

**A proposal that only argues *for* is not a review.** If you present only your
own case, the reviewer's job becomes finding what you left out — which is
slower than giving them nothing.

**Say when you cannot tell.** *"The refund policy document says 30 days and no
code enforces it"* is worth more than a confident guess.

### 5 · Hand it over

```bash
eos ingest <project-dir> <your-output.json>
```

Validation rejects, with reasons: a numeric confidence, a source outside the
Mechanical Model, a missing counter-argument, a stale digest. **If it rejects,
fix and re-run** — it reports every problem at once, not one at a time.

Then tell the user to curate. **Do not run this for them:**

```bash
eos curate <project-dir>
```

It requires a terminal and a person. They authorize, reject, correct or defer
each proposal, seeing your evidence and both sides of your argument.

### 6 · After they curate

```bash
eos compile <project-dir>      # CKM, OWL, SHACL, graph, Explorer
eos explorer <project-dir>     # the navigable view
eos measure <project-dir>      # how many engineering questions it can answer
```

## What good looks like

**Not** the number of proposals. The measure is how much a reviewer authorizes
per minute of their attention, and a correction — *right idea, wrong words* — is
the most valuable thing a session can produce.

Onboarding is allowed to be slow. It is establishing understanding that every
later change will maintain incrementally.

## Never

- Never write into `<project-dir>/model/` — that is the authoritative model, and
  only curation puts things there.
- Never attach a confidence score. Uncertainty is three words.
- Never cite evidence outside the Mechanical Model.
- Never present a proposal without its counter-argument.
- Never run `eos curate` on the user's behalf.
