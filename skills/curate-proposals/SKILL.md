---
name: curate-proposals
description: Help a human review and authorize proposed engineering knowledge before it becomes authoritative. Use when proposals exist and need reviewing, when the user asks what is waiting for approval, or after onboarding or maintenance has produced a candidate model.
---

# Human curation

**This is the only stage where anything is decided, and it is not yours to
do.** Every proposal — from a deterministic rule or from a model like you —
enters the authoritative model here or not at all.

```bash
eos status <project>      # where this project is in the loop
eos curate <project>      # the session itself — the user runs this
```

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

## Your role

**Prepare and explain. Do not decide.**

`eos curate` requires a terminal and refuses to run without one, deliberately: a
scripted session would manufacture the reviewer-efficiency measurements the
product exists to earn honestly.

What you can usefully do:

- run `eos status` and tell them what is waiting;
- summarise the proposals by type and by uncertainty so they know the shape of
  the work before starting;
- when they ask about a specific proposal, **open its cited source and locator**
  and show them the evidence;
- after the session, run `eos compile` and `eos measure` and report what the
  authorized subset can now answer.

## What they will see

Each proposal alone, with its evidence, its relationships, whether its producer
was non-deterministic, and the argument for and against it.

| Key | Decision |
|---|---|
| `a` | authorize |
| `r` | reject, with a reason |
| `c` | **correct** — keep it, with their statement instead of the proposed one |
| `d` | defer |
| `q` | save and stop |

Sessions resume automatically. Only undecided and deferred proposals return.

**Point out `c` if they have not noticed it.** A correction — *right idea, wrong
words* — is the most valuable thing a session produces, and reviewers who do not
know it exists reject instead.

## Then

```bash
eos compile <project>
eos explorer <project>
eos measure <project>
```
