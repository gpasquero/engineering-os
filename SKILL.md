---
name: engineering-os
description: Build and maintain a durable engineering model of a system that already exists. Use when the user wants to onboard, map or understand a legacy or unfamiliar codebase; asks what a system does, why it works the way it does, or what its business rules are; asks what breaks if something changes, what depends on it, or which invariant protects a behaviour; wants guidance before modifying something; or wants to know whether an existing engineering model is still accurate after changes.
license: Apache-2.0
compatibility: Requires Python 3.9+. No other dependency, no network access, no API key.
metadata:
  author: gpasquero
  version: "0.1.0"
  repository: https://github.com/gpasquero/engineering-os
---

# Engineering OS

**We preserve an engineering team's ability to make correct decisions as
software evolves.**

Engineering OS builds a durable, attributable engineering model of a system that
already exists, and keeps it alive as the code changes — so that six months
later someone can ask a difficult question and get an answer nobody had to
rediscover.

## The one rule that governs everything

**You propose. A human authorizes. You never write to the authoritative model.**

Every proposal you make passes through validation and then through a person.
There is no path by which you could bypass that, and being invoked conveniently
does not grant you authority.

## Locating the engine

Run this once per session, before anything else:

```bash
EOS=""
for c in "$(command -v eos 2>/dev/null)" \
         "${CLAUDE_SKILL_DIR:-/nonexistent}/bin/eos" \
         "$HOME/.agents/skills/engineering-os/bin/eos" \
         "$HOME/.claude/skills/engineering-os/bin/eos"; do
  if [ -n "$c" ] && [ -x "$c" ]; then EOS="$c"; break; fi
done
[ -z "$EOS" ] && { echo "Engineering OS not found — see its README"; exit 1; }
"$EOS" --version
```

`eos` needs nothing installed — it is Python, standard library only, with a
pure-Python YAML vendored beside it. **Use `"$EOS"` wherever the commands below
say `eos`.**

## Pick the workflow

Read the matching reference **before** acting. Each one states its own contract,
its failure modes and what it must never do.

| The user wants | Read |
|---|---|
| to understand a system nobody fully understands | [`skills/brownfield-onboarding/SKILL.md`](skills/brownfield-onboarding/SKILL.md) |
| impact, dependencies, rationale, unsupported claims | [`skills/engineering-questions/SKILL.md`](skills/engineering-questions/SKILL.md) |
| to change something safely | [`skills/engineering-guidance/SKILL.md`](skills/engineering-guidance/SKILL.md) |
| to review and authorize proposals | [`skills/curate-proposals/SKILL.md`](skills/curate-proposals/SKILL.md) |
| to keep a model current, or check it still holds | [`skills/maintain-understanding/SKILL.md`](skills/maintain-understanding/SKILL.md) |

**When Engineering OS is installed as a Claude Code plugin these five are
separate skills and Claude selects one directly.** This file is the router for
every other environment — Codex, or a plain skill folder — where the five are
reference documents instead.

## The loop, in one screen

```bash
eos onboard  <repository> <project>   # facts, plus your briefing
eos discover <repository> <project>   # deterministic proposals — run this first
eos ingest   <project> <your.json>    # your proposals, validated
eos curate   <project>                # A HUMAN does this. Never run it for them
eos compile  <project>                # CKM, OWL, SHACL, graph, Explorer
eos ask      <project> Q-impact <subject>
eos advise   <project>
eos measure  <project>
eos maintain <before> <after> <project>
```

`<project>` is where the model lives — **in the user's workspace**, never inside
Engineering OS's own directory. Ask them where if they have not said.

`eos --help` lists everything; every subcommand takes `--help`.

## Never

- Never write into `<project>/model/` — only curation puts things there.
- Never attach a confidence score. Uncertainty is `high`, `medium` or `low`.
- Never cite evidence outside the Mechanical Model.
- Never present a proposal without its counter-argument.
- Never run `eos curate` on the user's behalf — it requires a terminal and a
  person, and refuses without both.
